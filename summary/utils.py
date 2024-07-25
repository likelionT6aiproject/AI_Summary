import os
from django.conf import settings
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from django.utils import timezone

def save_text_file(content, user_id, file_type):
    timestamp = timezone.now().strftime('%Y%m%d%H%M%S')
    file_name = f"{file_type}_{user_id}_{timestamp}.txt"
    path = os.path.join(file_type, file_name)
    content_file = ContentFile(content.encode('utf-8'))
    full_path = default_storage.save(path, content_file)
    file_url = settings.MEDIA_URL + full_path
    return file_url