import requests
import json

def emo_detection():
    text_to_analyze = "I am so happy I am doing this."
    URL = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    Headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    to_analyze = { "raw_document": { "text": text_to_analyze } }
    req = requests.post(URL, json = to_analyze, headers=Headers)
    fmt_resp = json.loads(req.text)
    anger_score = fmt_resp['emotionPredictions'][0]["emotion"]["anger"]
    disgust_score= fmt_resp['emotionPredictions'][0]["emotion"]["disgust"]
    fear_score= fmt_resp['emotionPredictions'][0]["emotion"]["fear"]
    joy_score= fmt_resp['emotionPredictions'][0]["emotion"]["joy"]
    sadness_score= fmt_resp['emotionPredictions'][0]["emotion"]["sadness"]
    emo_dict = fmt_resp['emotionPredictions'][0]["emotion"]
    dominant_emo = max(emo_dict, key = emo_dict.get)
    return {
            'anger': anger_score,
            'disgust': disgust_score,
            'fear': fear_score,
            'joy': joy_score,
            'sadness': sadness_score,
            'dominant_emotion': dominant_emo
            }