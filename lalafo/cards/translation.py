from modeltranslation.translator import TranslationOptions, translator

from .models import Category


class CategoryTranslation(TranslationOptions):
    fields = ("name",)


translator.register(Category, CategoryTranslation)
