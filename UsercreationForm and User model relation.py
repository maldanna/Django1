#link nice  to understand extend User model 
https://simpleisbetterthancomplex.com/tutorial/2016/07/22/how-to-extend-django-user-model.html

important note:
    
    
    1.we have signup form to create acccount for user we can make form using bootstrap or html others and can get data form them and s
    store into table is old process and basic one
    #2
    2.make simple signup form django providing cool featue for  it  that is it 
    """have in built form that is UserCreationForm we havee
    
    "we have few fields int it we can ovrride that exisiting filed and also we can add more fields as per our requirement 
    code is below"""
    
    




user model is built in django so wew can use this model for hadle user details
class SignUpForm(UserCreationForm):
    username = forms.CharField(forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}))
    first_name = forms.CharField(forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}), max_length=32, help_text='First name')
    last_name=forms.CharField(forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}), max_length=32, help_text='Last name')
    email=forms.EmailField(forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}), max_length=64, help_text='Enter a valid email address')
    password1=forms.CharField(forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))
    password2=forms.CharField(forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password Again'}))

    class Meta(UserCreationForm.Meta):
        model = User
        # I've tried both of these 'fields' declaration, result is the same
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', ) or 
        fields = UserCreationForm.Meta.fields + ('first_name', 'last_name', 'email',) or        


        
        

from django import forms 
from django.contrib.auth.forms. import UserCreation
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    email = forms.CharField(max_length=254, required=True, widget=forms.EmailInput())
    teamNumber = forms.CharField(max_length=4, required=True)

    class Meta:
        Model = User
        fields= ('username', 'email', 'teamNumber', 'password1', 'password2')
I have




above allt he staff make form to get from user while signup only try analysis do it


#sddsglllkkkkkkkkkn





You can achieve this using one-to-one linking method, what you have to do is create new model (say 'Profile') with additional fields and link this model to built-in user model as one-to-one.

class Profile(models.Model):
    #one-to-one link with built-in model
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    #additional fields
    email = forms.CharField(max_length=254, required=True, widget=forms.EmailInput())
    teamNumber = forms.CharField(max_length=4, required=True)
    
    
#This links the two models, but still you have to define two signals (in the same model.py file) to get the model working,

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

    
    """These signals create and save profile entries on create and update of built-in user model.

Also you need not create your own email field as built-in User model already has a email field, make sure you check it out :)

Note: There are other methods of achieving this but I personally prefer this method over other two (mentioned on below link) as it is much cleaner and simpler to maintain and think about.

Do check out this awesome blog about extending Django's built-in user model: link The author there has beautifully explained all the three methods and how they work.

sha """"
