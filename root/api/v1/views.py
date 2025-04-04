from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from root.models import About, Contact, Team, Client, Star, Testimonials
from .serializer import (
    AboutSerializer, ContactSerializer, TeamSerializer,
    ClientSerializer, StarSerializer, TestimonialsSerializer
)
from .permissions import IsAdminOrReadOnly

class AboutViewSet(ModelViewSet):
    queryset = About.objects.all()
    serializer_class = AboutSerializer
    permission_classes = [IsAdminOrReadOnly]

class ContactViewSet(ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class TeamViewSet(ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer
    permission_classes = [IsAdminOrReadOnly]

class ClientViewSet(ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    permission_classes = [IsAdminOrReadOnly]

class StarViewSet(ModelViewSet):
    queryset = Star.objects.all()
    serializer_class = StarSerializer
    permission_classes = [IsAdminOrReadOnly]

class TestimonialsViewSet(ModelViewSet):
    queryset = Testimonials.objects.all()
    serializer_class = TestimonialsSerializer
    permission_classes = [IsAdminOrReadOnly]

from rest_framework.response import Response
from rest_framework.views import APIView

class APIHomeView(APIView):
    def get(self, request):
        return Response({
            "message": "Welcome, API version 1",
            "endpoints": {
                "blog": "/api/v1/blog/",
                "services": "/api/v1/service/",
                "portfolio": "/api/v1/portfolio/",
                "accounts": "/api/v1/accounts/",
            }
        })
