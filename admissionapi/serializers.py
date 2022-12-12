from rest_framework import serializers
from admissionapi.models import User,Batches

def age_limit_Validation(value):
    if value < 18 or value > 65:
        raise serializers.ValidationError(" Age Should be 18 < > 65 ")
def mobile_no_Validation(value):
    if len(value) != 10:
        raise serializers.ValidationError("Mobile Number Should be 10 digit")
def Name_Validation(value):
    if value.isalpha():
        raise serializers.ValidationError("Name Only Charector allowed")
        
class UserSerializer(serializers.ModelSerializer):
    age = serializers.IntegerField(validators=[age_limit_Validation])
    mobile = serializers.CharField(validators=[mobile_no_Validation])
    name = serializers.CharField(validators=[Name_Validation])
    class Meta:
        model=User
        fields=['id','name','age','email','mobile','password']

    def create(self, validated_data):
        return User.objects.create(**validated_data)

class BatchesSerializer(serializers.ModelSerializer):
    class Meta:
        model=Batches
        fields=['batches_id','fees','batch','date']
