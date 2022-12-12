from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=60)
    age = models.CharField(max_length=2)
    email = models.EmailField(max_length=50,unique=True)
    mobile = models.CharField(max_length=10)
    password = models.CharField(max_length=30)

    submitted_at = models.DateTimeField(auto_now_add=True,null=True)
    updated_at = models.DateTimeField(auto_now=True,null=True)
    #created_at = models.DateTimeField(auto_now_add=True,null=True)
    # lastlogin_at = models.DateTimeField(auto_now=True,null=True)
    class Meta:
        db_table="user"

slots={"6-7AM":"6-7AM",
        "7-8AM":"7-8AM",
        "8-9AM":"8-9AM",
        "5-6PM":"5-6PM"}

class Batches(models.Model):
    batches_id = models.ForeignKey(User,on_delete=models.CASCADE)
    fees = models.IntegerField()
    batch = models.CharField(max_length=30)
    date = models.DateField()
    class Meta:
        db_table="batches"
