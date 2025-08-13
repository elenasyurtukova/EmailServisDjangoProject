from django.utils import timezone
from django.utils.timezone import localtime
from django.core.mail import send_mail
from .models import Mailing, Attempt
from config.settings import EMAIL_HOST_USER


def send_message(pk, request=None):
    """Отправка рассылки по требованию"""
    mailing = Mailing.objects.get(pk=pk)
    now = timezone.now()

    # if request and mailing.owner != request.user:
    #     Attempt.objects.create(
    #         mailing=mailing,
    #         status_attempt=Attempt.unsuccess,
    #         server_answer=f'Рассылку пытался отправить посторонний человек: {request.user.email}',
    #         created_at=now,
    #     )
    #     return False

    subject = mailing.message.subject
    message=mailing.message.body
    client_list = [client.email for client in mailing.clients.all()]

    if mailing.status_mailing == 'end':
        Attempt.objects.create(
            mailing=mailing,
            status_attempt=Attempt.unsuccess,
            server_answer='Рассылка уже завершена',
            created_at=now,
        )
        return False

    if not client_list:
        Attempt.objects.create(
            mailing=mailing,
            status_attempt=Attempt.unsuccess,
            server_answer='Нет получателей рассылки',
            created_at=now,
        )
        return False

    try:
        send_mail(
            subject=subject,
            message=message,
            from_email=EMAIL_HOST_USER,
            client_list=client_list,
            fail_silently=False,
        )

        Attempt.objects.create(
            mailing=mailing,
            status_attempt=Attempt.success,
            server_answer='Рассылка отправлена',
            created_at=now,
        )
        if mailing.status_mailing == Mailing.start:
            mailing.status_mailing = Mailing.run
            mailing.save()

        return True

    except Exception as ex:
        Attempt.objects.create(
            mailing=mailing,
            status_attempt=Attempt.unsuccess,
            server_answer=str(ex),
            created_at=now,
        )
        return False