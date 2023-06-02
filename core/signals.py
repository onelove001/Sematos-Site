from core.models import *
from django.dispatch import receiver
from django.db.models.signals import *


@receiver(post_save, sender = Company_Profile)
def create_about(sender, created, instance, **kwargs):
    if created:
        Company_About.objects.create(company = instance)



@receiver(post_save, sender = Company_Profile)
def create_contact(sender, created, instance, **kwargs):
    if created:
        Company_Contact.objects.create(company = instance)



