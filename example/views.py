from django.shortcuts import render,redirect
from django.http import JsonResponse, HttpResponse,HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
from django.template import loader
#from datatable.views import ServerSideDatatableViewSPP

from utils import custom_sql, custom_procedure, movecol, custom_procedure_multiple_results,insert_sql

from example.models import DBTEST_MODEL
import json
#import cv2
#import numpy as np
#from matplotlib import pyplot as plt

#import openai

import requests

#import tinify

def example(request):
  template = loader.get_template('home.html')
  return HttpResponse(template.render())

def adminHome(request):
  template = loader.get_template('adminHome.html')
  context = {
    'title': 'Mano Driving School',
  }
  return HttpResponse(template.render(context,request))

def login(request):
  template = loader.get_template('Login.html')
  context = {
    'title': 'Mano Driving School',
  }
  return HttpResponse(template.render(context,request))

def contact(request):
  template = loader.get_template('contact.html')
  context = {
    'title': 'Mano Driving School',
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
    name = request.POST['name']
    Mobile = request.POST['Mobile']
    valuenext = request.POST['valuenext']
    try:
      results = custom_sql('default',"SELECT 1 FROM tblLogin WHERE txtuname = '"+name+"' AND txtpwd ='"+Mobile+"';")
      if len(results) >0:
        #data['msg']='Success'
        return redirect(valuenext)
      else:
        raise Exception("No Such user!")
    except Exception as e:
      data['msg'] = str(e)
      context = {'error': 'The username and password combination is incorrect'
                 ,'errMsg':str(e)}
    return render(request, '/login/', context)
    #return JsonResponse(data)

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