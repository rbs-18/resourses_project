from django import forms
from django.core.exceptions import ValidationError

from .models import Resourse


class ResourseForm(forms.ModelForm):
    class Meta:
        model = Resourse
        fields = ('ip_address', 'port', 'resourse_type')

    def clean_ip_address(self):
        ip_address = self.cleaned_data['ip_address']
        groups = ip_address.split('.')
        if len(groups) != 4:
            raise ValidationError(f'Wrong ip address! {ip_address}')
        for group in groups:
            if (int(group) > 255) or (int(group) < 0):
                raise ValidationError(f'Wrong ip address! {ip_address}')
        return ip_address

    def clean_port(self):
        port = self.cleaned_data['port']
        if port < 1 or port > 65535:
            raise ValidationError(f'Wrong port! {port}')
        return port
