from django.apps import AppConfig


class UserauthsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "userauths"
    verbose_name = "User Authentication"

    def ready(self):
        import userauths.signals
