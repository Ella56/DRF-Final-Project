from rest_framework import serializers
from portfolio.models import Portfolio, Category
from root.models import Team, Client

class PortfolioSerializer(serializers.ModelSerializer):
    category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all())
    team = serializers.PrimaryKeyRelatedField(queryset=Team.objects.all())
    client = serializers.PrimaryKeyRelatedField(queryset=Client.objects.all())

    class Meta:
        model = Portfolio
        fields = "__all__"

    def to_representation(self, instance):
        rep = super().to_representation(instance)

        rep["category"] = instance.category.name if instance.category else None
        
        rep["team"] = instance.team.name if instance.team else None
        
        rep["client"] = instance.client.name if instance.client else None

        return rep
