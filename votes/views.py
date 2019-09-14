from django.http import JsonResponse
from django.shortcuts import render, redirect
from .models import Caketang, Pemilih
from django.core import serializers
from django.contrib.admin.views.decorators import staff_member_required
import json 
from datetime import datetime
import binascii, os
import re

def index(request):
    return redirect('token')

def token(request):
    return render(request, 'votes/token.html', None)

def vote(request):
    nimCookie = request.COOKIES.get('nim')
    tokenCookie = request.COOKIES.get('token')
    if nimCookie == None and tokenCookie == None:
        return redirect('token')
    cktJson = serializers.serialize('json',Caketang.objects.all())
    cktContext = { 'caketangJSON': cktJson }
    return render(request, 'votes/vote.html', cktContext)

def check_token(request):
    identity = json.loads(request.body)
    pemilih = Pemilih.objects.filter(nim=identity['nim'])
    if len(pemilih) > 0:
        pemilih = pemilih[0]
        if pemilih.hasvoted == True:
            retcode = 1
            retmes = 'You have already voted!'
        if pemilih.token == '':
            retcode = 1
            retmes = 'Invalid token in db, please contact admin'
        elif pemilih.token == identity['token']:
            retcode = 4
            retmes = 'Success!'
        else:
            retcode = 1
            retmes = 'Token invalid!'
    else:
        retcode = 1
        retmes = 'not registered as voter.'
    response = JsonResponse({'code': retcode, 'return': retmes})
    if retcode == 4:
        response.set_cookie('token', identity['token'])
        response.set_cookie('nim', identity['nim'])
    return response

def submit_vote(request):
    data = json.loads(request.body) 
    if len(data) > 0:
        submit_date = datetime.now()
        currentVote = data['current_vote']
        nim = data['nim']
        token = data['token']
        ckt = Caketang.objects.get(pk=currentVote)
        pil = Pemilih.objects.get(nim=nim, token=token)
        pil.hasvoted = True
        pil.date = submit_date
        pil.vote = ckt
        pil.save()
        response = JsonResponse({'nim':nim, 'token':token, 'pub_date':submit_date, 'currentVote':currentVote,'redirect_to': '/'})
        response.delete_cookie('nim')
        response.delete_cookie('token')
        return response

@staff_member_required
def generate_token(request):
    niminput = json.loads(request.body)["nim"]
    pemilih = Pemilih.objects.filter(nim = niminput)[0]
    if pemilih.token:
        return JsonResponse({'token': pemilih.token})
    all_pemilih = Pemilih.objects.all()
    def gen():
        return binascii.hexlify(os.urandom(2)).decode()
    gen_token = gen()
    while(len(all_pemilih.filter(token=gen_token))>0):
        gen_token = gen()
    pemilih.token = gen_token 
    pemilih.save()
    return JsonResponse({'token': gen_token})

@staff_member_required
def generate_token_page(request):
    return render(request, 'token_generator.html')

# Create your views here.
