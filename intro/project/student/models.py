from django.db import models

# Create your models here.
# name,model

class BranchModel(models.Model):
    title = models.CharField(max_length=50, blank=True, null=True)
    
    created_at=models.DateTimeField(auto_now_add=True,editable=False)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class CourseModel(models.Model):
    title = models.CharField(max_length=50, blank=True, null=True)
    
    created_at=models.DateTimeField(auto_now_add=True,editable=False)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class StudentDetailModel(models.Model):
    first_name=models.CharField(max_length=50,null=True, blank=True)
    last_name=models.CharField(max_length=50,null=True, blank=True)
    roll_no=models.IntegerField(null=True, blank=True)
    branch=models.ForeignKey(BranchModel,on_delete=models.CASCADE, null=True, blank=True,related_name="StudentDetailModel_branch")
    courses=models.ManyToManyField(CourseModel,related_name="StudentDetailModel_courses",blank=True)

    created_at=models.DateTimeField(auto_now_add=True,editable=False)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.first_name