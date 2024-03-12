import pyttsx3

text_speech = pyttsx3.init()
while True:
    answer = input("Enter what do you want to speak: ")
    if answer == 'q':
        text_speech.say("Bye Bye Friend.")
        text_speech.runAndWait()
        break
    text_speech.say(answer)
    text_speech.runAndWait()