from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    my_dict = {'insert_me': 'I just added new content here'}
    return render(request, 'index.html', context=my_dict)
