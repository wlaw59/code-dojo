from django.shortcuts import render, HttpResponse
def index(request):
    return render(request, 'index.html')
def new(request):
    return HttpResponse('this is the new route')



def name(request, my_name):
    context={
        'name':my_name
    }

    return render(request, 'name.html', context)