from .models import *
from .serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view

# Create your views here.

class ImageView(APIView):
    def get(self, req):
        images = Images.objects.all()
        serializers = ImageSerializer(images, many=True)
        return Response(serializers.data)


@api_view(['GET','POST'])
def ContactView(req):
    if req.method == 'POST':
        data = req.data
        serializer = ContactSerializer(data=data)  
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors)