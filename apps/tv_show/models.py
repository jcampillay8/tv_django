from __future__ import unicode_literals
# import re
from django.db import models
import datetime
import re

DATE_REGEX = re.compile(r'^([12]\d{3}-(0[1-9]|1[0-2])-(0[1-9]|[12]\d|3[01]))')

class ShowManager(models.Manager):
    def validator(self, postData):
        errors = {}
        # print('Hola validator')
        print(postData['release_date'])

        if(len(postData['title'])) < 2:
            errors['title'] = "El titulo debe tener a los menos 2 caracteres"
        
        if(len(postData['network'])) < 3:
            errors['network'] = "El network debe tener a los menos 3 caracteres"
        
        # if len(postData['release_date']<=8):
        #     errors['release_date'] = "Fecha lanzamiento no tiene largo correcto"
        
        if len(postData['release_date']) < 1:
            errors['release_date'] = "release_date cannot be blank"
        elif not DATE_REGEX.match(postData['release_date']):
            errors['release_date'] = "Invalid date, use dd-mm-yyyy format"
        else:
            current_time = datetime.datetime.now()
            temp_time = datetime.datetime.strptime(postData['release_date'], "%Y-%m-%d")
            if temp_time >= current_time:
                errors['release_date'] = "Invalid date, cannot be equal or in the future"
        
        if len(postData['description']) < 10:
            errors['description'] = "La descripción debe tener a los menos 3 caracteres"
        
        return errors

class Show(models.Model):
    title = models.CharField(max_length=250)
    network = models.CharField(max_length=250)
    release_date = models.DateField(auto_now_add = False, auto_now= False, blank= True)
    description = models.CharField(max_length=500, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ShowManager()