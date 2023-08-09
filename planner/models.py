from django.db import models
from django.utils.translation import gettext_lazy as _
from .managers import ScheduledPaymentManager, CurrencyManager


class ScheduledPayment(models.Model):
    user = models.ForeignKey("user.NewUser", models.CASCADE, null=True, blank=True)
    name = models.CharField(_("payment name"), max_length=64)
    due_date = models.DateField(_("due date"))
    periodicity = models.DurationField(_("periodicity"), blank=True, null=True)
    completed = models.BooleanField(default=False)
    amount = models.FloatField(_("amount"))
    currency = models.ForeignKey("planner.Currency", models.SET_NULL, null=True, blank=True)
    created = models.DateField(auto_now_add=True)
    modified = models.DateField(auto_now=True)
    # TODO : category can be changed to a foreign key to a category model
    category = models.CharField(_("category"),blank=True, max_length=64)

    objects = ScheduledPaymentManager()


    def __str__(self):
        return self.name

class Currency(models.Model):
    name = models.CharField(_("currency name"), max_length=64, unique=True)
    code = models.CharField(_("currency code"), max_length=3, unique=True)

    objects = CurrencyManager()

    def __str__(self):
        return self.name