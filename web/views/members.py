# coding=utf-8
from django.conf import settings
from django.views.generic.base import View
from restful.decorators import restful_view_templates
from django.core.mail import send_mail
from django import forms


@restful_view_templates
class MembersView(View):
    def post(self, request):
        form = Form(data=request.params)

        status = 200
        if form.is_valid():
            try:
                # send email
                send_mail(
                    'Включи се нов участник',
                    u'Проект: ' + form.cleaned_data['project'] + "\n" +
                    u'Email: ' + form.cleaned_data['email'] + "\n" +
                    u'Умения: ' + ", ".join(form.cleaned_data['position']) + "\n",
                    'noreply@obshtestvo.bg',
                    ['antitoxic@gmail.com'],
                    fail_silently=False
                )
                message = 'Ура! Веднага можете да се включите във Facebook или Github.'
            except:
                status = 400
                message = 'Изникна грешка при получаването на вашата информацията. Моля, опитайте по-късно'
        else:
            status = 400
            message = 'Данните които попълнихте не са валидни'

        return {'status': message}, status


class Form(forms.Form):
    position = forms.MultipleChoiceField(required=True,
                                         choices=settings.MEMBER_POSITIONS.items())
    email = forms.EmailField(required=True)
    project = forms.CharField(required=True)