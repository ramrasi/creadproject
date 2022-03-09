from django.db import models

class Employee(models.Model):
    name = models.CharField(max_length=50, db_column="emp_name")
    age  = models.PositiveSmallIntegerField()
    email = models.EmailField(max_length=50)
    designation = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(obj):
        return obj.name

    def json(obj):
        return {
            'id': obj.id,
            'name': obj.name,
            'age' : obj.age,
            'email': obj.email,
            'designation': obj.designation,
            'created_at': obj.created_at,
            'updated_at': obj.updated_at
        }

