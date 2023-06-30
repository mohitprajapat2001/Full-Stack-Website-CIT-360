from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User, auth
from home.mydatecheck import datecheck
from django.contrib import messages
from .models import (
    funFact,
    carosuelImages,
    citinMedia,
    topNews,
    importantNotice,
    faculty,
    alumani,
    imggallery,
    Notes,
    documentsteps,
    achievers,
    seminar,
    internship,
    eventsimages,
    bannernews,
)
from accounts.models import student
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

#Lambda Functios 
get_student = lambda request: student.objects.get(username=request.user.username)

filterdata = lambda model, field, value: model.objects.filter(**{field: value})

getdata = lambda model, field, value: model.objects.get(**{field: value})

#Quality Functions
def validate(request, *args):
    map(lambda x: request.POST[x], args)
    
def create_params(*args):
    data_dictionary = {}
    for arg in args:
        key = arg.__name__+'_data'
        data_dictionary[key] = arg.objects.all()
    return data_dictionary

# Main Functions
def home(request):
    datecheck()
    params = create_params(carosuelImages,
                          citinMedia,
                          topNews,
                          importantNotice,
                          bannernews,
                          faculty,
                          alumani,
                          faculty,
                          alumani,
                          imggallery,
                          seminar,
                          internship,
                          student,
                          eventsimages)
    params['facts'] = funFact.objects.all()[0]
    params['users'] = student.objects.all()
    if request.user.is_authenticated:
        params['current_user'] = get_student(request)    
    return render(request, "home.html", params)

def gallery(request, category):
    params = create_params(citinMedia,
                                    topNews,
                                    importantNotice,
                                    bannernews)
    params['current_user'] = get_student(request)
    params['category_data'] = filterdata(imggallery, 'category', category)
    params['category'] = category
    return render(request, "element/gallerybase.html", params)


def profile(request, username):
    params = create_params(bannernews)
    params['current_user'] = get_student(request)
    if get_student(request).role == 'faculty':
        params["facultydata"] = getdata(faculty, 'username', username)
        if not faculty.objects.get(username = request.user.username).images:
            messages.info(request, "Please ADD Profile Image For Better Accessibility")
    return render(request, "accountsHTML\profile.html", params)

@csrf_exempt
def edituser(request, username):
    try:
        if request.method == "POST":
            current_user = student.objects.get(username=username)
            if current_user != None:
                current_user.auth_id = request.user.id
                current_user.name = request.POST.get("fullname")
                if len(request.FILES) != 0:
                    current_user.profile_image = request.FILES["profile_image"]
                current_user.phone = request.POST.get("phone")
                current_user.address = request.POST.get("address")
                current_user.gender = request.POST.get("gender")
                current_user.date_of_birth = request.POST.get("date_of_birth")
                current_user.facebook = request.POST.get("facebook")
                current_user.github = request.POST.get("github")
                current_user.twitter = request.POST.get("twitter")
                current_user.instagram = request.POST.get("instagram")
                current_user.save()
                facultyedit(request, username)
                return redirect(f"/profile/{current_user.username}")
    except Exception as e:
        messages.info(request, f"{e}")
        return redirect("/")
    
@csrf_exempt
def facultyedit(request, username):
    try:
        if request.method == "POST":
            validate(
                ('title', 'email', 'description')
            )
            faculty_edit = faculty.objects.get(username=username)
            if faculty_edit != None:
                faculty_edit.auth_id = request.user.id
                faculty_edit.name = get_student(request).name
                faculty_edit.images = get_student(request).profile_image
                faculty_edit.title = request.POST.get("title")
                faculty_edit.about = request.POST.get("description")
                faculty_edit.link_facebook = get_student(request).facebook
                faculty_edit.link_github = get_student(request).github
                faculty_edit.link_twitter = get_student(request).twitter
                faculty_edit.link_instagram = get_student(request).instagram
                faculty_edit.save()
                return redirect(f"/profile/{get_student(request).username}")
    except Exception as e:
        messages.info(request, f"{e}")
        return redirect("/")


def panel(request,role):
    if role == 'student':
        params = create_params(citinMedia,
                            topNews,
                            importantNotice,
                            bannernews,)
        params['current_user'] = get_student(request)
        return render(request, "accountsHTML/studentpanel.html", params)
    elif role == 'faculty':
        params = create_params(citinMedia,
                           topNews,
                           importantNotice,
                           bannernews,)
        params['current_user'] = get_student(request)
        return render(request, "accountsHTML/teacherspanel.html", params)

@csrf_exempt
def notesdownload(request):
    try:
        if request.method == "POST":
            course = request.POST.get("course")
            semester = request.POST.get("semester")
            notesdata = Notes.objects.filter(course=course, semester=semester)
            usernotes = list(notesdata.values())
            print(usernotes)
            return JsonResponse(
                {"status": "Data Fetched Successfully", "usernotes": usernotes}
            )
    except Exception as e:
        print("Error", e)
        return JsonResponse("Error")


def documentview(request, document):
    params = create_params(citinMedia,
                           topNews,
                           importantNotice,
                           bannernews,)
    params['current_user'] = get_student(request)
    params['mysteps'] = documentsteps.objects.get(documenttitle=document)
    return render(request, "accountsHTML/documentbase.html", params)


def achievements(request):
    params = create_params(citinMedia,
                           topNews,
                           importantNotice,
                           bannernews,
                           achievers)
    params['current_user'] = get_student(request)
    return render(request, "element/achievements.html", params)

@csrf_exempt
def notescreate(request):
    if request.method == "POST":
        validate(("note_creator", "title", "course", "semester"))
        if not faculty.objects.filter(name = request.user.first_name):
            messages.info(request, "You are Not Authorized Please Update Profile Section!!")
            return redirect(f"panel/faculty")
        Notes.objects.create(
            creator=request.POST.get("note_creator"),
            title=request.POST.get("title"),
            course=request.POST.get("course"),
            semester=request.POST.get("semester"),
            file=request.FILES.get("file"),
        )
        messages.info(request, "Notes Succesfully Added")
        return redirect(f"panel/faculty")
    else:
        messages.info(request, "Notes Details Error")
        return redirect(f"panel/faculty")


@csrf_exempt
def internshipcreate(request):
    if not faculty.objects.filter(name = request.user.first_name):
        messages.info(request, "You are Not Authorized Please Update Profile Section!!")
        return redirect(f"panel/faculty")
    if request.method == "POST":
        validate(("internshipcreator","field","jobtitle","stipend","url_internship","jobdescription",))
        internship.objects.create(
            internshipcreator=request.POST.get("internshipcreator"),
            field=request.POST.get("field"),
            jobtitle=request.POST.get("jobtitle"),
            stipend=request.POST.get("stipend"),
            url_internship=request.POST.get("url_internship"),
            jobdescription=request.POST.get("jobdescription"),
            jobimage=request.FILES.get("jobimage"),
        )
        messages.info(request, "Internship Details Succesfully Added")
        return redirect(f"panel/faculty")
    else:
        messages.info(request, "Internship Details Error")
        return redirect(f"panel/faculty")


@csrf_exempt
def seminarcreate(request):
    if not faculty.objects.filter(name = request.user.first_name):
        messages.info(request, "You are Not Authorized Please Update Profile Section!!")
        return redirect(f"panel/faculty")
    if request.method == "POST":
        validate(("seminarcreator","seminar_tag","seminartitle","seminardate","duration","seminarprice","seminar_description","seminar_url",))
        seminar.objects.create(
            seminarcreator=request.POST.get("seminarcreator"),
            seminar_tag=request.POST.get("seminar_tag"),
            seminartitle=request.POST.get("seminartitle"),
            seminardate=request.POST.get("seminardate"),
            duration=request.POST.get("duration"),
            seminarprice=request.POST.get("seminarprice"),
            seminar_description=request.POST.get("seminar_description"),
            seminar_url=request.POST.get("seminar_url"),
            seminarimage=request.FILES.get("seminarimage"),
        )
        print(faculty.objects.get(username = request.user.username))
        messages.info(request, "Seminar Added Succesfully Added")
        return redirect(f"panel/faculty")
    else:
        messages.info(request, "Seminar Details Error")
        return redirect(f"panel/faculty")
    
    
def internshipdetails(request, data):
    if not request.user.is_authenticated:
        messages.info(request, "User is Not Authenticate to View")
        return redirect('/')
    params = create_params(bannernews)
    params['current_user'] = get_student(request)
    if data == 'all':
        params['internship_data'] = internship.objects.all()
        params['data'] = data
        return render(request, 'element/internship landing.html', params)
    params['internship_data'] = getdata(internship, 'id', data)
    params['facultydata'] = getdata(faculty, 'name', getdata(internship, 'id', data).internshipcreator)
    return render(request, 'element/internship landing.html', params)
       
