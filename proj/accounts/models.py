from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.text import slugify
from django.urls import reverse

# Create your models here.
class UserAccount(AbstractUser):
    name = models.CharField(max_length=50)
    inn = models.CharField(max_length=150, null=True)
    is_organization = models.BooleanField(default=False)
    balance= models.FloatField(default=0)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    user_slug = models.SlugField()

    def save(self, *args, **kwargs):
        self.name = self.name.lower()
        self.slug = slugify(self.name)
        super(UserAccount, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('account', kwargs={'useraccount_slug': self.user_slug}) 

class PrivateKey(models.Model):
    key = models.CharField(max_length=51)
    status = models.CharField(max_length=10)
    pk_slug = models.SlugField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    last_used = models.DateTimeField(null=True, blank=True)
    user = models.ForeignKey(UserAccount, on_delete=models.CASCADE)
    #status_from_api = models.CharField(default='Legacy', max_length=3, null=True, blank=True)

    def save(self, *args, **kwargs):
        self.pk_slug = slugify(self.key.lower())
        super(PrivateKey, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('privatekey', kwargs={'privatekey_slug': self.pk_slug}) 