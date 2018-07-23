from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

# Create your models here.
class UserProfile(models.Model):
	user = models.OneToOneField(User,on_delete=models.CASCADE)
	Description = models.CharField(max_length=100 ,default='')
	city = models.CharField(max_length=100 ,default='')
	website = models.URLField(default='')
	phone = models.IntegerField(default=0)

#desde aqui hasta *
def create_profile(sender, **kwargs):
	if kwargs['created']:
		user_profile = UserProfile.objects.create(user=kwargs['instance'])

post_save.connect(create_profile, sender=User)
# *todo esto hace que cuando se crea un user django 
#automaticamente crea un Userprofile object