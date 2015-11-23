from django.core.management import BaseCommand
from list.models import List


class Command(BaseCommand):

    def handle(self, *args, **options):
        for lists in List.objects.all():
            lists.mark_inactive()
            self.stdout.write("list {} set to inactive".format(lists.id))
