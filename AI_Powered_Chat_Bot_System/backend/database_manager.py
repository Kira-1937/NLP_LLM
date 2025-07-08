from pymongo import MongoClient
import datetime

class DatabaseManager:
    def __init__(self):
        self.client = MongoClient('mongodb://localhost:27017/')
        self.db = self.client['chatbot_db']
        self.collection = self.db['interactions']

    def save_interaction(self, user_id, question, answer):
        document = {
            'user_id': user_id,
            'question': question,
            'answer': answer,
            'timestamp': datetime.datetime.now()
        }
        self.collection.insert_one(document)
