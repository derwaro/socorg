from django.http import HttpResponse
from django.shortcuts import render, redirect

from charts.models import Chart, Persona

from .forms import CreateEgoForm

# Create your views here.
def index(request):
    return HttpResponse("Hello")


def show_ego(request, chart_name):
    output = (
        Chart.objects.filter(chart_name=chart_name)
        .get()
        .persona_set.filter(is_ego=True)
    )
    return HttpResponse(output)


def create_ego(request):
    if request.method == "POST":
        form = CreateEgoForm(request.POST)
        if form.is_valid():
            if form.cleaned_data["chart"]:
                c = Chart(chart_name=form.cleaned_data["chart"])
                c.save()
            else:
                c = Chart()
                c.save()
            e = Persona(
                chart=Chart.objects.filter(chart_name=c.chart_name).get(),
                name=form.cleaned_data["name"],
                surname=form.cleaned_data["surname"],
                is_ego=True,
                step=0,
            )
            e.clean()
            e.save()
            return redirect("show_ego", c.chart_name)
    else:
        form = CreateEgoForm()
    return render(request, "charts/create_ego.html", {"form": form})


def chart_step(request, chart_name, step):
    output = (
        Chart.objects.filter(chart_name=chart_name)
        .get()
        .persona_set.filter(step=int(step))
    )
    return HttpResponse(output)
