from django.db import models

# Create your models here.
class Summary(models.Model):
    origin_text_path=models.URLField()
    summary_text_path=models.URLField()
    created_at=models.DateTimeField()
    
