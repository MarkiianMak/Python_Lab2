import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myproject.settings")
django.setup()

from courses.repository import Repository

repo = Repository()

repo.create_user("Іван", "Коваленко", "ivan@example.com")
repo.create_category("Програмування")
repo.create_course("Python для початківців", 30, 1)

users = repo.get_all_users()
for user in users:
    print(f"User: {user.firstName} {user.lastName}, Email: {user.email}")

repo.get_user_by_id(1)    

repo.create_additional_resource("http://example.com/resource1", 1)
