from django.shortcuts import render, render_to_response
from django.template import RequestContext
#from loanapp.models import AuthUsers, LoanEntries,LoanEligibility
def index(request):
    return render_to_response("index.html", context_instance = RequestContext(request))