from .models import TaskActive


def parse_generated_sdg_quest_text(text: str) -> dict[str, str]:
    lines = text.strip().split("\n")
    result = {}

    for line in lines:
        if line.startswith("Task title"):
            result["title"] = line.split(":")[1]
        elif line.startswith("Task description"):
            result["description"] = line.split(":")[1]
        elif line.startswith("Location"):
            result["location"] = line.split(":")[1]
        elif line.startswith("Benefits"):
            result["benefits_description"] = line.split(":")[1]

    return result