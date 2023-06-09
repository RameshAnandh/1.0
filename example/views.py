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
    context = {
      'title': 'Mano Driving School',
      'page': 'Admin Home'
    }
    return HttpResponse(template.render(context,request))

def login(request):
  if request.method=='GET':
    template = loader.get_template('Login.html')
    context = {
      'title': 'Mano Driving School',
      'page': 'Login'
    }
    return HttpResponse(template.render(context,request))

def contact(request):
  template = loader.get_template('contact.html')
  context = {
    'title': 'Mano Driving School',
    'page':'Contact Us'
  }
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
      results_info = custom_sql('default',"select count(*) as COUNT from tblUserQuery;")
      results = custom_sql('default',"select txtName as Name,txtMobile as Mobile,txtQuery as Query from tblUserQuery LIMIT "+str(offset)+","+str(length)+";")
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
      results = insert_sql('default',"INSERT INTO `tblUserQuery` values('"+name+"','"+Mobile+"','"+Query+"');")
      if results >0:
        data['msg']='Success'
      else:
        raise Exception("Failed!")
    except Exception as e:
      data['msg'] = str(e)
    return JsonResponse(data)