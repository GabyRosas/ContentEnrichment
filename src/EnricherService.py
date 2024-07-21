from dotenv import load_dotenv
import requests
import os
import textwrap

load_dotenv()


class EnricherService:
    API_KEY = os.getenv('API_KEY')
    API_URL = os.getenv('API_URL')
    def wrap_text(text, width):
        wrapped_lines = textwrap.wrap(text, width)
        return "\n".join(wrapped_lines)
    @staticmethod
    def enrich(text):
        url = EnricherService.API_URL + "/texts/expansions"
        headers = {
            "charset": "utf-8",
            "Authorization": "Bearer " + EnricherService.API_KEY,
            "Content-Type": "application/json",
        }

        json = {
            "formality": "default",
            "max_tokens": 2048,
            "model": "claude-3-haiku",
            "n": 1,
            "temperature": 0,
            "text": text
        }

        try:
            response = requests.post(url, json=json, headers=headers)
            response = response.json()

            if response['status'] == 'success':
                enriched_text = response['data']['outputs'][0]['text']
                wrapped_enriched_text = EnricherService.wrap_text(enriched_text, 100)
                return wrapped_enriched_text.split('\n')
            else:
                return None
        except requests.exceptions.RequestException as e:
            print(f"Ha occurrido un error: {e}")
            return None
