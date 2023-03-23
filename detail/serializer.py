from rest_framework import serializers

from detail.models import Company


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields='__all__'

    def get_activityOrganizerName(self, instance):

        return "hahhahahah"