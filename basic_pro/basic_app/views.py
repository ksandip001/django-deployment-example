from django.shortcuts import render
from django.http import HttpResponse
from basic_app.models import Bjp,Access
from basic_app.forms import FormName


# Create your views here.

def index(request):
    mydict = {'insert_me':'He is the Best PM of India'}
    return render(request,'basic_app/index.html',mydict)

def one(request):
    webpg_list = Bjp.objects.order_by('name')
    mydict1 = {'insert_me_2':webpg_list}

    return render(request,'basic_app/one.html',context=mydict1 )

def two(request):
    form = FormName()

    if request.method == 'POST':
        form = FormName(request.POST)

        if form.is_valid():
            form.save(commit = True)
            return index(request)
        else:
            print("Error")

    return render(request,'basic_app/two.html',{'insert_form':form})
