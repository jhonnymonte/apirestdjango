from unittest.util import _MAX_LENGTH
from rest_framework import serializers

class HelloSerializers(serializers.Serializer):
    """serializa un campo para probar nuestro APIview"""
    name=serializers.CharField()