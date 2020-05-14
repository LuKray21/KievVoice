
from kivy.lang.builder import Builder
from kivy.uix.boxlayout import BoxLayout

with open('KievVol\\src\\AppElements\\NewsWorker\\NewsWidget.kv', encoding='utf-8') as f:
    presentation = Builder.load_string(f.read())

class NewsWorker():
    def __init__(self):
        self.newsWidget = NewsWidget()

class NewsWidget(BoxLayout):
    def __init__(self):
        super(NewsWidget, self).__init__()
        self.loadNews('Дякуємо, що ви з нами')
        self.loadNews('Медиа, финансируемые Ахметовым, Коломойским, Медведчуком, Путиным, будут работать в любой кризис, а мы без вашей помощи — нет.')
        self.loadNews('Офис станет креативным хабом. Там будут проводить важные встречи и мероприятия. Но большинство сотрудников будут работать дистанционно.Новым офисом уже становятся Zoom, Slack, Telegram, Hangouts, Teams. Так, количество пользователей Zoom в марте выросло в 20 раз - до 200 млн человек в день. ')
        self.loadNews('Новина, новинаНовина, новинаНовина, новинаНовина, новинаНовина, новинаНовина, новинаНовина, новинаНовина, новина')

    def loadNews(self, text):
        title = 'НовинаТестова НовинаТестова НовинаТестова'
        # text = 'Суп па пу па хот крюСуп па пу па хот крюСуп па пу па хот крюСупСуп па пу па хот крюСуп па пу па хот крюСуп па пу па хот крюСуп па пу па хот крюСуп па пу па хот крюСуп па пу па хот крюСуп па пу па хот крюСуп па пу па хот крюСуп па пу па хот крюСуп па пу па хот крюСуп па пу па хот крюСуп па пу па хот крю па пу па хот крю'
        timestamp = '13.05 11:22'
        self.news = News(title, text, timestamp)
        self.ids.newsBox.add_widget(self.news)


class News(BoxLayout):
    def __init__(self, title, text, timestamp):
        super(News, self).__init__()
        # self.height = 20
        self.title = title
        self.text = text
        self.timestamp = timestamp
        self.ids.newsText.text = text
        self.ids.newsTitle.text = title
        self.ids.newsTime.text = timestamp
        print(self.height)
        self.height = self.calculateRowHeight(self.text, self.title)
        self.ids.newsTitleBox.height = (len(title)/26)*50

    def calculateRowHeight(self, text, title):
        if len(text) / 26 < 1:
            return 40 + (len(title)/26)*55 + 25
        else:
            return (len(text)/34)*33 + (len(title)/26)*55 + 25
             

