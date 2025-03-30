from rest_framework import serializers
from root.models import About, Contact, Team, Client, Star, Testimonials

class AboutSerializer(serializers.ModelSerializer):
    class Meta:
        model = About
        fields = "__all__"

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = "__all__"

class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = "__all__"

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = "__all__"

class StarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Star
        fields = "__all__"

class TestimonialsSerializer(serializers.ModelSerializer):
    stars = serializers.CharField(source="stars.count", read_only=True)

    class Meta:
        model = Testimonials
        fields = "__all__"
