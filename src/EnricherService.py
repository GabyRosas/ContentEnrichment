from dotenv import load_dotenv
import requests
import os

load_dotenv()


class EnricherService:
    API_KEY = os.getenv('API_KEY')
    API_URL = os.getenv('API_URL')

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
                return response['data']['outputs'][0]['text']
            else:
                return None
        except requests.exceptions.RequestException as e:
            print(f"Ha occurrido un error: {e}")
            return None