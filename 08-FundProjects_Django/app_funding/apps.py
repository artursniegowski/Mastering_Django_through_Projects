from django.apps import AppConfig


class AppFundingConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'app_funding'
    
    def ready(self):
        import app_funding.signals 
