from django.contrib.auth import authenticate, login
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from courses.models import User

@csrf_exempt
def api_login(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(request, username=username, password=password)
    if user:
        login(request, user)  
        return JsonResponse({'message': 'Logged in'})
    else:
        return JsonResponse({'message': 'Invalid credentials'}, status=401)

@csrf_exempt
def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = User.objects.create_user(username=username, password=password)
        return JsonResponse({'message': f'User {username} created'})
    return JsonResponse({'message': 'Method not allowed'}, status=405)