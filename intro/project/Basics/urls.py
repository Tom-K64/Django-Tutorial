from django.urls import path
from .views import json_view

urlpatterns=[
    #   path name/route  view  reference name
    path('json-view-api/',json_view,name='json_view')
]