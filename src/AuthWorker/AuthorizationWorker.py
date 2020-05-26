from kivy.uix.boxlayout import BoxLayout

from .authorizationNetworkController import authorizationNetworkController
from kivy.lang import Builder 

with open('src/AuthWorker/AuthorizationWidget.kv', encoding='utf-8') as f:
    presentation = Builder.load_string(f.read())

goodStatusText = 'Успішно зареестровано'
badStatusText = 'Реестрація не вдалась\n  Спробуйте пізніще'

class AuthorizationWorker():
    def __init__(self, androidApp, authorizedCallback):
        self.authRegWindow = BoxLayout(orientation = 'vertical')
        
        self.authorizedCallback = authorizedCallback
        self.androidApp = androidApp
        self.authNetwork = authorizationNetworkController()
        #WORK WINDOWS
        self.authWindow = AuthWindow()
        self.registWindow = RegistrationWindow()
        # self.goodWidget = GoodResultPage()
        self.authRegWindow.add_widget(self.authWindow)
        self.userRegion = 'Шевченківський'

    def setUserRegion(self, region):
        self.userRegion = region 
        print(region)
    
    def getUserRegion(self):
        return self.userRegion

    def setRegistrationWindow(self):
        self.removeWindow(self.authWindow)
        self.addNewWindow(self.registWindow)

    def setAuthWindow(self):
        self.removeWindow(self.registWindow)
        self.addNewWindow(self.authWindow)

    def addNewWindow(self, widget):
        try:
            self.authRegWindow.add_widget(widget)
        except Exception as err:
            print(err)
    def removeWindow(self, widget):
        try:
            self.authRegWindow.remove_widget(widget)
        except Exception as err:
            print(err)

    def endAuthorization(self, userData):
        self.removeWindow(self.authWindow)
        self.authorizedCallback(userData)

    def setAuthWindowAfReg(self):
        self.addNewWindow(self.authWindow)


##AUTHORIZATION
    def tryToRegister(self, login, name, surname, region, age, phone, email, password):
        result = self.authNetwork.register(login, name, surname, region, age, phone, email, password)
        self.authRegWindow.remove_widget(self.registWindow)
        if result:
            self.androidApp.setResultWidget(self.authRegWindow, goodStatusText, (0.24,0.60,0.27,1), lambda: self.setAuthWindowAfReg())
        else:
            self.androidApp.setResultWidget(self.authRegWindow, badStatusText, (0.87, 0.31, 0.31, 1), lambda: self.setAuthWindowAfReg())

    def tryToAuthorize(self, login, password):
        userData = self.authNetwork.authorize(login, password)
        self.authRegWindow.remove_widget(self.authWindow)
        if userData is not None:
            print('AUTHORIZERD')
            self.endAuthorization(userData)
        else:
            self.androidApp.setResultWidget(self.authRegWindow, 'Авторизація не вдалась\n   Спробуйте пізніше', (0.87, 0.31, 0.31, 1), lambda: self.setAuthWindowAfReg())

class UserRegionDropDown(BoxLayout):
    pass

class AuthWindow(BoxLayout):
    def __init__(self):
        super(AuthWindow, self).__init__()

class RegistrationWindow(BoxLayout):
    def __init__(self):
        super(RegistrationWindow, self).__init__()