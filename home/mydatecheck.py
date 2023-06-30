from home.models import seminar
from datetime import date

current_date = date.today()
def datecheck():
    tempdate = seminar.objects.all()
    for i in tempdate:
        if current_date > i.seminardate:
            i.show = False
            i.save()
