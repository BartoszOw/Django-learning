from django.db import models

# Create your models here.


OPERATION_CHOICES = (
    ('add', 'add'),
    ('sub', 'sub'),
    ('mul', 'mul'),
    ('div', 'div'),
)
class Math(models.Model):
    operation = models.CharField(max_length=5, choices=OPERATION_CHOICES)
    a = models.IntegerField()
    b = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)
    result = models.ForeignKey(
        'maths.result',
        on_delete=models.CASCADE,
        null=True,
        blank=True
        )
    
class Result(models.Model):
    value = models.FloatField(blank=True,null=True, unique=True)
    error = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        unique=True
    )