from django.db import models

# Create your models here.


class Feedback(models.Model):
    name=models.CharField(max_length=255,null=True)
    phone_number=models.CharField(max_length=25,null=True)
    email=models.EmailField(null=True)
    message=models.TextField(null=True)
    created_at=models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.name