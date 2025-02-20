from django.contrib import admin
from .models import Membership, Client


class MembershipAdmin(admin.ModelAdmin):

    # fields = (
    #     ('name', 'membership_plan'),
    #     'membership_active', 'unique_code'
    # )
    # randomely change the list of fields
    # exclude = ('unique_code',)
    list_display = ['id', 'name',
                    'membership_plan',
                    'membership_active']
    # list_filter = ['membership_plan']
    # search_fields = ['name']
    # # list_display_links = ['name', 'membership_plan']
    # list_editable = ['name', 'membership_plan']
    exclude = ('', )
    actions = ('set_membership_to_active',)
    prepopulated_fields = {
        'unique_code': ('membership_plan',)
    }

    def set_membership_to_active(self, request, queryset):

        queryset.update(membership_active=True)
        self.message_user(request, 'membership(s) activated')

    set_membership_to_active \
        .short_description = 'Mark selected memberships as active'


admin.site.register(Membership, MembershipAdmin)
admin.site.register(Client)
