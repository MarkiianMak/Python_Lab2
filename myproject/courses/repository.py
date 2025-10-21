from .models import User, Teacher, Course, Category, AdditionalResource


class Repository:

    # ---------- USER ----------
    def get_all_users(self):
        return User.objects.all()

    def get_user_by_id(self, user_id):
        return User.objects.get(userId=user_id)

    def create_user(self, first_name, last_name, email):
        return User.objects.create(firstName=first_name, lastName=last_name, email=email)
    
    def delete_user(self, user_id):
        user = User.objects.get(userId=user_id)
        user.delete()
        

    # ---------- TEACHER ----------
    def get_all_teachers(self):
        return Teacher.objects.all()

    def get_teacher_by_id(self, teacher_id):
        return Teacher.objects.get(teacherId=teacher_id)

    def create_teacher(self, first_name, last_name):
        return Teacher.objects.create(firstName=first_name, lastName=last_name)

    # ---------- COURSE ----------
    def get_all_courses(self):
        return Course.objects.all()

    def get_course_by_id(self, course_id):
        return Course.objects.get(courseId=course_id)

    def create_course(self, name, duration, category_id=None):
        category = Category.objects.get(categoryId=category_id) if category_id else None
        return Course.objects.create(courseName=name, duration=duration, category=category)


    # ---------- CATEGORY ----------
    def get_all_categories(self):
        return Category.objects.all()

    def get_category_by_id(self, category_id):
        return Category.objects.get(categoryId=category_id)

    def create_category(self, name):
        return Category.objects.create(categoryName=name)
    

    # ---------- ADDITIONAL RESOURCE ----------
    def get_all_additional_resources(self):
        return AdditionalResource.objects.all()

    def get_additional_resource_by_id(self, resource_id):
        return AdditionalResource.objects.get(additionalResourcesId=resource_id)
    
    def create_additional_resource(self, url, course_id):
        course = Course.objects.get(courseId=course_id)
        return AdditionalResource.objects.create(url=url, course=course)
    

