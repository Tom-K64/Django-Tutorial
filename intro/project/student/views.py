from django.shortcuts import render
from rest_framework import views,status,generics
from rest_framework.response import Response
from .serializers import StudentDetailModelListSerializer,StudentDetailModelCreateSerializer,StudentDetailModelUpdateSerializer
from .models import StudentDetailModel
# Create your views here.

# get,post,put,delete
class StudentDetailModelListAPIView(views.APIView):
    def get(self,request):
        try:
            obj=StudentDetailModel.objects.all()
            serializer=StudentDetailModelListSerializer(obj,many=True)
            return Response(serializer.data,status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"message":f"something went wrong : {e}"},status=status.HTTP_400_BAD_REQUEST)

class StudentDetailModelCreateAPIView(views.APIView):
    def post(self, request):
        try:
            serializer=StudentDetailModelCreateSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({"message":"Student details Created Successfully"},status=status.HTTP_200_OK)
            return Response({"message":serializer.errors},status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"message":f"something went wrong : {e}"},status=status.HTTP_400_BAD_REQUEST)


class StudentDetailModelUpdateAPIView(views.APIView):
    def get(self, request,id):
        try:
            obj=StudentDetailModel.objects.get(id=id)
            serializer=StudentDetailModelUpdateSerializer(obj,many=False)
            return Response(serializer.data,status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"message":f"something went wrong : {e}"},status=status.HTTP_400_BAD_REQUEST)

    def put(self,request,id):
        try:
            obj=StudentDetailModel.objects.get(id=id)
            serializer=StudentDetailModelUpdateSerializer(instance=obj,data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({"message":"Student details Updated Successfully"},status=status.HTTP_200_OK)
            return Response({"message":serializer.errors},status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"message":f"something went wrong : {e}"},status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request,id):
        try:
            obj=StudentDetailModel.objects.get(id=id)
            obj.delete()
            return Response({"message":"Student Detail deleted Successfully"},status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"message":f"something went wrong : {e}"},status=status.HTTP_400_BAD_REQUEST)


#####################################GENERICS################################################

class StudentDetailModelListGenericAPIView(generics.ListAPIView):
    queryset=StudentDetailModel.objects.all()
    serializer_class=StudentDetailModelListSerializer

class StudentDetailModelGetGenericAPIView(generics.RetrieveAPIView):
    queryset=StudentDetailModel.objects.all()
    serializer_class=StudentDetailModelUpdateSerializer

class StudentDetailModelCreateGenericAPIView(generics.CreateAPIView):
    queryset=StudentDetailModel.objects.all()
    serializer_class=StudentDetailModelCreateSerializer

class StudentDetailModelUpdateGenericAPIView(generics.UpdateAPIView):
    queryset=StudentDetailModel.objects.all()
    serializer_class=StudentDetailModelUpdateSerializer

class StudentDetailModelDeleteGenericAPIView(generics.DestroyAPIView):
    queryset=StudentDetailModel.objects.all()
    serializer_class=StudentDetailModelUpdateSerializer

class StudentDetailModelListCreateGenericAPIView(generics.ListCreateAPIView):
    queryset=StudentDetailModel.objects.all()
    serializer_class=StudentDetailModelCreateSerializer

class StudentDetailModelRUDGenericAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset=StudentDetailModel.objects.all()
    serializer_class=StudentDetailModelUpdateSerializer

# generics.RetrieveUpdateAPIView
# generics.RetrieveDestroyAPIView


"""
TASK:
1- Create crud apis without serializer
2- Create crud apis with serializer
3- Create crud apis using generics
"""