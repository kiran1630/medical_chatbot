import psycopg2
import uuid
class database:
        
        def __init__(self,name,age,gender,symptoms,disease):
                
                self.infix = 'JASK'
                self.user_id =self.infix + str(uuid.uuid4())[:3] 
                self.age  = age
                self.name = name
                self.gender = gender
                self.symptoms = symptoms
                self.disease = disease
                
                
        
        def insert_row(self):
                # Establish connection
                conn = psycopg2.connect(
                    dbname="patient_details",
                    user="postgres",
                    password='123',
                    host='127.0.0.1',
                    port='5432'
                )

                # Create a cursor object
                cur = conn.cursor()
                
                command = f"insert into patient_data (date,time,user_id,name,age,gender,symptoms,predicted_disease) values (current_date,current_time,'{self.user_id}','{self.name}','{self.age}','{self.gender}','{self.symptoms}','{self.disease}')"
                
                cur.execute(command)
               
                conn.commit()
                

                
                # Close cursor and connection
                cur.close()
                conn.close()
               

