from django.urls import path

from snacks.models import Snack
from .views import SnacksDetailView, SnacksListView

urlpatterns=[
path('snacks_list',SnacksListView.as_view(),name="snacks_list"),
path('<int:pk>/',SnacksDetailView.as_view(),name="snack_detail"),

]