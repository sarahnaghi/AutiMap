from django.contrib import admin
from .models import DigitalGame,Toy

from .models import DigitalGame,Toy

# Register your models here.


class DigitalGameAdmin(admin.ModelAdmin):

    list_display = ("game_name", "game_description", "game_url_appstore", "game_play_store")
    list_filter = ("game_name",)


class ToyAdmin(admin.ModelAdmin):

    list_display = ("game_name", "game_description", "game_url",)
    list_filter = ("game_name",)



admin.site.register(DigitalGame,DigitalGameAdmin)
admin.site.register(Toy,ToyAdmin)
