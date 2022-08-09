# pyda.py

import wolframalpha

input = raw_input("Questions: ")

app_id ="içine app id girilecek"

client = wolframalpha.Client(app_id)

res = client.query(input)

answer = next(res.result).text

print(answer)


________________________________________________________________

import wikipedia

input = raw_input("Q: ")

print wikipedia.summary(input)


tekrarlı sorulara sokmak için

import wikipedia

while True:
	input = raw_input("Q: ")
	print wikipedia.summary(input)

________________________________________________


import wikipedia

while True:
	input = raw_input("Q: ")
	print wikipedia.summary(input, sentences=2)

_____________________________________________________
dil değiştirmek için

import wikipedia

while True:
	input = raw_input("Q: ")
	wikipedia.set_lang("es")  --ispanyolca 
	print wikipedia.summary(input,sentences=2)


_______________________________________________________

Şimdi wolframalpha ile wikipedia birleştirelim

import wikipedia
import wolframalpha

while True:
	input = raw_input("Q: ")
		
	try:
		#wolframalpha
		app_id ="içine app id girilecek"
		client = wolframalpha.Client(app_id)
		res = client.query(input)
		answer = next(res.result).text
		print answer
	except:
		#wikipedia
		print wikipedia.summary(input)


________________________________________________________________


import wx
import wikipedia
import wolframalpha

class MyFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None,
            pos=wx.DefaultPosition, size=wx.Size(450, 100),
            style=wx.MINIMIZE_BOX | wx.SYSTEM_MENU | wx.CAPTION |
             wx.CLOSE_BOX | wx.CLIP_CHILDREN,
            title="PyDa")
        panel = wx.Panel(self)
        my_sizer = wx.BoxSizer(wx.VERTICAL)
        lbl = wx.StaticText(panel,
        label="Hello I am Pyda the Python Digital Assistant. How can I help you?")
        my_sizer.Add(lbl, 0, wx.ALL, 5)
        self.txt = wx.TextCtrl(panel, style=wx.TE_PROCESS_ENTER,size=(400,30))
        self.txt.SetFocus()
        self.txt.Bind(wx.EVT_TEXT_ENTER, self.OnEnter)
        my_sizer.Add(self.txt, 0, wx.ALL, 5)
        panel.SetSizer(my_sizer)
        self.Show()

	
    def OnEnter(self, event):
        input = self.txt.GetValue()
        input = input.lower()
        try:
            #wolframalpha
            app_id = "YOUR APP ID"
            client = wolframalpha.Client(app_id)
            res = client.query(input)
            answer = next(res.results).text
            print answer
        except:
            #wikipedia  who what soruları için alttaki kodu ekledik
	    input = input.split(' ')
	    input = " ".join(input[2:])
            print wikipedia.summary(input)


if __name__ == "__main__":
    app = wx.App(True)
    frame = MyFrame()
    app.MainLoop()


____Sesle çağırmayı ekleyelim_________________________________________


import wx
import wikipedia
import wolframalpha
from espeak import espeak

espeak.synth("Welcome")

class MyFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None,
            pos=wx.DefaultPosition, size=wx.Size(450, 100),
            style=wx.MINIMIZE_BOX | wx.SYSTEM_MENU | wx.CAPTION |
             wx.CLOSE_BOX | wx.CLIP_CHILDREN,
            title="PyDa")
        panel = wx.Panel(self)
        my_sizer = wx.BoxSizer(wx.VERTICAL)
        lbl = wx.StaticText(panel,
        label="Hello I am Pyda the Python Digital Assistant. How can I help you?")
        my_sizer.Add(lbl, 0, wx.ALL, 5)
        self.txt = wx.TextCtrl(panel, style=wx.TE_PROCESS_ENTER,size=(400,30))
        self.txt.SetFocus()
        self.txt.Bind(wx.EVT_TEXT_ENTER, self.OnEnter)
        my_sizer.Add(self.txt, 0, wx.ALL, 5)
        panel.SetSizer(my_sizer)
        self.Show()

	
    def OnEnter(self, event):
        input = self.txt.GetValue()
        input = input.lower()
        try:
            #wolframalpha
            app_id = "YOUR APP ID"
            client = wolframalpha.Client(app_id)
            res = client.query(input)
            answer = next(res.results).text
            print answer
	    espeak.synth("The answer is "+answer)
        except:
            #wikipedia  who what soruları için alttaki kodu ekledik
	    input = input.split(' ')
	    input = " ".join(input[2:])
	    espeak.synth("Searched for "+input)
            print wikipedia.summary(input)


if __name__ == "__main__":
    app = wx.App(True)
    frame = MyFrame()
    app.MainLoop()


________________________________________________________________________________


import wx
import wikipedia
import wolframalpha
#from espeak import espeak
import speech_recognition as sr

#espeak.synth("Welcome")

class MyFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None,
            pos=wx.DefaultPosition, size=wx.Size(450, 100),
            style=wx.MINIMIZE_BOX | wx.SYSTEM_MENU | wx.CAPTION |
             wx.CLOSE_BOX | wx.CLIP_CHILDREN,
            title="PyDa")
        panel = wx.Panel(self)
        my_sizer = wx.BoxSizer(wx.VERTICAL)
        lbl = wx.StaticText(panel,
        label="Hello I am Pyda the Python Digital Assistant. How can I help you?")
        my_sizer.Add(lbl, 0, wx.ALL, 5)
        self.txt = wx.TextCtrl(panel, style=wx.TE_PROCESS_ENTER,size=(400,30))
        self.txt.SetFocus()
        self.txt.Bind(wx.EVT_TEXT_ENTER, self.OnEnter)
        my_sizer.Add(self.txt, 0, wx.ALL, 5)
        panel.SetSizer(my_sizer)
        self.Show()

	
    def OnEnter(self, event):
        input = self.txt.GetValue()
        input = input.lower()
	if input =='':
	    r = sr.Recognizer()
	    with sr.Microphone() as source:
	        audio = r.listen(source)
	    try:
	        self.txt.SetValue(r.recognize_google(audio))
	    except sr.UnknownValueError:    
	        print("Google Speech Recognition could not understand audio")
	    except sr.RequestError as e:
    	        print("Could not request results from Google Speech Recognition service; {0}".format(e))
        else:
	    try:
                #wolframalpha
                app_id = "YOUR APP ID"
                client = wolframalpha.Client(app_id)
                res = client.query(input)
                answer = next(res.results).text
                print answer
	        espeak.synth("The answer is "+answer)
            except:
                #wikipedia  who what soruları için alttaki kodu ekledik
	        input = input.split(' ')
	        input = " ".join(input[2:])
	        espeak.synth("Searched for "+input)
                print wikipedia.summary(input)


if __name__ == "__main__":
    app = wx.App(True)
    frame = MyFrame()
    app.MainLoop()