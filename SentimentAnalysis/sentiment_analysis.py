import requests
import json

def sentiment_analyzer(text_to_analyse):
    url = 'https://sn-watson-sentiment-bert.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/SentimentPredict'
    myobj = { "raw_document": { "text": text_to_analyse } }
    headers = {
        "Content-Type": "application/json","grpc-metadata-mm-model-id": "sentiment_aggregated-bert-workflow_lang_multi_stock"}
    try:
        response = requests.post(url, json=myobj, headers=headers)
        response.raise_for_status()  # Raise an exception for HTTP errors
        
        formatted_response = response.json()
        if response.status_code == 200:
            label = formatted_response['documentSentiment']['label']
            score = formatted_response['documentSentiment']['score']
        elif response.status_code == 500:
            label = None
            score = None
        return {'label': label, 'score': score}
    
    except requests.exceptions.RequestException as e:
        return {'error': str(e)}
    except json.JSONDecodeError:
        return {'error': 'Error decoding the JSON response'}
    except KeyError:
        return {'error': 'Unexpected response structure'}


