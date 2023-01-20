from django.apps import AppConfig


class GradeConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Grade'


class UsersConfig(AppConfig):
    name = 'Grade2'

    def ready(self):
        import Grade2.signals