from django.template import loader
from django.http import HttpResponse
from datetime import datetime
from django.contrib.auth.decorators import login_required

# Create your views here.

def members(request):
    template = loader.get_template('myfirst.html')
    context = {
        'date': datetime.today()
    }
    return HttpResponse(template.render(context, request))

@login_required(login_url='/admin')

def authorized(request):
    tem = loader.get_template('authorized.html')
    cont = {}
    return HttpResponse(tem.render(cont, request))