from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from user.auth.serializers import UserCredentialsSerializer
from .serializers import *
from .models import *


def manageUser(data, type):
    serializer = CreateUserSerializer(data=data)
    res = {'data': 'Error', 'success': False}
    if serializer.is_valid():
        user = serializer.save()
        datas = data.copy()
        datas["user_id"] = user.id
        if type == 2:
            serializer_intern = InternSerializer(data=datas)
            if serializer_intern.is_valid():
                user = serializer_intern.save()
        res = {'data': user, 'success': True}
    return res


class AgentView(viewsets.ModelViewSet):
    queryset = Agent.objects.all()
    serializer_class = AgentSerializer

    def get_queryset(self):
        return self.queryset.filter(active=True)

    def create(self, request, *args, **kwargs):
        datas = request.data.copy()
        user = manageUser(datas, 1)
        if user.get('success'):
            datas["user"] = user.get('data').id
            serializer = self.get_serializer(data=datas)
            if serializer.is_valid(raise_exception=True):
                self.perform_create(serializer)
                headers = self.get_success_headers(serializer.data)
                return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
        return Response(data={"error": "Algo sucedió mal creando usuario"}, status=status.HTTP_400_BAD_REQUEST)

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request,  *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(
            instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.active = False
        instance.save()
        return Response(status=status.HTTP_204_NO_CONTENT)


class InternView(viewsets.ModelViewSet):
    queryset = Intern.objects.all()
    serializer_class = InternSerializer
    filterset_fields = ['card_id',]

    def get_queryset(self):
        return self.queryset.filter(active=True)

    def create(self, request, *args, **kwargs):
        datas = request.data.copy()
        user = manageUser(datas, 2)
        if user.get('success'):
            datas["user"] = user.get('data').id
            serializer = self.get_serializer(data=datas)
            if serializer.is_valid(raise_exception=True):
                self.perform_create(serializer)
                headers = self.get_success_headers(serializer.data)
                return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
        return Response(data={"error": "Algo sucedió mal creando usuario"}, status=status.HTTP_400_BAD_REQUEST)

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request,  *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(
            instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.active = False
        instance.save()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CustomAuthToken(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        serializer = UserCredentialsSerializer(data=request.data,
                                               context={'request': request})
        if serializer.is_valid(raise_exception=True):
            user = authenticate(username=serializer.validated_data['username'], password=serializer.validated_data['password'])
            if user:
                token, created = Token.objects.get_or_create(user=user)
                try:
                    intern = Intern.objects.get(user__id=user.id)
                except Intern.DoesNotExist:
                    intern = ''
                info = {
                    'token': token.key,
                    'user': user.id,
                    'intern': intern.id,
                    'username': user.username,
                    'name': f"{user.first_name} {user.last_name}",
                }
                return Response(data=info, status=status.HTTP_201_CREATED)
        return Response(data={"error": "Credenciales incorrectas."}, status=status.HTTP_400_BAD_REQUEST)


