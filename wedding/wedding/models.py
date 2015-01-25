from django.db import models

class Guest(models.Model):
    """
    Guest Model
    """
    created_date = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=300)
    email = models.CharField(max_length=300)
    guests = models.IntegerField()
    
    def __unicode__(self):
        return self.name

class GuestPost(models.Model):
    created_date = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=300)
    email = models.CharField(max_length=300)
    body  = models.CharField(max_length=5000)

    def __unicode__(self):
        return self.name
