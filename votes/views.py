from django.http import JsonResponse
from django.shortcuts import render
from .models import Caketang, Pemilih 
from django.core import serializers
import json, DateTime

def index(request):
    return render(request, 'votes/token.html', None)

def vote(request):
    cktJson = serializers.serialize('json',Caketang.objects.all())
    cktContext = { 'caketangJSON': cktJson }
    return render(request, 'votes/vote.html', cktContext)

def check_token(request):
    identity = json.loads(request.body)
    if identity['token'] == 'abcd':
        retcode = 4
        retmes = 'success'
    else:
        retcode = 1
        retmes = 'fail'
    response = JsonResponse({'code': retcode, 'return': retmes})

    if retcode == 4:
        response.set_cookie('token', identity['token'])
        response.set_cookie('nim', identity['nim'])
    return response

def submit_vote(request):
    data = json.loads(request)
    if data != None:
        submit_date = DateTime.now()


# Create your views here.
