from kivy.uix.boxlayout import BoxLayout
from kivy.lang.builder import Builder
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.label import Label
from kivy.uix.dropdown import DropDown
from kivy.uix.button import Button

from .utils import getConstructedTimeFormat, getcurrentTimestamp, getTimeFromTimestamp

with open('KievVol\src\AppElements\EventWorker\EventWidget.kv', encoding='utf-8') as f:
    presentation = Builder.load_string(f.read())

class EventWorker():
    def __init__(self):
        super(EventWorker, self).__init__()
        self.eventListWorker = EventListWorker(self)
        self.eventCreatorWidget = BoxLayout(orientation = 'vertical')
        self.contactsPage = EventCreatorContactsPage()
        self.descPage = EventCreatorDescPage()
        self.goodResultPage = EventCreatorGoodResultPage()
        self.eventCreatorWidget.add_widget(self.descPage)
        self.eventListWorker.addEvent('Зібрати мусор', 'Мусора багато, давайте зьеремо', '+380979879024', 'Соломянский', 'вул Соломьянська 71а', 'mishok_lub@meta.ua', '21', "листопада", '11:50')
        self.eventListWorker.addEvent('Почистити річку', 'Потрібно добре почистити річку, бо вона грязна', '+380983254761', 'Дніпровський', 'вул. Параходна 22/1', 'Lukray21@gmail.comє', '11', 'жотвня', '19:50')
        ####
        self.eventMonth = 'Січень'
        self.eventRegion = 'Шевченківський'

    def setEventMonth(self, eventMonth):
        self.eventMonth = eventMonth 

    def getEventMonth(self):
        return self.eventMonth
    
    def setEventRegion(self, eventRegion):
        self.eventRegion = eventRegion 

    def getEventRegion(self):
        return self.eventRegion

    def setContactsPage(self, eventName, eventDesc):
        self.eventName = eventName
        self.eventDesc = eventDesc
        self.eventCreatorWidget.remove_widget(self.descPage)
        self.eventCreatorWidget.add_widget(self.contactsPage)

    def setDescPage(self):
        self.eventCreatorWidget.remove_widget(self.contactsPage)
        self.eventCreatorWidget.add_widget(self.descPage)

    def setGoodResultPage(self):
        self.eventCreatorWidget.remove_widget(self.contactsPage)
        self.eventCreatorWidget.add_widget(self.goodResultPage)

    def closeGoodResultPage(self):
        self.eventCreatorWidget.remove_widget(self.goodResultPage)
        self.eventCreatorWidget.add_widget(self.descPage)

    def addEventToServerAndDevice(self, eventName, eventDesc, eventPhone, eventRegion, eventAddress, eventEmail, eventDay, eventMonth, eventTime):
        # login = self.session.getUserLogin()                                                           #TODO
        #result = self.networkWorker.addEvent(name, desc, phone, region, address, email)                #TODO
        result = True
        if result == True:      #резулт запроса на сервер
            self.setGoodResultPage()
            self.eventListWorker.addEvent(str(eventName), str(eventDesc), str(eventPhone), str(eventRegion), str(eventAddress), str(eventEmail), str(eventDay), str(eventMonth), str(eventTime))      #СЮДА ТЕЖ ДОДАТИ ЛОГІН, ПАРОЛЬ І НЕЙМ
        self.setEventMonth('Січень')
        self.setEventRegion('Шевченківський')

    def setChoosedEventWidget(self):
        self.eventListWorker.widget.remove_widget(self.eventListWorker)
        pass



class EventCreatorDescPage(BoxLayout):
    def __init__(self):
        super(EventCreatorDescPage, self).__init__()

class EventCreatorContactsPage(BoxLayout):
    def __init__(self):
        super(EventCreatorContactsPage, self).__init__()

class MonthDropDown(BoxLayout):
    pass

class RegionDropDown(BoxLayout):
    pass



class EventCreatorGoodResultPage(BoxLayout):
    def __init__(self):
        super(EventCreatorGoodResultPage, self).__init__()


##########
class EventListWorker():
    def __init__(self, eventWorker):
        self.widget = BoxLayout()
        self.eventListMainWidget = EventListWidget()
        self.widget.add_widget(self.eventListMainWidget)
        self.eventWorker = eventWorker

    def addEvent(self, eventName, eventDesc, eventPhone,  eventRegion, eventAddress, eventEmail, eventDay, eventMonth, eventTime):
        try:
            self.event = Event(self, eventName, eventDesc,eventPhone, eventRegion, eventAddress, eventEmail, eventDay, eventMonth, eventTime)
            self.eventListMainWidget.ids.eventBox.add_widget(self.event)
        except Exception as err:
            print('EVENTLISTWORKER addEvent Exception: ', err)

    def setChoosedEventWidget(self, widget):
        self.choosed_event = widget
        self.widget.remove_widget(self.eventListMainWidget)
        self.widget.add_widget(widget)
    
    def setEventListWidget(self):
        self.widget.remove_widget(self.choosed_event)
        self.widget.add_widget(self.eventListMainWidget)

class EventListWidget(BoxLayout):
    def __init__(self):
        super(EventListWidget, self).__init__()

class Event(ButtonBehavior, BoxLayout):
    def __init__(self, eventListWorker, name, desc, phone, region, address, email, day, month, time):
        super(Event, self).__init__()
        try:
            self.eventListWorker = eventListWorker
            self.userName = 'Михайло'
            self.userSurname = 'Рогальський'
            self.userLogin = 'LuKray21'
            self.name = name
            self.desc = desc
            self.region = region
            self.address = address
            self.email = email
            self.phone = phone
            self.day = day
            self.month = month
            self.time = time

            self.ids.eventName.text = self.name
            self.ids.eventRegion.text = self.region
            self.ids.eventDatetime.text = getConstructedTimeFormat(self.day, self.month, self.time)

        except:
            print('[EVENT CLASS EXCEPTION]')

    def on_press(self):
        self.eventListWorker.setChoosedEventWidget(CurrentEventWidget(self.userLogin, self.name, self.userName, self.userSurname, self.desc, self.region, self.address, self.email, self.phone, self.day, self.month, self.time))

class CurrentEventWidget(BoxLayout):
    def __init__(self, userLogin, name, userName, userSurname, desc, region, address, email, phone, day, month, time):
        super(CurrentEventWidget, self).__init__()
        self.name = name
        self.userLogin = userLogin
        self.userName = userName
        self.userSurname = userSurname
        self.desc = desc
        self.region = region
        self.address = address
        self.email = email
        self.phone = phone
        self.day = day
        self.month = month
        self.time = time

        self.ids.eventFullName.text = self.userName + ' ' + self.userSurname
        self.ids.eventName.text = self.name
        self.ids.eventDesc.text = self.desc
        self.ids.eventDescBox.height = (len(self.desc)/40)*37
        self.ids.eventDatetime.text = getConstructedTimeFormat(self.day, self.month, self.time)
        self.ids.eventRegionAndAdress.text = self.getConstructedAddress(self.region, self.address)
        self.ids.eventEmail.text = self.email
        self.ids.eventPhone.text = self.phone
        
        self.ids.commentButton.bind(on_release=lambda x: self.commentButtonClicked())

    def getConstructedAddress(self, region, address):
        return region + ' район, ' + address

    def getTimeString(self):
        timeString = ''
        return timeString

    def commentButtonClicked(self):

        commentId = '0'                         #генерувати коли буду отправляти на сервер
        self.timestamp = getcurrentTimestamp()            #генерувати коли буду отправляти на сервер
        self.comment = EventComment(commentId, self.userLogin, self.userName, self.userSurname, self.ids.eventCommentInput.text, self.timestamp)
        self.ids.eventCommentBox.add_widget(self.comment)
        

    # def generateCommentId(self)

class EventComment(Label):
    def __init__(self, commentId, login, userName, userSurname, text, timestamp):
        super(EventComment, self).__init__(color = [0.01, 0.01, 0.01, 1], text_size = (374.0, None), padding_x = 5)
        self.commentId = commentId
        
        # 374.0
        self.login = login
        self.userName = userName
        self.userSurname = userSurname
        self.text = text
        self.timestamp = timestamp
        self.time = getTimeFromTimestamp(self.timestamp)

        self.text = str(self.time) + ': ' + str(self.userName) + ' ' + str(self.userSurname) + ': ' + str(text)
