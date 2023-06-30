from django.db import models

# Create your models here.


class carosuelImages(models.Model):
    images = models.ImageField(upload_to="carosuelImages")
    image_href = models.CharField(max_length=10)
    show = models.BooleanField(default=True)


class importantNotice(models.Model):
    title = models.CharField(max_length=50)
    href = models.CharField(max_length=100)
    show = models.BooleanField(default=True)


class topNews(models.Model):
    title = models.CharField(max_length=50)
    href = models.CharField(max_length=100)
    show = models.BooleanField(default=True)


class citinMedia(models.Model):
    title = models.CharField(max_length=50)
    href = models.CharField(max_length=100)
    show = models.BooleanField(default=True)


class funFact(models.Model):
    proudalumani = models.IntegerField()
    placement = models.IntegerField()


class eventsimages(models.Model):
    eventimage = models.ImageField(upload_to="events")
    show = models.BooleanField(default=True)


class faculty(models.Model):
    images = models.ImageField(upload_to="faculty",null=True,blank=True)
    username = models.CharField(max_length=50)
    name = models.CharField(max_length=25,null=True,blank=True)
    title = models.CharField(max_length=50,null=True,blank=True)
    about = models.CharField(max_length=500,null=True,blank=True)
    link_facebook = models.CharField(max_length=50,null=True,blank=True)
    link_github = models.CharField(max_length=50,null=True,blank=True)
    link_instagram = models.CharField(max_length=50,null=True,blank=True)
    link_twitter = models.CharField(max_length=50,null=True,blank=True)
    show = models.BooleanField(default=True,null=True,blank=True)


class alumani(models.Model):
    images = models.ImageField(upload_to="alumani")
    name = models.CharField(max_length=25)
    title = models.CharField(max_length=50)
    text = models.CharField(max_length=100)
    show = models.BooleanField(default=True)


class imggallery(models.Model):
    CATEGORY_GALLERY = (
        ("citcampus", "CIT Campus"),
        ("labs", "Labs"),
        ("hostel", "Hostel"),
        ("workshop", "Workshop"),
        ("tarunya", "Tarunya"),
        ("lakshya", "Lakshya"),
    )
    images = models.ImageField(upload_to="image_gallery")
    title = models.CharField(max_length=50)
    category = models.CharField(max_length=25, choices=CATEGORY_GALLERY)
    thumbnail = models.BooleanField(default=False)
    show = models.BooleanField(default=True)
    def __str__(self):
        return self.title


class documentsteps(models.Model):
    DOCUMENT_CHOICES = (
        ("consolidated-marksheet", "Consolidated Marksheet"),
        ("provisional-degree", "Provisional Degree"),
        ("duplicate-marksheet", "Duplicate Marksheet"),
        ("migration-certificate", "Migration Certificate"),
    )
    documenttitle = models.CharField(max_length=30, choices=DOCUMENT_CHOICES)
    steps = models.CharField(max_length=5000)
    href = models.CharField(max_length=200)
    def __str__(self):
        return self.documenttitle


class achievers(models.Model):
    thumb = models.ImageField(upload_to="Achievement Thumbnails")
    name = models.CharField(max_length=50)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=2000)
    show = models.BooleanField(default=True)
    def __str__(self):
        return self.name


class Notes(models.Model):
    COURSE_CHOICES = (
        ("cse", "Computer Science"),
        ("ee", "Electrical"),
        ("me", "Mechanical"),
        ("electronics", "Electronics"),
        ("ce", "Civil"),
    )
    creator = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    course = models.CharField(max_length=25, choices=COURSE_CHOICES)
    semester = models.IntegerField()
    file = models.FileField(upload_to="notes")
    show = models.BooleanField(default=True)


class internship(models.Model):
    JOB_FIELD = (
        ("cse", "Computer Science"),
        ("ee", "Electrical"),
        ("me", "Mechanical"),
        ("electronics", "Electronics"),
        ("ce", "Civil"),
    )
    internshipcreator = models.CharField(max_length=50)
    field = models.CharField(max_length=100, choices=JOB_FIELD)
    jobtitle = models.CharField(max_length=50)
    stipend = models.IntegerField()
    url_internship = models.CharField(max_length=50)
    jobdescription = models.CharField(max_length=5000)
    jobimage = models.ImageField(upload_to="Internship Thumbnails")
    show = models.BooleanField(default=True)
    def __str__(self):
        return self.jobtitle


class seminar(models.Model):
    SEMINAR_TAG = (
        ("cse", "Computer Science"),
        ("ee", "Electrical"),
        ("me", "Mechanical"),
        ("electronics", "Electronics"),
        ("ce", "Civil"),
    )
    seminarcreator = models.CharField(max_length=50)
    seminar_tag = models.CharField(max_length=50, choices=SEMINAR_TAG)
    seminartitle = models.CharField(max_length=50)
    seminardate = models.DateField()
    duration = models.IntegerField()
    seminarprice = models.IntegerField()
    seminar_description = models.CharField(max_length=5000)
    seminar_url = models.CharField(max_length=100)
    seminarimage = models.ImageField(upload_to="Seminar Thumbnails")
    show = models.BooleanField(default=True)
    def __str__(self):
        return self.seminartitle
    
class bannernews(models.Model):
    category = models.CharField(max_length=20, null=True, blank=True)
    description = models.CharField(max_length=100, null=True, blank=True)
    href = models.CharField(max_length=200, null=True, blank=True)
    show = models.BooleanField(default=True)
    def __str__(self):
        return self.description
