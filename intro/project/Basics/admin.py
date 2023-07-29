from django.contrib import admin
from .models import StudentDetailsModel,ContactDetailModel,StudentModel,OrganisationModel,SubjectModel
# Register your models here.

admin.site.register(StudentDetailsModel)
admin.site.register(ContactDetailModel)
admin.site.register(StudentModel)
admin.site.register(OrganisationModel)
admin.site.register(SubjectModel)