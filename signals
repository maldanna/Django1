https://simpleisbetterthancomplex.com/tutorial/2016/07/28/how-to-create-django-signals.html
from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    image = models.ImageField(default='profile_pics/image001.jpg', upload_to='profile_pics')
    phone=models.CharField(max_length=200)
    HomeAddress=models.CharField(max_length=800, default="")
    FieldAddress=models.CharField(max_length=300,default="gjkg")

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self,*args, **kwargs):
        super(Profile, self).save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)




def create_profile(sender, **kwargs):
    if kwargs['created']:
        user_profile = Profile.objects.create(user=kwargs['instance'])

post_save.connect(create_profile, sender=User)
