from django.http import HttpResponse
from django.template import loader

from web.models import Contact, ContactNumber

def home(request):
    """Renders a list of contacts"""
    contacts_list = Contact.objects.all()

    template = loader.get_template("web/index.html")
    context = {
        'contacts_list': contacts_list
    }

    return HttpResponse(template.render(context, request))

def contact(request, contact_id):
    """Renders a inidividual contact based on ID"""
    return HttpResponse(f"Contact id is {contact_id}")
