from .models import Post
from rest_framework import serializers

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        # fields = '__all__' 다 입력받겠다
        fields = ['title','body']