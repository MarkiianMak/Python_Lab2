from django.db import models


class User(models.Model):
    userId = models.AutoField(primary_key=True)
    firstName = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    def __str__(self):
        return f"{self.firstName} {self.lastName}"


class Teacher(models.Model):
    teachersId = models.AutoField(primary_key=True)
    firstName = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.firstName} {self.lastName}"


class Category(models.Model):
    categoryId = models.AutoField(primary_key=True)
    categoryName = models.CharField(max_length=100)

    def __str__(self):
        return self.categoryName


class Course(models.Model):
    courseId = models.AutoField(primary_key=True)
    courseName = models.CharField(max_length=100)
    duration = models.FloatField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.courseName


class AdditionalResource(models.Model):
    additionalResourcesId = models.AutoField(primary_key=True)
    url = models.TextField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='resources')

    def __str__(self):
        return f"Resource for {self.course.courseName}"


class UserTeacherQuestion(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    body = models.TextField(null=True, blank=True)
    createdAt = models.DateTimeField()

    class Meta:
        unique_together = ('teacher', 'user')

    def __str__(self):
        return f"Question from {self.user.firstName} to {self.teacher.firstName}"


class UserCourseComment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    body = models.TextField(null=True, blank=True)
    createdAt = models.DateTimeField()

    class Meta:
        unique_together = ('user', 'course')

    def __str__(self):
        return f"Comment by {self.user.firstName} on {self.course.courseName}"


class UserCourseReview(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    rating = models.IntegerField()
    reviewText = models.TextField(null=True, blank=True)

    class Meta:
        unique_together = ('user', 'course')

    def __str__(self):
        return f"Review {self.rating}/5 by {self.user.firstName} on {self.course.courseName}"


class UserCourseEnrollment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    enrolledAt = models.DateTimeField()
    progress = models.IntegerField()

    class Meta:
        unique_together = ('user', 'course')

    def __str__(self):
        return f"{self.user.firstName} enrolled in {self.course.courseName}"


class TeacherCourse(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('teacher', 'course')

    def __str__(self):
        return f"{self.teacher.firstName} teaches {self.course.courseName}"
