from kivy.uix.boxlayout import BoxLayout
from kivy.lang.builder import Builder

with open('C:\Work\Bachelor\KievVol\src\AppElements\FeedbackWorker\FeedbackWidget.kv', encoding='utf-8') as f:
    presentation = Builder.load_string(f.read())

class FeedbackWorker():
    def __init__(self):
        self.feedbackWidget = FeedbackWidget()

    def createNewFeedback(self, title, email, feedback):
        print('feedback created')
        # Відправляти на серве

class FeedbackWidget(BoxLayout):
    def __init__(self):
        super(FeedbackWidget, self).__init__()