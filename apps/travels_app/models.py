# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.db.models import F
from ..login_and_registration_app.models import User

import datetime
now = datetime.datetime.now()

# Create your models here.
class TravelManager(models.Manager):
    def create_new_plan(self,data,user_id):
        print "Creating new plans"
        print "*************"
        print "Current time:",now

        errors = []
        #Fields cannot be empty
        if len(data['destination']) < 1:
            print "Destination cannot be empty"
            errors.append("Destination cannot be empty")
        if len(data['plan']) < 1:
            print "Plan description cannot be empty"
            errors.append("Plan description cannot be empty")
        if len(data['travel_start']) < 1:
            print "Travel start date cannot be empty"
            errors.append("Travel start date cannot be empty")
        if data['travel_end'] < data['travel_start']:
            print "Travel end date cannot be earlier than travel start date"
            errors.append("Travel end date cannot be earlier than travel start date")
        if len(data['travel_end']) < 1:
            print "Travel end date cannot be empty"
            errors.append("Travel end date cannot be empty")
        #COME BACK TO ADD DATE VALIDATIONS
        if errors:
            return(False, errors)
        else:
            print "Lets add data to database"
            user = User.objects.get(id=user_id)
            print "THIS IS THE USER ID:",user
            new_plan = Travel.objects.create(
                destination = data['destination'],
                plan = data['plan'],
                travel_start = data['travel_start'],
                travel_end = data['travel_end'],
                user_id = user
            )

            print "Plans should be added here!"
            print "NEW PLAN ------>", new_plan

            return (True, new_plan)

    def current_user(self,user_id):
        print "Getting specific user"
        current_user = User.objects.get(id=user_id)
        return current_user

    def my_travel(self,user_id):
        print "specific travel plans pulled here"
        specific_plans = Travel.objects.current_user(user_id=user_id)
        print "specific travel plans pulled here:", specific_plans.first_name
        return specific_plans

    def user_travels(self,user_id):
        #filter for user_id = user_id which is the session_id in views
        object_to_return = Travel.objects.filter(user_id=user_id)
        return object_to_return

    def other_user_travels(self,user_id):
        #filter for user_id = user_id which is the session_id in views
        object_to_return = Travel.objects.exclude(user_id=user_id)
        return object_to_return

    def join_other_trip(self,id):
        joined_trip = Travel.objects.other_user_travels(id=id)


class Travel(models.Model):
    destination = models.CharField(max_length = 75)
    plan = models.TextField()
    travel_start = models.DateTimeField()
    travel_end = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user_id = models.ForeignKey(User)

    objects = TravelManager()
