from django.apps import AppConfig


class SiteOperationConfig(AppConfig):
    name = 'site_operation'

    def ready(self):
        import site_operation.signals
