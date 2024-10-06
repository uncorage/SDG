import google.generativeai as genai
from google.generativeai.types import RequestOptions
from google.api_core import retry


class SDGQuestGenerator:
    GENERATION_CONTEXT = \
        "I will give you a random SDG goal name and location where it is gonna happen.\n" \
        "Then you generate an SDG quest/event/test/task for that SDG goal in this format below:\n" \
        "Task title: {task_title}\n" \
        "Task description: {task_description}\n" \
        "Location: {task_location}\n" \
        "Benefits/Result: {task_result}\n" \
        "\n" \
        "There is no need to format your response because we only need raw text.\n" \

    def __init__(self, api_key: str):
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel("gemini-1.5-pro-latest")
        self.chat = self.model.start_chat(history=[
            {
                "role": "user",
                "parts": SDGQuestGenerator.GENERATION_CONTEXT
            }
        ])

    def _create_request_text(self, sdg_name: str, location: str):
        return f"SDG Goal: {sdg_name}\nLocation: {location}"

    def generate_sdg_quest(self, sdg_name: str, location: str):
        '''Generates an SDG Quest

        Generates SDG Quest based on SDG goal and location passed

        Args:
            sdg_name (str): One of SDG Goal names (17 goals exist)
            location (str): Location where the generated SDG quest gonna happen

        Returns:
            (str): Text based human readable response
        '''

        response = self.chat.send_message(
            self._create_request_text(sdg_name, location),
            request_options=RequestOptions(
                retry=retry.Retry(initial=1, multiplier=2,
                                  maximum=60, timeout=120)
            )
        )

        return response.text
