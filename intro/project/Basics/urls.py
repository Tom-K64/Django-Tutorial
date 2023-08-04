from django.urls import path
#fucntion based views
from .views import json_view,StudentDetailModelView,GetAllStudentDetails
#class Based Views
from .views import StudentDetailsModelListAPIView,StudentDetailsModelCreateAPIView,StudentDetailsModelUpdateAPIView,StudentDetailsModelDeleteAPIView

urlpatterns=[
    #   path name/route      view     reference name
    path('json-view-api/',json_view,name='json_view'),
    #dynamic api
    path('student-details-api/<id>/',StudentDetailModelView,name="StudentDetailModelView"),
    path('all-student-details-api/',GetAllStudentDetails,name="GetAllStudentDetails"),

    #Class Based Views
    path('Student-details-list-api/',StudentDetailsModelListAPIView.as_view(),name="StudentDetailsModelListAPIView"),
    path('Student-details-create-api/',StudentDetailsModelCreateAPIView.as_view(),name="StudentDetailsModelCreateAPIView"),
    path('Student-details-update-api/<id>/',StudentDetailsModelUpdateAPIView.as_view(),name="StudentDetailsModelUpdateAPIView"),
    path('Student-details-delete-api/<id>/',StudentDetailsModelDeleteAPIView.as_view(),name="StudentDetailsModelDeleteAPIView"),
]