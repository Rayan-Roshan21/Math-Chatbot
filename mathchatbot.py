import google.generativeai as genai
import speech_recognition as sr
import pyttsx3 
import os

genai.configure(api_key="Enter your key!")

# Create the model
generation_config = {
  "temperature": 0.05,
  "top_p": 1,
  "top_k": 64,
  "max_output_tokens": 250,
  "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
  model_name="tunedModels/mathchatbot-m4ggorut00v8",
  generation_config=generation_config,
  # safety_settings = Adjust safety settings
  # See https://ai.google.dev/gemini-api/docs/safety-settings
)

chat_session = model.start_chat(
  history=[]
)

# Initialize the recognizer 
r = sr.Recognizer() 

# Function to convert text to
# speech
def SpeakText(command):
    
    # Initialize the engine
    engine = pyttsx3.init()
    engine.say(command) 
    engine.runAndWait()
    
    
# Loop infinitely for user to
# speak

for i in range (1):    
    
    # Exception handling to handle
    # exceptions at the runtime
    try:
        
        # use the microphone as source for input.
        with sr.Microphone() as source2:
            
            # wait for a second to let the recognizer
            # adjust the energy threshold based on
            # the surrounding noise level 
            r.adjust_for_ambient_noise(source2, duration=0.2)
            
            #listens for the user's input 
            audio2 = r.listen(source2)
            
            # Using google to recognize audio
            MyText = r.recognize_google(audio2)
            MyText = MyText.lower()

            print(MyText)
            response = chat_session.send_message(MyText)
            SpeakText(response.text)
            
    except sr.RequestError as e:
        print("Could not request results")
        
    except sr.UnknownValueError:
        print("unknown error")

print(response.text)

