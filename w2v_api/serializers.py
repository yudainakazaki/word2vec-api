from rest_framework import serializers
from .models import W2V

class W2VSerializer(serializers.ModelSerializer):
    class Meta:
        model = W2V
        fields = ['id', 'word1', 'word2', 'result']
