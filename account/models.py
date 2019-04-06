# from django.db import models
# from userdetail.models import UserDetail
# from accounttype.models import AccountType


# # Create your models here.
# class Account(models.Model):
#     accountid = models.AutoField(db_column='AccountID', primary_key=True)  # Field name made lowercase.
#     userdetailid = models.ForeignKey(UserDetail, models.DO_NOTHING, db_column='UserDetailID', blank=True, null=True)  # Field name made lowercase.
#     accounttypeid = models.ForeignKey(AccountType, models.DO_NOTHING, db_column='AccountTypeID', blank=True, null=True)  # Field name made lowercase.
#     #accounttypeid = models.IntegerField(db_column='AccountTypeID', blank=True, null=True)  # Field name made lowercase.
#     username = models.CharField(db_column='Username', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     password = models.CharField(db_column='Password', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     createdate = models.DateTimeField(db_column='CreateDate', blank=True, null=True)  # Field name made lowercase.
#     editdate = models.DateTimeField(db_column='EditDate', blank=True, null=True)  # Field name made lowercase.
#     avatar = models.CharField(db_column='Avatar', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     resetcode = models.CharField(db_column='ResetCode', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     isenable = models.IntegerField(db_column='IsEnable', blank=True, null=True)  # Field name made lowercase.
#     note = models.CharField(db_column='Note', max_length=100, blank=True, null=True)  # Field name made lowercase.

#     class Meta:
#         managed = True
#         db_table = 'account'