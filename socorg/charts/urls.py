from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<str:chart_name>/show_ego/", views.show_ego, name="show_ego"),
    path("<str:chart_name>/step/<str:step>", views.chart_step, name="chart_step"),
    path("create_ego/", views.create_ego, name="create_ego"),
]
