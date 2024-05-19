from rest_framework.views import APIView
from rest_framework.response import Response


class HelloAPIView(APIView):
    """Test API view."""

    def get(self, request, format=None):
        """Return a list of APIView features"""
        an_apiview = [
            "is similar to traditional django view",
            "Uses HTTP method as functions(get,post.patch.put,delete)",
            "Gives you the most control over your logic",
            "Is mapped manually to URLs",
        ]

        return Response({
            " message": "Hello world!",
            'an_apiview': an_apiview
        })
