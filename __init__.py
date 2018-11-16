from mycroft import MycroftSkill, intent_file_handler


class SpeakFilipino(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('filipino.speak.intent')
    def handle_filipino_speak(self, message):
        name = self.config_core.get("listener", {}).get("wake_word", "mycroft")
        name = name.lower().replace("hey ", "")
        self.speak_dialog('filipino.speak', {"name":name})


def create_skill():
    return SpeakFilipino()

