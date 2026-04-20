#FONT Files are on my computer , PLEASE CHANGE LOCATION OF FONT FILE 




















from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QPlainTextEdit,
    QPushButton, QListWidget, QMessageBox, QCheckBox, QDialog
)
from PyQt5.QtGui import QFontDatabase, QFont
from PyQt5.QtCore import QSettings
from datetime import datetime
import sys


# --- SETTINGS DIALOG ---
class SettingsDialog(QDialog):
    def __init__(self, current_value, parent=None):
        super().__init__(parent)

        self.setWindowTitle("Settings")
        layout = QVBoxLayout()

        self.checkbox_time = QCheckBox("Always include time")
        self.checkbox_time.setChecked(current_value)
        layout.addWidget(self.checkbox_time)

        save_btn = QPushButton("Save")
        save_btn.clicked.connect(self.accept)
        layout.addWidget(save_btn)

        self.setLayout(layout)


# --- MAIN APP ---
class NoteApp(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Notepad")
        self.resize(500, 400)

        layout = QVBoxLayout()

        # --- SETTINGS STORAGE ---
        self.settings = QSettings("MyApp", "Notes")
        self.always_include_time = self.settings.value("always_time", False, type=bool)

        # --- FONT (KEPT) ---
        font_id = QFontDatabase.addApplicationFont(
            "/Users/nguyenphidieu/Downloads/VCR_OSD_MONO_1.001.ttf"
        )
        families = QFontDatabase.applicationFontFamilies(font_id)
        self.family = families[0] if (font_id != -1 and families) else "Arial"
        self.setFont(QFont(self.family, 10))
        
        # --- WIDGETS ---
        self.editor = QPlainTextEdit()
        self.button = QPushButton("Save Note")
        self.note_list = QListWidget()
        self.settings_btn = QPushButton("Settings")
        self.note_list.setFont(QFont(self.family, 10))
        layout.addWidget(self.editor)
        layout.addWidget(self.button)
        layout.addWidget(self.note_list)
        layout.addWidget(self.settings_btn)

        self.setLayout(layout)

        # --- CONNECT ---
        self.button.clicked.connect(self.save_note)
        self.settings_btn.clicked.connect(self.open_settings)

        # --- STYLE (FIXED CSS) ---
        self.setStyleSheet("""
            QWidget {
                background-color: rgb(0,0,0);
                color: rgb(255, 255, 255);
                font-size: 14px;
            }

            QPlainTextEdit, QListWidget {
                background-color: rgb(30, 30, 30);
                border: 1px solid rgb(68, 68, 68);
                padding: 4px;
            }

            QCheckBox {
                color: rgb(255,255,255);
                font-family: "VCR OSD Mono";
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
        """)

    # --- OPEN SETTINGS ---
    def open_settings(self):
        dialog = SettingsDialog(self.always_include_time, self)

        if dialog.exec_():
            self.always_include_time = dialog.checkbox_time.isChecked()

            # SAVE TO DISK (this is what you were missing)
            self.settings.setValue("always_time", self.always_include_time)

    # --- SAVE NOTE ---
    def save_note(self):
        text = self.editor.toPlainText().strip()

        if not text:
            QMessageBox.critical(self, "Error", "Please enter some text before saving.")
            return

        time_now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        if self.always_include_time:
            note = f"[{time_now}] {text}"
        else:
            note = text

        self.note_list.addItem(note)
        self.editor.clear()

        QMessageBox.information(self, "Saved", "Note saved successfully!")


# --- RUN APP ---
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = NoteApp()
    window.show()
    sys.exit(app.exec_())
