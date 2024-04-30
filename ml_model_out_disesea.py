class ml_predict:
    def __init__(self):
        import joblib
        import numpy as np
        self.model = joblib.load('random_model.pkl')
        self.names = joblib.load('name_of_disease.joblib')
        self.np = np
        self.joblib = joblib

    def predict(self,value):
            value = self.np.array(value).reshape(1,-1)
            num = self.model.predict(value)
            disease =self.names[num[0]]
            return disease
    
