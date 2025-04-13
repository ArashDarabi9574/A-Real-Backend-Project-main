from django.contrib.auth import get_user_model
from rest_framework import serializers


class UserListSerializer(serializers.ModelSerializer):
    permissions = serializers.SerializerMethodField()

    class Meta:
        model = get_user_model()
        fields = (
            'id', 'phone_number', 'email', 'full_name', 'verify_date',
            'permissions', 'is_active', 'is_verify', 'is_staff'
        )
        depth = 1
        
    def get_permissions(self, instance):
        permissions = instance.permissions
        # Assuming permissions is a dictionary
        try:
            permissions = [key for key, value in vars(permissions).items() if value]
        except:
            permissions = None
        return permissions
