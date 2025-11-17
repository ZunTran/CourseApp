from django.contrib.auth.models import AbstractUser
from django.db import models
from ckeditor.fields import RichTextField


class User(AbstractUser):
    pass


class BaseModel(models.Model):
    createdDate = models.DateTimeField(auto_now_add=True,null=True)
    updatedDate = models.DateTimeField(auto_now=True,null=True)
    active = models.BooleanField(default=True)

    class Meta:
        abstract = True


class Category(BaseModel):
    name=models.CharField(max_length=100, null=False)

    def __str__(self):
        return self.name

class Courses(BaseModel):
    name=models.CharField(max_length=100, null=False)
    # description = models.TextField()
    description = RichTextField()
    image=models.ImageField(upload_to='courses/%Y/%m')
    tags=models.ManyToManyField('Tag')

    category=models.ForeignKey(Category,on_delete=models.RESTRICT)

    def __str__(self):
        return self.name
    class Meta:
        unique_together = ('category','name')


class Lessons(BaseModel):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=100, null=False)
    # content = models.TextField()
    content = RichTextField()
    image=models.ImageField(upload_to='lessons/%Y/%m')
    course=models.ForeignKey(Courses,on_delete=models.CASCADE)
    tags=models.ManyToManyField('Tag')

    def __str__(self):
        return self.name

    class Meta:
        unique_together = ('course', 'name')


class Tag(BaseModel):
    name=models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name