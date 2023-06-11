# management/commandspopulate_db.py
from django.core.management.base import BaseCommand
from rules_app.models import Rule, Example

class Command(BaseCommand):
    help = 'Populates the database with mocked data'

    def handle(self, *args, **options):
        mock_data = [
            {
                "id": 1,
                "topic": "Noun Case Endings",
                "rule": "In Arabic, nouns can have different case endings...",
                "highlightColor": "#FF0000",
                "sound": "https://cdn.obsess-vr.com/RT3DTest/VFX/Audio/WalkSound.mp4",
                "examples": [
                    {
                        "sentence": "This is a test sentence.",
                        "highlightedIndices": [0, 1, 2],
                    },
                    {
                        "sentence": "This is another test sentence.",
                        "highlightedIndices": [5, 6, 7],
                    }
                ]
            },
            {
                "id": 2,
                "topic": "Verb Conjugation",
                "rule": "Arabic verbs change based on the subject...",
                "highlightColor": "#00FF00",
                "sound": "https://cdn.obsess-vr.com/RT3DTest/VFX/Audio/WalkSound.mp4",
                "examples": [
                    {
                        "sentence": "This is a test sentence for verb conjugation.",
                        "highlightedIndices": [0, 1, 2],
                    },
                    {
                        "sentence": "This is another test sentence for verb conjugation.",
                        "highlightedIndices": [5, 6, 7],
                    }
                ]
            },
            {
                "id": 3,
                "topic": "Adjective Agreement",
                "rule": "Adjectives in Arabic agree with the noun they modify...",
                "highlightColor": "#0000FF",
                "sound": "https://cdn.obsess-vr.com/RT3DTest/VFX/Audio/WalkSound.mp4",
                "examples": [
                    {
                        "sentence": "This is a test sentence for adjective agreement.",
                        "highlightedIndices": [0, 1, 2],
                    },
                    {
                        "sentence": "This is another test sentence for adjective agreement.",
                        "highlightedIndices": [5, 6, 7],
                    }
                ]
            }
        ]

        for rule in mock_data:
            new_rule = Rule.objects.create(
                topic=rule["topic"],
                rule=rule["rule"],
                highlightColor=rule["highlightColor"],
                sound=rule["sound"]
            )
            for example in rule["examples"]:
                Example.objects.create(
                    rule=new_rule,
                    sentence=example["sentence"],
                    highlightedIndices=','.join(str(i) for i in example["highlightedIndices"])
                )
        self.stdout.write(self.style.SUCCESS('Successfully populated database'))
