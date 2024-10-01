import requests
from .urls import TRANSLATION_URL

def get_translations(text: str, source='ita', target='eng'):
    response = requests.post(TRANSLATION_URL, headers={
        'Content-Type': 'application/json',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:131.0) Gecko/20100101 Firefox/131.0'
    }, json={
        'from': source,
        'to': target,
        'format': 'text',
        'input': text,
        'options': {
            'contextResults': True,
            'languageDetection': True,
            'origin': 'reversomobile',
            'sentenceSplitter': False,
        },
    })

    if response.status_code != 200:
        raise Exception(f"Request failed with status code {response.status_code}: {response.text}")

    try:
        page = response.json()
        isContext = page.get('languageDetection', {}).get('originalDirectionContextMatches') > 0

        if not isContext:
            translations = page.get('translation')
            return translations

        context_results = page.get('contextResults', {}).get('results', [])
        translations = [c.get('translation') for c in context_results]
        return translations
    except requests.exceptions.JSONDecodeError:
        raise Exception(f"Failed to parse JSON response: {response.text}")