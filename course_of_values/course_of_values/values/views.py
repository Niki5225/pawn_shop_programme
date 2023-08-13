from django.shortcuts import render, redirect
from django.views import generic as views

from course_of_values.values.forms import GetPriceBuyingForm


# Create your views here.

class IndexView(views.TemplateView):
    template_name = 'index.html'


def buying(request):
    if request.method == 'GET':
        form = GetPriceBuyingForm()
    else:
        form = GetPriceBuyingForm(request.POST)
        if form.is_valid():
            form.save()

    context = {
        'form': form,
    }
    return render(request, 'buying.html', context)


def selling(request):
    return render(request, 'selling.html')
