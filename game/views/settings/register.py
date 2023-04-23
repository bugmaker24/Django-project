from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User
from game.models.player.player import Player

class PlayerView(APIView):
    def post(self, request):
        data = request.POST
        username = data.get("username", "").strip()
        password = data.get("password", "").strip()
        password_confirm = data.get("password_confirm", "").strip()

        if not username or not password:
            return Response({
                'result':"用户名或密码不能为空",
            })

        if password != password_confirm:
            return Response({
                'result':"两次密码不一致",
            })

        if User.objects.filter(username=username).exists():
            return Response({
                'result':"用户名已存在"
            })
        user = User(username=username)
        user.set_password(password)
        user.save()

        Player.objects.create(user=user, photo="https://tse2-mm.cn.bing.net/th/id/OIP-C.cCwOJhGaHW2iri4X1tMknQHaHa?w=186&h=186&c=7&r=0&o=5&dpr=1.25&pid=1.7")
        return Response({
            'result':"success",
        })
