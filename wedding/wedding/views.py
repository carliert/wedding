from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse,HttpResponseRedirect
from django import forms

from wedding.models import Guest, GuestPost

@csrf_exempt
def home(request):
    book = GuestPost.objects.all().order_by('-created_date')
    if request.method == 'POST':
        if 'guestbook' in request.POST:
            form = GuestBookForm(request.POST)
            if form.is_valid():
                name = form.cleaned_data['name']
                email = form.cleaned_data['email']
                body = form.cleaned_data['body']
                g = GuestPost(name=name,email=email,body=body)
                g.save()
                return HttpResponseRedirect('/#guestbook')
        else:
            form = GuestForm(request.POST)
            if form.is_valid():
                name = form.cleaned_data['name']
                email = form.cleaned_data['email']
                guests = form.cleaned_data['guests']
                g = Guest(name=name,email=email,guests=guests)
                g.save()
                return HttpResponseRedirect('/#rsvp')
    return render_to_response("index.html",{'book':book})

class GuestForm(forms.Form):
    name = forms.CharField(label='Nom', max_length=300)
    email = forms.EmailField(label='Email')
    guests = forms.IntegerField(label='Invite')

class GuestBookForm(forms.Form):
    name = forms.CharField(label='Nom', max_length=300)
    email = forms.EmailField(label='Email')
    body = forms.CharField(label='Contenu', max_length=5000)