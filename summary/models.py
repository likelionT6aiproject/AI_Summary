from django.db import models
from django.conf import settings

# Create your models here.
class Summary(models.Model):
    summary_id = models.AutoField(primary_key=True)    
    #user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    origin_text_path=models.URLField()
    summary_text_path=models.URLField()
    created_at=models.DateTimeField()
    
