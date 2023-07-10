from django.db import models

# Create your models here.
class Question(models.Model):
    vote_question= models.CharField(max_length=300)
    vote_date= models.DateTimeField('published date')

    def __str__(self):
        return  self.vote_question

class choice(models.Model):
    question= models.ForeignKey(Question,on_delete=models.CASCADE)
    choice_field= models.CharField(max_length=200)
    votes=models.IntegerField(default=0)

    def __str__(self):
        return  self.choice_field
class name(models.Model):
    student_name= models.CharField(max_length=50)
    student_id=models.CharField(max_length=10)

    def __str__(self):
        return  self.student_name

class Image(models.Model):
    question= models.ForeignKey(Question,on_delete=models.CASCADE,default=1)
    title = models.CharField(max_length=20)
    photo = models.ImageField(upload_to='pics')


class UsersDetail(models.Model):
    # question= models.ForeignKey(Question,on_delete=models.CASCADE,default=0)
    Name = models.TextField()
    Gender = models.CharField(max_length=2)
    Student_id = models.IntegerField(default=0)
    birth_date = models.CharField(max_length=255)
    Street = models.TextField()
    Hometown = models.TextField()
    Class = models.TextField()
    start_date = models.DateField()
    position = models.CharField(max_length=255)

    def __str__(self):
        return self.Name
# class UploadImage(models.Model):  
#     question= models.ForeignKey(Question,on_delete=models.CASCADE)
#     caption = models.CharField(max_length=200)  
#     image = models.ImageField(upload_to='images')  
  
#     def __str__(self):  
#         return self.caption  