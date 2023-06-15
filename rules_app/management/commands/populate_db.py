import csv
import os
from django.core.management.base import BaseCommand
from rules_app.models import Rule, Example
from django.conf import settings
import random

def get_random_color():
    return "#{:06x}".format(random.randint(0, 0xFFFFFF))

class Command(BaseCommand):
    help = 'Populates the database with mocked data'

    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str, nargs='?', default="default")

    def handle(self, *args, **options):
        csv_dir = os.path.join(settings.BASE_DIR, "rules_app/management/commands/csv_files")
        files = [options['csv_file']] if options['csv_file'] != "default" else os.listdir(csv_dir)

        for file in files:
            self.populate(os.path.join(csv_dir, file))

        self.stdout.write(self.style.SUCCESS('Successfully populated database'))

    def populate(self, csv_file):
        with open(csv_file, newline='', encoding='utf-8') as f:
            reader = csv.reader(f)
            data = list(reader)

        # Get the rule from the first line
        rule_topic = data[0][0]
        new_rule = Rule.objects.create(
            topic=rule_topic,
            rule=f"In Arabic, {rule_topic}...",
            highlightColor = get_random_color(),
            sound="https://cdn.obsess-vr.com/RT3DTest/VFX/Audio/WalkSound.mp4"
        )

        # The rest of the lines are examples for the rule
        for row in data[1:]:
            sentence = row[0]
            highlighted_indices = sorted(random.sample(range(len(sentence)), k=len(sentence)//10))
            Example.objects.create(
                rule=new_rule,
                sentence=sentence,
                highlightedIndices=','.join(str(i) for i in highlighted_indices)
            )
