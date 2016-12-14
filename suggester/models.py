from django.db import models
from tastypie.utils.timezone import now
from django.contrib.auth.models import User
from django.utils.text import slugify


# Create your models here.

class BookSuggester(models.Model):
    name = models.CharField(max_length=300, blank=True, null=True)
    isbn = models.CharField(db_column='ISBN', max_length=255, blank=True, null=True)  # Field name made lowercase.
    author = models.CharField(max_length=255, blank=True, null=True)
    publisher = models.CharField(max_length=255, blank=True, null=True)

    def __unicode__(self):
        return self.title

    def save(self, *args, **kwargs):
        # For automatic slug generation.
        if not self.slug:
            self.slug = slugify(self.title)[:50]

        return super(Entry, self).save(*args, **kwargs)

    class Meta:
        managed = False
        db_table = 'bookinfo_sugester'
