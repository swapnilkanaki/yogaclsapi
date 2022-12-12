from django.test import TestCase
from admissionapi.models import User
# Create your tests here.

data = User.objects.filter(email="admin@gmail.com", password="admin@123")
print(data)
