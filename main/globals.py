from django.conf import settings
from .ai import SDGQuestGenerator

_sdg_quest_generator = None


def get_sdg_quest_generator():
    global _sdg_quest_generator

    if _sdg_quest_generator is None:
        _sdg_quest_generator = SDGQuestGenerator(settings.GENAI_API_KEY)

    return _sdg_quest_generator
