from kivy.app import App
import dataHandler
from kivy.metrics import dp
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.graphics import Color
from kivy.uix.button import Button
from kivy.uix.togglebutton import ToggleButton
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
from googletrans import Translator
from kivy.uix.popup import Popup
import googletrans
import random
import sqlite3


class WindowManager(ScreenManager):
    pass


class StartWindow(Screen):

    try:
        
        dataHandler.checkCounterTable()

        def __init__(self, **kwargs):
            super(StartWindow, self).__init__(**kwargs)

            self.boxlayout = BoxLayout( orientation='vertical',
                                        size_hint=(0.5,0.8),
                                        pos_hint={'x':(0.5-0.25),'y':0.15})
            self.gridlayout = GridLayout(cols=1, rows=2)

            self.greet = Label(text='Hi', font_size=48, size_hint=(1,0.8), color=(0,0,0,1))
            self.open_dictionary_btn = Button(text='OPEN YOUR PERSONAL DICTOINARY', size_hint=(1,0.2))
            self.open_dictionary_btn.bind(on_press=self.openDictionaryButton)

            self.gridlayout.add_widget(self.greet)
            self.gridlayout.add_widget(self.open_dictionary_btn)
            self.boxlayout.add_widget(self.gridlayout)
            self.add_widget(self.boxlayout)


        def learningLanguage(self):

            data = dataHandler.checkCurrentDictionary()[-1][-1]

            db = sqlite3.connect('database.db')
            cursor = db.cursor()
            cursor.execute("""

                        SELECT primary_language, learning_language
                        FROM track_language
                        WHERE dictionary = (?)

                """, (data,))

            wordLabel = cursor.fetchall()
            return ''.join(wordLabel[-1][-1].split(' '))

            db.close()

        def primaryLanguage(self):

            data = dataHandler.checkCurrentDictionary()[-1][-1]

            db = sqlite3.connect('database.db')
            cursor = db.cursor()
            cursor.execute("""

                        SELECT primary_language, learning_language
                        FROM track_language
                        WHERE dictionary = (?)

                """, (data,))

            wordLabel = cursor.fetchall()
            return ''.join(wordLabel[-1][0].split(' '))

            db.close()

        def openDictionaryButton(self, instance):

            self.manager.get_screen('DictionaryWindow').ids.words.text = self.learningLanguage()
            self.manager.get_screen('DictionaryWindow').ids.meanings.text = self.primaryLanguage()
            self.manager.get_screen('ViewWindow').ids.words.text = self.learningLanguage()
            self.manager.get_screen('ViewWindow').ids.meanings.text = self.primaryLanguage()
            self.manager.get_screen('DictionaryWindow').ids.DictionaryWindow_words.text = self.manager.get_screen('DictionaryWindow').showWords()
            self.manager.get_screen('DictionaryWindow').ids.DictionaryWindow_meanings.text = self.manager.get_screen('DictionaryWindow').showMeanings()
            self.manager.get_screen('ViewWindow').ids.ViewWindow_words.text = self.manager.get_screen('DictionaryWindow').showWords()
            self.manager.get_screen('ViewWindow').ids.ViewWindow_meanings.text = self.manager.get_screen('DictionaryWindow').showMeanings()
            self.manager.current = 'DictionaryWindow'
            self.manager.transition.direction = 'up'
            self.manager.get_screen('TranslateWindow').ids.learningLanguage.text = f'Translate To\n    {self.learningLanguage()}'
            self.manager.get_screen('TranslateWindow').ids.primaryLanguage.text = f'Translate To\n    {self.primaryLanguage()}'
            self.manager.get_screen('AddDictionaryWindow').ids.dictionary1.text = f'{self.primaryLanguage()} - {self.learningLanguage()} Dictionary'
            if len(dataHandler.checkDictionaries()) > 1:
                if len(dataHandler.checkDictionaries()) == 2:
                    self.manager.get_screen('AddDictionaryWindow').ids.dictionary2.text = f'{dataHandler.dictionaryLanguages("dictionary2")[0][0]} - {dataHandler.dictionaryLanguages("dictionary2")[0][1]} Dictionary'
                    self.manager.get_screen('AddDictionaryWindow').ids.dictionary3.text = 'CREATE THIRD DICTIONARY'
                elif len(dataHandler.checkDictionaries()) == 3:
                    self.manager.get_screen('AddDictionaryWindow').ids.dictionary2.text = f'{dataHandler.dictionaryLanguages("dictionary2")[0][0]} - {dataHandler.dictionaryLanguages("dictionary2")[0][1]} Dictionary'
                    self.manager.get_screen('AddDictionaryWindow').ids.dictionary3.text = f'{dataHandler.dictionaryLanguages("dictionary3")[0][0]} - {dataHandler.dictionaryLanguages("dictionary3")[0][1]} Dictionary'
            else:
                self.manager.get_screen('AddDictionaryWindow').ids.dictionary2.text = 'CREATE SECOND DICTIONARY'
                self.manager.get_screen('AddDictionaryWindow').ids.dictionary3.text = 'CREATE THIRD DICTIONARY'


    except:

        def __init__(self, **kwargs):
            super(StartWindow, self).__init__(**kwargs)

            self.boxlayout = BoxLayout( orientation='vertical',
                                        size_hint=(0.5,0.8),
                                        pos_hint={'x':(0.5-0.25),'y':0.15})

            self.gridlayout = GridLayout(cols=1, rows=4, size_hint=(1,0.8))
            self.primary_lang_label = Label(text='Type your Primary Language', font_size=32)
            self.primary_lang_input = TextInput(multiline=False)
            self.learning_lang_label = Label(text='Type your Learning Language', font_size=32)
            self.learning_lang_input = TextInput(multiline=False)

            self.gridlayout.add_widget(self.primary_lang_label)
            self.gridlayout.add_widget(self.primary_lang_input)
            self.gridlayout.add_widget(self.learning_lang_label)
            self.gridlayout.add_widget(self.learning_lang_input)

            self.btn_gridlayout = GridLayout(cols=1, rows=1, size_hint=(1,0.2))
            self.create_button = Button(text='CREATE YOUR FIRST DICTIONARY')
            self.create_button.bind(on_press=self.createButton)
            self.btn_gridlayout.add_widget(self.create_button)

            self.boxlayout.add_widget(self.gridlayout)
            self.boxlayout.add_widget(self.btn_gridlayout)
            self.add_widget(self.boxlayout)


        def learningLanguage(self):

            data = dataHandler.checkCurrentDictionary()[-1][-1]

            db = sqlite3.connect('database.db')
            cursor = db.cursor()
            cursor.execute("""

                        SELECT primary_language, learning_language
                        FROM track_language
                        WHERE dictionary = (?)

                """, (data,))

            wordLabel = cursor.fetchall()
            return ''.join(wordLabel[-1][-1].split(' '))

            db.close()

        def primaryLanguage(self):

            data = dataHandler.checkCurrentDictionary()[-1][-1]

            db = sqlite3.connect('database.db')
            cursor = db.cursor()
            cursor.execute("""

                        SELECT primary_language, learning_language
                        FROM track_language
                        WHERE dictionary = (?)

                """, (data,))

            wordLabel = cursor.fetchall()
            return ''.join(wordLabel[-1][0].split(' '))

            db.close()


        def createButton(self, instance):

            if ''.join(''.join(self.primary_lang_input.text.split(' ')).split('\t')).isalpha() and ''.join(''.join(self.learning_lang_input.text.split(' ')).split('\t')).isalpha():

                if ''.join(''.join(self.primary_lang_input.text.split(' ')).split('\t')).lower() in googletrans.LANGUAGES.values() and ''.join(''.join(self.learning_lang_input.text.split(' ')).split('\t')).lower() in googletrans.LANGUAGES.values():

                    dataHandler.createDatabase()

                    dataHandler.createCounterTable()

                    dataHandler.addDictionary('dictionary1')

                    dataHandler.addCurrentDictionary('dictionary1')

                    primarylanguage = ''.join(''.join(self.primary_lang_input.text.split(' ')).split('\t'))
                    learninglanguage = ''.join(''.join(self.learning_lang_input.text.split(' ')).split('\t'))

                    dataHandler.addTrackLanguage('dictionary1', primarylanguage, learninglanguage)

                    dataHandler.createDictionaryData()

                    self.manager.get_screen('DictionaryWindow').ids.words.text = self.learningLanguage()
                    self.manager.get_screen('DictionaryWindow').ids.meanings.text = self.primaryLanguage()
                    self.manager.get_screen('ViewWindow').ids.words.text = self.learningLanguage()
                    self.manager.get_screen('ViewWindow').ids.meanings.text = self.primaryLanguage()
                    self.manager.get_screen('DictionaryWindow').ids.DictionaryWindow_words.text = self.manager.get_screen('DictionaryWindow').showWords()
                    self.manager.get_screen('DictionaryWindow').ids.DictionaryWindow_meanings.text = self.manager.get_screen('DictionaryWindow').showMeanings()
                    self.manager.get_screen('ViewWindow').ids.ViewWindow_words.text = self.manager.get_screen('DictionaryWindow').showWords()
                    self.manager.get_screen('ViewWindow').ids.ViewWindow_meanings.text = self.manager.get_screen('DictionaryWindow').showMeanings()
                    self.manager.current = 'DictionaryWindow'
                    self.manager.transition.direction = 'up'
                    self.manager.get_screen('TranslateWindow').ids.learningLanguage.text = f'Translate To\n    {self.learningLanguage()}'
                    self.manager.get_screen('TranslateWindow').ids.primaryLanguage.text = f'Translate To\n    {self.primaryLanguage()}'
                    self.manager.get_screen('AddDictionaryWindow').ids.dictionary1.text = f'{self.primaryLanguage()} - {self.learningLanguage()} Dictionary'
                    if len(dataHandler.checkDictionaries()) > 1:
                        if len(dataHandler.checkDictionaries()) == 2:
                            self.manager.get_screen('AddDictionaryWindow').ids.dictionary2.text = f'{dataHandler.dictionaryLanguages("dictionary2")[0][0]} - {dataHandler.dictionaryLanguages("dictionary2")[0][1]} Dictionary'
                            self.manager.get_screen('AddDictionaryWindow').ids.dictionary3.text = 'CREATE THIRD DICTIONARY'
                        elif len(dataHandler.checkDictionaries()) == 3:
                            self.manager.get_screen('AddDictionaryWindow').ids.dictionary2.text = f'{dataHandler.dictionaryLanguages("dictionary2")[0][0]} - {dataHandler.dictionaryLanguages("dictionary2")[0][1]} Dictionary'
                            self.manager.get_screen('AddDictionaryWindow').ids.dictionary3.text = f'{dataHandler.dictionaryLanguages("dictionary3")[0][0]} - {dataHandler.dictionaryLanguages("dictionary3")[0][1]} Dictionary'
                    else:
                        self.manager.get_screen('AddDictionaryWindow').ids.dictionary2.text = 'CREATE SECOND DICTIONARY'
                        self.manager.get_screen('AddDictionaryWindow').ids.dictionary3.text = 'CREATE THIRD DICTIONARY'

                else:

                    popup = Popup(content=Label(text='Please Type A Valid Language!'), size_hint=(dp(.4), dp(.15)), pos_hint={'x': .3, 'top': .9})
                    popup.open()


class DictionaryWindow(Screen):

    def wordUnknown(self):

        words_list = [v[0] for v in dataHandler.getDictionary()]
        
        inputText = self.ids.searchbar.text.split(' ')

        if self.ids.searchbar.text not in words_list and ''.join(inputText).isalpha():

            return True

    def meaningUnknown(self):

        meanings_list = [v[1] for v in dataHandler.getDictionary()]

        if self.ids.searchbar.text not in meanings_list:

            return True

    def showWords(self):

        try:

            words = dataHandler.getDictionaryWords()

        except:

            words = 'Add Your First Word'

        return words

    def showMeanings(self):

        try:

            meanings = dataHandler.getDictionaryMeanings()

        except:

            meanings = 'Add Your First Meaning'

        return meanings

    def searchWord(self):

        if self.ids.searchbar.text != '':

            words_list = [v[0] for v in dataHandler.getDictionary()]
            meanings_list = [v[1] for v in dataHandler.getDictionary()]

            if self.ids.searchbar.text in words_list:
                self.ids.DictionaryWindow_words.text = self.ids.searchbar.text
                self.ids.DictionaryWindow_meanings.text = meanings_list[words_list.index(self.ids.searchbar.text)]

            elif self.ids.searchbar.text in meanings_list:
                self.ids.DictionaryWindow_meanings.text = self.ids.searchbar.text
                self.ids.DictionaryWindow_words.text = words_list[meanings_list.index(self.ids.searchbar.text)]

        else:
            self.ids.DictionaryWindow_words.text = self.showWords()
            self.ids.DictionaryWindow_meanings.text = self.showMeanings()
        

    def sort_words(self):

        words = '\n'.join(dataHandler.sortedDictionary()[0])

        return words


    def sort_meanings(self):

        meanings = '\n'.join(dataHandler.sortedDictionary()[1])

        return meanings


    def ViewButton(self):
        self.manager.get_screen('ViewWindow').ids.ViewWindow_words.text = self.showWords()
        self.manager.get_screen('ViewWindow').ids.ViewWindow_meanings.text = self.showMeanings()
        self.manager.get_screen('ViewWindow').ids.searchbar.text = ''
        self.manager.current = 'ViewWindow'
        self.manager.transition.direction = 'left'


class ViewWindow(Screen):

    def searchWord(self):
        
        if self.ids.searchbar.text != '':

            words_list = [v[0] for v in dataHandler.getDictionary()]
            meanings_list = [v[1] for v in dataHandler.getDictionary()]

            if self.ids.searchbar.text in words_list:
                self.ids.ViewWindow_words.text = self.ids.searchbar.text
                self.ids.ViewWindow_meanings.text = meanings_list[words_list.index(self.ids.searchbar.text)]

            elif self.ids.searchbar.text in meanings_list:
                self.ids.ViewWindow_meanings.text = self.ids.searchbar.text
                self.ids.ViewWindow_words.text = words_list[meanings_list.index(self.ids.searchbar.text)]

        else:

            self.ids.ViewWindow_words.text = self.showWords()
            self.ids.ViewWindow_meanings.text = self.showMeanings()

    def backButton(self):

        self.manager.get_screen('DictionaryWindow').ids.DictionaryWindow_words.text = self.manager.get_screen('DictionaryWindow').showWords()
        self.manager.get_screen('DictionaryWindow').ids.DictionaryWindow_meanings.text = self.manager.get_screen('DictionaryWindow').showMeanings()
        self.manager.get_screen('DictionaryWindow').ids.sortbutton.text = 'Sort Alphabetically'
        self.ids.sortbutton.text = 'Sort Alphabetically'
        self.manager.current = 'DictionaryWindow'
        self.manager.transition.direction = 'right'


class CommandWindow(Screen):
    
    def addWordButton(self):

        self.manager.get_screen('AddWordWindow').first_word = True
        self.manager.get_screen('AddWordWindow').first_meaning = True
        self.manager.get_screen('AddWordWindow').wordsToAdd = []
        self.manager.get_screen('AddWordWindow').meaningsToAdd = []
        self.manager.get_screen('AddWordWindow').ids.word_label.text = 'Words'
        self.manager.get_screen('AddWordWindow').ids.meaning_label.text = 'Meanings'
        self.manager.get_screen('AddWordWindow').ids.inputbox.text = ''
        self.manager.current = 'AddWordWindow'
        self.manager.transition.direction = 'left'

    def testCustomizationButton(self):

        self.manager.get_screen('TestCustomizationWindow').words_list = []
        self.manager.get_screen('TestCustomizationWindow').checkWordReq()
        self.manager.get_screen('TestCustomizationWindow').toggleButtons()
        self.manager.current = 'TestCustomizationWindow'
        self.manager.transition.direction = 'left'

    def settingsButton(self):
        
        self.manager.get_screen('SettingsWindow').ids.themeButton.state = 'down'
        self.manager.get_screen('SettingsWindow').ids.dictionaryButton.state = 'normal'
        self.manager.current = 'SettingsWindow'
        self.manager.transition.direction = 'left'

    def backButton(self):

        self.manager.get_screen('DictionaryWindow').ids.DictionaryWindow_words.text = self.manager.get_screen('DictionaryWindow').showWords()
        self.manager.get_screen('DictionaryWindow').ids.DictionaryWindow_meanings.text = self.manager.get_screen('DictionaryWindow').showMeanings()
        self.manager.get_screen('DictionaryWindow').ids.searchbar.text = ''
        self.manager.get_screen('DictionaryWindow').ids.sortbutton.text = 'Sort Alphabetically'
        self.manager.current = 'DictionaryWindow'
        self.manager.transition.direction = 'right'



class AddWordWindow(Screen):

    def __init__(self, **kwargs):
        super(AddWordWindow, self).__init__(**kwargs)

        self.wordsToAdd = []
        self.meaningsToAdd = []
        self.first_word = True
        self.first_meaning = True

    def repeatWord(self):

        words = [v[0] for v in dataHandler.getDictionary()]
        if self.ids.inputbox.text in words:
            return True

    def notAWord(self):

        inputText = self.ids.inputbox.text.split(' ')

        if not ''.join(inputText).isalpha():
            return True

    def notAMeaning(self):

        inputText = self.ids.inputbox.text.split(' ')

        if not ''.join(inputText).isalpha():
            return True

    def save_word_meaning(self):
        
        dataHandler.addDataToDictionary(self.wordsToAdd[-1], self.meaningsToAdd[-1])

    def addButton(self):

        if self.ids.add_button.text == 'Add Words' and not self.repeatWord() and not self.notAWord():

            if self.first_word:

                self.ids.word_label.text = self.ids.inputbox.text

                self.ids.add_button.text = 'Add Meaning'

                self.first_word = False

                self.wordsToAdd.append(self.ids.inputbox.text)

                self.ids.inputbox.text = ''
            
            else:
                
                self.ids.word_label.text = self.ids.word_label.text + '\n' + self.ids.inputbox.text
                
                self.ids.add_button.text = 'Add Meaning'

                self.wordsToAdd.append(self.ids.inputbox.text)

                self.ids.inputbox.text = ''


        elif self.ids.add_button.text == 'Add Meaning' and not self.notAMeaning():

            if self.first_meaning:

                self.ids.meaning_label.text = self.ids.inputbox.text
                
                self.ids.add_button.text = 'Add Words'

                self.first_meaning = False

                self.meaningsToAdd.append(self.ids.inputbox.text)
                
                self.save_word_meaning()

                self.ids.inputbox.text = ''

            else:

                self.ids.meaning_label.text = self.ids.meaning_label.text + '\n' + self.ids.inputbox.text

                self.ids.add_button.text = 'Add Words'

                self.meaningsToAdd.append(self.ids.inputbox.text)
                
                self.save_word_meaning()

                self.ids.inputbox.text = ''


    def backButton(self):

        self.first_word = True
        self.first_meaning = True
        self.manager.current = 'CommandWindow'
        self.manager.transition.direction = 'right'
        self.ids.add_button.text = 'Add Words'


class DelWordWindow(Screen):

    def wordUnknown(self):

        words_list = [v[0] for v in dataHandler.getDictionary()]
            
        inputText = self.ids.inputbox.text.split(' ')

        if self.ids.inputbox.text not in words_list and ''.join(inputText).isalpha():

            return True

    def showWarning(self):

        inputText = self.ids.inputbox.text.split(' ')
        
        self.ids.DelWordWindow_label.text = 'Word not in Dictionary' if ''.join(inputText).isalpha() else 'Please Type A Valid Word!'


    def delete_word(self):

        inputText = self.ids.inputbox.text.split(' ')
        dataHandler.deleteWord(self.ids.inputbox.text)
        self.ids.DelWordWindow_label.text = 'Successfully Deleted' if ''.join(inputText).isalpha() else 'Please Type A Valid Word!'


class EditWordWindow(Screen):

    def wordUnknown(self):

        words_list = [v[0] for v in dataHandler.getDictionary()]

        inputText = self.ids.editableWord.text.split(' ')

        if self.ids.editableWord.text not in words_list and ''.join(inputText).isalpha():

            return True

    def meaningUnknown(self):

        meanings_list = [v[1] for v in dataHandler.getDictionary()]

        inputText = self.ids.editableWord.text.split(' ')

        if self.ids.editableWord.text not in meanings_list and ''.join(inputText).isalpha():
            return True

    def showWarning(self):

        inputText = self.ids.editableWord.text.split(' ')

        if self.ids.wordedit.state == 'down' or self.ids.meaningedit.state == 'down':

            if self.wordUnknown() and self.ids.wordedit.state == 'down' and ''.join(inputText).isalpha():
                self.ids.EditWordWindow_label.text = 'Word not in Dictionary'

            elif self.meaningUnknown() and self.ids.meaningedit.state == 'down' and ''.join(inputText).isalpha():
                self.ids.EditWordWindow_label.text = 'Meaning not in Dictionary'

            elif not ''.join(inputText).isalpha():
                self.ids.EditWordWindow_label.text = 'Please Type A Valid Word'

        else:
            self.ids.EditWordWindow_label.text = 'Please Select What you want to edit'

    def editSubmit(self):

        meanings = [v[1] for v in dataHandler.getDictionary()]

        if not self.wordUnknown() and ''.join(self.ids.editableWord.text.split(' ')).isalpha() and self.ids.wordedit.state == 'down' :
            self.manager.current = 'ChangeWindow'

        elif not self.meaningUnknown() and ''.join(self.ids.editableWord.text.split(' ')).isalpha() and self.ids.meaningedit.state == 'down':

            if meanings.count(self.ids.editableWord.text) == 1:
                self.manager.current = 'ChangeWindow'
            else:

                self.manager.get_screen('MultiMeaningEdit').btnDic = {}
                self.manager.get_screen('MultiMeaningEdit').createLayout()
                self.manager.current = 'MultiMeaningEdit'

        else:
            self.showWarning()

        self.manager.transition.direction = 'left'
            


class ChangeWindow(Screen):
    
    def changeButton(self):
        
        words = [v[0] for v in dataHandler.getDictionary()]
        meanings = [v[1] for v in dataHandler.getDictionary()]

        editableWord = self.manager.get_screen('EditWordWindow').ids.editableWord.text

        if self.manager.get_screen('EditWordWindow').ids.wordedit.state == 'down':
            dataHandler.changeWord(self.ids.inputbox.text, meanings[words.index(editableWord)])
            self.ids.ChangeWindow_label.text = 'Edit Successfull!'

        elif self.manager.get_screen('EditWordWindow').ids.meaningedit.state == 'down' and meanings.count(self.manager.get_screen('EditWordWindow').ids.editableWord.text) == 1:
            dataHandler.changeMeaning(self.ids.inputbox.text, words[meanings.index(editableWord)])
            self.ids.ChangeWindow_label.text = 'Edit Successfull!'

        else:
            confirmed_word = self.manager.get_screen('MultiMeaningEdit').confirmEdit(self)
            dataHandler.changeMeaning(self.ids.inputbox.text, confirmed_word)
            self.ids.ChangeWindow_label.text = 'Edit Successfull!'


class MultiMeaningEdit(Screen):

    def createLayout(self):

        self.boxlayout = BoxLayout( orientation='vertical',
                                    size_hint=(0.6,0.6),
                                    pos_hint={'x':(0.23),'y':0.25})

        self.label = Label(text='Which One?',
                            size_hint=(1,0.2),
                            font_size=32,
                            color=(0,0,0,1))
        self.boxlayout.add_widget(self.label)

        self.gridlayout = GridLayout(size_hint=(1,0.8))
        self.gridlayout.rows = 0
        self.gridlayout.cols = 1
        self.btnDic = {}

        words = [v[0] for v in dataHandler.getDictionary()]
        meanings = [v[1] for v in dataHandler.getDictionary()]

        meanings_list = [v[1] for v in dataHandler.getDictionary() if v[1] == self.manager.get_screen('EditWordWindow').ids.editableWord.text]

        for v in range(len(meanings_list)):
            self.gridlayout.rows += 1
            index = meanings.index(meanings_list[v])
            self.btn = ToggleButton(text=f'Word : {words[index]}                Meaning : {meanings_list[v]}', font_size=18)
            self.btn.id = f'meaning{v}'
            self.btnDic[self.btn.id] = self.btn
            self.gridlayout.add_widget(self.btn)
            del words[index]
            del meanings[index]

        self.gridlayout2 = GridLayout()
        self.confirm_edit = Button(text='Confirm')
        self.confirm_edit.bind(on_press=self.confirmEdit)
        self.gridlayout2.add_widget(self.confirm_edit)

        self.boxlayout.add_widget(self.gridlayout)
        self.boxlayout.add_widget(self.gridlayout2)
        self.add_widget(self.boxlayout)

    def confirmEdit(self, instance):

        words = [v[0] for v in dataHandler.getDictionary()]
        meanings = [v[1] for v in dataHandler.getDictionary()]

        meanings_list = [v[1] for v in dataHandler.getDictionary() if v[1] == self.manager.get_screen('EditWordWindow').ids.editableWord.text]

        for v in range(len(meanings_list)):

            if self.btnDic[f'meaning{v}'].state == 'down':

                self.manager.current = 'ChangeWindow'
                self.manager.transition.direction = 'right'
                text = self.btnDic[f'meaning{v}'].text
                textList = text.split(':')
                textList.pop()
                textList.remove(textList[0])
                final = ''.join(textList).split('               ')
                final.pop()
                result = ''.join(final).lstrip().rstrip()
                return result


    def backButton(self):

        self.boxlayout.remove_widget(self.gridlayout)
        self.remove_widget(self.boxlayout)
        self.btnDic = {}
        self.manager.current = 'EditWordWindow'
        self.manager.transition.direction = 'right'


class TestCustomizationWindow(Screen):

    def __init__(self, **kwargs):
        super(TestCustomizationWindow, self).__init__(**kwargs)

        self.words_list = []


    def checkWordReq(self):

        self.words_list = [v[0] for v in dataHandler.getDictionary()]

        if len(self.words_list) != 0:
            self.ids.testButton.disabled = False

        else:
            self.ids.testButton.disabled = True

    def questionSelected(self):

        self.ids.tenQuestions.state = 'normal'
        self.ids.fifteenQuestions.state = 'normal'
        self.ids.twentyQuestions.state = 'normal'
        self.ids.allQuestions.state = 'normal'


    def toggleButtons(self):

        if len(self.words_list) < 10:
            self.ids.tenQuestions.disabled = True

        else:
            self.ids.tenQuestions.disabled = False

        if len(self.words_list) < 15:
            self.ids.fifteenQuestions.disabled = True

        else:
            self.ids.fifteenQuestions.disabled = False

        if len(self.words_list) < 20:
            self.ids.twentyQuestions.disabled = True

        else:
            self.ids.twentyQuestions.disabled = False

        if not self.ids.tenQuestions.disabled:
            self.ids.tenQuestions.state = 'down'

        if self.ids.tenQuestions.disabled:
            self.ids.tenQuestions.state = 'normal'
            self.ids.allQuestions.state = 'down'


    def customizedNumber(self):
        
        choosenNumber = 0

        if self.ids.customInput.text == '':
            if self.ids.tenQuestions.state == 'down':
                choosenNumber = 10
            if self.ids.fifteenQuestions.state == 'down':
                choosenNumber = 15
            if self.ids.twentyQuestions.state == 'down':
                choosenNumber = 20
            if self.ids.allQuestions.state == 'down':
                choosenNumber = len(self.words_list)

        else:
            try:
                if self.ids.customInput.text <= len(self.words_list):
                    choosenNumber = int(self.ids.customInput.text)
                else:
                    choosenNumber = len(self.words_list)
            except:
                choosenNumber = len(self.words_list)

        return choosenNumber

    def testStartButton(self):

        self.manager.get_screen('TestWindow').customizedNumber = self.customizedNumber()
        self.manager.get_screen('TestWindow').generateQuestions()
        self.ids.tenQuestions.state = 'normal'
        self.ids.fifteenQuestions.state = 'normal'
        self.ids.twentyQuestions.state = 'normal'
        self.ids.allQuestions.state = 'normal'
        self.ids.customInput.text = ''
        self.manager.current = 'TestWindow'
        self.manager.transition.direction = 'left'

    def customInput(self):

        try:
            
            self.manager.get_screen('TestWindow').customizedNumber = int(self.ids.customInput.text)

        except ValueError:

            popup = Popup(content=Label(text='Please Type A Number!'), size_hint=(dp(.4), dp(.15)), pos_hint={'x': .3, 'top': .9})
            popup.open()

        self.ids.tenQuestions.state = 'normal'
        self.ids.fifteenQuestions.state = 'normal'
        self.ids.twentyQuestions.state = 'normal'
        self.ids.allQuestions.state = 'normal'


    def backButton(self):

        self.manager.current = 'CommandWindow'
        self.manager.transition.direction = 'right'
        self.ids.tenQuestions.state = 'normal'
        self.ids.fifteenQuestions.state = 'normal'
        self.ids.twentyQuestions.state = 'normal'
        self.ids.allQuestions.state = 'normal'
        self.ids.customInput.text = ''


class TestWindow(Screen):

    def __init__(self, **kwargs):
        super(TestWindow, self).__init__(**kwargs)

        self.words = []
        self.meanings = []
        self.questions = []
        self.customizedNumber = 0
        self.count = 0

    def generateQuestions(self):

        self.words = [v[0] for v in dataHandler.getDictionary()]
        self.meanings = [v[1] for v in dataHandler.getDictionary()]

        while len(self.questions) < self.customizedNumber:
            qw = random.choice(self.words + self.meanings)
            if qw not in self.questions:
                if qw in self.words and self.meanings[self.words.index(qw)] not in self.questions:
                    self.questions.append(qw)
                elif qw in self.meanings and self.words[self.meanings.index(qw)] not in self.questions:
                    self.questions.append(qw)

        self.ids.test_question.text = f'What does {self.questions[-1]} mean?'

    def submit(self):
        
        if self.questions[-1] in self.words:

            if self.ids.test_answer.text == self.meanings[self.words.index(self.questions[-1])]:
                self.ids.result.text = 'Correct Answer!'
                self.count += 1
                self.questions.pop()
                self.ids.submit_button.text = 'Next'
            
            elif self.ids.test_answer.text != self.meanings[self.words.index(self.questions[-1])]:
                self.ids.result.text = f'Wrong! The Answer is {self.meanings[self.words.index(self.questions[-1])]}'
                self.questions.pop()
                self.ids.submit_button.text = 'Next'
        
        elif self.questions[-1] in self.meanings:
            
            if self.ids.test_answer.text == self.words[self.meanings.index(self.questions[-1])]:
                self.ids.result.text = 'Correct Answer!'
                self.count += 1
                self.questions.pop()
                self.ids.submit_button.text = 'Next'
            
            elif self.ids.test_answer.text != self.words[self.meanings.index(self.questions[-1])]:
                self.ids.result.text = f'Wrong! The Answer is {self.words[self.meanings.index(self.questions[-1])]}'
                self.questions.pop()
                self.ids.submit_button.text = 'Next'


    def next(self):
        
        try:

            self.ids.test_answer.text = ''
            self.ids.result.text = ''
            self.ids.test_question.text = f'What does {self.questions[-1]} mean?'
            self.ids.submit_button.text = 'Submit'

        except:
            
            self.ids.submit_button.disabled = True
            self.ids.test_question.text = 'Test Completed'
            self.ids.result.text = f'You got total {self.count} points!'
            self.ids.test_answer.text = ''

    def backButton(self):

        self.customizedNumber = 0
        self.count = 0
        self.words = []
        self.meanings = []
        self.questions = []
        self.ids.submit_button.disabled = False
        self.manager.get_screen('TestCustomizationWindow').toggleButtons()
        self.manager.get_screen('TestCustomizationWindow').words_list = []
        self.manager.get_screen('TestCustomizationWindow').checkWordReq()
        self.ids.result.text = ''
        self.ids.submit_button.text = 'Submit'
        self.manager.current = 'TestCustomizationWindow'
        self.manager.transition.direction = 'right'



class SettingsWindow(Screen):
    pass


class AddDictionaryWindow(Screen):

    def dictionaryChanged(self):
        self.manager.get_screen('DictionaryWindow').ids.words.text = self.manager.get_screen('StartWindow').learningLanguage()
        self.manager.get_screen('DictionaryWindow').ids.meanings.text = self.manager.get_screen('StartWindow').primaryLanguage()
        self.manager.get_screen('ViewWindow').ids.words.text = self.manager.get_screen('StartWindow').learningLanguage()
        self.manager.get_screen('ViewWindow').ids.meanings.text = self.manager.get_screen('StartWindow').primaryLanguage()
        self.manager.get_screen('DictionaryWindow').ids.DictionaryWindow_words.text = self.manager.get_screen('DictionaryWindow').showWords()
        self.manager.get_screen('DictionaryWindow').ids.DictionaryWindow_meanings.text = self.manager.get_screen('DictionaryWindow').showMeanings()
        self.manager.get_screen('ViewWindow').ids.ViewWindow_words.text = self.manager.get_screen('DictionaryWindow').showWords()
        self.manager.get_screen('ViewWindow').ids.ViewWindow_meanings.text = self.manager.get_screen('DictionaryWindow').showMeanings()
        self.manager.current = 'DictionaryWindow'
        self.manager.transition.direction = 'up'
        self.manager.get_screen('TranslateWindow').ids.learningLanguage.text = f'Translate To\n    {self.manager.get_screen("StartWindow").learningLanguage()}'
        self.manager.get_screen('TranslateWindow').ids.primaryLanguage.text = f'Translate To\n    {self.manager.get_screen("StartWindow").primaryLanguage()}'
        self.manager.get_screen('AddDictionaryWindow').ids.dictionary1.text = f'{self.manager.get_screen("StartWindow").primaryLanguage()} - {self.manager.get_screen("StartWindow").learningLanguage()} Dictionary'
        if len(dataHandler.checkDictionaries()) > 1:
            if len(dataHandler.checkDictionaries()) == 2:
                self.manager.get_screen('AddDictionaryWindow').ids.dictionary2.text = f'{dataHandler.dictionaryLanguages("dictionary2")[0][0]} - {dataHandler.dictionaryLanguages("dictionary2")[0][1]} Dictionary'
                self.manager.get_screen('AddDictionaryWindow').ids.dictionary3.text = 'CREATE THIRD DICTIONARY'
            elif len(dataHandler.checkDictionaries()) == 3:
                self.manager.get_screen('AddDictionaryWindow').ids.dictionary2.text = f'{dataHandler.dictionaryLanguages("dictionary2")[0][0]} - {dataHandler.dictionaryLanguages("dictionary2")[0][1]} Dictionary'
                self.manager.get_screen('AddDictionaryWindow').ids.dictionary3.text = f'{dataHandler.dictionaryLanguages("dictionary3")[0][0]} - {dataHandler.dictionaryLanguages("dictionary3")[0][1]} Dictionary'
        else:
            self.manager.get_screen('AddDictionaryWindow').ids.dictionary2.text = 'CREATE SECOND DICTIONARY'
            self.manager.get_screen('AddDictionaryWindow').ids.dictionary3.text = 'CREATE THIRD DICTIONARY'

    def toggleButtons(self):

        data = dataHandler.checkCurrentDictionary()

        if data[-1][-1] == 'dictionary1':
            self.ids.dictionary1.state = 'down'
            self.ids.dictionary2.state = 'normal'
            self.ids.dictionary3.state = 'normal'

        elif data[-1][-1] == 'dictionary2':
            self.ids.dictionary2.state = 'down'
            self.ids.dictionary1.state = 'normal'
            self.ids.dictionary3.state = 'normal'

        elif data[-1][-1] == 'dictionary3':
            self.ids.dictionary3.state = 'down'
            self.ids.dictionary1.state = 'normal'
            self.ids.dictionary2.state = 'normal'
        
        try:
            if len(dataHandler.checkDictionaries()) == 3:
                self.ids.createNewDicbtn.disabled = True
        except:
            pass

        self.ids.dictionary1.text = f'{dataHandler.dictionaryLanguages("dictionary1")[0][0]} - {dataHandler.dictionaryLanguages("dictionary1")[0][1]} Dictionary'
        if len(dataHandler.checkDictionaries()) > 1:
            if len(dataHandler.checkDictionaries()) == 2:
                self.ids.dictionary2.text = f'{dataHandler.dictionaryLanguages("dictionary2")[0][0]} - {dataHandler.dictionaryLanguages("dictionary2")[0][1]} Dictionary'
                self.ids.dictionary3.text = 'CREATE THIRD DICTIONARY'
            elif len(dataHandler.checkDictionaries()) == 3:
                self.ids.dictionary2.text = f'{dataHandler.dictionaryLanguages("dictionary2")[0][0]} - {dataHandler.dictionaryLanguages("dictionary2")[0][1]} Dictionary'
                self.ids.dictionary3.text = f'{dataHandler.dictionaryLanguages("dictionary3")[0][0]} - {dataHandler.dictionaryLanguages("dictionary3")[0][1]} Dictionary'
        else:
            self.ids.dictionary2.text = 'CREATE SECOND DICTIONARY'
            self.ids.dictionary3.text = 'CREATE THIRD DICTIONARY'

    def buttonSelected(self):

        self.ids.dictionary1.state = 'normal'
        self.ids.dictionary2.state = 'normal'
        self.ids.dictionary3.state = 'normal'

    def changeDictionary(self, dictionaryName):

        dataHandler.addCurrentDictionary(dictionaryName)

        try:

            self.manager.get_screen('StartWindow').openDictionaryButton(self)

        except:

            self.dictionaryChanged()

    def dictionary1Selected(self):

        self.buttonSelected()
        self.ids.dictionary1.state = 'down'
        self.changeDictionary('dictionary1')

    def dictionary2Selected(self):

        self.buttonSelected()
        self.ids.dictionary2.state = 'down'

        if self.ids.dictionary2.text != 'CREATE SECOND DICTIONARY':
            self.changeDictionary('dictionary2')
        else:
            self.manager.get_screen('CreateNewDicWindow').primary_lang_input.text = ''
            self.manager.get_screen('CreateNewDicWindow').learning_lang_input.text = ''
            self.manager.current = 'CreateNewDicWindow'
            self.manager.transition.direction = 'left'

    def dictionary3Selected(self):

        self.buttonSelected()
        self.ids.dictionary3.state = 'down'

        if self.ids.dictionary3.text != 'CREATE THIRD DICTIONARY':
            self.changeDictionary('dictionary3')
        else:
            self.manager.get_screen('CreateNewDicWindow').primary_lang_input.text = ''
            self.manager.get_screen('CreateNewDicWindow').learning_lang_input.text = ''
            self.manager.current = 'CreateNewDicWindow'
            self.manager.transition.direction = 'left'


class CreateNewDicWindow(Screen):

    def __init__(self, **kwargs):
        super(CreateNewDicWindow, self).__init__(**kwargs)

        self.boxlayout = BoxLayout( orientation='vertical',
                                    size_hint=(0.5,0.8),
                                    pos_hint={'x':(0.5-0.25),'y':0.15})

        self.gridlayout = GridLayout(cols=1, rows=4, size_hint=(1,0.8))
        self.primary_lang_label = Label(text='Type your Primary Language', font_size=32, color=(0,0,0,1))
        self.primary_lang_input = TextInput(multiline=False)
        self.learning_lang_label = Label(text='Type your Learning Language', font_size=32, color=(0,0,0,1))
        self.learning_lang_input = TextInput(multiline=False)

        self.gridlayout.add_widget(self.primary_lang_label)
        self.gridlayout.add_widget(self.primary_lang_input)
        self.gridlayout.add_widget(self.learning_lang_label)
        self.gridlayout.add_widget(self.learning_lang_input)

        self.btn_gridlayout = GridLayout(cols=1, rows=1, size_hint=(1,0.2))
        self.create_button = Button(text='CREATE YOUR NEW PERSONAL DICTIONARY')
        self.create_button.bind(on_press=self.createButton)
        self.btn_gridlayout.add_widget(self.create_button)

        self.boxlayout.add_widget(self.gridlayout)
        self.boxlayout.add_widget(self.btn_gridlayout)
        self.add_widget(self.boxlayout)

    def createButton(self, instance):

        if ''.join(''.join(self.primary_lang_input.text.split(' ')).split('\t')).isalpha() and ''.join(''.join(self.learning_lang_input.text.split(' ')).split('\t')).isalpha():

            if ''.join(''.join(self.primary_lang_input.text.split(' ')).split('\t')).lower() in googletrans.LANGUAGES.values() and ''.join(''.join(self.learning_lang_input.text.split(' ')).split('\t')).lower() in googletrans.LANGUAGES.values():

                if len(dataHandler.checkDictionaries()) == 1:

                    dataHandler.addDictionary('dictionary2')
                    dataHandler.createDictionaryData()
                    dataHandler.addCurrentDictionary('dictionary2')
                    primarylanguage = ''.join(''.join(self.primary_lang_input.text.split(' ')).split('\t'))
                    learninglanguage = ''.join(''.join(self.learning_lang_input.text.split(' ')).split('\t'))
                    dataHandler.addTrackLanguage('dictionary2', primarylanguage, learninglanguage)
                    self.manager.get_screen('DictionaryWindow').ids.words.text = self.manager.get_screen('StartWindow').learningLanguage()
                    self.manager.get_screen('DictionaryWindow').ids.meanings.text = self.manager.get_screen('StartWindow').primaryLanguage()
                    self.manager.get_screen('ViewWindow').ids.words.text = self.manager.get_screen('StartWindow').learningLanguage()
                    self.manager.get_screen('ViewWindow').ids.meanings.text = self.manager.get_screen('StartWindow').primaryLanguage()
                    self.manager.get_screen('TranslateWindow').ids.learningLanguage.text = f'Translate To\n    {self.manager.get_screen("StartWindow").learningLanguage()}'
                    self.manager.get_screen('TranslateWindow').ids.primaryLanguage.text = f'Translate To\n    {self.manager.get_screen("StartWindow").primaryLanguage()}'
                    self.manager.get_screen('AddDictionaryWindow').ids.dictionary2.text = f'{self.manager.get_screen("StartWindow").primaryLanguage()} - {self.manager.get_screen("StartWindow").learningLanguage()} Dictionary'
                    self.manager.get_screen('SettingsWindow').ids.themeButton.state = 'down'
                    self.manager.get_screen('SettingsWindow').ids.dictionaryButton.state = 'normal'
                    self.manager.current = 'SettingsWindow'
                    self.manager.transition.direction = 'right'

                elif len(dataHandler.checkDictionaries()) == 2:

                    dataHandler.addDictionary('dictionary3')
                    dataHandler.createDictionaryData()
                    dataHandler.addCurrentDictionary('dictionary3')
                    primarylanguage = ''.join(''.join(self.primary_lang_input.text.split(' ')).split('\t'))
                    learninglanguage = ''.join(''.join(self.learning_lang_input.text.split(' ')).split('\t'))
                    dataHandler.addTrackLanguage('dictionary3', primarylanguage, learninglanguage)
                    self.manager.get_screen('DictionaryWindow').ids.words.text = self.manager.get_screen("StartWindow").learningLanguage()
                    self.manager.get_screen('DictionaryWindow').ids.meanings.text = self.manager.get_screen("StartWindow").primaryLanguage()
                    self.manager.get_screen('ViewWindow').ids.words.text = self.manager.get_screen("StartWindow").learningLanguage()
                    self.manager.get_screen('ViewWindow').ids.meanings.text = self.manager.get_screen("StartWindow").primaryLanguage()
                    self.manager.get_screen('TranslateWindow').ids.learningLanguage.text = f'Translate To\n    {self.manager.get_screen("StartWindow").learningLanguage()}'
                    self.manager.get_screen('TranslateWindow').ids.primaryLanguage.text = f'Translate To\n    {self.manager.get_screen("StartWindow").primaryLanguage()}'
                    self.manager.get_screen('AddDictionaryWindow').ids.dictionary3.text = f'{self.manager.get_screen("StartWindow").primaryLanguage()} - {self.manager.get_screen("StartWindow").learningLanguage()} Dictionary'
                    self.manager.get_screen('SettingsWindow').ids.themeButton.state = 'down'
                    self.manager.get_screen('SettingsWindow').ids.dictionaryButton.state = 'normal'
                    self.manager.current = 'SettingsWindow'
                    self.manager.transition.direction = 'right'

            else:

                popup = Popup(content=Label(text='Please Type A Valid Language!'), size_hint=(dp(.4), dp(.15)), pos_hint={'x': .3, 'top': .9})
                popup.open()

    def backButton(self):

        self.manager.get_screen('SettingsWindow').ids.themeButton.state = 'down'
        self.manager.get_screen('SettingsWindow').ids.dictionaryButton.state = 'normal'
        self.manager.current = 'AddDictionaryWindow'
        self.manager.transition.direction = 'right'
        self.primary_lang_input.text = ''
        self.learning_lang_input.text = ''


class TranslateWindow(Screen):

    def __init__(self, **kwargs):
        super(TranslateWindow, self).__init__(**kwargs)
        self.hasConnection = True
        self.counter = 0

    def translateWord(self, text):

        self.primary_language = ''
        self.learning_language = ''

        self.counter = 1

        primary_language_input = self.manager.get_screen('StartWindow').primaryLanguage().lower()
        learning_language_input = self.manager.get_screen('StartWindow').learningLanguage().lower()

        for key,value in googletrans.LANGUAGES.items():

            if value == primary_language_input:
                self.primary_language = key

            if value == learning_language_input:
                self.learning_language = key

        try:

            translator = Translator()

            if self.ids.primaryLanguage.state == 'down':

                translated_word = translator.translate(text, src=self.learning_language, dest=self.primary_language)

            else:

                translated_word = translator.translate(text, src=self.primary_language, dest=self.learning_language)

            self.ids.showTranslate.text = translated_word.text
            self.hasConnection = True

        except:

            self.hasConnection = False
            popup = Popup(content=Label(text='Please Check Your Internet Connection!'), size_hint=(dp(.6), dp(.2)), pos_hint={'x': .2, 'top': .9})
            popup.open()

    def repeatWord(self):

        words = [v[0] for v in dataHandler.getDictionary()]

        if self.ids.learningLanguage.state == 'down':
            
            if self.ids.showTranslate.text in words:
                return True

        elif self.ids.primaryLanguage.state == 'down':

            if self.ids.inputbox.text in words:
                return True

        else:
            return False

    def addToDictionary(self, translated_word):

        if self.hasConnection:
        
            inputText = self.ids.inputbox.text.split(' ')

            if self.counter != 0 and ''.join(inputText).isalpha():

                if self.ids.primaryLanguage.state == 'down' and not self.repeatWord():

                    dataHandler.addDataToDictionary(self.ids.inputbox.text, translated_word)
                    self.ids.showTranslate.text = 'Word Successfully Added To Dictionary'

                elif self.ids.learningLanguage.state == 'down' and not self.repeatWord():

                    dataHandler.addDataToDictionary(translated_word, self.ids.inputbox.text)
                    self.ids.showTranslate.text = 'Word Successfully Added To Dictionary'

                else:
                    popup = Popup(content=Label(text='Word Already In Dictionary!'), size_hint=(dp(.6), dp(.2)), pos_hint={'x': .2, 'top': .9})
                    popup.open()


        else:

            popup = Popup(content=Label(text='Word Not Translated!'), size_hint=(dp(.6), dp(.2)), pos_hint={'x': .2, 'top': .9})
            popup.open()


    def backButton(self):

        self.ids.showTranslate.text = 'Translated Words will be shown here'
        self.manager.current = 'CommandWindow'
        self.manager.transition.direction = 'right'
        self.ids.inputbox.text = ''
        self.ids.primaryLanguage.state = 'normal'
        self.ids.learningLanguage.state = 'normal'


kvfile = Builder.load_file('dictionary.kv')


class DictionaryApp(App):
    def build(self):
        return kvfile
        # return AddDictionaryWindow()

DictionaryApp().run()

