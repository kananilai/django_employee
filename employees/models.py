from django.db import models

class Department(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Training (models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return (self.name)
    
class Employee(models.Model):
    employee_id = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    department =models.ForeignKey(Department, on_delete=models.CASCADE)
    training = models.ForeignKey(Training, on_delete=models.CASCADE)

    def __str__(self):
        return (self.name)
