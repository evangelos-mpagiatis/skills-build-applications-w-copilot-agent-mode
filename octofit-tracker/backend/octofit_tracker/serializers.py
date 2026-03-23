from rest_framework import serializers
from .models import Team, User, Activity, Workout, Leaderboard


class ObjectIdStringField(serializers.Field):
    """
    Serializer field that ensures MongoDB ObjectId (or any value) is rendered as a string.
    """
    def to_representation(self, value):
        return str(value) if value is not None else None

    def to_internal_value(self, data):
        # Let the model / database layer handle converting this back if needed.
        return data


class TeamSerializer(serializers.ModelSerializer):
    id = ObjectIdStringField(read_only=True)

    class Meta:
        model = Team
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    id = ObjectIdStringField(read_only=True)
    team = TeamSerializer(read_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'team']


class ActivitySerializer(serializers.ModelSerializer):
    id = ObjectIdStringField(read_only=True)
    user = UserSerializer(read_only=True)
    user_id = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(), source='user', write_only=True
    )

    class Meta:
        model = Activity
        fields = ['id', 'user', 'user_id', 'type', 'duration', 'distance', 'created_at']


class WorkoutSerializer(serializers.ModelSerializer):
    id = ObjectIdStringField(read_only=True)

    class Meta:
        model = Workout
        fields = '__all__'


class LeaderboardSerializer(serializers.ModelSerializer):
    id = ObjectIdStringField(read_only=True)
    user = UserSerializer(read_only=True)
    user_id = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(), source='user', write_only=True
    )

    class Meta:
        model = Leaderboard
        fields = ['id', 'user', 'user_id', 'points']
