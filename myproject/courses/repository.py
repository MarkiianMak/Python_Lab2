from .models import User, Teacher, Course, Category, AdditionalResource


class Repository:

    # ---------- USER ----------
    def get_all_users(self):
        return User.objects.all()

    def get_user_by_id(self, user_id):
        return User.objects.get(userId=user_id)

    def create_user(self, first_name, last_name, email):
        return User.objects.create(firstName=first_name, lastName=last_name, email=email)
    
    def update_user(self, user_id, first_name=None, last_name=None, email=None):
        user = User.objects.get(userId=user_id)
        if first_name:
            user.firstName = first_name
        if last_name:
            user.lastName = last_name
        if email:
            user.email = email
        user.save()
        return user
            
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
    
    def update_teacher(self, teacher_id, first_name=None, last_name=None):
        teacher = Teacher.objects.get(teacherId=teacher_id)
        if first_name:
            teacher.firstName = first_name
        if last_name:
            teacher.lastName = last_name
        teacher.save()
        return teacher
    
    def delete_teacher(self, teacher_id):
        teacher = Teacher.objects.get(teacherId=teacher_id)
        teacher.delete()

    # ---------- COURSE ----------
    def get_all_courses(self):
        return Course.objects.all()

    def get_course_by_id(self, course_id):
        return Course.objects.get(courseId=course_id)

    def create_course(self, name, duration, category_id=None):
        category = Category.objects.get(categoryId=category_id) if category_id else None
        return Course.objects.create(courseName=name, duration=duration, category=category)
    
    def update_course(self, course_id, name=None, duration=None, category_id=None):
        course = Course.objects.get(courseId=course_id)
        if name:
            course.courseName = name
        if duration:
            course.durationInHours = duration
        if category_id is not None:
            category = Category.objects.get(categoryId=category_id)
            course.category = category
        course.save()
        return course
    
    def delete_course(self, course_id):
        course = Course.objects.get(courseId=course_id)
        course.delete()


    # ---------- CATEGORY ----------
    def get_all_categories(self):
        return Category.objects.all()

    def get_category_by_id(self, category_id):
        return Category.objects.get(categoryId=category_id)

    def create_category(self, name):
        return Category.objects.create(categoryName=name)
    
    def update_category(self, category_id, name=None):
        category = Category.objects.get(categoryId=category_id)
        if name:
            category.categoryName = name
        category.save()
        return category
    
    def delete_category(self, category_id):
        category = Category.objects.get(categoryId=category_id)
        category.delete()    
    

    # ---------- ADDITIONAL RESOURCE ----------
    def get_all_additional_resources(self):
        return AdditionalResource.objects.all()

    def get_additional_resource_by_id(self, resource_id):
        return AdditionalResource.objects.get(additionalResourcesId=resource_id)
    
    def create_additional_resource(self, url, course_id):
        course = Course.objects.get(courseId=course_id)
        return AdditionalResource.objects.create(url=url, course=course)
    
    def update_additional_resource(self, resource_id, url=None, course_id=None):
        resource = AdditionalResource.objects.get(additionalResourcesId=resource_id)
        if url:
            resource.url = url
        if course_id:
            course = Course.objects.get(courseId=course_id)
            resource.course = course
        resource.save()
        return resource
    
    def delete_additional_resource(self, resource_id):
        resource = AdditionalResource.objects.get(additionalResourcesId=resource_id)
        resource.delete()
    

