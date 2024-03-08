from rest_framework import serializers
from .models import Recipe, Comment, Like

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = "__all__"

class RecipeSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only = True)
    class Meta:
        model = Recipe
        fields = ['id', 'title', 'ingredients', 'instructions', 'comments']
