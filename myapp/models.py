from django.db import models
from django.contrib.auth.models import User


# ================= COURSE =================
class Course(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    duration = models.CharField(max_length=50)
    trainer = models.CharField(max_length=100)
    price = models.IntegerField(default=0)

    def __str__(self):
        return self.title


# ================= STUDENT PROFILE =================
class StudentProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    course = models.ForeignKey(
        Course,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    paid_fees = models.IntegerField(default=0)
    result = models.CharField(max_length=20, default="Pending")

    def __str__(self):
        return self.user.username


# ================= MARKS =================
class Marks(models.Model):
    student = models.ForeignKey(
        StudentProfile,
        on_delete=models.CASCADE,
        related_name="marks_records"
    )
    subject = models.CharField(max_length=100)
    marks_obtained = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.student.user.username} - {self.subject}"


# ================= NOTICE =================
class Notice(models.Model):
    notice = models.TextField()
    status = models.CharField(max_length=20, default="Active")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.notice[:50]


# ================= ATTENDANCE =================
class Attendance(models.Model):
    student = models.ForeignKey(StudentProfile, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=10, default="Present")

    def __str__(self):
        return f"{self.student.user.username} - {self.status}"
    