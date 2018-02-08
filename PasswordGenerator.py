import base64
import os
from os import system
import itertools
import random
import wx

class App(wx.App):

    def OnInit(self):
        frame = MainFrame()
        frame.Center()
        frame.Show()
        self.SetTopWindow(frame)
        return True


class MainFrame(wx.Frame): # Main Frame

    title = "Password Generator V2.0"

    def __init__(self):
        wx.Frame.__init__(self, None, 1, self.title, size=(340,200),style=wx.SYSTEM_MENU | wx.CAPTION | wx.CLOSE_BOX)
  
        panel=wx.Panel(self)
        self.button1 = wx.Button(panel,label="Password Generator", pos=(30,50),size=(120,30))
        self.button1.Bind(wx.EVT_BUTTON, self.OnGenerate)
        self.button2 = wx.Button(panel,label="Password Decoder", pos=(180,50),size=(120,30))
        self.button2.Bind(wx.EVT_BUTTON, self.OnDecode)

    def OnQuit(self, event):
        App.Close()

    def OnGenerate(self, event):
        GenerateFrame().Show()

    def OnDecode(self, event):
        DecodeFrame().Show()

class GenerateFrame(wx.Frame): # Generate Frame

    title = "Password Generator"

    def __init__(self):
        wx.Frame.__init__(self, wx.GetApp().TopWindow, title=self.title, style=wx.SYSTEM_MENU | wx.CAPTION | wx.CLOSE_BOX, size=(500,250))
        self.Center()
        panel=wx.Panel(self)
        textbox1 = wx.TextCtrl(panel, pos=(10,10),size=(210,-1))
        textbox1.AppendText("Special Characters: Yes or No")
        textbox2 = wx.TextCtrl(panel, pos=(10,40),size=(210,-1))
        textbox2.AppendText("Use For Password:YouTube, etc")
        textbox3 = wx.TextCtrl(panel, pos=(10,70),size=(210,-1))
        textbox3.AppendText("Username/Email With Pass")
        textbox4 = wx.TextCtrl(panel, pos=(10,100),size=(210,-1))
        textbox4.AppendText("Length of Pass")
        textbox5 = wx.TextCtrl(panel, pos=(10,130),size=(210,-1), style=wx.TE_READONLY)
        def savin(event):
            self.dirname = ''
            dlg = wx.FileDialog(self, "Add to a file...", self.dirname, ".txt", "*.txt*", \
                                wx.OPEN, pos=self.Center())
            if dlg.ShowModal() == wx.ID_OK:
                itcontains = textbox2.GetValue() + ":\n" + textbox3.GetValue() + " = Username\n" + textbox5.GetValue() + " = Password\n"

                filename=dlg.GetFilename()
                dirname=dlg.GetDirectory()
                filehandle=open(os.path.join(dirname, filename), 'a+')
                filehandle.write(itcontains)
                filehandle.close()
            dlg.Destroy()

        def replacin(event):
            self.dirname = ''
            dlg = wx.FileDialog(self, "Create a file...", self.dirname, ".txt", "*.txt*", \
                                wx.SAVE | wx.OVERWRITE_PROMPT, pos=self.Center())
            if dlg.ShowModal() == wx.ID_OK:
                itcontains = textbox2.GetValue() + ":\n" + textbox3.GetValue() + " = Username\n" + textbox5.GetValue() + " = Password\n"

                filename=dlg.GetFilename()
                dirname=dlg.GetDirectory()
                filehandle=open(os.path.join(dirname, filename), 'w+')
                filehandle.write(itcontains)
                filehandle.close()
            dlg.Destroy()
        def generate(event):
            s = textbox1.GetValue()
            if s=="yes" or s=="Yes" or s=="yES" or s=="yeS" or s=="yEs":
        
                # What the password will be used for
                p = textbox2.GetValue()

                # The username/email the password will go with
                a = textbox3.GetValue()

                # The Length of the password
                q = textbox4.GetValue()
                
                # Randomly fenerate a password
                m = os.urandom(int(q))
                l = base64.b64encode(m)
                o = l.encode()
                j = base64.b64encode(o)
                t = j.encode()
                y = base64.b64encode(t)
                x = y.encode()
                h = base64.b64encode(x)
                r = h.encode()
                i = base64.b64encode(r)
                textbox5.AppendText("")
                textbox5.AppendText(i)
        
            elif s=="No" or s=="no" or s=="NO" or s=="nO":
                
                # What the password will be used for
                v = textbox2.GetValue()

                # The username/email the password will go with
                a = textbox3.GetValue()

                # The Length of the password
                q = textbox4.GetValue()

                # The characters to choose from
                stuff = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
                         "A","B",'C',"D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V",'W',"X","Y","Z",
                         '1','2','3','4','5','6','7','8','9','0','L','a']
                chars = ''.join(stuff)

                # Randomly choose a character
                f = ''.join(random.choice(stuff) for x in xrange(int(q)))
                l = base64.b64encode(f)
                o = l.encode()
                j = base64.b64encode(o)
                t = j.encode()
                y = base64.b64encode(t)
                x = y.encode()
                h = base64.b64encode(x)
                r = h.encode()
                i = base64.b64encode(r)
                textbox5.AppendText("")
                textbox5.AppendText(i)
              

        button1=wx.Button(panel, label="Generate!", pos=(10,160),size=(120,30))
        self.Bind(wx.EVT_BUTTON, generate, button1)
        button2=wx.Button(panel, label="Add To File!", pos=(150,160),size=(120,30))
        self.Bind(wx.EVT_BUTTON, savin, button2)
        button3=wx.Button(panel, label="Replace File!", pos=(290,160),size=(120,30))
        self.Bind(wx.EVT_BUTTON, replacin, button3)
                
                    

    def closewindow(self, event):
        self.Destroy()

class DecodeFrame(wx.Frame): # Decoder Frame

    title = "Password Decoder"

    def __init__(self):
        wx.Frame.__init__(self, wx.GetApp().TopWindow, title=self.title, style=wx.SYSTEM_MENU | wx.CAPTION | wx.CLOSE_BOX, size=(450,140))
        self.Center()
        panel=wx.Panel(self)
        textbox1 = wx.TextCtrl(panel, pos=(10,10),size=(210,-1))
        textbox1.AppendText("Type in Encrypted Password")
        def savin(event):
            self.dirname = ''
            dlg = wx.FileDialog(self, "Add to a file...", self.dirname, ".txt", "*.txt*", \
                                wx.OPEN, pos=self.Center())
            if dlg.ShowModal() == wx.ID_OK:
                itcontains = textbox2.GetValue() + ":\n" + textbox3.GetValue() + " = Username\n" + textbox5.GetValue() + " = Password\n"

                filename=dlg.GetFilename()
                dirname=dlg.GetDirectory()
                filehandle=open(os.path.join(dirname, filename), 'a+')
                filehandle.write(itcontains)
                filehandle.close()
            dlg.Destroy()

        def replacin(event):
            self.dirname = ''
            dlg = wx.FileDialog(self, "Create a file...", self.dirname, ".txt", "*.txt*", \
                                wx.SAVE | wx.OVERWRITE_PROMPT, pos=self.Center())
            if dlg.ShowModal() == wx.ID_OK:
                itcontains = textbox2.GetValue() + ":\n" + textbox3.GetValue() + " = Username\n" + textbox5.GetValue() + " = Password\n"

                filename=dlg.GetFilename()
                dirname=dlg.GetDirectory()
                filehandle=open(os.path.join(dirname, filename), 'w+')
                filehandle.write(itcontains)
                filehandle.close()
            dlg.Destroy()
            
        def decode(event):
            l = base64.b64decode(textbox1.GetValue())
            o = l.decode()
            j = base64.b64decode(o)
            t = j.decode()
            y = base64.b64decode(t)
            x = y.decode()
            h = base64.b64decode(x)
            r = h.decode()
            i = base64.b64decode(r)
            print "Password: " + i           
        button1=wx.Button(panel, label="Decode!", pos=(10,40),size=(120,30))
        self.Bind(wx.EVT_BUTTON, decode, button1)
                
                
    def closewindow(self, event):
        self.Destroy()


if __name__=='__main__':
    app = App(False)
    app.MainLoop()
