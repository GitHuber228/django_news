from modeltranslation.translator import register, TranslationOptions
from .models import SiteMainSettingsModel


@register(SiteMainSettingsModel)
class SiteContactsTranslationOptions(TranslationOptions):
    fields = ('description',)
