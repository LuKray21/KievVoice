
from kivy.lang.builder import Builder
from kivy.uix.boxlayout import BoxLayout

with open('src/AppElements/NewsWorker/NewsWidget.kv', encoding='utf-8') as f:
    presentation = Builder.load_string(f.read())

class NewsWorker():
    def __init__(self):
        self.newsWidget = NewsWidget()

class NewsWidget(BoxLayout):
    def __init__(self):
        super(NewsWidget, self).__init__()
        self.loadNews('Ми додали новий функціонал', "Новини про розробку", "13.05 9:00")
        self.loadNews('У Києві відсьогодні використані противовірусні засоби захисту - гумові рукавички та медичні маски - можна здати на утилізацію, викинувши їх у спеціальні контейнери, встановлені в магазинах мережі "МЕТРО Кеш енд Кері Україна"', "У Києві запрацювали пункти прийому використаних масок і рукавичок", "11.05 12:00")
        self.loadNews('Таке погодне явище зумовлене змінами клімату: безсніжна зима, відсутність звичної норми опадів. Як наслідок – повітряна ерозія ґрунтів, зниження рівня ґрунтових вод, що і є причинами утворення пилу, який у столицю приніс північно-західний вітер', "Екологи назвали причину пилової бурі, що накрила Київ", "10.05 16:53")
       
    def loadNews(self, text, title, date):
        # text = 'Суп па пу па хот крюСуп па пу па хот крюСуп па пу па хот крюСупСуп па пу па хот крюСуп па пу па хот крюСуп па пу па хот крюСуп па пу па хот крюСуп па пу па хот крюСуп па пу па хот крюСуп па пу па хот крюСуп па пу па хот крюСуп па пу па хот крюСуп па пу па хот крюСуп па пу па хот крюСуп па пу па хот крю па пу па хот крю'
        # timestamp = '13.05 11:22'
        self.news = News(title, text, date)
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
             

