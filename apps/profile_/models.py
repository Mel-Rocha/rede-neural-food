from uuid import uuid4

from django.db import models
from django.core.validators import MinValueValidator
from django.contrib.auth.models import User

from apps.profile_.enums import GOALS, DIET, GENDER


class Profile(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=100)
    age = models.IntegerField(validators=[MinValueValidator(1)])
    weight = models.FloatField(default=1, validators=[MinValueValidator(1)])
    height = models.FloatField(default=1, validators=[MinValueValidator(1)])
    illness = models.CharField(max_length=200, blank=True, null=True)
    intolerance = models.CharField(max_length=100, blank=True, null=True)
    goal = models.CharField(max_length=20, choices=GOALS, default='maintenance')
    diet = models.CharField(max_length=20, choices=DIET, default='ornivorous')
    gender = models.CharField(max_length=20, choices=GENDER, default='male')

    @property
    def bmi(self):
        """
        BMI is not stored in the database, but is calculated whenever you access
        the bmi property of a User object. If the profile_'s weight or height changes,
        the bmi value will reflect that change immediately.
        """
        return self.weight / (self.height ** 2)
