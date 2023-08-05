from django.contrib import admin
from .models import StudentDetailModel,BranchModel,CourseModel
# Register your models here.
admin.site.register(StudentDetailModel)
admin.site.register(BranchModel)
admin.site.register(CourseModel)