from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from .models import LeagueUser

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims based on LeagueUser fields
        token['username'] = user.username
        token['isAdmin'] = user.is_staff  # Adjust this field if `isAdmin` differs in LeagueUser

        return token

    def validate(self, attrs):
        data = super().validate(attrs)

        # Include additional fields in the response
        user = self.user  # The authenticated user
        data['username'] = user.username
        data['isAdmin'] = user.is_staff  # Adjust this based on your model
        return data


class LeagueUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = LeagueUser
        fields = '__all__'
