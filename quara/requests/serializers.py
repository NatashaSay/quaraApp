from rest_framework import serializers


class ControlSerializer(serializers.Serializer):
    # title = serializers.CharField(max_length=120)
    # description = serializers.CharField()
    # body = serializers.CharField()


    userprofile = serializers.CharField()
    date = serializers.DateTimeField()
    temperature = serializers.FloatField()
    cough = serializers.BooleanField()
    headache = serializers.BooleanField()
    comment = serializers.CharField()
