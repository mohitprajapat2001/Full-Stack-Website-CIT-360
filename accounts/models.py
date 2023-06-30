from django.db import models


# Create your models here.
class student(models.Model):
    GENDER_CHOICES = (
        ("M", "Male"),
        ("F", "Female"),
        ("O", "Other"),
    )
    ROLE_CHOICES = (
        ("teacher", "Teacher"),
        ("student", "Student"),
    )
    COURSE_CHOICES = (
        ("cse", "Computer Science"),
        ("ee", "Electrical"),
        ("me", "Mechanical"),
        ("electronics", "Electronics"),
        ("ce", "Civil"),
    )
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, null=True)
    profile_image = models.ImageField(upload_to="profile_images", null=True)
    name = models.CharField(max_length=50, null=True)
    username = models.CharField(max_length=25, null=True)
    email = models.CharField(max_length=50, null=True)
    date_of_birth = models.DateField(null=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, null=True)
    phone = models.BigIntegerField(null=True)
    address = models.CharField(max_length=150, null=True)
    course = models.CharField(max_length=50, choices=COURSE_CHOICES, null=True)
    status = models.BooleanField(default=True)
    github = models.CharField(max_length=150, null=True)
    instagram = models.CharField(max_length=150, null=True)
    twitter = models.CharField(max_length=150, null=True)
    facebook = models.CharField(max_length=150, null=True)
    auth_id = models.IntegerField(null=True)

    def __str__(self):
        return self.name
