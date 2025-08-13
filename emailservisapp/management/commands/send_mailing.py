from django.core.management import BaseCommand
from django.utils import timezone
from emailservisapp.models import Mailing
from emailservisapp.services import send_message


class Command(BaseCommand):
    help = 'Send current mailings'

    def handle(self, *args, **options):
        now = timezone.now()
        try:
            mailings = Mailing.objects.filter(
                start_sending__lte=now,
                end_sending__gte=now,
                status__in=[Mailing.start, Mailing.run]
            )
            for mailing in mailings:
                send_message(mailing.pk)

                if mailing.status_mailing == Mailing.start:
                    mailing.status_mailing = Mailing.run
                    mailing.save()
            return 'Рассылки отправлены.'
        except Exception as ex:
            return str(ex)