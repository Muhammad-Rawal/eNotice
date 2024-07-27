from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Notice(models.Model):
    title = models.CharField(max_length=100)
    message = models.TextField(max_length=2000)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, related_name='posts', on_delete=models.DO_NOTHING)
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    video = models.FileField(upload_to='videos/', null=True, blank=True)
    document = models.FileField(upload_to='documents/', null=True, blank=True)

    def __str__(self):
        return self.title


class SavedNotice(models.Model):
    user = models.ForeignKey(User, related_name='saved_notices', on_delete=models.CASCADE)
    notice = models.ForeignKey(Notice, related_name='saved_by_users', on_delete=models.CASCADE)
    saved_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'notice')

    def __str__(self):
        return f"{self.user.username} saved {self.notice.title}"
