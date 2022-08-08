import azure.cognitiveservices.speech as speechsdk
import time

def main():
    f = open('api.txt')
    data =f.read()
    f.close()
    text = transcription(data)

    return text

def transcription(speech_key):
    service_region, language = "japanwest", "ja-JP"
    speech_config = speechsdk.SpeechConfig(subscription=speech_key, region=service_region,speech_recognition_language=language)

    speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config)
    result = speech_recognizer.recognize_once()

    if result.reason == speechsdk.ResultReason.RecognizedSpeech:
        #print("Recognized: {}".format(result.text))
        return result.text
    elif result.reason == speechsdk.ResultReason.NoMatch:
        #print(-1)
        return -1
    elif result.reason == speechsdk.ResultReason.Canceled:
        cancellation_details = result.cancellation_details
        return -1