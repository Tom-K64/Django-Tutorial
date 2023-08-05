from rest_framework import serializers
from .models import StudentDetailModel,BranchModel,CourseModel


class StudentDetailModelListSerializer(serializers.ModelSerializer):
    class Meta:
        model=StudentDetailModel
        fields="__all__"

class StudentDetailModelCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model=StudentDetailModel
        fields="__all__"
        

class StudentDetailModelUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model=StudentDetailModel
        exclude=['id','created_at','updated_at']
        # fields=["first_name","last_name","roll_no","branch","courses"]
