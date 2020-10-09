from django.shortcuts import render, redirect
from .models import Dolist
from .forms import InputForm
# Create your views here.


def show_todo_list(request):
    myarr = Dolist.objects.all()
    i_form = InputForm(request.POST or None)

    if 'submit_i_form' in request.POST:
        if(i_form.is_valid()):
            i_form.save()
            i_form = InputForm()
        return redirect('/')

    para = {
        'todolist': myarr,
        'i_form': i_form
    }
    return render(request, "todo/home.html", para)


def update_item(request, pkk):
    talk = Dolist.objects.get(pk=pkk)

    ui_form = InputForm(request.POST or None, instance=talk)

    if 'submit_ui_form' in request.POST:
        print(request.POST)
        if(ui_form.is_valid()):
            print("here")
            ui_form.save()
            ui_form = InputForm()
            return redirect('/')

    para = {
        'talk': talk,
        'ui_form': ui_form
    }

    return render(request, "todo/update.html", para)


def delete_item(request, pkk):
    talk = Dolist.objects.get(pk=pkk)

    if 'submit_d_form' in request.POST:
        talk.delete()
        return redirect('/')

    para = {
        'talk': talk,
    }

    return render(request, "todo/delete.html", para)
