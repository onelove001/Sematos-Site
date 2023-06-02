"""sematos URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""


from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from core.views import *
from core.admin_views import *

urlpatterns = [
    
    # User urls 
    path('admin/', admin.site.urls),
    path("", home_page, name = 'home-page'),
    path("about", about_us, name = 'about-us'),
    path("contact", contact_us, name = 'contact-us'),
    path("services", services, name = 'our-services'),
    path("lead", lead_gen, name = 'lead-gen'),
    path("list", list_gen, name = 'list-gen'),
    path("lead_gen_save", lead_gen_save, name = 'lead-gen-save'),
    path("list_gen_save", list_gen_save, name = 'list-gen-save'),

    # Admin Urls 
    path("login_admin", login_admin, name = 'login-admin'),
    path("login", login, name = 'login'),
    path("logout", logout, name = 'logout'),
    path("admin_dashboard", admin_home, name = 'admin-dashboard'),
    path("admin_contact/<str:company_id>", admin_contact, name = 'admin-contact'),
    path("admin_about_details/<str:company_id>", admin_about_details, name = 'admin-about-details'),
    path("admin_messages", admin_messages, name = 'admin-messages'),
    path("message_details/<str:message_id>", message_details, name = 'message-details'),
    path("delete_message/<str:message_id>", delete_message, name = 'delete-message'),
    path("admin_list", admin_list, name = 'admin-list'),
    path("admin_leads", admin_leads, name = 'admin-leads'),
    path("admin_contact_update_save", admin_contact_update_save, name = 'admin-contact-save'),
    path("admin_about_update_save", admin_about_update_save, name = 'admin-about-save'),
    path("add_company", add_company, name = 'add-company'),
    path("add_company_save", add_company_save, name = 'add-company-save'),


]


urlpatterns+=static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
urlpatterns+=static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)