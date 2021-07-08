from django.apps import AppConfig


class AppsiteConfig(AppConfig):
    name = 'appsite'

    def ready(self):
        import appsite.signals