from unicodedata import name
from django.urls import URLPattern, path
from .views import ThingsListView

urlpatterns ={
    path('things-list',ThingsListView.as_view(),name='things_list')

}