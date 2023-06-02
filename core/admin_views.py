from django.contrib import messages
from django.shortcuts import *
from core.models import *
from django.contrib import auth
from django.contrib.auth.decorators import *



def login_admin(request):
    return render(request, "admin_templates/admin_login.html", context = {})



def login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = auth.authenticate(username = username, password = password)
        if user != None:
            auth.login(request, user)
            company = Company_Profile.objects.filter(name = "SEMATOS")
            if company:
                return redirect("admin-dashboard")
            company = Company_Profile(name = "SEMATOS")
            company.save()
            return redirect("admin-dashboard")
        messages.error(request, "Invalid Login Details")
        return redirect(request.META.get("HTTP_REFERER"))



def logout(request):
    auth.logout(request)
    return redirect("home-page")


@login_required
def admin_home(request):
    try:
        company = Company_Profile.objects.get(id = 1)
        leads = Leads.objects.all().count()
        list = List.objects.all().count()
        total = leads + list
        zero_error = list + leads
        if zero_error == 0:
            zero_error = 1
        won_per = (leads / zero_error) * 100
        context = {"company":company, "leads":leads, "list":list, "won_per":won_per, "total":total}
    except:
        leads = Leads.objects.all().count()
        list = List.objects.all().count()
        total = leads + list
        won_per = (leads / (list + leads)) * 100
        context = {"leads":leads, "list":list, "won_per":won_per, "total":total}
    return render(request, "admin_templates/admin_home.html", context)



@login_required
def admin_about_details(request, company_id):
    company = Company_Profile.objects.get(id = company_id)
    about = Company_About.objects.get(company = company)
    context = {"company":company, "about":about}
    return render(request, "admin_templates/admin_about_details.html", context)



@login_required
def admin_contact(request, company_id):
    company = Company_Profile.objects.get(id = company_id)
    contact = Company_Contact.objects.get(company = company)
    context = {"company":company, "contact":contact}
    return render(request, "admin_templates/admin_contact_details.html", context)



@login_required
def admin_messages(request):
    company = Company_Profile.objects.get(id = 1)
    messages = Leads.objects.all()
    context = {"company":company, "messages":messages}
    return render(request, "admin_templates/admin_messages.html", context)


@login_required
def admin_list(request):
    company = Company_Profile.objects.get(id = 1)
    list = List.objects.all()
    context = {"company":company, "list":list}
    return render(request, "admin_templates/admin_list.html", context)


@login_required
def admin_leads(request):
    company = Company_Profile.objects.get(id = 1)
    leads = Leads.objects.all()
    context = {"company":company, "leads":leads}
    return render(request, "admin_templates/admin_leads.html", context)


@login_required
def add_company(request):
    company = Company_Profile.objects.get(id = 1)
    context = {"company":company}
    return render(request, "admin_templates/add_company.html", context)



def add_company_save(request):
    if request.method == "POST":
        name = request.POST.get("name")
        try:
            company = Company_Profile(name = name)
            company.save() 
            messages.success(request, "Successfully Added " + str(name))
            return redirect(request.META.get("HTTP_REFERER"))
        except:
            messages.error(request, "Add Company Failed")
            return redirect(request.META.get("HTTP_REFERER"))



def admin_contact_update_save(request):
    if request.method == "POST":
        email_address = request.POST.get("email_address")
        company_phone = request.POST.get("company_phone")
        office_address = request.POST.get("office_address")
        try:
            company                             = Company_Profile.objects.get(id = 1)
            company_contact                     = Company_Contact.objects.get(company = company)
            company_contact.email               = email_address
            company_contact.phone_no            = company_phone
            company_contact.address             = office_address
            company_contact.save()

            messages.success(request, "Successfully Updated SEMATOS Contact")
            return redirect(request.META.get("HTTP_REFERER"))
        except:
            messages.error(request, "Update Contact Failed")
            return redirect(request.META.get("HTTP_REFERER"))




def admin_about_update_save(request):
    if request.method == "POST":
        about_us = request.POST.get("about_us")
        our_mission = request.POST.get("our_mission")
        our_vision = request.POST.get("our_vision")
        brief_description = request.POST.get("brief_description")
        core_values = request.POST.get("core_values")
        try:
            company                     = Company_Profile.objects.get(id = 1)
            company_about               = Company_About.objects.get(company = company)
            company_about.about_us      = about_us
            company_about.our_mission   = our_mission
            company_about.our_vision    = our_vision
            company_about.brief_description   = brief_description
            company_about.core_values   = core_values
            company_about.save()
            messages.success(request, "Successfully Updated SEMATOS BIO")
            return redirect(request.META.get("HTTP_REFERER"))
        except:
            messages.error(request, "Update BIO Failed")
            return redirect(request.META.get("HTTP_REFERER"))



@login_required
def message_details(request, message_id):
    message = Leads.objects.get(id = message_id)
    company = Company_Profile.objects.get(id = 1)
    context = {"message":message, "company":company}
    return render(request, "admin_templates/message_details.html", context)



@login_required
def delete_message(request, message_id):
    message = Leads.objects.get(id = message_id)
    message.delete()
    return redirect(request.META.get("HTTP_REFERER"))





