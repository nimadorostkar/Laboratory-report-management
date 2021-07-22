from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render, get_object_or_404, redirect
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from django import template
from . import models
from django.contrib.auth.models import User
from .forms import UserForm
from django.urls import reverse







@login_required()
def index(request):
    a = "n"
    context = { 'a': a }
    return render(request, 'index.html', context)





@login_required()
def about(request):
    a = "n"
    context = { 'a': a }
    return render(request, 'about.html', context)





@login_required()
def pages(request):
    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:

        load_template      = request.path.split('/')[-1]
        context['segment'] = load_template

        html_template = loader.get_template( load_template )
        return HttpResponse(html_template.render(context, request))

    except template.TemplateDoesNotExist:

        html_template = loader.get_template( 'page-404.html' )
        return HttpResponse(html_template.render(context, request))

    except:

        html_template = loader.get_template( 'page-500.html' )
        return HttpResponse(html_template.render(context, request))





@login_required
def profile(request):
  if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        if user_form.is_valid():
            username = user_form.cleaned_data['username']
            first_name = user_form.cleaned_data['first_name']
            last_name = user_form.cleaned_data['last_name']
            email = user_form.cleaned_data['email']
            password1 = user_form.cleaned_data['password1']
            password2 = user_form.cleaned_data['password2']
            user_form.save()
            context = {'user_form': user_form }
            return render(request, 'profile.html', context)
  else:
      user_form = UserForm(instance=request.user)

  context = { 'user_form': user_form }
  return render(request, 'profile.html', context)











#End
