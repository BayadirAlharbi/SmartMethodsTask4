from ibm_watson import TextToSpeechV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
api= IAMAuthenticator("EgSq9AWTvivbSCTr4rGW5TqIuLHjPTyQ0M7potH-9O9u")
text_2_speech = TextToSpeechV1(authenticator=api)
text_2_speech.set_service_url("https://api.eu-gb.text-to-speech.watson.cloud.ibm.com/instances/452c983e-9f0d-4878-822f-f0c8cc896d95")

import speech_recognition as sr
r=sr.Recognizer()
with sr.Microphone() as source:
    print("Speak Anything")
    audio=r.listen(source)
    try:
        text=r.recognize_google(audio)
        print("You said:{}".format(text))
    except:
        print("Sorry, I can't listen!") 
    
            
file = open('hi.txt','w')
file.write(format(text))
file.close()

with open("hi.txt")as text_file:
    data=text_file.read()
    text_file.close()

with open("hi.mp3","wb") as audio :
 audio.write(text_2_speech.synthesize(data,accept="audio/mp3").get_result().content)