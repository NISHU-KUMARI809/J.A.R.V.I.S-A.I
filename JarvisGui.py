import sys
from subprocess import call
from jarvis import Ui_Form
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtCore import *
from PyQt5.QtGui import QMovie
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt, QTime, QTime, QDate
from PyQt5.uic import loadUiType
import main
import os
import webbrowser as web
import datetime
import sys
import pywhatkit as pwt

class MainThread(QThread):
    def __init__(self):
        super(MainThread,self).__init__()
    def run(self):
        call(["python","main.py"])

startExe = MainThread()
class Gui_Start(QMainWindow):
    def __init__(self):
        super().__init__()
        self.gui=Ui_Form()
        self.gui.setupUi(self)
        self.gui.pushButton.clicked.connect(self.startTask)
        self.gui.pushButton_3.clicked.connect(self.close)

        self.gui.Youtube_button.clicked.connect(self.youtube_app)
        # self.gui.Whatshapp_3.clicked.connect(self.spotify_app)
        self.gui.Whatshapp.clicked.connect(self.whatsapp_app)
        self.gui.Chrome_button.clicked.connect(self.chrome_app)
        # self.gui.Whatshapp_4.clicked.connect(self.Alarm)
        # self.gui.Whatshapp_2.clicked.connect(self.Wikipedia)
        # self.gui.Whatshapp_5.clicked.connect(self.Book_pdf)
        # self.gui.Whatshapp_6.clicked.connect(self.Maps)
        # self.gui.Whatshapp_7.clicked.connect(self.Language_Translator)
    def chrome_app(self):
        os.startfile("chrome app")
    def youtube_app(self):
        main.say("What do you want to search Sir")
        text = main.takeCommand()
        main.say("Opening Youtube sir")
        pwt.playonyt(text)
    def whatsapp_app(self):
        main.whatsapp()
    

    def startTask(self):
        self.gui.label1=QtGui.QMovie("UI//gifloader.gif")
        self.gui.gif1.setMovie(self.gui.label1)
        self.gui.label1.start()

        self.gui.label2 = QtGui.QMovie("UI//f1.gif")
        self.gui.gif2.setMovie(self.gui.label2)
        self.gui.label2.start()

        self.gui.label3 = QtGui.QMovie("UI//Iron_Template_1.gif")
        self.gui.gif3.setMovie(self.gui.label3)
        self.gui.label3.start()

        self.gui.label4 = QtGui.QMovie("UI//live (1).gif")
        self.gui.gif4.setMovie(self.gui.label4)
        self.gui.label4.start()

        self.gui.label5 = QtGui.QMovie("UI//Jrvis.gif")
        self.gui.label_2.setMovie(self.gui.label5)
        self.gui.label5.start()

        timer =QTimer(self)
        timer.timeout.connect(self.showTimeLive)
        timer.start(999)
        startExe.start()
    def showTimeLive(self):
        t_ime =QTime.currentTime()
        time=t_ime.toString()
        d_ate =QDate.currentDate()
        date=d_ate.toString()
        label_Time="Time :"+time
        label_Date="Date :"+date
        self.gui.Text_Time.setText(label_Time)
        self.gui.text_Date.setText(label_Date)



GuiApp = QApplication(sys.argv)
jarvis_gui = Gui_Start()
jarvis_gui.show()
exit(GuiApp.exec_())














