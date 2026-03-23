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
    members = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = Team
        fields = ['id', 'name', 'members']


class UserSerializer(serializers.ModelSerializer):
    id = ObjectIdStringField(read_only=True)
    team = TeamSerializer(read_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'team']


class ActivitySerializer(serializers.ModelSerializer):
    id = ObjectIdStringField(read_only=True)
    user = UserSerializer(read_only=True)
    activity_type = serializers.CharField(source='type')
    date = serializers.DateTimeField(source='created_at', read_only=True)

    class Meta:
        model = Activity
        fields = ['id', 'user', 'activity_type', 'duration', 'distance', 'date']


class WorkoutSerializer(serializers.ModelSerializer):
    id = ObjectIdStringField(read_only=True)

    class Meta:
        model = Workout
        fields = '__all__'


class LeaderboardSerializer(serializers.ModelSerializer):
    id = ObjectIdStringField(read_only=True)
    user = UserSerializer(read_only=True)
    user_id = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(),
        source='user',
        write_only=True
    )
    class Meta:
        model = Leaderboard
        fields = '__all__'
