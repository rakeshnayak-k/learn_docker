from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
import json

# Create your views here.
def func_based_view(request):
    res = {'msg': "hello world"}
    res_json = json.dumps(res)
    return HttpResponse(res_json, content_type='application/json')