from django.db import models

class Instructor(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField(max_length=254)

    def __str__(self):
        return self.email

class Course(models.Model):
    title=models.CharField(max_length=30)
    rating=models.IntegerField()
    instructor=models.ForeignKey(Instructor,on_delete=models.CASCADE,related_name='courses')

    # The "instructor" field is a ForeignKey to the "Instructor" model,
    # which means that each course is associated with a single instructor, 
    # and that instructor can have multiple courses.

    # "on_delete=models.CASCADE" argument specifies that 
    # if an instructor is deleted, all of their associated courses will also be deleted

    #  related_name is often used to specify custom names for reverse relationships.

# The Course model has a ForeignKey to the Instructor model with the related_name='courses' argument. 
# This means that we can access all of the courses associated with an instructor by calling the courses 
# attribute on an Instructor object. Here's an example to illustrate how this works:


# >>> john = Instructor.objects.create(name='John Smith', email='john.smith@example.com')
# >>> math = Course.objects.create(title='Math 101', rating=4, instructor=john)
# >>> physics = Course.objects.create(title='Physics 101', rating=5, instructor=john)

# # We can access all of the courses associated with an instructor by calling the `courses` attribute on the `Instructor` object.

# >>> john.courses.all()
# <QuerySet [<Course: Course object (1)>, <Course: Course object (2)>]>

# As you can see, calling john.courses.all() returns a queryset containing all of the courses associated with the john instructor.
 
# This is equivalent to calling Course.objects.filter(instructor=john). If we hadn't specified related_name='courses' in the ForeignKey field,
# we would have to use the default name of the reverse relationship, which is course_set:


# # We can also access all of the courses associated with an instructor using the default `course_set` attribute.

# >>> john.course_set.all()
# <QuerySet [<Course: Course object (1)>, <Course: Course object (2)>]>

# However, using related_name to specify a custom name for the reverse relationship (courses in this case) makes the code more readable and easier to understand.



