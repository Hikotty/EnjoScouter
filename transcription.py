import azure.cognitiveservices.speech as speechsdk
import time

def transcription(speech_key):
    service_region, language = "japanwest", "ja-JP"
    speech_config = speechsdk.SpeechConfig(subscription=speech_key, region=service_region,speech_recognition_language=language)

    speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config)
    
    print("Say something...")
    
    def recognized(evt):
        print('「{}」'.format(evt.result.text))
        # do something
    
    def start(evt):
        print('SESSION STARTED: {}'.format(evt))
    
    def stop(evt):
        print('SESSION STOPPED {}'.format(evt))
    
    speech_recognizer.recognized.connect(recognized)
    speech_recognizer.session_started.connect(start)
    speech_recognizer.session_stopped.connect(stop)
    
    try:
        speech_recognizer.start_continuous_recognition()
        time.sleep(20)
    except KeyboardInterrupt:
        print("bye.")
        speech_recognizer.recognized.disconnect_all()
        speech_recognizer.session_started.disconnect_all()
        speech_recognizer.session_stopped.disconnect_all()
