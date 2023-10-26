from django.urls import path
from . import views

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('contact_form', views.contact_form, name='contact_form'),
    path('faq', views.faq, name='faq'),
    path('feedback', views.feedback, name='feedback'),
    path('signup', views.signup, name='signup'),
    path('login', views.login, name='login'),
    path('prompt', views.prompt, name='prompt'),
    path('client_interface', views.client_interface, name='client_interface'),

]




 
