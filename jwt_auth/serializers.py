from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
from django.core.exceptions import ValidationError
from django.apps import apps 
from resources.serializers import ResourceSerializer
from tasks.serializers import TaskSerializer
from contacts.serializers import ContactSerializer
# import django.contrib.auth.password_validation as validations

User = get_user_model()
Job = apps.get_model('jobs', 'Job')

class JobSerializer(serializers.ModelSerializer):

    class Meta:
        model = Job
        fields = ('id', 'job_title', 'company')


class UserSerializer(serializers.ModelSerializer):

    password = serializers.CharField(write_only=True)
    password_confirmation = serializers.CharField(write_only=True)

    def validate(self, data):
        password = data.pop('password')
        password_confirmation = data.pop('password_confirmation')
        if password != password_confirmation:
            raise ValidationError({'password_confirmation': 'does not match'})
        # try:
        #     validations.validate_password(password=password)
        # except ValidationError as err:
        #     raise ValidationError({'password': err.messages})
        data['password'] = make_password(password)
        return data


    class Meta:
        model = User
        fields = '__all__'
        

class PopulatedUserSerializer(UserSerializer):
    created_resources = ResourceSerializer(many=True)
    created_tasks = TaskSerializer(many=True)
    created_contacts = ContactSerializer(many=True)
    created_jobs = JobSerializer(many=True)
