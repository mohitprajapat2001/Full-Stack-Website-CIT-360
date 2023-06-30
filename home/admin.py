from django.contrib import admin
from .models import (
    carosuelImages,
    topNews,
    importantNotice,
    citinMedia,
    faculty,
    alumani,
    imggallery,
    Notes,
    bannernews,
    achievers,
    eventsimages,
)

# Register your models here.
# admin.site.register(funFact)
admin.site.register(carosuelImages)
admin.site.register(topNews)
admin.site.register(importantNotice)
admin.site.register(citinMedia)
admin.site.register(faculty)
admin.site.register(alumani)
admin.site.register(imggallery)
admin.site.register(Notes)
admin.site.register(bannernews)
admin.site.register(achievers)
admin.site.register(eventsimages)
