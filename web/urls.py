from django.urls import path

from . import views

urlpatterns = [
    # http://localhost:8000/web/
    path('contact/', views.home, name="index"),
    path('contact/<int:contact_id>', views.contact, name="contact") # http://localhost:8000/web/contact/1
]