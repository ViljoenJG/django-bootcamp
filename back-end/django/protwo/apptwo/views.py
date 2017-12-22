from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse('<em>My second app</em>')

def help(request):
    my_dict = {'my_help': 'Check yourself, before you wreck yourself'}
    return render(request, 'help.html', context=my_dict)
