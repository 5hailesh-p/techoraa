from django.db import models

# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateField()

    def __str__(self):
        return self.name
    
class Contact_form(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    created_at = models.DateField()

    def __str__(self):
        return self.name

class SiteSettings(models.Model):
    site_name = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='logos/' ,blank=True,null=True)
    fav = models.ImageField(upload_to='fav/' ,blank=True,null=True)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    address = models.TextField(blank=True,null=True)

    telegram = models.URLField(blank=True,null=True)
    instagram = models.URLField(blank=True,null=True)
    github = models.URLField(blank=True,null=True)

    def __str__(self):
        return self.site_name
    
    