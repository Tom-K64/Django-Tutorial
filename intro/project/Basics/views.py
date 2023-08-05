from django.shortcuts import render
from django.http import JsonResponse
from .models import StudentDetailsModel
from rest_framework import views,status
from rest_framework.response import Response
# Create your views here.

def json_view(request):
    data={
        "Name":"Kanhaya",
        "Age":25,
        "Address":"BBSR"
    }
    return JsonResponse(data)
    
def StudentDetailModelView(request,id):
    obj=StudentDetailsModel.objects.get(id=id)
    var={
        "Name":obj.name,
        "phone_number":obj.phone_number,
        "gender":obj.gender,
        "standard":obj.standard
    }
    return JsonResponse(var)


def GetAllStudentDetails(request):
    obj=StudentDetailsModel.objects.all()
    data_list=[]
    for i in obj:
        var={
        "Name":i.name,
        "phone_number":i.phone_number,
        "gender":i.gender,
        "standard":i.standard,
        "age":i.age
        }
        data_list.append(var)
    return JsonResponse(data_list,safe=False)

"""
STATUS CODES:
200 - everything goes perfectly
400 - something went wrong
"""

####These views are created witgout using Serializer####
class StudentDetailsModelListAPIView(views.APIView):#GET -> READ
    def get(self, request):
        obj=StudentDetailsModel.objects.all()
        data_list=[]
        for i in obj:
            var={
            "name":i.name,
            "phone_number":i.phone_number,
            "gender":i.gender,
            "standard":i.standard,
            "age":i.age
            }
            data_list.append(var)
        return Response(data_list,status=status.HTTP_200_OK)
    
    # def post(self,request):
    #     try:
    #         # print(request.data)
    #         # print(request.data['name'])
    #         obj=StudentDetailsModel.objects.create(**(request.data))
    #         return Response({"message":"Student Details created successfully"},status=status.HTTP_200_OK)
    #     except Exception as e:
    #         return Response({"message":f"something went wrong : {e}"},status=status.HTTP_400_BAD_REQUEST)
        
"""
{
"name":"Kanhaya",
"phone_number":"987654",
"gender":"Male",
"standard":"15",
"age":"90"
}
"""
class StudentDetailsModelCreateAPIView(views.APIView):#POST -> Create 
    def post(self,request):
        try:
            # print(request.data)
            # print(request.data['name'])
            obj=StudentDetailsModel.objects.create(**(request.data))
            return Response({"message":"Student Details created successfully"},status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"message":f"something went wrong : {e}"},status=status.HTTP_400_BAD_REQUEST)

class StudentDetailsModelUpdateAPIView(views.APIView):#PUT -> Update
    def get(self,request,id):
        try:
            obj=StudentDetailsModel.objects.get(id=id)
            data={
            "name":obj.name,
            "phone_number":obj.phone_number,
            "gender":obj.gender,
            "standard":obj.standard,
            "age":obj.age
            }
            return Response(data,status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"message":f"something went wrong : {e}"},status=status.HTTP_400_BAD_REQUEST)


    def put(self,request,id):
        try:
            obj=StudentDetailsModel.objects.get(id=id)
            obj.name=request.data['name']
            obj.phone_number=request.data["phone_number"]
            obj.gender=request.data["gender"]
            obj.standard=request.data['standard']
            obj.age=request.data['age']
            obj.save()
            return Response({"message":"Student Details Updated successfully"},status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"message":f"something went wrong : {e}"},status=status.HTTP_400_BAD_REQUEST)
    
    # def delete(self, request,id):
    #     try:
    #         obj=StudentDetailsModel.objects.get(id=id)
    #         obj.delete()
    #         return Response({"message":"Student Details deleted successfully"},status=status.HTTP_200_OK)
    #     except Exception as e:
    #         return Response({"message":f"something went wrong : {e}"},status=status.HTTP_400_BAD_REQUEST)


class StudentDetailsModelDeleteAPIView(views.APIView):#Delete -> delete
    def delete(self, request,id):
        try:
            obj=StudentDetailsModel.objects.get(id=id)
            obj.delete()
            return Response({"message":"Student Details deleted successfully"},status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"message":f"something went wrong : {e}"},status=status.HTTP_400_BAD_REQUEST)

"""
List API
CReate API
PUT API
DELETE API

(List + Create) API
(GET,PUT,DELETE) API
"""

