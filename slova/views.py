# coding: utf-8

from django.shortcuts import RequestContext, Http404, redirect, render_to_response, HttpResponseRedirect
from django.template.response import SimpleTemplateResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import ensure_csrf_cookie
from django.http import JsonResponse
from slova.models import Slova
from slova.forms import AddNewWordForm


def hello(request):
    return render_to_response('hello.html', RequestContext(request))


@login_required(login_url='/login/')
def grid(request):
    context = RequestContext(request)

    table = Slova.objects.filter(user__email=request.user.email)
    return render_to_response('grid.html', {'table': table}, context)


def add_word(request):
    context = RequestContext(request)

    if request.method == 'POST':
        form = AddNewWordForm(request.POST)
        if form.is_valid():
            word = form.save(commit=False)
            # commit=False tells Django that "Don't send this to database yet.
            # I have more things I want to do with it."
            word.user = request.user # Set the user object here
            word.save() # Now you can send it to DB
            return HttpResponseRedirect('/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = AddNewWordForm()

    return render_to_response('addword.html', {'form': form}, context)


@ensure_csrf_cookie
def delete_word(request):
    if request.is_ajax() and request.method == u'GET':
        GET = request.GET
        if 'pk' in GET:
            pk = int(GET['pk'])
            Slova.objects.get(pk=pk).delete()



@ensure_csrf_cookie
def change_points(request):
    if request.is_ajax() and request.method == u'GET':
        GET = request.GET
        if 'accumulated_points' in GET and 'pk' in GET:
            accumulated_points = int(GET['accumulated_points'])
            pk = int(GET['pk'])

            slovo = Slova.objects.get(pk=pk)
            slovo.points += accumulated_points
            slovo.save()

            points = Slova.objects.get(pk=pk).points

            results = {'points': points}
            return JsonResponse(results)

