from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.template import RequestContext
from cartapp.models import RegisterUsers


def index(request):
    return render_to_response("index.html", context_instance = RequestContext(request))

def register(request):
    if request.method == "POST":
        firstname = request.POST['first_name']
        print firstname
        lastname = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        address = request.POST['address']
        phone = request.POST['phone']
        city = request.POST['city']
        zipcode = request.POST['zipcode']
        country = request.POST['country']
        print firstname, lastname,email,password,address,phone,city,zipcode,country
        # password = hashlib.md5(pword).hexdigest()
        # print(password)
        registration = RegisterUsers(
            firstname = firstname,
            lastname =lastname,
            # password = md5_crypt.encrypt(pword),
            # password = hashlib.md5(pword),
            # password = hashlib.new(pword).hexdigest(),
            email= email,
            password= password,
            address = address,
            contact = phone,
            city = city,
            zipcode = zipcode,
            country = country

        )
        registration.save()
        return render_to_response("register.html", {'mess': 'Registration successfully Completed', 'status': 'True'},
                                      context_instance=RequestContext(request))
    else:
        return render_to_response("register.html", context_instance=RequestContext(request))

    return render_to_response("register.html", context_instance = RequestContext(request))

def contact(request):
    return render_to_response("contact.html", context_instance = RequestContext(request))

def collection(request):
    return render_to_response("collection.html", context_instance = RequestContext(request))

def aboutUs(request):
    return render_to_response("about-us.html", context_instance=RequestContext(request))

# @csrf_protect
# def register(request):
#     if request.method == 'POST':
#         form = RegistrationForm(request.POST)
#         if form.is_valid():
#             user = User.objects.create_user(
#                 username=form.cleaned_data['username'],
#                 password=form.cleaned_data['password1'],
#                 email=form.cleaned_data['email']
#             )
#             return HttpResponseRedirect('/register/success/')
#     else:
#         form = RegistrationForm()
#     variables = RequestContext(request, {
#         'form': form
#     })
#
#     return render_to_response(
#         'registration/register.html',
#         variables,
#     )
#
#
# def register_success(request):
#     return render_to_response(
#         'registration/success.html',
#     )
#
#
# def logout_page(request):
#     logout(request)
#     return HttpResponseRedirect('/')
#
#
# @login_required
# def home(request):
#     return render_to_response(
#         'home.html',
#         {'user': request.user}
#     )