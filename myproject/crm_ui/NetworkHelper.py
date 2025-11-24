import requests
import json

class NetworkHelper:
    """
    NetworkHelper для доступу до REST API колеги.
    Підтримує TokenAuthentication і CRUD для двох ресурсів: activities та projects.
    """
    BASE_URL = "http://127.0.0.1:12345/api"
    token = None

    @staticmethod
    def login(username, password):
        """
        Логіниться і отримує токен.
        """
        url = f"http://127.0.0.1:12345/api-token-auth/"
        headers = {'Content-Type': 'application/json'}
        data = {'username': username, 'password': password}
        response = requests.post(url, headers=headers, data=json.dumps(data))

        if response.status_code != 200:
            print("Login failed:", response.status_code, response.text)
            return False

        response_json = response.json()
        NetworkHelper.token = response_json['token']
        print("Token:", NetworkHelper.token)
        return True

    @staticmethod   
    def set_token(token):
        NetworkHelper.token = token

    @staticmethod
    def _auth_headers():
        if not NetworkHelper.token:
            raise Exception("Token не встановлено. Виконайте login() спочатку.")
        return {'Authorization': f'Token {NetworkHelper.token}',
                'Content-Type': 'application/json'}



    @staticmethod
    def get_activities():
        url = f"{NetworkHelper.BASE_URL}/activities/"
        response = requests.get(url, headers=NetworkHelper._auth_headers())
        response.raise_for_status()
        return response.json()

    @staticmethod
    def get_activity(activity_id):
        url = f"{NetworkHelper.BASE_URL}/activities/{activity_id}/"
        response = requests.get(url, headers=NetworkHelper._auth_headers())
        response.raise_for_status()
        return response.json()

    @staticmethod
    def create_activity(data):
        url = f"{NetworkHelper.BASE_URL}/activities/"
        response = requests.post(url, headers=NetworkHelper._auth_headers(), data=json.dumps(data))
        response.raise_for_status()
        return response.json()

    @staticmethod
    def update_activity(activity_id, data):
        url = f"{NetworkHelper.BASE_URL}/activities/{activity_id}/"
        response = requests.put(url, headers=NetworkHelper._auth_headers(), data=json.dumps(data))
        response.raise_for_status()
        return response.json()

    @staticmethod
    def delete_activity(activity_id):
        url = f"{NetworkHelper.BASE_URL}/activities/{activity_id}/"
        response = requests.delete(url, headers=NetworkHelper._auth_headers())
        response.raise_for_status()
        return response.status_code
    


    @staticmethod
    def get_comments():
        url = f"{NetworkHelper.BASE_URL}/comments/"
        response = requests.get(url, headers=NetworkHelper._auth_headers())
        response.raise_for_status()
        return response.json()

    @staticmethod
    def get_comment(comment_id):
        url = f"{NetworkHelper.BASE_URL}/comments/{comment_id}/"
        response = requests.get(url, headers=NetworkHelper._auth_headers())
        response.raise_for_status()
        return response.json()

    @staticmethod
    def create_comment(data):
       
        url = f"{NetworkHelper.BASE_URL}/comments/"
        response = requests.post(url, headers=NetworkHelper._auth_headers(), json=data)
        response.raise_for_status()
        return response.json()

    @staticmethod
    def update_comment(comment_id, data):
        url = f"{NetworkHelper.BASE_URL}/comments/{comment_id}/"
        response = requests.patch(url, headers=NetworkHelper._auth_headers(), json=data)
        response.raise_for_status()
        return response.json()

    @staticmethod
    def delete_comment(comment_id):
        url = f"{NetworkHelper.BASE_URL}/comments/{comment_id}/"
        response = requests.delete(url, headers=NetworkHelper._auth_headers())
        response.raise_for_status()
        return response.status_code