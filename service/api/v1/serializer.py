from rest_framework import serializers
from service.models import Service, Special_services
from portfolio.models import Category

class ServiceSerializer(serializers.ModelSerializer):
    category = serializers.PrimaryKeyRelatedField(many=True, queryset=Category.objects.all())  
    specials = serializers.PrimaryKeyRelatedField(many=True, queryset=Special_services.objects.all())  

    class Meta:
        model = Service
        fields = "__all__"

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        
        rep["category"] = [category.name for category in instance.category.all()]
        
        rep["specials"] = [special.title for special in instance.specials.all()]
        
        return rep
