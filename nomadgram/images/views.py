from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . import models, serializers


class Feed(APIView):

    def get(self, request, format=None):

        user = request.user

        print(user)

        following_users = user.following.all()

        print(following_users)

        return Response(status=200)


class LikeImage(APIView):

    def post(self, request, image_id, format=None):
        
        user = request.user

        try:
            image = models.Image.objects.get(id=image_id)
        except models.Image.DoesNotExist:
            return Response(status=404)

        new_like = models.Like.objects.create(
                creator=user,
                image=found_image
            )
        new_like.save()

        return Response(status=200)


class ListAllImages(APIView):

    def get(self, request, format=None):

        all_images = models.Image.objects.all()

        serializer = serializers.ImageSerializer(all_images, many=True)

        return Response(data=serializer.data)        