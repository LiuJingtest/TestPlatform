from django.db import models


class Fps(models.Model):
    """
    项目表
    """
    pro_id = models.AutoField(primary_key=True)

