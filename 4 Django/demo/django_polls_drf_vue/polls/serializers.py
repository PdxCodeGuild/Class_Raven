from rest_framework import serializers

from .models import Question, Choice
from users.serializers import UserDetailSerializer

class ChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Choice
        fields = '__all__'


class QuestionDetailSerializer(serializers.ModelSerializer):

    # customize the user serializer field
    user = UserDetailSerializer()

    # add the reverse ForeignKey relationship to a question's choices
    choices = ChoiceSerializer(many=True)

    class Meta:
        model = Question
        fields = ['question_text', 'status', 'user', 'pub_date', 'choices']