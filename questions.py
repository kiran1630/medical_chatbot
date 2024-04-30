class question:
    def __init__(self):
        import random
        self.random = random
        pass



    def ask_name(self):
        num = self.random.randint(0,5)
        name_questions = [
        "What's your name?",
        "May I know your name, please?",
        "Could you tell me your name?",
        "Hello! What name do you go by?",
        "Could you share your name with me?",
        "Would you mind telling me your name?"
        ]
        return name_questions[num]

    def ask_age(self):
        num = self.random.randint(0,4)
        age_questions = [
        "How old are you?",
        "What's your age?",
        "Could you inform me about your current age?",
        "Could you share your age with us?",
        "Would you mind telling me how old you are?",
        "Do you mind revealing your age?",
    ]
        return age_questions[num]

    def ask_gender(self):
        num = self.random.randint(0,7)
        gender_question = [
        "What is your gender?",
        "Are you male, female, or prefer not to say?",
        "Could you specify your gender?",
        "May I know your gender identity?",
        "How do you identify in terms of gender?",
        "Do you identify as male, female, or another gender?",
        "What gender do you identify with?",
        "Would you like to share your gender with me?"
    ]
        return gender_question[num]


    def ask_symptom_question(self):
        num =self.random.randint(0,6)
        symptom_questions = [
        "Could you describe any symptoms or health concerns you're experiencing?",
        "What symptoms are you currently experiencing?",
        "Are you feeling any discomfort or noticing any changes in your health?",
        "Can you tell me about any symptoms you're dealing with?",
        "How are you feeling physically? Any symptoms to report?",
        "Please describe any symptoms you've noticed recently.",
        "Are there any specific health issues you'd like to discuss?",
        
        ]
        return symptom_questions[num]