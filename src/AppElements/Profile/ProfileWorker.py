from kivy.uix.boxlayout import BoxLayout
from kivy.lang.builder import Builder

with open('KievVol\src\AppElements\Profile\ProfileWidget.kv', encoding='utf-8') as f:
    presentation = Builder.load_string(f.read())

class ProfileWorker():
    def __init__(self, androidApp):
        super(ProfileWorker, self).__init__()
        self.androidApp = androidApp
        self.profileWidget = BoxLayout()
        self.profileMainWidget = ProfileMainWidget()

        self.profileWidget.add_widget(self.profileMainWidget)
        profileRegion = "Шевченківський"
    
    def setProfileRegion(self, region):
        self.profileRegion = region

    def getProfileRegion(self):
        return self.profileRegion
    
    def updateProfile(self, name, surname, email, region, phone):
        result = True
        self.profileWidget.remove_widget(self.profileMainWidget)
        if result:
            self.androidApp.setResultWidget(self.profileWidget, 'Дані оновлено', (0.24,0.60,0.27,1), self.setProfileWidget)
        else:
            self.androidApp.setResultWidget(self.profileWidget, "Сталася помилка\n   Спробуйте пізніше", (0.87, 0.31, 0.31, 1), self.setFeedbackWidget)
            
    def updatePassword(self, oldPassword, newPassword):
        result = True
        self.profileWidget.remove_widget(self.profileMainWidget)
        if result:
            self.androidApp.setResultWidget(self.profileWidget, 'Пароль оновлено', (0.24,0.60,0.27,1), self.setProfileWidget)
        else:
            self.androidApp.setResultWidget(self.profileWidget, "Сталася помилка\n   Спробуйте пізніше", (0.87, 0.31, 0.31, 1), self.setProfileWidget)

    def setProfileWidget(self, d):
        self.profileWidget.remove_widget(self.androidApp.resultWidget)
        self.profileWidget.add_widget(self.profileMainWidget)

class ProfileMainWidget(BoxLayout):
    def __init__(self):
        super(ProfileMainWidget, self).__init__()

class ProfileRegionDropDown(BoxLayout):
    pass