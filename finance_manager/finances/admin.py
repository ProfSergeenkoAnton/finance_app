from django.contrib import admin
from .models import Income, Expense, Budget, Goal

admin.site.register(Income)
admin.site.register(Expense)
admin.site.register(Budget)
admin.site.register(Goal)

