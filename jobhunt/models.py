from django.db import models

from config import settings


class Company(models.Model):
    title = models.CharField(max_length=220)
    logo = models.ImageField(upload_to='/media')


class Experience(models.Model):
    company_title = models.CharField(max_length=220)
    start_date = models.DateField()
    end_date = models.DateField()
    assignment = models.CharField(max_length=250)


class Resume(models.Model):
    first_name = models.CharField(max_length=220)
    last_name = models.CharField(max_length=220)
    direction = models.CharField(max_length=220)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)


class Vacancy(models.Model):
    title = models.CharField(max_length=220)
    solary = models.IntegerField()
    location = models.CharField(max_length=220)
    description = models.CharField(max_length=500)
    tasks = models.CharField(max_length=220)
    requirement = models.CharField(max_length=220)


class Commentary(models.Model):
    text = models.TextField()
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
