# coding=utf-8
from django.conf import settings
from django.views.generic.base import View
from restful.decorators import restful_view_templates
from django.core.mail import send_mail
from django import forms


@restful_view_templates('contact')
class ContactView(View):
    def post(self, request):
        form = Form(data=request.params)

        status = 200
        if form.is_valid():
            try:
                # send email
                send_mail(
                    'Контакт от сайта на obshtestvo.bg',
                    u'Тип контакт: ' + form.cleaned_data['type'] + "\n" +
                    u'Организация: ' + form.cleaned_data['name'] + "\n" +
                    u'Проект: ' + form.cleaned_data['project'] + "\n" +
                    u'Email: ' + form.cleaned_data['email'] + "\n" +
                    u'Предложена помощ: ' + form.cleaned_data['help'] + "\n",
                    'noreply@obshtestvo.bg',
                    ['antitoxic@gmail.com'],
                    fail_silently=False
                )
                message = 'Благодарим Ви. Ще се свържем с Вас възможно най-скоро.'
            except:
                status = 400
                message = 'Изникна грешка при получаването на вашата информацията. Моля, опитайте по-късно'
        else:
            status = 400
            message = 'Данните които попълнихте не са валидни'

        return {'status': message}, status


class Form(forms.Form):
    name = forms.CharField(required=True)
    type = forms.CharField(required=True)
    help = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    project = forms.CharField(required=True)