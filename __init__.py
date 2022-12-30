from mycroft import MycroftSkill, intent_handler


class DesktopAssistant(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_handler('assistant.desktop.intent')
    def handle_assistant_desktop(self, message):
        self.speak_dialog('assistant.desktop')


def create_skill():
    return DesktopAssistant()

