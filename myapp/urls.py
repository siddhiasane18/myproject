from django.urls import path

from . import views

urlpatterns = [

    # ================= HOME =================
    path(
        '',
        views.index,
        name='home'
    ),

    # ================= ABOUT =================
    path(
        'about/',
        views.about,
        name='about'
    ),

    # ================= AUTH =================
    path(
        'register/',
        views.register,
        name='register'
    ),

    path(
        'login/',
        views.user_login,
        name='login'
    ),

    path(
        'logout/',
        views.user_logout,
        name='logout'
    ),

    # ================= DASHBOARD =================
    path(
        'dashboard/',
        views.dashboard,
        name='dashboard'
    ),

    # ================= STUDENTS =================
    path(
        'students/',
        views.students,
        name='students'
    ),

    # ================= COURSES =================
    path(
        'courses/',
        views.courses,
        name='courses'
    ),

    path(
        'add-course/',
        views.add_course,
        name='add_course'
    ),

    # ================= UPDATE STUDENT =================
    path(
        'update/<int:id>/',
        views.update_student,
        name='update_student'
    ),

    # ================= DELETE STUDENT =================
    path(
        'delete/<int:id>/',
        views.delete_student,
        name='delete_student'
    ),

    # ================= ATTENDANCE =================
    path(
        'attendance/',
        views.attendance,
        name='attendance'
    ),

    # ================= MARKS =================
    path(
        'marks/',
        views.marks,
        name='marks'
    ),

    # ================= RESULT =================
    path(
        'result/',
        views.result,
        name='result'
    ),

    # ================= NOTICE =================
    path(
        'notice/',
        views.notice,
        name='notice'
    ),

    # ================= FEES =================
    path(
        'fees/',
        views.fees,
        name='fees'
    ),

    # ================= EDIT FEES =================
    path(
        'edit-fees/<int:id>/',
        views.edit_fees,
        name='edit_fees'
    ),
]