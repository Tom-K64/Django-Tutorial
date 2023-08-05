from django.urls import path
from .views import StudentDetailModelListAPIView,StudentDetailModelCreateAPIView,StudentDetailModelUpdateAPIView

urlpatterns=[
    path('student-detail-list-api-view/',StudentDetailModelListAPIView.as_view(),name='StudentDetailModelListAPIView'),
    path('student-detail-create-api-view/',StudentDetailModelCreateAPIView.as_view(),name='StudentDetailModelCreateAPIView'),
    path('student-detail-update-api-view/<id>/',StudentDetailModelUpdateAPIView.as_view(),name='StudentDetailModelUpdateAPIView'),

]