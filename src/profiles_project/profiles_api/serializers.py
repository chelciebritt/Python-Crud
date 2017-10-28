from rest_framework import serializers


class HelloSerializer(serializers.Serializer):
    """name field for testing apiview."""

    name = serializers.CharField(max_length=10)
