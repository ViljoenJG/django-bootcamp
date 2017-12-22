from django.shortcuts import render
from django.http import HttpResponse
from apptwo.models import User

# Create your views here.
def index(request):
    return HttpResponse('<em>My second app</em>')

def users(request):
    user_list = User.objects.order_by('first_name')
    user_dict = {'user_list': user_list}
    return render(request, 'users.html', context=user_dict)

def help(request):
    my_dict = {'my_help': 'Check yourself, before you wreck yourself'}
    return render(request, 'help.html', context=my_dict)
