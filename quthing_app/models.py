from django.db import models

class QuthingPatientModel(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()

    class Meta:
        db_table = 'patients'
        
# class QuthingStaffModel(models.Model):
#     name = models.CharField(max_length=100)
#     position = models.CharField(max_length=100)

#     class Meta:
#         db_table = 'staff'

