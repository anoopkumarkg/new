from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import StudentTable
from .serializer import StudentSerializer
from rest_framework.authentication import BasicAuthentication,SessionAuthentication,TokenAuthentication
from rest_framework.permissions import BasePermission,DjangoModelPermissionsOrAnonReadOnly,DjangoModelPermissions,AllowAny,IsAuthenticated,IsAdminUser,IsAuthenticatedOrReadOnly
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication
from django_filters.rest_framework import DjangoFilterBackend

class MyPermission(BasePermission):

    def has_permission(self,request,view):
        if  request.user.username == 'aman' and request.method == 'GET':
           return True

        return False


class GetToken(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({'token': token.key,"email": user.id})


# Create your views here.
class StudentView(ModelViewSet):
    queryset= StudentTable.objects.all()
    serializer_class= StudentSerializer
    authentication_classes= [JWTAuthentication]
    permission_classes= [IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name', 'city']





# AllowAny = chahe user login ya na ho vo sara data dekh sakta hai default ye hi hota hai
# IsAuthenticated = user login hona chahiye chahe vo simple user ho ya admin user ho
# IsAdminUser  = Allow only Admin user
# IsAuthenticatedOrReadOnly = agar user authenticate hoga to vo sab kuch kar sakta hai varna vo only read karsakta hai like get 

# jab bhi mai ViewSet ka use karunga to mujhe apna urls bana hoga urls.py file gunrate karke