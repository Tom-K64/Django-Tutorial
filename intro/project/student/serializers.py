from rest_framework import serializers
from .models import StudentDetailModel,BranchModel,CourseModel

class BranchModelListSerializer(serializers.ModelSerializer):
    class Meta:
        model=BranchModel
        fields="__all__"

class CourseModelListSerializer(serializers.ModelSerializer):
    class Meta:
        model=CourseModel
        fields="__all__"

class StudentDetailModelListSerializer(serializers.ModelSerializer):
    branch=serializers.SerializerMethodField()
    branch_details=serializers.SerializerMethodField()
    courses_details=serializers.SerializerMethodField()
    class Meta:
        model=StudentDetailModel
        fields="__all__"
    
    def get_branch(self,obj):
        # return obj.branch.title
        try:
            data=obj.branch.title
        except:
            data=""
        return data

    def get_branch_details(self,obj):
        try:
            data=BranchModelListSerializer(obj.branch,many=False).data
        except:
            data={}
        return data

    def get_courses_details(self,obj):
        try:
            data=CourseModelListSerializer(obj.courses,many=True).data
        except:
            data=[]
        return data

class StudentDetailModelCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model=StudentDetailModel
        fields="__all__"
        

class StudentDetailModelUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model=StudentDetailModel
        exclude=['id','created_at','updated_at']
        # fields=["first_name","last_name","roll_no","branch","courses"]
