from kivy.uix.boxlayout import BoxLayout
from kivy.lang.builder import Builder

with open('KievVol\src\AppElements\FeedbackWorker\FeedbackWidget.kv', encoding='utf-8') as f:
    presentation = Builder.load_string(f.read())

goodStatusText = 'Звернення відправлено'
badStatusText = 'Звернення не відправлено\n      Спробуйте пізніше'

class FeedbackWorker():
    def __init__(self, androidApp):
        self.androidApp = androidApp
        self.feedbackWidget = BoxLayout()
        self.feedbackFormWidget = FeedbackFormWidget()

        self.feedbackWidget.add_widget(self.feedbackFormWidget)

    def createNewFeedback(self, title, email, feedback):
        print('feedback created')
        result = True
        self.feedbackWidget.remove_widget(self.feedbackFormWidget)
        if result:
            self.androidApp.setResultWidget(self.feedbackWidget, goodStatusText, (0.24,0.60,0.27,1), self.setFeedbackWidget)
        else:
            self.androidApp.setResultWidget(self.feedbackWidget, badStatusText, (0.87, 0.31, 0.31, 1), self.setFeedbackWidget)
            
    def setFeedbackWidget(self, d):
        print(d)
        self.feedbackWidget.remove_widget(self.androidApp.resultWidget)
        self.feedbackWidget.add_widget(self.feedbackFormWidget)

class FeedbackResultWidget(BoxLayout):
    def __init__(self, ):
        super(FeedbackResultWidget, self).__init__()

class FeedbackFormWidget(BoxLayout):
    def __init__(self):
        super(FeedbackFormWidget, self).__init__()