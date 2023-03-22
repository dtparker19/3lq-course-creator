from django.db import models

# Create your models here.
#create a class for the course model

class Course(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(max_length=1000)
    image = models.ImageField(upload_to='course_images')
    link = models.URLField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name
    
#create a class for the course section model

class CourseSection(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    description = models.TextField(max_length=1000)
    image = models.ImageField(upload_to='course_images')    
    link = models.URLField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name
    
#create a class for the course lesson model

class CourseLesson(models.Model):
    course_section = models.ForeignKey(CourseSection, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    description = models.TextField(max_length=1000)
    image = models.ImageField(upload_to='course_images')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
