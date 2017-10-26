from django.db import models


class Project(models.Model):
    """
    项目表
    """
    pro_id = models.AutoField(primary_key=True)
    pro_name = models.CharField(max_length=20, null=True)
    pro_desc = models.TextField(null=True)
