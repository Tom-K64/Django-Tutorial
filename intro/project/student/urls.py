from django.urls import path
from .views import StudentDetailModelListAPIView,StudentDetailModelCreateAPIView,StudentDetailModelUpdateAPIView
#GEnericAPIVIews
from .views import StudentDetailModelListGenericAPIView,StudentDetailModelCreateGenericAPIView,StudentDetailModelUpdateGenericAPIView,StudentDetailModelDeleteGenericAPIView,StudentDetailModelListCreateGenericAPIView,StudentDetailModelRUDGenericAPIView,StudentDetailModelGetGenericAPIView
urlpatterns=[
    path('student-detail-list-api-view/',StudentDetailModelListAPIView.as_view(),name='StudentDetailModelListAPIView'),
    path('student-detail-create-api-view/',StudentDetailModelCreateAPIView.as_view(),name='StudentDetailModelCreateAPIView'),
    path('student-detail-update-api-view/<id>/',StudentDetailModelUpdateAPIView.as_view(),name='StudentDetailModelUpdateAPIView'),

    path('student-detail-generic-list-api/',StudentDetailModelListGenericAPIView.as_view(),name='StudentDetailModelListGenericAPIView'),
    path('student-detail-generic-create-api/',StudentDetailModelCreateGenericAPIView.as_view(),name='StudentDetailModelCreateGenericAPIView'),
    path('student-detail-generic-retrieve-api/<pk>/',StudentDetailModelGetGenericAPIView.as_view(),name='StudentDetailModelGetGenericAPIView'),
    path('student-detail-generic-update-api/<pk>/',StudentDetailModelUpdateGenericAPIView.as_view(),name='StudentDetailModelUpdateGenericAPIView'),
    path('student-detail-generic-delete-api/<pk>/',StudentDetailModelDeleteGenericAPIView.as_view(),name='StudentDetailModelDeleteGenericAPIView'),

    path('student-detail-generic-list-create-api/',StudentDetailModelListCreateGenericAPIView.as_view(),name='StudentDetailModelListCreateGenericAPIView'),
    path('student-detail-generic-rud-api/<pk>/',StudentDetailModelRUDGenericAPIView.as_view(),name='StudentDetailModelRUDGenericAPIView'),

]