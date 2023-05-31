from django.db import models

class DBTEST_MODEL(models.Model):
    name = models.CharField(max_length=30)
    emailId = models.CharField(max_length=50)
    Mobile = models.CharField(max_length=10)
    class Meta:
        db_table = 'tblRegister'
        db_tablespace = "dbtest"

