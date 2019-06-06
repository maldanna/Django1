from django.db import models

#generally User model which is in built so better to use tha model for our website user and we  can add extra features


from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)  # we can setnull on_delete=models.SET_NULL
    
    #in oracle
    CONSTRAINT fk_supplier
    FOREIGN KEY (supplier_id)
    REFERENCES supplier(supplier_id)
    ON DELETE SET NULL  # on delete cascade

    def __str__(self):
        return self.title  # it shows for objects like modelname.objects.all()
    #if you not mention then reference of object will be display
    
    
