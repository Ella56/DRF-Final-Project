from rest_framework import serializers
from service.models import Service, Special_services
from portfolio.models import Category
from accounts.models import User



class ServiceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Service
        fields = "__all__"

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        cat = []
        for category_id in rep["category"]:
            title = Category.objects.get(id=category_id).title
            cat.append(title)
        rep["category"] = cat
        return rep