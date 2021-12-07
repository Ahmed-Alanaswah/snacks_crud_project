from  django.urls import path
from django.views.generic import detail

from .views import (ListSnackView,CreateSnackView,DeleteeSnackView,UpdateSnackView,DetailSnackView)

urlpatterns= [
    path('',ListSnackView.as_view(),name= 'snack_list'),
    path('<int:pk>',DetailSnackView.as_view(),name = 'snack_detail'),
    path('create/',CreateSnackView.as_view(),name = 'snack_create'),
    path('delete/<int:pk>',DeleteeSnackView.as_view(),name="snack_delete"),
    path('update/<int:pk>',UpdateSnackView.as_view(),name='snack_update'),

]