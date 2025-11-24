import requests
import json
from crm_ui.NetworkHelper import NetworkHelper


success = NetworkHelper.login("test", "1")
if not success:
    exit()


activities = NetworkHelper.get_activities()
print("Activities:", json.dumps(activities, indent=2))


new_activity = {
    "activity_type": "running",  
    "duration_sec": 3600.0,
    "distance_m": 10000.0,
    "elevation_gain_m": 200,
    "height": 180,
    "start_time": "2025-11-24T08:00:00Z",
    "end_time": "2025-11-24T09:00:00Z"
}

created = NetworkHelper.create_activity(new_activity)
print("Created activity:", json.dumps(created, indent=2))

activity_id = created['id']
activity = NetworkHelper.get_activity(activity_id)
print("Single activity:", json.dumps(activity, indent=2))

updated_data = {
    "activity_type": "cycling",
    "duration_sec": 5400.0,
    "distance_m": 20000.0,
    "elevation_gain_m": 150,
    "height": 180,
    "start_time": "2025-11-24T10:00:00Z",
    "end_time": "2025-11-24T11:30:00Z"
}

updated_activity = NetworkHelper.update_activity(activity_id, updated_data)
print("Updated activity:", json.dumps(updated_activity, indent=2))

status = NetworkHelper.delete_activity(activity_id)
print("Deleted status:", status)

comments = NetworkHelper.get_comments()
print("Comments:", json.dumps(comments, indent=2))

# 2️⃣ Створити коментар
new_comment = {
    "activity": 1,
    "body": "Це тестовий коментар",
    "parent_comment": None
}
created = NetworkHelper.create_comment(new_comment)
print("Created comment:", created)

# 3️⃣ Отримати коментар за ID
comment = NetworkHelper.get_comment(created['id'])
print("Single comment:", comment)

# 4️⃣ Оновити коментар
update_data = {
    "body": "Оновлений текст коментаря"
}
updated = NetworkHelper.update_comment(created['id'], update_data)
print("Updated comment:", updated)

# 5️⃣ Видалити коментар
status = NetworkHelper.delete_comment(created['id'])
print("Deleted status:", status)