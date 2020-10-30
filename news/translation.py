from modeltranslation.translator import register, TranslationOptions
from .models import PostCategoryModel, PostTagModel, PostModel


@register(PostCategoryModel)
class PostCategoryTranslationOptions(TranslationOptions):
    fields = ('title',)


@register(PostTagModel)
class PostTagTranslationOptions(TranslationOptions):
    fields = ('title',)


@register(PostModel)
class PostTranslationOptions(TranslationOptions):
    fields = ('title', 'content')
