from django.db import models

# Create your models here.
class StudentDetailsModel(models.Model):
    name=models.CharField(max_length=100,null=True, blank=True)
    phone_number=models.CharField(max_length=15,null=True, blank=True)
    gender=models.CharField(max_length=10,null=True, blank=True)
    standard=models.IntegerField(null=True, blank=True)

"""
anish
sahil
kanhaya
riya

"""
#Relations between Model

class ContactDetailModel(models.Model):
    email=models.EmailField(null=True, blank=True)
    phone_number=models.CharField(max_length=10,null=True, blank=True)
    linked_in=models.URLField(null=True, blank=True)
    git_hub=models.CharField(max_length=50,null=True, blank=True)
    
class OrganisationModel(models.Model):
    title=models.CharField(max_length=50)

class SubjectModel(models.Model):
    subject_name=models.CharField(max_length=20,null=True, blank=True)

    def __str__(self):
        return self.subject_name

class StudentModel(models.Model):
    first_name=models.CharField(max_length=20,null=True, blank=True)
    last_name=models.CharField(max_length=20,null=True,blank=True)
    date_of_birth=models.DateField(null=True, blank=True)
    contact_detail=models.OneToOneField(ContactDetailModel,on_delete=models.CASCADE,related_name="StudentModel_contact_detail",null=True,blank=True)
    organisation=models.ForeignKey(OrganisationModel,on_delete=models.DO_NOTHING,null=True,blank=True,related_name="StudentModel_organisation")
    subjects=models.ManyToManyField(SubjectModel,related_name="StudentModel_subjects",blank=True)

    def __str__(self):
        return self.first_name

