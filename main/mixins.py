from django.db import models

class MetaTagMixin(models.Model):
    name = None
    meta_title = models.CharField(max_length=255, blank=True, null=True)
    meta_description = models.TextField(blank=True, null=True)
    meta_keywords = models.TextField(blank=True, null=True)
    
    def get_meta_title(self):
        return self.meta_title or self.name
    
    class Meta:
        abstract = True