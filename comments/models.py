from django.db import models

# Create your models here.
class Comment(models.Model):
    username = models.CharField(max_length=255)
    email = models.EmailField()
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self) :
        return f'{self.text}'
    
    class Meta:
        ordering = ['-created_at']