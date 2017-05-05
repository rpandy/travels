# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Travel, User

# Create your views here.
def index(request):
    print "TRAVEL INDEX ROUTE"
    print "*****************"
    context = {
        'users': User.objects.all(),
        # 'plans': Travel.objects.all(),
        'current_user_plans': Travel.objects.user_travels(request.session['user_id']),
        'other_user_plans': Travel.objects.other_user_travels(request.session['user_id']),
    }
    return render(request,'travels_app/index.html', context)

def add(request):
    print "TRAVEL ADD ROUTE"
    print "*****************"

    return render(request,'travels_app/add.html')

def new(request):
    print "*****************"
    print "ADD PLANS ROUTE"
    print "request.POST:",request.POST
    print "session_user:", request.session['user_id']
    print "*****************"
    if request.method == 'POST':
        #passing two parameters into create_new_plan method - data and session
        valid, data = Travel.objects.create_new_plan(request.POST,request.session['user_id'])

        if valid == True:
            print "New plan added!"
            print "***********"
        else:
            for err in data:
                messages.error(request,err)
            return redirect('travel:add')
    else:
        return redirect('auth:index')

    return redirect('travel:index')

def join(request, id):
    pass

def destination(request, id):
    user_plans = Travel.objects.filter(id=id)#<--getting id of specific travel plan
    context = {
        'user_plans': user_plans
    }
    return render(request,'travels_app/destination.html', context)

def join(request, id):
    print "JOIN ROUTE"
    print "***********"

    return redirect('travel:index')


def logout(request):
    #passing request.POST over as request
    print "*************"
    print "Logout Route"
    print "*************"
    request.session.clear()
    return redirect('auth:index')
