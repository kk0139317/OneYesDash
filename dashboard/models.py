from django.db import models
from django.contrib.auth.models import User

class Datasets(models.Model):
    end_year = models.IntegerField(null=True, default=None)
    intensity = models.IntegerField(null=True, default=None)
    sector = models.CharField(max_length=20, null=True, default=None)
    topic = models.CharField(max_length=20, null=True, default=None)
    insight = models.CharField(max_length=250, null=True, default=None)
    url = models.CharField(max_length=250, null=True, default=None)
    region = models.CharField(max_length=50, null=True, default=None)
    start_year = models.IntegerField(null=True, default=None)
    impact = models.IntegerField(null=True, default=None)
    added = models.DateTimeField(null=True, default=None)
    published = models.DateTimeField(null=True, default=None)
    country = models.CharField(max_length=100, null=True, default=None)
    relevance = models.IntegerField(null=True, default=None)
    pestle = models.CharField(max_length=50, null=True, default=None)
    source = models.CharField(max_length=50, null=True, default=None)
    title = models.CharField(max_length=250, null=True, default=None)
    likelihood = models.IntegerField(null=True, default=None)

class CompanyGrowth(models.Model):
    year = models.IntegerField(null=True, default=None)
    growth = models.IntegerField(null=True, default=None)
    expences = models.IntegerField(null=True, default=None)
    profit = models.IntegerField(null=True, default=None)
    
class ChatApp(models.Model):
    sender  = models.CharField(max_length=30)
    recever = models.CharField(max_length=30)
    chat = models.TextField()
    Date_time = models.DateTimeField(auto_now_add=True)
    room_id = models.CharField(null=True, max_length=100)
    
class Chating(models.Model):
    sender  = models.CharField(max_length=30)
    recever = models.CharField(max_length=30)
    chat = models.TextField(null=True)
    file = models.FileField(null=True)
    Date_time = models.DateTimeField(auto_now_add=True)
    room_id = models.CharField(null=True, max_length=100)

class Resister(models.Model):
    id = models.AutoField(primary_key=True, auto_created=True)
    user_types = models.CharField(max_length=100)
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    password = models.CharField(max_length=255)
    confirm_password = models.CharField(max_length=255)

    def __str__(self):
        return self.email
    
    