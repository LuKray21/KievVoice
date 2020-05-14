from kivy.lang.builder import Builder
from kivy.uix.boxlayout import BoxLayout

with open('KievVol\src\AppElements\Settings\SettingsWidget.kv', encoding='utf-8') as f:
    presentation = Builder.load_string(f.read())

class SettingsWorker():
    def __init__(self):
        super(SettingsWorker, self).__init__()
        self.settingsWidget = BoxLayout()
        self.settingsMainWidget = SettingsMainWidget()

        self.settingsWidget.add_widget(self.settingsMainWidget)

class SettingsMainWidget(BoxLayout):
    def __init__(self):
        super(SettingsMainWidget, self).__init__()