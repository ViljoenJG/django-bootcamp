from django.shortcuts import render
from django.http import HttpResponse
from first_app.models import AccessRecord, Topic, Webpage

# Create your views here.
def index(request):
    page_list = AccessRecord.objects.order_by('date')
    date_dict = {'access_records': page_list}
    return render(request, 'index.html', context=date_dict)
