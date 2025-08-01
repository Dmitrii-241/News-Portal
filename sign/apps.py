from django.apps import AppConfig

class SignConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'  # если у вас Django >=3.2, можно добавить
    name = 'sign'

    def ready(self):
        # Импортируем signals, чтобы они были зарегистрированы
        import sign.signals
