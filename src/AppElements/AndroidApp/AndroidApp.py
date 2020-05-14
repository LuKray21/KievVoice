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
SidePanel_AppMenu = {'Профіль': ['loadProfileWidget', None],
                     'Новини':['loadNewsWidget',None],
                     'Події':['loadFutureEvents',None],
                     'Створити подію':['loadEventCreatorWidget',None],
                     "Зворотній зв'язок":['loadFeedbackWidget', None],
                     'Вихід':['exitApp',None]
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

from src.AuthWorker.AuthorizationWorker import AuthorizationWorker
from src.AppElements.NewsWorker.NewsWorker import NewsWorker
from src.AppElements.EventWorker.EventWorker import EventWorker
from src.AppElements.FeedbackWorker.FeedbackWorker import FeedbackWorker
from src.AppElements.Settings.SettingsWorker import SettingsWorker
from src.AppElements.Profile.ProfileWorker import ProfileWorker

Config.set('graphics', 'resizable', False)
with open('KievVol\src\AppElements\AndroidApp\SidePanel.kv', encoding='utf-8') as f:
    presentation = Builder.load_string(f.read())

class MenuItem(Button):
    def __init__(self, **kwargs):
        super(MenuItem, self).__init__( **kwargs)
        self.background_normal = ''
        self.color = 0,0,0,1
        self.background_color = 1,1,1,1
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

class ResultWidget(BoxLayout):
    def __init__(self):
        super(ResultWidget, self).__init__()
        self.ids.resultButton.background_normal = ''

    def setResultText(self, text):
        self.ids.resultButton.text = text
    
    def setResultColor(self, color):
        self.ids.resultButton.background_color = color

    def setFunc(self, func):
        self.ids.resultButton.bind(on_release=func)


class AndroidApp(App):

    def build(self):
        global RootApp
        RootApp = self
        Window.size = (414,736)
        self.mainWindow = BoxLayout(orientation = 'vertical', spacing = 1)      #ОСнова
        self.authWorker = AuthorizationWorker(self.mainWindow, self.authorizedCallback)              
        self.mainWindow.add_widget(self.authWorker.authWindow)

        self.resultWidget = ResultWidget()

        return self.mainWindow

    def authorizedCallback(self):
        self.main_panel = MainPanel()              
        self.eventWorker = EventWorker()
        self.newsWorker = NewsWorker()
        self.profileWorker = ProfileWorker(self)
        self.settingsWorker = SettingsWorker()
        self.feedbackWorker = FeedbackWorker(self)
        self.navigationdrawer = NavDrawer()        
        side_panel = SidePanel()
        self.navigationdrawer.add_widget(side_panel)
        self.navigationdrawer.anim_type = 'slide_above_anim'
        self.navigationdrawer.add_widget(self.main_panel)
        self.mainWindow.add_widget(self.navigationdrawer)

        self.loadNewsWidget()

    def setResultWidget(self, widget, text, color, func):
        widget.add_widget(self.resultWidget)
        self.resultWidget.setResultText(text)
        self.resultWidget.setResultColor(color)
        self.resultWidget.setFunc(func)

    def toggle_sidepanel(self):
        self.navigationdrawer.toggle_state()

    def loadNewsWidget(self):
        self.time_switch_main_page('Новини', self.newsWorker.newsWidget)

    def loadFutureEvents(self):
        self.time_switch_main_page('Події', self.eventWorker.eventListWorker.widget)
        
    def loadEventCreatorWidget(self):
        self.time_switch_main_page('Створити подію',  self.eventWorker.eventCreatorWidget)

    def loadFeedbackWidget(self):
        self.time_switch_main_page("Зворотній зв'язок", self.feedbackWorker.feedbackWidget)

    def loadProfileWidget(self):
        self.time_switch_main_page("Профіль", self.profileWorker.profileWidget)

    def exitApp(self):
        RootApp.stop()
    
    def time_switch_main_page(self, key,  panel):
        self.navigationdrawer.close_sidepanel()
        if not SidePanel_AppMenu[key][id_AppMenu_PANEL]:
            SidePanel_AppMenu[key][id_AppMenu_PANEL] = panel
        main_panel = SidePanel_AppMenu[key][id_AppMenu_PANEL]
        self.navigationdrawer.remove_widget(self.main_panel)    
        self.navigationdrawer.add_widget(main_panel)            
        self.main_panel = main_panel

