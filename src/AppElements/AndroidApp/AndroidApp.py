#!/usr/bin/env python
# -*- coding: utf-8 -*-#
#-------------------------------------------------------------------------------
# Name:        AndroidApp.py
# Purpose:     Simple example of a android application skeleton that manages
#              application menu using ActionBar and SidePanelMenu that slides
#              over the main panel
#
# Author:      Licia Leanza
#
# Created:     13-04-2014
# Copyright:   (c) Licia Leanza: 2014
# Licence:     GPL v2
#-------------------------------------------------------------------------------

__author__ = 'licia'

#--------------------------------------------------------------------------
'''dictionary that contains the correspondance between items descriptions
and methods that actually implement the specific function and panels to be
shown instead of the first main_panel
'''
SidePanel_AppMenu = {'newsWidget':['loadNewsWidget',None],
                     'futureEvents':['loadFutureEvents',None],
                     'eventCreatorWidget':['loadEventCreatorWidget',None],
                     'feedbackWidget':['loadFeedbackWidget', None],
                     'Exit':['exitApp',None]
                     }
id_AppMenu_METHOD = 0
id_AppMenu_PANEL = 1


#--------------------------------------------------------------------------
import kivy
kivy.require('1.8.0')

from kivy.app import App
from kivy.garden.navigationdrawer import NavigationDrawer
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.uix.actionbar import ActionBar, ActionButton, ActionPrevious
from kivy.properties import  ObjectProperty
from kivy.config import Config
from kivy.core.window import Window
from kivy.lang import Builder 

from src.AuthWorker.AuthorizationController import AuthorizationController
from src.SessionController.SessionController import SessionController

Config.set('graphics', 'resizable', False)
with open('C:\Work\Bachelor\KievVol\src\AppElements\AndroidApp\SidePanel.kv', encoding='utf-8') as f:
    presentation = Builder.load_string(f.read())

class MenuItem(Button):
    def __init__(self, **kwargs):
        super(MenuItem, self).__init__( **kwargs)
        self.bind(on_press=self.menuitem_selected)

    def menuitem_selected(self, *args):
        print (self.text, SidePanel_AppMenu[self.text], SidePanel_AppMenu[self.text][id_AppMenu_METHOD])
        try:
            function_to_call = SidePanel_AppMenu[self.text][id_AppMenu_METHOD]
        except:
            print ('errore di configurazione dizionario voci menu')
            return
        getattr(RootApp, function_to_call)()

#
class AppActionBar(ActionBar):
    pass

class ActionMenu(ActionPrevious):
    def menu(self):
        print ('ActionMenu')
        RootApp.toggle_sidepanel()

class ActionQuit(ActionButton):
    pass
    def menu(self):
        print( 'App quit')
        RootApp.stop()

class ActionAuthorization(ActionButton):
    def menu(self):
        print("AUTH")

class SidePanel(BoxLayout):
    pass

class MainPanel(BoxLayout):
    pass

class AppArea(FloatLayout):
    pass

class NewsWidget(FloatLayout):
    pass

class FutureEvents(FloatLayout):
    pass

class EventCreatorWidget(FloatLayout):
    pass

class FeedbackWidget(FloatLayout):
    pass

class AppButton(Button):
    nome_bottone = ObjectProperty(None)
    def app_pushed(self):
        print (self.text, 'button', self.nome_bottone.state)


class NavDrawer(NavigationDrawer):
    def __init__(self, **kwargs):
        super(NavDrawer, self).__init__( **kwargs)

        
    def close_sidepanel(self, animate=True):

        if self.state == 'open':
            if animate:
                self.anim_to_state('closed')
            else:
                self.state = 'closed'


class AndroidApp(App):

    def build(self):
        global RootApp
        RootApp = self
        Window.size = (414,736)
        self.session = SessionController()
        self.mainWindow = BoxLayout(orientation = 'vertical', spacing = 1)      #ОСнова
        self.authController = AuthorizationController(self.mainWindow, self.session, self.authorizedCallback)              
        self.mainWindow.add_widget(self.authController.authWindow)

        return self.mainWindow

    def authorizedCallback(self):
        self.navigationdrawer = NavDrawer()        
        self.main_panel = MainPanel()               #ПОТОМ УБРАТЬ ПОХОДУ
        side_panel = SidePanel()
        self.navigationdrawer.add_widget(side_panel)
        self.navigationdrawer.anim_type = 'slide_above_anim'
        self.navigationdrawer.add_widget(self.main_panel)
        self.mainWindow.add_widget(self.navigationdrawer)

    def auth(self):
        print("AUSUUSAUSUSU")

    def toggle_sidepanel(self):
        self.navigationdrawer.toggle_state()

    def loadNewsWidget(self):
        self._switch_main_page('newsWidget', NewsWidget)

    def loadFutureEvents(self):
        self._switch_main_page('futureEvents', FutureEvents)
        
    def loadEventCreatorWidget(self):
        self._switch_main_page('eventCreatorWidget',  EventCreatorWidget)

    def loadFeedbackWidget(self):
        self._switch_main_page('feedbackWidget', FeedbackWidget)

    def exitApp(self):
        RootApp.stop()

    def _switch_main_page(self, key,  panel):
        self.navigationdrawer.close_sidepanel()
        if not SidePanel_AppMenu[key][id_AppMenu_PANEL]:
            SidePanel_AppMenu[key][id_AppMenu_PANEL] = panel()
        main_panel = SidePanel_AppMenu[key][id_AppMenu_PANEL]
        self.navigationdrawer.remove_widget(self.main_panel)    # FACCIO REMOVE ED ADD perchè la set_main_panel
        self.navigationdrawer.add_widget(main_panel)            # dà un'eccezione e non ho capito perchè
        self.main_panel = main_panel

