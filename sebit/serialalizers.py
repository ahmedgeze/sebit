
from rest_framework import serializers

class UserSendSerializer(serializers.Serializer):
    personName = serializers.CharField(required=True)
    cityName = serializers.CharField(required=True)
    countryName = serializers.CharField(required=True)


    default_error_messages = {
        'inactive_account': _('User account is disabled.'),
        'invalid_credentials': _('Unable to login with provided credentials.')
    }

    def __init__(self, *args, **kwargs):
        super(UserSendSerializer, self).__init__(*args, **kwargs)
        self.user = None

    
