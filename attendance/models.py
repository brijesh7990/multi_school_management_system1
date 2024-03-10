from django.db import models

from base.models import BaseModel

# Create your models here.

# class StudentAttendance(BaseModel):
#     standard = models.ForeignKey("academic.Standard", on_delete=models.CASCADE, related_name = "standard_attendance" )
#     section = models.ForeignKey("academic.Section", on_delete=models.CASCADE, related_name = "section_attendance" )
#     date = models.DateField()
#     student = models.ManyToManyField("users.Student")
#     present = models.BooleanField(default = False)
#     late_present = models.BooleanField(default = False)
#     absent = models.BooleanField(default = False)
#     school = models.ForeignKey("school.School", on_delete=models.CASCADE, related_name = "school_student_attendance")

#     def __str__(self):
#         return "Attendance for " + str(self.standard) + " " + str(self.section) + " " + str(self.date)

# class TeacherAttendance(BaseModel):
#     teacher = models.ManyToManyField("users.Teacher")
#     date = models.DateField()
#     present = models.BooleanField(default = False)
#     late_present = models.BooleanField(default = False)
#     absent = models.BooleanField(default = False)
#     school = models.ForeignKey("school.School", on_delete=models.CASCADE, related_name = "school_teacher_attendance")

#     def __str__(self):
#         return "Attendance for " + str(self.teacher) + " " + str(self.date)
