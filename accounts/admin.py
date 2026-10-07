from django.contrib import admin
from django.contrib.auth.models import User
from django.template.response import TemplateResponse
from django.db.models import Sum
from .models import MostPurchasedUsers

class UserMoviePurchaseAdmin(admin.ModelAdmin):
    pass

class MostPurchasedUsersAdmin(admin.ModelAdmin):
    change_list_template = "admin/most_purchased_users.html"

    def has_delete_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def changelist_view(self, request, extra_context=None):
        top_user = User.objects.annotate(movies_count = Sum('order__item__quantity')
                                         ).filter(movies_count__isnull=False).order_by('-movies_count').first()

        order = []
        if top_user:
            orders = top_user.order_set.all()

        extra_context = extra_context or {}
        extra_context['top_user'] = top_user
        extra_context['orders'] = orders
        extra_context['opts'] = self.model._meta
        extra_context['app_label'] = 'accounts'

        return TemplateResponse(request, self.change_list_template, extra_context)

admin.site.unregister(User)
admin.site.register(User,UserMoviePurchaseAdmin)
admin.site.register(MostPurchasedUsers, MostPurchasedUsersAdmin)
