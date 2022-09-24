from googletrans import Translator
import engine
from dataList import translate_list
import pyttsx3

class TranslateEngine:
    def __init__(self) -> None:
        self.engine_value = pyttsx3.init()
        self.motor = engine.Engine()

    def __speak_translate(self, engine, nyelv, nem='VoiceGenderFemale'):
        for voice in engine.getProperty('voices'):
            if nyelv in voice.languages and nem == voice.gender:
                engine.setProperty('voice', voice.id)
                return True

    def translate_engine(self, string):
        translator = Translator()
        self.motor.Output("What should I translate the text to?")
        while True:
            language = self.motor.Input()
            try:
                if language in translate_list.language_google_translate.keys():
                    language.replace('translate', '').replace('please', '')

                    if language == translate_list.language_google_translate['english']:
                        self.motor.Output('Seriously? Ha ha ha.')

                    speak_language = translate_list.language_google_translate[language]
                    language2 = translate_list.language_google_translate[language]

                    translation = translator.translate(string, dest=language2).text

                    print(translation)

                    self.__speak_translate(self.engine_value, speak_language, "VoiceGenderFemale")
                    self.engine_value.say(translation)
                    self.engine_value.runAndWait()

                else:
                    self.motor.Output('This language is not included in the database.')

            except RuntimeError:
                self.motor.Output(f"ERROR: Language '{language}' is not found.")

            except KeyError:
                self.motor.Output("There is no such language.")

            except ValueError:
                self.motor.Output("ERROR: The parameters are incorrectly specified in the program code.")

            except TypeError:
                print('EROR: Not good -> TypeError')

            if 'not yet' in language or "I don't want to translate" in language or "I don't want to translate it though" in language:
                self.motor.Output('Okay.')
            break

if "__main__" == __name__:
    anyad = TranslateEngine()
    anyad.translate_engine("Fuck you")