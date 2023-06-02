from django.db import models
from django.db.models.fields import AutoField, EmailField



class Leads(models.Model):
    full_name = models.CharField(max_length=50)
    phone_no = models.CharField(max_length=15)
    email = models.EmailField(max_length=50)
    subject = models.CharField(max_length=20)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.email} - {self.subject}"

    def show_message(self):
        return f"{self.message[:30]} ..."

    def show_subject(self):
        return f"{self.message[:30]} ..."



class List(models.Model):
    email = models.EmailField(max_length=255)

    def __str__(self):
        return f"{self.email}"


class Company_Profile(models.Model):
    id = AutoField(primary_key=True)
    name = models.CharField(max_length=15)

    def __str__(self):
        return f"{self.id} - {self.name}"


class Company_About(models.Model):
    company             = models.ForeignKey(Company_Profile, on_delete=models.CASCADE)
    about_us            = models.TextField(max_length=500, null = True, blank = True)
    our_mission         = models.TextField(max_length=500, null = True, blank = True)
    our_vision          = models.TextField(max_length=500, null = True, blank = True)
    brief_description   = models.TextField(max_length=500, null = True, blank = True)
    core_values         = models.TextField(max_length=500, null = True, blank = True)


    def __str__(self):
        return f"{self.company.id} - {self.company.name}"


class Company_Contact(models.Model):
    company             = models.ForeignKey(Company_Profile, on_delete=models.CASCADE)
    email               = models.CharField(max_length=50, null = True, blank = True)
    phone_no            = models.CharField(max_length=50, null = True, blank = True)
    address             = models.CharField(max_length=50, null = True, blank = True)
    

    def __str__(self):
        return f"{self.company.id} - {self.company.name}"
