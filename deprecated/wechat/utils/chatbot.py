from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer


class chatbot:
    def __init__(self, text):
        self.chatbot = ChatBot("Lily BAI")
        self.response = "This is the default response"
        self.text = text

    def train(self):
        conversation = [
            "Hello",
            "Hi there!",
            "How are you doing?",
            "I'm doing great.",
            "That is good to hear",
            "Thank you.",
            "You're welcome."
        ]
        trainer1 = ListTrainer(self.chatbot)
        trainer1.train(conversation)

        trainer2 = ChatterBotCorpusTrainer(self.chatbot)
        trainer2.train('chatterbot.corpus.chinese')

        trainer2.export_for_training('./Output/my_export.json')

        return

    def get_response(self):
        self.response = self.chatbot.get_response(self.text)
        print(self.response)
        return

    def chatbot_caller(self):
        self.train()
        self.get_response()
        return self.response
