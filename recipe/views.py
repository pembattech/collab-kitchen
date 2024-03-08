from rest_framework import generics
from .models import Recipe, Comment
from .serializers import RecipeSerializer, CommentSerializer


# Create your views here.
class RecipeListAPIView(generics.ListAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer


class RecipeCreateAPIView(generics.CreateAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer


class RecipeRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
    lookup_field = "pk"

    def get_serializer_context(self):
        """
        Add comments to the serializer context.
        """
        context = super().get_serializer_context()
        context["comments"] = self.get_object().comments.all()
        return context


class CommentListAPIView(generics.ListAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class CommentCreateAPIView(generics.CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
