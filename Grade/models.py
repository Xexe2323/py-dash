from django.db import models
from django.contrib.auth.models import User
# Create your models here.
from PIL import Image
    
class Grade(models.Model):
    fullname = models.CharField(max_length=255, default="")
    score = models.CharField(max_length=10, default="1-100")
    exam = models.CharField(max_length=50)
    passed = models.CharField(max_length=50, choices=[('Yes', 'Yes'), ('No', 'No')])
    onclass = models.CharField(max_length=256, choices=[('A1', 'A1'), ('A2', 'A2'), ('A3', 'A3'), ('A4', 'A4')])


class Student(models.Model):
    fullname = models.CharField(max_length=50)
    paid = models.CharField(max_length=26, choices=[('Yes', 'Yes'), ('No', 'No')])
    presents = models.CharField(max_length=100)
    absents = models.CharField(max_length=100)
    term = models.CharField(max_length=100)
    learning = models.CharField(max_length=26, choices=[('GER', 'German'), ('EN', 'English'), ('FR', 'French'), ('IR', 'Persian')])




    def __stf__(self):
        return f"{self.author}"



class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'

    # Override the save method of the model
    def save(self):
        super().save()

        img = Image.open(self.image.path) # Open image

        # resize image
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size) # Resize image
            img.save(self.image.path) # Save it again and override the larger image
