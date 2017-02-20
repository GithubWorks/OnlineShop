from django.shortcuts import render, render_to_response
from django.template import RequestContext


def index(request):
    return render_to_response("index.html", context_instance = RequestContext(request))

def register(request):
    return render_to_response("register.html", context_instance = RequestContext(request))

def contact(request):
    return render_to_response("contact.html", context_instance = RequestContext(request))

def collection(request):
    return render_to_response("collection.html", context_instance = RequestContext(request))
