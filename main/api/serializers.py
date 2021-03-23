from rest_framework import serializers
from django.db.models import fields
from main.models import Join


class JoinCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Join
        fields = (
            'first_name',
            'last_name',
            'email',
        )

class JoinSerializer(serializers.ModelSerializer):
    class Meta:
        model = Join
        fields = [
            'first_name',
            'last_name',
            'email',
        ]