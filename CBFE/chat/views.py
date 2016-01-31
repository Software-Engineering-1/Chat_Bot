from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
# Create your views here.
def interact(request):
    template = loader.get_template('chat/chat.html')
    context={'state':1}
    return HttpResponse(template.render(context,request))