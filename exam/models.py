from django.db import models

from base.models import BaseModel

# Create your models here.


class Exam(BaseModel):
    school = models.ForeignKey("school.School", on_delete = models.CASCADE, related_name = "school_exam")
    standard = models.ForeignKey("academic.Standard", on_delete = models.CASCADE, related_name = "standard_exam")
    name = models.CharField(max_length = 255)
    section = models.ForeignKey("academic.Section", on_delete = models.CASCADE, related_name = "section_exam")
    subject = models.ForeignKey("academic.Subject", on_delete = models.CASCADE, related_name = "subject_exam")
    date = models.DateField()
    time_from = models.TimeField()
    time_to  = models.TimeField()
    room = models.CharField(max_length = 255)

class Grade(BaseModel):
    name = models.CharField(max_length = 255)
    point = models.FloatField()
    mark_from = models.FloatField()
    mark_upto = models.FloatField()
    note = models.CharField(max_length = 255)

