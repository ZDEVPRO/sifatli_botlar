from django.contrib import admin
from home.models import HomeTitle, Customers, Faq, Projects, Contact

admin.site.index_title = 'АДМИНИСТРАЦИЯ САЙТА'
admin.site.site_header = 'Sifatli Botlar - Панель управления'
admin.site.site_title = 'Панель управления'


class ProjectsAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'image_tag']
    readonly_fields = ['image_tag']
    prepopulated_fields = {'slug': ('title',)}


class ContactAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'phone', 'ip']
    readonly_fields = ['first_name', 'last_name', 'phone', 'telegram', 'message', 'create_time', 'create_date', 'ip']


admin.site.register(Contact, ContactAdmin)
admin.site.register(Projects, ProjectsAdmin)
admin.site.register(Customers)
admin.site.register(HomeTitle)
admin.site.register(Faq)
