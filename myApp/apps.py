from django.apps import AppConfig


class MyappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'myApp'
    
    def ready(self):
        import myApp.signals.sync_Q1
        import myApp.signals.thread_Q2
        import myApp.signals.transaction_Q3
        import myApp.signals.rectangle
