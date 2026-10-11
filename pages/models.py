from django.db import models


# Create your models here.
class Department(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return str(self.name)


class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    age = models.PositiveIntegerField()
    department = models.ForeignKey(
        Department, on_delete=models.PROTECT, related_name="students"
    )

    def __str__(self):
        return str(self.name)
