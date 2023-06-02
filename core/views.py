from django.contrib import messages
from django.shortcuts import *
from core.models import *

# Create your views here.


def home_page(request):
    about = Company_About.objects.all()
    about_count = Company_About.objects.all().count()

    if about_count > 0 and about.first().our_mission is not None:
        aboutt = about.first()
        about_mission = aboutt.our_mission[:40]
        about_vision = aboutt.our_vision[:40]
        core_values = aboutt.core_values[:40]
        context = {"about_mission":about_mission, "about_vision":about_vision, "core_values":core_values}

    elif about_count > 0 and about.first().our_mission is None:
        context = {"about_mission":"...", "about_vision":"...", "core_values":"..."}

    else:
        context = {}
    return render(request, "user_templates/home_page.html", context)



def about_us(request):
    about = Company_About.objects.all()
    aboutt = about.first()
    context = {"aboutt":aboutt}
    return render(request, "user_templates/about_us.html", context)



def services(request):

    context = {}
    return render(request, "user_templates/our_services.html", context)



def contact_us(request):
    contact = Company_Contact.objects.all()
    contactt = contact.first()
    context = {"contacct":contactt}
    return render(request, "user_templates/contact_us.html", context)



def lead_gen(request):

    context = {}
    return render(request, "user_templates/lead_gen.html", context)



def list_gen(request):

    context = {}
    return render(request, "user_templates/list_gen.html", context)



def list_gen_save(request):
    if request.method == "POST":
        email = request.POST.get("email")
        try:
            list_email = List(email = email)
            list_email.save()
            messages.success(request, "Request Submitted Successfully")
            return redirect(request.META.get("HTTP_REFERER"))
        except:
            messages.errors(request, "Invalid Request")
            return redirect(request.META.get("HTTP_REFERER"))



def lead_gen_save(request):
      if request.method == "POST":
        full_name = request.POST.get("full_name")
        email = request.POST.get("email")
        subject = request.POST.get("subject")
        phone_no = request.POST.get("phone_no")
        message = request.POST.get("message_body")
        try:
            leads = Leads(full_name = full_name, email = email, phone_no = phone_no, subject = subject, message = message)
            leads.save()
            messages.success(request, "Your Message Has Submitted Successfully")
            return redirect(request.META.get("HTTP_REFERER"))
        except:
            messages.error(request, "Invalid Request")
            return redirect(request.META.get("HTTP_REFERER"))

