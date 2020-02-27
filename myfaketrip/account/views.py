import json
import bcrypt
import jwt

import my_settings

from .models import Account

from django.views import View
from django.http  import HttpResponse, JsonResponse

SECRET_KEY = my_settings.SECRET_KEY

class SignUp(View):
    def post(self, request):
        data = json.loads(request.body)

        try:
            if Account.objects.filter(email=data['email']).exists():
                return JsonResponse({'message':"다른 이메일을 입력하세요."}, status = 400)
            
            password = data['password'].encode('utf-8')
            password_securated = bcrypt.hashpw(password, bcrypt.gensalt()).decode('utf-8')

            