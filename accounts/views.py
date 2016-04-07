# coding: utf-8
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from django.template.context_processors import csrf


from .forms import UserRegistrationForm
from slova.models import Slova

def user_registration(request):
    """
    User account registration view.
    """
    context = RequestContext(request)

    #check if user is already logged in and if he is redirect him to some other url, e.g. home
    if request.user.is_authenticated():
        messages.add_message(request, messages.SUCCESS, 'You are already registered!')
        return HttpResponseRedirect('/grid/')

    if request.method == 'POST':
        form = UserRegistrationForm(data=request.POST)
        #email, password = request.POST['email'], request.POST['password']
        if form.is_valid():
            user = form.save()
            #user.save()
            registered = True

            slovo = Slova(rus='Привет!', eng="Hello!", user=user)
            slovo.save()

            # #Send email about new user accounts
            # send_mail('Новая заявка на регистрацию!',                                       # subject
            #           u'Регистрация! Email: '+user.email+u' Website: '+user.website,        # тело письма
            #           'from@django.com',                                                    # from
            #           ['mr.swasher@gmail.com', 'wscip@ukr.net'],                            # to
            #           fail_silently=False)

            ###   Immediately  loggining

            user = authenticate(username=form.cleaned_data['email'], password=form.cleaned_data['password'])
            if user is not None:
                if user.is_active:
                    messages.add_message(request, messages.SUCCESS, 'You are sucessfully registered!')
                    login(request, user)
                    return HttpResponseRedirect('/grid')
                else:
                    messages.add_message(request, messages.SUCCESS, 'Your account are disabled')
                    return HttpResponseRedirect('hello')
            else:
                messages.add_message(request, messages.WARNING, 'Invalid login')
                return HttpResponseRedirect('login')
    else:
        form = UserRegistrationForm()

    # token = {}
    # token.update(csrf(request))
    # token['form'] = form

    return render_to_response('registration/registration.html', {'form': form}, context)



def user_login(request):
    if request.user.is_authenticated():
        messages.add_message(request, messages.SUCCESS, 'You are logged in already')
        return redirect('grid')

    if request.POST:
        email = request.POST['email']
        password = request.POST['password']

        user = authenticate(email=email, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                messages.add_message(request, messages.SUCCESS, 'You are sucessfully login!')
                return redirect('grid')
        else:
            messages.add_message(request, messages.WARNING, 'Login or password are incorrect')
    return render_to_response('registration/login.html', context_instance=RequestContext(request))


# def login(request):
#     context = RequestContext(request)
#     if request.method == 'POST':
#         username, password = request.POST['username'], request.POST['password']
#         user = authenticate(username=username, password=password)
#         if user is not None:
#             if user.is_active:
#                 django_login(request, user)
#                 messages.add_message(request, messages.SUCCESS, 'You are sucessfully login!')
#             else:
#                 #context['error'] = 'Non active user'
#                 messages.add_message(request, messages.INFO, 'Non active user')
#         else:
#             messages.add_message(request, messages.INFO, 'Wrong username or password')
#     return redirect('hello')
#     #return render_to_response('grid.html', ???)


def login_redirect(request):
    messages.add_message(request, messages.INFO, 'Вы должны быть зарегистрированны для выполнения этой операции.')
    return redirect('hello')


