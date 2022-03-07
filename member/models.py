from django.db import models

# Create your models here.
class Member(models.Model):
    name = models.TextField(default="mmn_noname")
    age = models.TextField(default="777")
    last_modify_date = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "member"