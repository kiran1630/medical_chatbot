import chainlit as cl
import random
from database_conn import database
import subprocess
from chainlit import AskUserMessage, Message, on_chat_start
from gemini import gemini_bot
from ml_model_out_disesea import ml_predict
from recommend_to_user import langchain
from questions import question

g1 = gemini_bot()
m1 = ml_predict()
l1 = langchain()
request = question()

class detail:
    def __init__(self):
        self.details =[]
        pass


patient = detail()
@on_chat_start
async def main():
   
    await info()
    
   
    
    
    val = await get_symptom_data()
    symptoms,array = g1.symptom_detect(str(val))

    disease = m1.predict(array)
    # patient.details.append(str(symptoms))
    # patient.details.append(str(disease))
    text_to_recommend = l1.recommendation_text(disease)
    print('===========',symptoms,disease,'===========')

    await cl.Message(content=f"Based on your symptoms the disease you might have {disease}").send()
    await cl.Message(content=str(text_to_recommend)).send()
    
   
    
       
   
   
    
    symptoms = ','.join(symptoms)
    patient_table = database(patient.details[0],int(patient.details[1]),patient.details[2],str(symptoms),str(disease))
    patient_table.insert_row()
    
    
    @cl.on_message
    async  def chat_gemini(message:cl.Message):
        response = g1.chat(message.content)
        await cl.Message(content = response).send()
    

    print('==========ended===========')




    


async def info():    
        
        name = await AskUserMessage(content=request.ask_name(), timeout=30).send()
        if name:
            await Message(
                content=f"HI !!!{name['output']}"
            ).send()
            patient.details.append(name['output'])

        
        age= await AskUserMessage(content=request.ask_age(), timeout=30).send()
        if age:
            patient.details.append(age['output'])
            
        
        gender = await AskUserMessage(content=request.ask_gender(), timeout=30).send()
        if gender:
            patient.details.append(gender['output'])
async def get_symptom_data():
            symptom = await AskUserMessage(content=request.ask_symptom_question(), timeout=300).send()
            if symptom:
                patient.details.append(symptom['output'])
            val = str(symptom['output'])
            return val


     
            
def run_chainlit():
    try:
        # Run the command using subprocess
        subprocess.run(["chainlit", "run", "ui_chatbot_tester.py", "-w"], check=True)
    except subprocess.CalledProcessError as e:
        # Handle errors if the command fails
        print("Error:", e)

