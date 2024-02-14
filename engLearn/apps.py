from django.apps import AppConfig


class EnglearnConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'engLearn'

    def ready(self):
        # Добавьте импорт вашей команды здесь
        pass
