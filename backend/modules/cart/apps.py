from django.apps import AppConfig


class CartConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "modules.cart"

    def ready(self):
        import modules.cart.signals
