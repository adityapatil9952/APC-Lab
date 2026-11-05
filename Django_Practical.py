# Django (simple single-file example)
#
# Problem Statement:
# A college wants to store Student records (name, age, course) in a database.
# Using Django's ORM, create the table, insert records, then read, update
# and delete them.
#
# Run:  pip install django
#       python Django_Practical.py

import django
from django.conf import settings

# Minimal settings so Django works without a full project
settings.configure(
    DEBUG=True,
    INSTALLED_APPS=[],
    DATABASES={
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": ":memory:",          # temporary database in RAM
        }
    },
    DEFAULT_AUTO_FIELD="django.db.models.AutoField",
)
django.setup()

from django.db import models, connection


# Model = one database table
class Student(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    course = models.CharField(max_length=50)

    class Meta:
        app_label = "lab"

    def __str__(self):
        return f"{self.name}, {self.age}, {self.course}"


if __name__ == "__main__":
    # Create the table
    with connection.schema_editor() as editor:
        editor.create_model(Student)

    # CREATE
    Student.objects.create(name="Sanket", age=20, course="BCA")
    Student.objects.create(name="Aditya", age=21, course="BSc CS")
    Student.objects.create(name="Riya", age=22, course="MCA")

    # READ
    print("--- All Students ---")
    for s in Student.objects.all():
        print(s)

    print("\n--- Students older than 20 ---")
    for s in Student.objects.filter(age__gt=20):
        print(s)

    # UPDATE
    s = Student.objects.get(name="Sanket")
    s.age = 21
    s.save()
    print("\nAfter update:", Student.objects.get(name="Sanket"))

    # DELETE
    Student.objects.filter(name="Riya").delete()
    print("\n--- After delete ---")
    for s in Student.objects.all():
        print(s)

    print("\nTotal students:", Student.objects.count())
