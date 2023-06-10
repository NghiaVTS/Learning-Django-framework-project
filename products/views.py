from django.shortcuts import render
from datetime import date
from django.http import HttpResponse
from .forms import SignUpTable
from django.template import loader
from .models import Submit
from django.contrib import messages
# Create your views here.


def index(request):
    user = "tom"
    num = 4
    return render(request, "products/home.html", {
        "name": user,
        "number": num,
    })


def aboutUs(request):
    return render(request, "products/aboutus.html")


def services(request):
    return render(request, "products/services.html")


def events(request):
    return render(request, "products/events.html")


def menu(request):
    return render(request, "products/menu.html")


def diemden(request):
    return render(request, "products/diemden.html")

def thuvien(request):
    return render(request, "products/thuvien.html")

def lienhe(request):
    return render(request, "products/lienhe.html")


def submit(request):
    form = SignUpTable()
    if request.method == "GET":
        return render(request, "products/submit.html", {
            "form": form
        })
    else:
        form = SignUpTable(request.POST)
        if form.is_valid():
            submit = Submit(
                name=form.cleaned_data["name"],
                phoneNumber=form.cleaned_data["phoneNumber"],
                ammount=form.cleaned_data["ammount"],
                date=form.cleaned_data["date"],
                time=form.cleaned_data["time"]
            )
            submit.save()
            messages.success(
                request, "Đặt bàn thành công. Vui lòng có mặt để check-in trước hẹn 15 phút.")
            form = SignUpTable()
        return render(request, "products/submit.html", {
            "form": form
        })


def testing(request):
    submit = Submit.objects.all().values()
    template = loader.get_template('products/submited.html')
    context = {
        'submit': submit,
    }
    return HttpResponse(template.render(context, request))


def day_filter(request):
    today = []
    submit = Submit.objects.all().values()
    template2 = loader.get_template('products/submited_today.html')
    for x in submit:
        if x['date'] == date.today():
            today.append(x)

    data = {
        'today': today,
    }
    return HttpResponse(template2.render(data, request))


def product_cat(request, product):
    if product == "suits" or product == "dresses" or product == "shirts" or product == "shoes":
        return HttpResponse(f"Here is the list of our {product}.")
    else:
        return HttpResponse("Page your are looking doesn't exist!")
