#importing modules
from tkinter import *
from translate import Translator
# initializing window
Screen = Tk()
Screen.geometry('1080x400')
Screen.config(bg = 'ghost white')
Screen.title("Language Translator")

InputLanguageChoice = StringVar()
TranslateLanguageChoice = StringVar()

#tuple for choosing languages
LanguageChoices = {'Hindi','English','French','German','Spanish'}
InputLanguageChoice.set('English')
TranslateLanguageChoice.set('Hindi')

def Translate():
    translator = Translator(from_lang= InputLanguageChoice.get(),to_lang=TranslateLanguageChoice.get())
    Translation = translator.translate(TextVar.get())
    OutputVar.set(Translation)

#choice for input language
InputLanguageChoiceMenu = OptionMenu(Screen,InputLanguageChoice,*LanguageChoices)
title_lbl = Label(Screen,text="LANGAUGE TRANSLATOR", font=("sans serif",18,"bold","italic"))
title_lbl.place(relx=0.5,rely=0.1,anchor=CENTER)
InputLanguageChoiceMenu.place(relx=0.14,rely=0.4,anchor=CENTER)
InputLanguageChoiceMenu.config(width=20)


#choice in which the language is to be translated
NewLanguageChoiceMenu = OptionMenu(Screen,TranslateLanguageChoice,*LanguageChoices)
Label(Screen,text="Translated Language", font=("sans serif",12,"bold","italic")).place(relx=0.8,rely=0.8,anchor=CENTER)
NewLanguageChoiceMenu.place(relx=0.64,rely=0.4,anchor=CENTER)
NewLanguageChoiceMenu.config(width=20)



Label(Screen,text="Enter Text",font=("sans serif",10,"bold","italic")).place(relx=0.09,rely=0.3,anchor=CENTER)
TextVar = StringVar()
TextBox = Entry(Screen,textvariable=TextVar,width = 60, bg="#FFFCF9", bd=4).place(relx=0.25,rely=0.6,anchor=CENTER,height=100)


Label(Screen,text="Output Text",font=("sans serif",10,"bold","italic")).place(relx=0.59,rely=0.3,anchor=CENTER)
OutputVar = StringVar()
TextBox = Entry(Screen,textvariable=OutputVar,width = 60, bg="#FFFCF9", bd=4).place(relx=0.75,rely=0.6,anchor=CENTER,height=100)

#Button for calling function
B = Button(Screen,text="Translate",command=Translate, relief = GROOVE,font=("sans serif",18,"bold","italic")).place(relx=0.5,rely=0.9,anchor=CENTER)

mainloop()
