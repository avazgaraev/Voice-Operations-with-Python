import os
import azure.cognitiveservices.speech as speechsdk


def recognize_from_microphone():
    
    #               Speech to text

    # This example requires environment variables named "SPEECH_KEY" and "SPEECH_REGION"
    speech_config = speechsdk.SpeechConfig(subscription = 'SubsKey', region='eastus', speech_recognition_language='az-AZ')
    # speech_config.speech_recognition_language="az-AZ"

    #audio_config = speechsdk.audio.AudioConfig(filename="Record.wav")
    audio_config = speechsdk.audio.AudioConfig(use_default_microphone=True)
    speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config, audio_config=audio_config)

    print("Speak into your microphone.")
    # print("Recognizing speech.")
    speech_recognition_result = speech_recognizer.recognize_once_async().get()

    if speech_recognition_result.reason == speechsdk.ResultReason.RecognizedSpeech:
        print("Recognized: {}".format(speech_recognition_result.text))
    elif speech_recognition_result.reason == speechsdk.ResultReason.NoMatch:
        print("No speech could be recognized: {}".format(speech_recognition_result.no_match_details))
    elif speech_recognition_result.reason == speechsdk.ResultReason.Canceled:
        cancellation_details = speech_recognition_result.cancellation_details
        print("Speech Recognition canceled: {}".format(cancellation_details.reason))
        if cancellation_details.reason == speechsdk.CancellationReason.Error:
            print("Error details: {}".format(cancellation_details.error_details))
            print("Did you set the speech resource key and region values?")

    file = open("speechRecognition1.txt", "w", encoding='utf-8')
    file.write("Recognized speech: {}".format(speech_recognition_result.text))
    file.close()

    #                   Text to speech
    
    audio_config = speechsdk.audio.AudioOutputConfig(filename="./recordSpeech1.wav")

    # The language of the voice that speaks.
    speech_config.speech_synthesis_voice_name='az-AZ-BabekNeural'

    speech_synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config, audio_config=audio_config)

    # Get text from the console and synthesize to the default speaker.
    print("Enter some text that you want to speak >")
    #text = input()

    speech_synthesis_result = speech_synthesizer.speak_text_async("{}".format(speech_recognition_result.text)).get()
    #speech_synthesis_result = speech_synthesizer.speak_text_async("Zəhmət olmasa VÖEN kodunuzu qeyd edin.").get()

    if speech_synthesis_result.reason == speechsdk.ResultReason.SynthesizingAudioCompleted:
        print("Speech synthesized for text [{}]".format(speech_recognition_result.text))
    elif speech_synthesis_result.reason == speechsdk.ResultReason.Canceled:
        cancellation_details = speech_synthesis_result.cancellation_details
        print("Speech synthesis canceled: {}".format(cancellation_details.reason))
        if cancellation_details.reason == speechsdk.CancellationReason.Error:
            if cancellation_details.error_details:
                print("Error details: {}".format(cancellation_details.error_details))
                print("Did you set the speech resource key and region values?")

recognize_from_microphone()