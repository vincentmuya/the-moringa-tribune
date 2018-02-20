from django.db import models

#Editors Model
class Editor(models.Models):
    first_name = models.CharField(max_length = 30)
    last_name = models.CharField(max_length = 30)
    email = models.EmailFiled()
