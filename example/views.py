from django.shortcuts import render,redirect
from django.http import JsonResponse, HttpResponse,HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
# Create your views here.
from django.template import loader
#from datatable.views import ServerSideDatatableViewSPP

from utils import custom_sql, custom_procedure, movecol, custom_procedure_multiple_results,insert_sql
from django.contrib.auth import authenticate, login as auth_login,logout

from example.models import DBTEST_MODEL
import json
#import cv2
#import numpy as np
#from matplotlib import pyplot as plt

#import openai

import requests

#import tinify
def logout_view(request):
  logout(request)
  return redirect('/')

def example(request):
  template = loader.get_template('home.html')
  return HttpResponse(template.render())

@login_required
def adminHome(request):
  if request.method == "GET":
    template = loader.get_template('adminHome.html')
    main_sql = "SELECT * FROM tblClientDetails where active=1;"
    results = custom_sql('default', main_sql)
    if len(results) > 0:
      cname = results[0]['txtClientname']
      mobile1 = results[0]['txtMobile1']
      mobile2 = results[0]['txtMobile2']
      Address = results[0]['txtAddress']
      emailid = results[0]['txtEmailID']
      context = {
        'title': cname,
        'page': 'Admin Home',
        'mobile1': mobile1,
        'mobile2': mobile2,
        'address': Address,
        'email': emailid
      }
    # context = {
    #   'title': 'Mano Driving School',
    #   'page': 'Admin Home'
    # }
    return HttpResponse(template.render(context,request))

def login(request):
  if request.method=='GET':
    template = loader.get_template('Login.html')
    main_sql = "SELECT * FROM tblClientDetails where active=1;"
    results = custom_sql('default', main_sql)
    if len(results) > 0:
      cname = results[0]['txtClientname']
      mobile1 = results[0]['txtMobile1']
      mobile2 = results[0]['txtMobile2']
      Address = results[0]['txtAddress']
      emailid = results[0]['txtEmailID']
      context = {
        'title': cname,
        'page': 'Login',
        'mobile1': mobile1,
        'mobile2': mobile2,
        'address': Address,
        'email': emailid
      }
    # context = {
    #   'title': 'Mano Driving School',
    #   'page': 'Login',
    # }
    return HttpResponse(template.render(context,request))

def contact(request):
  template = loader.get_template('contact.html')
  main_sql = "SELECT * FROM tblClientDetails where active=1;"
  results = custom_sql('default', main_sql)
  if len(results) > 0:
    cname=results[0]['txtClientname']
    mobile1=results[0]['txtMobile1']
    mobile2 = results[0]['txtMobile2']
    Address = results[0]['txtAddress']
    emailid = results[0]['txtEmailID']
    context = {
      'title': cname,
      'page': 'Contact Us',
      'mobile1':mobile1,
      'mobile2': mobile2,
      'address':Address,
      'email':emailid
    }
  # context = {
  #   'title': 'Mano Driving School',
  #   'page':'Contact Us'
  # }
  return HttpResponse(template.render(context,request))

def EmpMaster(request):
  template = loader.get_template('EmployeeMaster.html')
  return HttpResponse(template.render())

@csrf_exempt
def get_user_query(request):
  data = []
  if request.method == "POST":
    try:
      length = request.POST['length']
      start = request.POST['start']
      offset=0
      if(int(start)>0):
        offset=start
      result_info_sql=""
      main_sql = ""
      #delete_sql="DELETE FROM tblUserQuery where id="
      #results = custom_sql('default', delete_sql)
      ord_sql=int(request.POST['order[0][column]'])+1
      if(request.POST['search[value]']!=''):
        search_val=request.POST['search[value]']
        where_sql="where txtName like '%"+search_val+"%' or txtMobile like '%"+search_val+"%'  or txtQuery like '%"+search_val+"%' "
        main_sql="select txtName as Name,txtMobile as Mobile,txtQuery as Query,id from tblUserQuery "+where_sql+" order by query_date desc, "+str(ord_sql)+" "+request.POST['order[0][dir]']+" LIMIT "+str(offset)+","+str(length)+";"
        result_info_sql="select count(*) as COUNT from tblUserQuery "+where_sql+";"
      else:
        main_sql="select txtName as Name,txtMobile as Mobile,txtQuery as Query,id from tblUserQuery order by query_date desc, "+str(ord_sql)+" "+request.POST['order[0][dir]']+" LIMIT "+str(offset)+","+str(length)+";"
        result_info_sql = "select count(*) as COUNT from tblUserQuery;"

      results = custom_sql('default',main_sql)
      results_info = custom_sql('default', result_info_sql)
      if len(results_info) >0:
        records = {
          "recordsTotal":results_info[0]['COUNT'],
          "recordsFiltered":results_info[0]['COUNT'],
          'aaData': results,
        }
      else:
        raise Exception("No Data!")
    except Exception as e:
      data['msg'] = str(e)
    return HttpResponse(json.dumps(records), content_type='application/json')

@csrf_exempt
def login_auth(request):
  data = {}
  if request.method == "POST":
    try:
      name = request.POST['dom_username']
      Mobile = request.POST['dom_password']
      valuenext = request.POST['valuenext']
      user = authenticate(request, username=name, password=Mobile)
      if user is not None:
        auth_login(request, user)
        return redirect('/adminHome/')
      else:
        raise redirect('/')
    except Exception as e:
      data['msg'] = str(e)
      """context = {'error': 'The username and password combination is incorrect'
                 ,'errMsg':str(e)}
      return render(request, '/login/', context)
      """

@csrf_exempt
def post_query(request):
  data = {}
  if request.method == "POST":
    name = request.POST['name']
    Mobile = request.POST['Mobile']
    Query = request.POST['Query']
    try:
      results = insert_sql('default',"INSERT INTO `tblUserQuery`(txtName,txtMobile,txtQuery) values('"+name+"','"+Mobile+"','"+Query+"');")
      if results >0:
        data['msg']='Success'
      else:
        raise Exception("Failed!")
    except Exception as e:
      data['msg'] = str(e)
    return JsonResponse(data)