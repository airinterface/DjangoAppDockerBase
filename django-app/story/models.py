from django.db import models


class Story(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    index   = models.IntegerField()
    title   = models.CharField( max_length=200, blank=True, default='')
    img     = models.CharField( max_length=250, blank=True, default='')    
    body    = models.TextField( blank=True, null=True)
    data    = models.JSONField( default={} )

    class Meta:
        ordering = ['created']

