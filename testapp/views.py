from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
def get_example(request, a):
    response = {"mensaje": a}
    return JsonResponse(response, safe=False, json_dumps_params={'indent': 2})