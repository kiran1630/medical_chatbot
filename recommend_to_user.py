class langchain:
        def __init__(self):
                import joblib
                import os
                from transformers import pipeline
                from langchain_community.vectorstores import Chroma
                print('imported library')

                os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'
                print('os configured')
                self.joblib = joblib
                self.pipeline = pipeline
                self.Chroma = Chroma


        def recommendation_text(self,disease):    
                        load = self.joblib.load('embedded.pickle')
                        print('embedded model loaded')

                        query = f' what is the recommedation for the {str(disease)}'

                        db3 = self.Chroma(persist_directory="./chroma_db", embedding_function=load)
                        print('vector database loaded')
                        docs = db3.similarity_search(query,k=4)

                        text = ''
                        for i in range(1,3):
                            text+=str(docs[i])


                        pipe = self.pipeline("summarization",model = r"C:\Users\lenovo\Desktop\bot3.11")
                        print('summarizer LOADED')
                        out = pipe(text, max_length=512, min_length=200)
                        print(out[0]['summary_text'])
                        return out[0]['summary_text']

