from django.shortcuts import render, redirect, get_object_or_404

from django.contrib.auth import (
    authenticate,
    login,
    logout
)

from django.contrib.auth.decorators import login_required

from django.contrib.auth.models import User

from .models import (
    StudentProfile,
    Notice,
    Course
)


# ================= HOME =================
def index(request):

    return redirect('register')


# ================= ABOUT =================
def about(request):

    return render(request, "about.html")


# ================= REGISTER =================
def register(request):

    if request.user.is_authenticated:
        return redirect("dashboard")

    if request.method == "POST":

        username = request.POST.get("username")

        email = request.POST.get("email")

        password = request.POST.get("password")

        user = User.objects.create_user(

            username=username,

            email=email,

            password=password
        )

        StudentProfile.objects.create(
            user=user
        )

        return redirect("login")

    return render(request, "register.html")


# ================= LOGIN =================
def user_login(request):

    if request.user.is_authenticated:
        return redirect("dashboard")

    if request.method == "POST":

        username = request.POST.get("username")

        password = request.POST.get("password")

        user = authenticate(

            request,

            username=username,

            password=password
        )

        if user:

            login(request, user)

            return redirect("dashboard")

    return render(request, "login.html")


# ================= LOGOUT =================
def user_logout(request):

    logout(request)

    return redirect("login")


# ================= DASHBOARD =================
@login_required(login_url='/login/')
def dashboard(request):

    total_students = StudentProfile.objects.count()

    total_notices = Notice.objects.count()

    total_courses = Course.objects.count()

    return render(request, "dashboard.html", {

        "total_students": total_students,

        "total_notices": total_notices,

        "total_courses": total_courses
    })


# ================= STUDENTS =================
@login_required(login_url='/login/')
def students(request):

    students = StudentProfile.objects.select_related(
        "user",
        "course"
    ).all()

    return render(request, "students.html", {

        "students": students
    })


# ================= COURSES =================
@login_required(login_url='/login/')
def courses(request):

    all_courses = Course.objects.all().order_by("-id")

    return render(request, "courses.html", {

        "courses": all_courses
    })


# ================= ADD COURSE =================
@login_required(login_url='/login/')
def add_course(request):

    if request.method == "POST":

        Course.objects.create(

            title=request.POST.get("title"),

            description=request.POST.get(
                "description"
            ),

            duration=request.POST.get(
                "duration"
            ),

            trainer=request.POST.get(
                "trainer"
            ),

            price=request.POST.get("price")
        )

        return redirect("courses")

    return render(request, "add_course.html")


# ================= UPDATE STUDENT =================
@login_required(login_url='/login/')
def update_student(request, id):

    student = get_object_or_404(
        StudentProfile,
        id=id
    )

    courses = Course.objects.all()

    if request.method == "POST":

        # EMAIL
        student.user.email = request.POST.get(
            "email"
        )

        student.user.save()

        # COURSE
        course_id = request.POST.get("course")

        if course_id:

            course = Course.objects.get(
                id=course_id
            )

            student.course = course

        # MARKS
        student.marks = int(
            request.POST.get("marks") or 0
        )

        # PAID FEES
        student.paid_fees = int(
            request.POST.get("paid_fees") or 0
        )

        # RESULT
        if student.marks >= 35:

            student.result = "Pass"

        else:

            student.result = "Fail"

        # SAVE
        student.save()

        return redirect("students")

    return render(request, "update.html", {

        "student": student,

        "courses": courses
    })


# ================= DELETE STUDENT =================
@login_required(login_url='/login/')
def delete_student(request, id):

    student = get_object_or_404(
        StudentProfile,
        id=id
    )

    if request.method == "POST":

        student.user.delete()

        return redirect("students")

    return render(request, "delete.html", {

        "student": student
    })


# ================= ATTENDANCE =================
@login_required(login_url='/login/')
def attendance(request):

    students = StudentProfile.objects.select_related(
        "user",
        "course"
    ).all()

    return render(request, "attendance.html", {

        "students": students
    })


# ================= MARKS =================
@login_required(login_url='/login/')
def marks(request):

    students = StudentProfile.objects.select_related(
        "user",
        "course"
    ).all()

    return render(request, "marks.html", {

        "students": students
    })


# ================= RESULT =================
@login_required(login_url='/login/')
def result(request):

    students = StudentProfile.objects.select_related(
        "user",
        "course"
    ).all()

    return render(request, "result.html", {

        "students": students
    })


# ================= NOTICE =================
@login_required(login_url='/login/')
def notice(request):

    if request.method == "POST":

        Notice.objects.create(

            notice=request.POST.get("notice"),

            status="Active"
        )

        return redirect("notice")

    notices = Notice.objects.all().order_by("-id")

    return render(request, "notice.html", {

        "notices": notices
    })


# ================= FEES PAGE =================
@login_required(login_url='/login/')
def fees(request):

    students = StudentProfile.objects.select_related(
        "user",
        "course"
    ).all()

    return render(request, "fees.html", {

        "students": students
    })


# ================= EDIT FEES =================
@login_required(login_url='/login/')
def edit_fees(request, id):

    student = get_object_or_404(
        StudentProfile,
        id=id
    )

    courses = Course.objects.all()

    if request.method == "POST":

        course_id = request.POST.get(
            "course"
        )

        paid_fees = request.POST.get(
            "paid_fees"
        )

        # COURSE
        if course_id:

            course = Course.objects.get(
                id=course_id
            )

            student.course = course

        # PAID FEES
        student.paid_fees = int(
            paid_fees or 0
        )

        # SAVE
        student.save()

        return redirect("fees")

    return render(request, "edit_fees.html", {

        "student": student,

        "courses": courses
    })