from django.shortcuts import render
from . import forms

# Create your views here.
def index(request):
    return render(request, 'basicapp/index.html')

def my_form_view(request):
    form = forms.MyForm()

    if request.method == 'POST':
        form = forms.MyForm(request.POST)
        if form.is_valid():
            print('Validation success')
            print(
                f'Name: {form.cleaned_data["name"]}',
                f'Email: {form.cleaned_data["email"]}',
                f'Text: {form.cleaned_data["text"]}',
                sep='\n'
            )

    return render(request, 'basicapp/form_page.html', {'form': form})
