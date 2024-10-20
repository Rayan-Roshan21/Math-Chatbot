# This is to import necessary libaries to use and access our Math Chatbot API.
# In addition, it could be understanding
import google.generativeai as genai
import speech_recognition as sr
import pyttsx3 
import os

# This is where you input your API key. You can access when you use the Google Cloud AI Studio and create a project.
genai.configure(api_key="Enter your key!")

# This is to configure your model. This will dictate your chatbot's output. You can play around with this!
generation_config = {
  "temperature": 0.05,
  "top_p": 1,
  "top_k": 64,
  "max_output_tokens": 250,
  "response_mime_type": "text/plain",
}

# This is used to access our model. I wouldn't touch this if I were you lol.
model = genai.GenerativeModel(
  model_name="tunedModels/mathchatbot-m4ggorut00v8",
  generation_config=generation_config,
  # safety_settings = Adjust safety settings
  # See https://ai.google.dev/gemini-api/docs/safety-settings
)

# This is your chat history. You must be able to understand
chat_session = model.start_chat(
  history=[]
)

# Initialize the recognizer 
r = sr.Recognizer() 

# Function to convert text to speech
def SpeakText(command):
    
    # Initialize the engine
    engine = pyttsx3.init()
    engine.say(command) 
    engine.runAndWait()
    
    
# Loop infinitely for user.
while True:    
    
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
            
            # Using google API to recognize audio
            MyText = r.recognize_google(audio2)
            MyText = MyText.lower()

            # This print statement is used to see what you said through your microphone.
            print(MyText)

            # This is used to send your message to the google API and your model, and then grab it's output.
            response = chat_session.send_message(MyText)
            SpeakText(response.text)

    # These are here just in-case if you run into issues.
    except sr.RequestError as e:
        print("Could not request results")
        
    except sr.UnknownValueError:
        print("unknown error")

# This would print your math chatbot's response.
print(response.text)

