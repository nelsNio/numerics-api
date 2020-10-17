from rest_framework.routers import DefaultRouter
from django.urls import path
from . import views

router = DefaultRouter()

urlpatterns = [


    path('render_list/',views.render_list),
    path('history/',views.list)

] + router.urls

