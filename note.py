
# THIS CODE WAS MADE BY PLEASEGIVEMEFREEFLSTUDIOPLUGIN
#FONT VCR OSD Mono IS ACTUALLY A FONT ON MY COMPUTER , PLEASE CHANGE FILE NAME

















#importing
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QPlainTextEdit,
    QPushButton, QListWidget, QMessageBox
)
from PyQt5.QtGui import QFontDatabase, QFont
from datetime import datetime
import sys
#class
class NoteApp(QWidget):
    def __init__(self):
        #initting info
        super().__init__()
        #caption
        self.setWindowTitle("notepad")
        #size
        self.resize(500, 400)
        #layout
        layout = QVBoxLayout()
        #font
        font_id = QFontDatabase.addApplicationFont(
            "/Users/nguyenphidieu/Downloads/VCR_OSD_MONO_1.001.ttf"
)
        #font setting
        families = QFontDatabase.applicationFontFamilies(font_id)
        #checking if font loaded , else set default
        family = families[0] if (font_id != -1 and families) else "Arial"
        #setting font
        self.setFont(QFont(family, 10))
        #the input shit
        self.editor = QPlainTextEdit()
        #phâhhaha
        self.editor.toPlainText()
        #clear the text at first
        self.editor.clear()
        #button 
        self.button = QPushButton("Save Note")
        #time
        self.time_now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        #connect button to def
        self.button.clicked.connect(self.save_note)
        #list of note
        self.note_list = QListWidget()#list 
        #add widgets to laybout
        layout.addWidget(self.editor)
        layout.addWidget(self.button)
        layout.addWidget(self.note_list)
        self.setLayout(layout)
        #coloring 
        self.setStyleSheet("""
    QWidget {
        background-color: rgb(18, 18, 18);
        color: rgb(255, 255, 255);
        font-size: 14px;
    }

    QPlainTextEdit, QListWidget {
        background-color: rgb(30, 30, 30);
        border: 1px solid rgb(68, 68, 68);
        padding: 4px;
    }

    QPushButton {
        background-color: rgb(45, 45, 45);
        border: 1px solid rgb(85, 85, 85);
        padding: 8px;
        color: rgb(255, 255, 255);
        font-family: "VCR OSD Mono";
    }

    QPushButton:hover {
        background-color: rgb(58, 58, 58);
    }
""")#time importing
        time_now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        #box colro
        self.setFont(QFont(family, 10))  
    #saving the note into list 
    def save_note(self):
        text = self.editor.toPlainText().strip()

        if not text:
            QMessageBox.warning(self, "Error", "Empty note. Try typing something.")
            return
        self.note_list.setFont(QFont("VCR OSD Mono", 10))
        time_now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        note = f"[{time_now}] {text}"
        self.note_list.addItem(note)

        self.editor.clear()
        QMessageBox.information(self, "Saved", "Note saved successfully.")
if __name__ == "__main__":#setup theapp
    app = QApplication(sys.argv)#app
    window = NoteApp()#class
    window.show()#show 
    sys.exit(app.exec_())#exit
     
