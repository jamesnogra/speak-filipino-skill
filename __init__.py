from mycroft import MycroftSkill, intent_file_handler


class SpeakFilipino(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('filipino.speak.intent')
    def handle_filipino_speak(self, message):
        self.speak_dialog('filipino.speak')


def create_skill():
    return SpeakFilipino()

