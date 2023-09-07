import wave
from playsound import playsound
import azure.cognitiveservices.speech as speechsdk
import pypyodbc as odbc
import pandas as pd
#from credential import username, password

def textToSpeech(text):
    speech_config = speechsdk.SpeechConfig(subscription = 'SubscriptionKey', region='eastus', speech_recognition_language='az-AZ')
    #audio_config = speechsdk.audio.AudioOutputConfig(filename="recordSpeech.wav")
    audio_config = speechsdk.audio.AudioConfig(use_default_microphone=True)
    speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config, audio_config=audio_config)
    speech_recognition_result = speech_recognizer.recognize_once_async().get()
    # The language of the voice that speaks.
    speech_config.speech_synthesis_voice_name='az-AZ-BabekNeural'

    speech_synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config, audio_config=audio_config)

    # Get text from the console and synthesize to the default speaker.
    # print("Enter some text that you want to speak >")
    # text = "Salam " + row[1] + row[2] + ". Sizin borcunuz " + row[3] + " məbləğindədir. Təşəkkürlər!."

    speech_synthesis_result = speech_synthesizer.speak_text_async(text).get()
    #speech_synthesis_result = speech_synthesizer.speak_text_async("Zəhmət olmasa VÖEN kodunuzu qeyd edin.").get()




def gettingRequest():
    call = input()
    if(call == "195"):
        file = open("firstCommands.txt", "r", encoding="utf-8")
        print(file.read())
        playsound('recordSpeech.wav')
        #print(firstVoice)
        probDef = input()
        if(probDef=="1"):
            playsound('recordSpeech1.wav')
            voen = input("VÖEN kodunuz: ")
            #print("sql is {voen}")
            connection_string ='Driver={DriverName};Server={serverName};Database={dbName};Uid={uid};Pwd={Password};Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;'
            conn = odbc.connect(connection_string)
            sql = """
            select * from CCenter where VOIN=?
            """
            cursor = conn.cursor()
            cursor.execute(sql, (voen,))
            dataset = cursor.fetchall()
            for row in dataset:
                firstName = row[1]  # Assuming username is the first column
                lastName = row[2]  # Assuming column2 is the second column
                borc = row[3]
            finalText = "Salam " + row[1] + row[2] + ". Sizin borcunuz " + row[3] + " məbləğindədir. Təşəkkürlər!"




            speech_config = speechsdk.SpeechConfig(subscription = 'SubsKey', region='eastus', speech_recognition_language='az-AZ')
            #audio_config = speechsdk.audio.AudioOutputConfig(filename="recordSpeech.wav")
            audio_config = speechsdk.audio.AudioConfig(use_default_microphone=True)
            speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config, audio_config=audio_config)
            speech_recognition_result = speech_recognizer.recognize_once_async().get()
            # The language of the voice that speaks.
            speech_config.speech_synthesis_voice_name='az-AZ-BanuNeural'

            speech_synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config, audio_config=audio_config)

            # Get text from the console and synthesize to the default speaker.
            # print("Enter some text that you want to speak >")
            # text = "Salam " + row[1] + row[2] + ". Sizin borcunuz " + row[3] + " məbləğindədir. Təşəkkürlər!."

            speech_synthesis_result = speech_synthesizer.speak_text_async(finalText).get()





            print(finalText)
            cursor.close()
            conn.close()

    else:
        print("Zəhmət olmasa düzgün nömrəni qeyd edin.")

#textToSpeech()
gettingRequest()