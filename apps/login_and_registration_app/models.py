# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
import bcrypt
import re


LETTERS_ONLY = re.compile(r'[A-Za-z]')

# Create your models here.
class UserManager(models.Manager):
    #handles validations & database queries
    def validate_and_create(self,data):
        print data, "<<--here is the data from the validations and/or database"

        replicated = User.objects.filter(username=data['username'])

        errors = []
        #validate first name (2+ char/ Letters only/ cannot be empty)
        if len(data['name']) < 3:
            print "Name must be at least 3 characters"
            errors.append("Name must be at least 3 characters")
        #validate last name (2+ char/ Letters only/ cannot be empty)
        if len(data['username']) < 3:
            print "Username must be at least 3 characters"
            errors.append("Username must be at least 3 characters")
        if len(data['password']) < 8:
            print "Password must be at least 8 characters long"
            errors.append("Password must be at least 8 characters long")
        #validate password confirmation(match password)
        if data['password'] != data['password_confirmation']:
            print "Passwords do not match"
            errors.append("Passwords do not match")

        if errors:
            return (False, errors)
        else:
            #Bcrypt encryption
            pw = data['password']
            hashed_pw = bcrypt.hashpw(pw.encode(), bcrypt.gensalt())

            new_object = User.objects.create(
                name = data['name'],
                username = data['username'],
                password = hashed_pw, #<---HASHED PASSWORD
            )
            return (True, new_object)
    def validate_and_login(self,data):
        User_Exists = User.objects.filter(username=data['username'])
        print User_Exists, "<--- replicated"
        errors = []
        #Check to see if username entered is in database
        if len(User_Exists) == 0:
            print "Invalid username/password combo"
            errors.append("Invalid username/password combo")
        #validate password (at least 8 characters/ cannot be empty)
        if len(data['password']) < 8:
            print "Password must be at least 8 characters long"
            errors.append("Password must be at least 8 characters long")
        if errors:
            return (False, errors)
        else:
            login_user = User.objects.get(username=data['username'])
            pw = data['password']

            # hashed_pw = bcrypt.hashpw(pw.encode(), bcrypt.gensalt())
            if bcrypt.hashpw(pw.encode(), login_user.password.encode()) == login_user.password.encode():
            # if bcrypt.checkpw(pw.encode(), login_user.password.encode()):
                print "the passwords match"
                return (True, login_user)
            else:
                print "the passwords DONT match"
                errors.append("the passwords DONT match")
                return (False, errors)

class User(models.Model):
    name = models.CharField(max_length = 75)
    username = models.CharField(max_length = 75)
    password = models.CharField(max_length = 255)
    created_at = models.DateField(auto_now_add=True)
    created_at = models.DateField(auto_now=True)

    objects = UserManager()
