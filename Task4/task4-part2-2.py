import speech_recognition as sr
from ibm_watson import SpeechToTextV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
api=IAMAuthenticator("yEoyrKnd11yS9gHHV8KHmLZqti4lzWma21D9x-Zc2LgA")
speech_2_text=SpeechToTextV1(authenticator=api)
speech_2_text.set_service_url("https://api.eu-gb.speech-to-text.watson.cloud.ibm.com/instances/cdfc9720-66d9-4443-b0fc-3297f841a808")

with open("hi.wav","rb")as audio_file:
    result=speech_2_text.recognize(
        audio=audio_file,content_type="audio/wav"
    ).get_result()

print(result)

import speech_recognition as sr
r = sr.Recognizer()
with sr.AudioFile('hi.wav') as source :
    audio=r.listen(source)
    try:
        text=r.recognize_google(audio)
        print("working on...")
        print(text)

    except:
        print("sorry")

file = open('hi.txt','w')
file.write(text)
file.close()

with open("hi.txt")as text_file:
    data=text_file.read()
    text_file.close()