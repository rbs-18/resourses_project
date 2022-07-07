from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()

class Resourse(models.Model):

    WIN = 'WINDOWS'
    UNIX = 'UNIX'
    SQL = 'SQL'
    RESOURSE_TYPES = (
        (WIN, 'Windows'),
        (UNIX, 'Unix'),
        (SQL, 'Sql'),
    )

    ip_address = models.CharField('IP address', max_length=15)
    port = models.IntegerField('Port')
    resourse_type = models.CharField(
        'Resourse type',
        max_length=10,
        choices=RESOURSE_TYPES,
        default=WIN)
    host_user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='resourse'
    )
    change_datetime = models.DateTimeField(
        'Date and time of last changing', auto_now=True
    )
