from ibm_watson import TextToSpeechV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
api= IAMAuthenticator("EgSq9AWTvivbSCTr4rGW5TqIuLHjPTyQ0M7potH-9O9u")
text_2_speech = TextToSpeechV1(authenticator=api)
text_2_speech.set_service_url("https://api.eu-gb.text-to-speech.watson.cloud.ibm.com/instances/452c983e-9f0d-4878-822f-f0c8cc896d95")
with open("hi.wav","wb") as audiofile :
    audiofile.write(
        text_2_speech.synthesize("Hello, Good morning",accept="audio/wav").get_result().content
    )
