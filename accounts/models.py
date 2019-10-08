from django.db import models
from django.conf import settings


# Create your models here.

class user(models.Model):
    name = models.CharField(max_length = 100)
    email_id = models.EmailField()
    password = models.CharField(max_length = 100)

# ---------------------------------------------------------------------------


class mon(models.Model):
    breakfast = models.BooleanField(default=True)
    lunch = models.BooleanField(default=True)
    snacks = models.BooleanField(default=True)
    dinner = models.BooleanField(default=True)

class tue(models.Model):
    breakfast = models.BooleanField(default=True)
    lunch = models.BooleanField(default=True)
    snacks = models.BooleanField(default=True)
    dinner = models.BooleanField(default=True)

class wed(models.Model):
    breakfast = models.BooleanField(default=True)
    lunch = models.BooleanField(default=True)
    snacks = models.BooleanField(default=True)
    dinner = models.BooleanField(default=True)

class thu(models.Model):
    breakfast = models.BooleanField(default=True)
    lunch = models.BooleanField(default=True)
    snacks = models.BooleanField(default=True)
    dinner = models.BooleanField(default=True)

class fri(models.Model):
    breakfast = models.BooleanField(default=True)
    lunch = models.BooleanField(default=True)
    snacks = models.BooleanField(default=True)
    dinner = models.BooleanField(default=True)

class sat(models.Model):
    breakfast = models.BooleanField(default=True)
    lunch = models.BooleanField(default=True)
    snacks = models.BooleanField(default=True)
    dinner = models.BooleanField(default=True)

# -------------------------------------------------------------------------------


class select_food(models.Model):

    # stu = models.ForeignKey('login', related_name='Evaluation_Students')
    username = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # username = models.ForeignKey('login', related_name='Evaluation_Students')
    # monday = models.BooleanField(default=True)
    # tuesday = models.BooleanField(default=True)
    # wednesday = models.BooleanField(default=True)
    # thursday = models.BooleanField(default=True)
    # friday = models.BooleanField(default=True)
    # saturday = models.BooleanField(default=True)
    monday = models.ForeignKey(mon, on_delete=models.CASCADE)
    tuesday = models.ForeignKey(tue, on_delete=models.CASCADE)
    wednesday = models.ForeignKey(wed, on_delete=models.CASCADE)
    thursday = models.ForeignKey(thu,on_delete=models.CASCADE)
    friday = models.ForeignKey(fri, on_delete=models.CASCADE)
    saturday = models.ForeignKey(sat, on_delete=models.CASCADE)


