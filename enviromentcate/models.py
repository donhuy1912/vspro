# from django.db import models

# # Create your models here.
# class AccountType(models.Model):
#     accounttypeid = models.  AutoField(db_column='AccountTypeID', primary_key=True)  # Field name made lowercase.
#     accounttypename = models.CharField(db_column='AccountTypeName', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     createdate = models.DateTimeField(db_column='CreateDate', blank=True, null=True)  # Field name made lowercase.
#     editdate = models.DateTimeField(db_column='EditDate', blank=True, null=True)  # Field name made lowercase.
#     isenable = models.IntegerField(db_column='IsEnable', blank=True, null=True)  # Field name made lowercase.
#     note = models.CharField(db_column='Note', max_length=100, blank=True, null=True)  # Field name made lowercase.

#     # def __str__(self):
#     #     return self.firstname + " " + self.lastname