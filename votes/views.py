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
    token_in_db = Token.objects.filter(token=identity['token'])
    nim_in_db = Pemilih.objects.filter(nim=identity['nim'], token__isnull=False)
    if len(nim_in_db) > 0:
        retcode = 1
        retmes = 'you have already voted!'
    elif len(token_in_db) == 1:
        if not token_in_db[0].used:
            retcode = 4
            retmes = 'success'
        else:
            retcode = 1
            retmes = 'token has been used.'
    else:
        retcode = 1
        retmes = 'token invalid.'
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
        current_token = Token.objects.get(token=token)
        current_token.used = True
        current_token.save()
        ckt = Caketang.objects.get(pk=currentVote)
        pil = Pemilih(nim=nim, token=current_token, date=submit_date, vote=ckt)
        pil.save()
        response = JsonResponse({'nim':nim, 'token':token, 'pub_date':submit_date, 'currentVote':currentVote, 'redirect_to': '/'})
        response.delete_cookie('nim')
        response.delete_cookie('token')
        return response

@staff_member_required
def generate_token(request):
    niminput = json.loads(request.body["nim"])
    pemilih = Pemilih.objects.filter(nim = nim) 
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
