from rest_framework import serializers
from .models import Rule, Example

class ExampleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Example
        fields = ['id', 'sentence', 'highlightedIndices']

class RuleSerializer(serializers.ModelSerializer):
    examples = ExampleSerializer(many=True, read_only=True)

    class Meta:
        model = Rule
        fields = ['id', 'topic', 'rule', 'highlightColor', 'sound', 'examples']
