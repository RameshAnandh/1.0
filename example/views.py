from django.shortcuts import render,redirect
from django.http import JsonResponse, HttpResponse,HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
from django.template import loader
#from datatable.views import ServerSideDatatableViewSPP

#from utils import custom_sql, custom_procedure, movecol, custom_procedure_multiple_results

from example.models import DBTEST_MODEL

#import cv2
#import numpy as np
#from matplotlib import pyplot as plt

#import openai

import requests

#import tinify

def example(request):
  template = loader.get_template('home.html')
  return HttpResponse(template.render())

def login(request):
  template = loader.get_template('Login.html')
  return HttpResponse(template.render())

def EmpMaster(request):
  template = loader.get_template('EmployeeMaster.html')
  return HttpResponse(template.render())

@csrf_exempt
def login_auth(request):
  data = {}
  if request.method == "POST":
    name = request.POST['name']
    Mobile = request.POST['Mobile']
    try:
      results = custom_sql('default',"SELECT 1 FROM tblLogin WHERE txtuname = '"+name+"' AND txtpwd ='"+Mobile+"';")
      if len(results) >0:
        data['msg']='Success'
      else:
        raise Exception("No Such user!")
    except Exception as e:
      data['msg'] = str(e)
    return JsonResponse(data)

"""@csrf_exempt
def chat_gpt_functions(request):
  data = {}
  if request.method == "POST":
    imageQuery = request.POST['imageQuery']
    imageSize = request.POST['imageSize']
    queryType=request.POST['queryType']
    noofOutput = request.POST['noofOutput']
    try:
        openai.api_key = "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"
        #Feature 1
        # response = openai.Completion.create(
        #     model="text-davinci-003",
        #     prompt="What is your age?",
        #     temperature=0.9,
        #     max_tokens=150,
        #     top_p=1,
        #     frequency_penalty=0.0,
        #     presence_penalty=0.6,
        #     stop=[" Human:", " AI:"]
        # )
        #print(response)

        if(queryType=='Prompt'):
            # Feature 2
            response = openai.Image.create(
                prompt=imageQuery,
                n=int(noofOutput),
                size=imageSize
            )
            image_url = response['data'][0]['url']
            # print(image_url)
            return JsonResponse(response)

        # Feature 3
        # response = openai.Image.create_edit(
        #     image=open("images/sun.png", "rb"),
        #     mask=open("images/mask.png", "rb"),
        #     prompt=imageQuery,#A sunlit indoor lounge area with a pool containing a flamingo
        #     n=1,
        #     size=imageSize
        # )
        # image_url = response['data'][0]['url']
        # return JsonResponse(response)

        elif (queryType == 'Variation'):
            # Feature 4
            saveVariation = request.POST['saveVariation']
            imagePath = 'images/' + imageQuery

            # tinify.key = "lqZRXCTD7WTLTzyv07CNcR8qgtclYw6x"
            # source = tinify.from_file(imagePath)
            # source.to_file('images/'+"optimized.png")
            # imageQuery="optimized.png"
            # imagePath = 'images/' + imageQuery
            response = openai.Image.create_variation(
                image=open(imagePath, "rb"),
                n=noofOutput,
                size=imageSize
            )
            image_url = response['data'][0]['url']
            if(saveVariation=="saveVariation"):
                response_data = requests.get(image_url)
                with open('images/'+"latestVariation.png", "wb") as f:
                    f.write(response_data.content)
            return JsonResponse(response)
    except Exception as e:
      data['error_message'] = str(e)
      return JsonResponse(data)
"""