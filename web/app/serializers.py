import random
import string

from .models import ShortenedURL
from rest_framework import serializers


class ShortenedURLSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShortenedURL
        fields = ['id', 'original_url', 'short_code']
        read_only_fields = ['id', 'short_code']
    
    def create(self, validated_data):
        validated_data['short_code'] = self.generate_short_code()
        return super().create(validated_data)
    
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['shortened_url'] = f"http://localhost:8000/{instance.short_code}"
        return representation

    def generate_short_code(self):
        length = 6
        characters = string.ascii_letters + string.digits
        short_code = ''.join(random.choice(characters) for _ in range(length))
        return short_code
