import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myproject.settings")
django.setup()

from courses.repository import Repository

repo = Repository()

# a = repo.create_user("Alez", "Ковалеко", "i1@example.com")



# repo.delete_user(1)
# repo.create_category("Програмування")
# repo.create_course("Python для початківців", 30, 1)

# users = repo.get_all_users()
# for user in users:
#     print(f"User: {user.firstName} {user.lastName}, Email: {user.email}")

repo.update_course(2, name="Python for Beginners", duration=35)

# print(repo.get_user_by_id(a.userId))

# repo.create_additional_resource("http://example.com/resource1", 1)
