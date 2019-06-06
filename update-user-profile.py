1.in this we are going to extend User(built in user model) model


from django.db import models

from django.contrib.auth.models import User

""" now every user will have one profile if user will delete automatically profile will be delete
not viceversa
"""

"""important instruction in application use Userregistration form to sign up without any extra fields (but ovverride as you want like
to add placeholders or etc"

"then use profile i..e extending the User as oneto one link """


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'  #it will shows as object name
    
    
    
  orm:
    user1=user.object.filter(username="maldana")
    user1.profile ==> u will get profile 
    user1.profile.image  ===> u will get image of that profile 
    
    
    
    
    
    
    
    
