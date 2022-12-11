# -*- coding: utf-8 -*-

#############################################################
#                          IMPORTS                          #
#############################################################
# --> GUI
from distutils.debug import DEBUG
from PySide6 import QtCore, QtGui, QtWidgets
from main_ui import Ui_MainWindow
from ui_image_widget import Ui_Form
from ui_preview_widget import Ui_Preview
from qt_material import apply_stylesheet
from crop import Crop_frame
from PIL import Image

# CONSTANTS
import CONSTANT

# --> GLOBAL IMPORTS
import os
import sys
# from shutil import copyfile
from functools import partial

#############################################################
#                           PATH                            #
#############################################################
PATH = os.path.dirname(os.path.abspath(__file__))
os.chdir(PATH)

#############################################################
#                        GUI CLASS                          #
#############################################################

class GUI(QtWidgets.QMainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)

        # UI --> INTERFACE CODE
        ############################################

        # MAIN GUI
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # GLOBAL VARIABLES
        self.previous_sender = None
        self.size_buttons = []
        self.PRINT = {}
        self.global_widgets = {}
        self.path=""
        self.current_index = 0
        self.price = 0.0
        
        ## SET FONT SIZE AND COLORS
        self.setStyleSheet(
            f"font-size : {CONSTANT.FONT_SIZE}px; background-color: {CONSTANT.DARK};")
        self.ui.frame_top.setStyleSheet(
            f"background-color: {CONSTANT.LIGHT_GREY}")
        self.ui.frame_print_size.setStyleSheet(
            f"background-color: {CONSTANT.DARK_GREY}; margin-top: 13px") # Bug correction
        self.ui.frame_images.setStyleSheet(
            f"background-color: {CONSTANT.DARK_GREY}")
        self.ui.frame_buttons.setStyleSheet(
            f"background-color: {CONSTANT.LIGHT_GREY}")
        self.ui.scrollArea_widget.setStyleSheet(
            f"background-color: {CONSTANT.DARK}")
        self.ui.label_top.setStyleSheet(CONSTANT.BUTTON_BLUE)
        self.ui.label_price.setStyleSheet(CONSTANT.BUTTON_BLUE)
        self.ui.label_price.setText("0")

        ## BUTTONS
        ############################################
        self.ui.button_open.setStyleSheet(CONSTANT.BUTTON_PURPLE)
        self.ui.button_open.clicked.connect(self.open_folder)
        self.ui.button_validate.setStyleSheet(CONSTANT.BUTTON_PURPLE)
        self.ui.button_validate.clicked.connect(lambda : self.validate())
        self.ui.button_top_plus.setStyleSheet(CONSTANT.BUTTON_BLUE)
        self.ui.button_top_minus.setStyleSheet(CONSTANT.BUTTON_BLUE)

        ## SCROLLBAR
        self.ui.scrollArea.setStyleSheet("QScrollBar {width: 32px;}")

        ## SHOW --> MAIN WINDOW
        ############################################
        self.show()
        # --> END

    ## --> APP FUNCTIONS
    ############################################
    def print_selection(self, image, which_button, widget):
        result = eval(f"{widget.spinBox.value()} {which_button} 1")
        self.price = round(eval(f"{self.ui.label_price.text()} {which_button} {CONSTANT.SIZES[self.current_size]}"), 2)
        # print(CONSTANT.SIZES[self.current_size])
        
        if result < 0 :
            result = 0

        if self.price < 0.0:
            self.price = 0.0

        self.PRINT[self.current_size][image] = result
        self.ui.label_price.setText(str(self.price))

        ## REFRESH NUMBER OF PRINTS
        widget.spinBox.setValue(self.PRINT[self.current_size][image])
        self.color_widget(widget)


    def set_current_size(self):
        sender = self.sender()
        self.current_size = sender.text()
        sender.setStyleSheet(CONSTANT.BUTTON_GREEN)

        ## BYPASS AT PROGRAM START
        if self.previous_sender is not None:
            self.previous_sender.setStyleSheet(CONSTANT.BUTTON_BLUE)
            
        self.previous_sender = sender

        ## CHANGE THE SPINBOX OF EACH WIDGET TO THE USER SELECTION
        for key, value in self.global_widgets.items() :
            key.spinBox.setValue(self.PRINT[self.current_size][value])
            self.color_widget(key)
        

    def color_widget(self, widget):
        if widget.spinBox.value() > 0:
            widget.frame.setStyleSheet(CONSTANT.FRAME_GREEN)
            widget.spinBox.setStyleSheet(CONSTANT.BUTTON_GREEN)
        else:
            widget.frame.setStyleSheet(CONSTANT.FRAME)
            widget.spinBox.setStyleSheet(CONSTANT.BUTTON_BLUE)
            widget.button_add.setStyleSheet(CONSTANT.BUTTON_BLUE)
            widget.button_remove.setStyleSheet(CONSTANT.BUTTON_BLUE)
    
    
    def open_folder(self):
        ## RESETS THE LAYOUT
        self.global_widgets = {}
        self.previous_sender = None
        self.size_buttons = []
        self.PRINT = {}
        self.current_index = 0
        self.price = 0.0
        self.clear_layout(self.ui.scrollArea_images)
        self.clear_layout(self.ui.print_size_layout)

        ## CREATES SIZE BUTTONS AND LIST OF PRINTS
        ############################################
        self.current_size = list(CONSTANT.SIZES.keys())[0]

        for size in CONSTANT.SIZES.keys():
            button = QtWidgets.QPushButton(size)                
            button.setStyleSheet(CONSTANT.BUTTON_BLUE)
            self.ui.print_size_layout.addWidget(button)
            button.clicked.connect(self.set_current_size) # NO LAMBDA AND NO '()' !!!
            
            ## ADD ALL THE SIZES TO THE PRINT DICTIONNARY
            self.PRINT[size] = {}

            ## ADD ALL SIZE BUTTON TO THE SIZE_BUTTON LIST
            self.size_buttons.append(button)
        
        ## CHOOSE THE FOLDER FROM WHICH THE IMAGES WILL BE DISPLAYED
        dialog = QtWidgets.QFileDialog(None, caption='Choisissez votre dossier')
        dialog.setOption(QtWidgets.QFileDialog.DontUseNativeDialog, True)
        dialog.setDirectory(CONSTANT.ORIGIN)
        dialog.setFileMode(QtWidgets.QFileDialog.Directory)
        dialog.setOption(QtWidgets.QFileDialog.ShowDirsOnly, True)
        dialog.setLabelText(QtWidgets.QFileDialog.Accept, "Valider mon choix")
        if dialog.exec() == QtWidgets.QFileDialog.Accepted:
        ## IMAGES --> UI_IMAGE_WIDGET
        ############################################
            logdir = dialog.directoryUrl().toString()
            logdir = logdir[8:] if os.name == 'nt' else logdir[7:] # GETTING RID OF 'file://'

            self.path = QtCore.QDir.toNativeSeparators(logdir)
            
            ## LOADING ALL IMAGES
            self.images = []
            
            for file in os.listdir(self.path) :
                if file.lower().endswith(CONSTANT.EXTENSION):
                    self.images.append(file)
                    for size in CONSTANT.SIZES :
                        self.PRINT[size][file] = 0
            
            print(f"\n{self.path}")
            print("#" * 64)
            print(f"Nombre d'images : {len(self.images)}")
            self.populate_images()
    
    
    ## POPULATE THE IMAGE SELECTION WIDGETS
    def populate_images(self) :
        self.current_index = 0
        self.price = 0.0

        progress = QtWidgets.QProgressDialog("Merci de patienter", "Annuler ?", 1, len(self.images))
        progress.setWindowTitle("Chargement des fichiers...")
        progress.setWindowModality(QtCore.Qt.WindowModal)
        progress.resize(512, 128)
        # progress.setStyleSheet(CONSTANT.PROGRESS_BAR)
        progress.forceShow()
        
        x_counter = 0
        y_counter = 0
            
        for index, image in enumerate(self.images):
            progress.setValue(index)
            if progress.wasCanceled():
                break
            # QtWidgets.QApplication.processEvents()

            ## INSTANCIATE UI_IMAGE_WIDGET
            image_widget = Ui_Form()
            image_widget.setupUi(self)

            ## WIDGET STYLE
            image_widget.frame.setStyleSheet(CONSTANT.FRAME)
            image_widget.spinBox.setStyleSheet(CONSTANT.BUTTON_BLUE)
            image_widget.button_add.setStyleSheet(CONSTANT.BUTTON_BLUE)
            image_widget.button_remove.setStyleSheet(CONSTANT.BUTTON_BLUE)
            image_widget.button_add.setText("+")
            image_widget.button_remove.setText("-")

            ## PUTS IMAGES IN LABEL
            pixmap = QtGui.QPixmap(f"{self.path}/{image}")
            if pixmap.isNull():
                continue

            scaled_pixmap = pixmap.scaled(
                    CONSTANT.PREVIEW_SIZE, CONSTANT.PREVIEW_SIZE, QtCore.Qt.KeepAspectRatio, QtCore.Qt.SmoothTransformation)
            image_widget.label_image.setPixmap(scaled_pixmap)

            ## SETTING UP THE GRID VIEW
            if x_counter < CONSTANT.MAX_COLUMN:
                x_counter += 1
            else:
                x_counter = 1
                y_counter += 1

            ## ADDS WIDGET TO LAYOUT
            self.ui.scrollArea_images.addWidget(
                image_widget.frame, y_counter, x_counter)
            
            ## SAVE THE USER SELECTION (USED TO SHOW THE CORRECT SELECTION WHEN CHANGING SIZE)
            self.global_widgets[image_widget] = image
            
            ## SETTING UP INDIVIDUAL WIDGET BUTTONS
            image_widget.button_add.clicked.connect(
                lambda image=image, which_button="+", widget=image_widget: self.print_selection(image, which_button, widget))
            image_widget.button_remove.clicked.connect(
                lambda image=image, which_button="-", widget=image_widget: self.print_selection(image, which_button, widget))

            ## SETTING UP TOP BAR BUTTONS
            self.ui.button_top_plus.clicked.connect(
                lambda image=image, which_button="+", widget=image_widget: self.print_selection(image, which_button, widget))

            self.ui.button_top_minus.clicked.connect(
                lambda image=image, which_button="-", widget=image_widget: self.print_selection(image, which_button, widget))
            
            ## CLICK ON IMAGE
            image_widget.label_image.mousePressEvent = partial(self.show_preview, source=image_widget.label_image, index=index)

        progress.setValue(len(self.images))

    
    ## Creates folder if it doesn't exists
    def folder(self, folder):
        if not os.path.exists(folder):
            os.makedirs(folder)
            
            
    def show_preview(self, event, source=None, index=None):
        self.current_index = index
        print(f"\n\nCLICK {source}")
        self.preview = Ui_Preview()
        self.preview.setupUi(self)
        self.preview.setWindowModality(QtCore.Qt.WindowModal)
        # preview.showFullScreen()
        self.preview.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.preview.resize(CONSTANT.RESOLUTION[0], CONSTANT.RESOLUTION[1])
        self.preview.button_close.setStyleSheet(CONSTANT.BUTTON_RED)
        # self.preview.button_next.setStyleSheet(CONSTANT.BUTTON_BLUE)
        # self.preview.button_previous.setStyleSheet(CONSTANT.BUTTON_BLUE)
        
        pixmap = QtGui.QPixmap(f"{self.path}/{self.images[self.current_index]}")
        
        scaled_pixmap = pixmap.scaled(CONSTANT.RESOLUTION[0], CONSTANT.RESOLUTION[1], QtCore.Qt.KeepAspectRatio, QtCore.Qt.SmoothTransformation)
        self.preview.big_image.setPixmap(scaled_pixmap)        
        self.preview.show()
        # self.preview.showFullScreen()

        cp = Crop_frame(self.preview)
        cp.set_start_crop(True)
        cp.show()     
        
        self.preview.button_close.clicked.connect(lambda : self.preview.close())
        # self.preview.button_next.clicked.connect(lambda index = self.current_index, which_button = "+" : self.change_index(index, which_button))
        # self.preview.button_previous.clicked.connect(lambda index = self.current_index, which_button = "-" : self.change_index(index, which_button))
        
        
    def change_index(self, index, which_button) :
        result = eval(f"{index} {which_button} 1")
        if result > len(self.images) + 1 or result < 0 :
            result = 0
            print(result)
         
        self.current_index = result
        
        pixmap = QtGui.QPixmap(f"{self.path}/{self.images[self.current_index]}")
        
        scaled_pixmap = pixmap.scaled(CONSTANT.RESOLUTION[0], CONSTANT.RESOLUTION[1], QtCore.Qt.KeepAspectRatio, QtCore.Qt.SmoothTransformation)
        self.preview.big_image.setPixmap(scaled_pixmap)
                    
    
    def clear_layout(self, layout):
        while layout.count():
            item = layout.takeAt(0)
            widget = item.widget()
            if widget is not None:
                widget.deleteLater()
            # else:
            #     clear_layout(item.layout())
        
        
    def validate(self) :
        self.clear_layout(self.ui.scrollArea_images)
        message = QtWidgets.QMessageBox()
        message.setWindowTitle("MERCI !")
        # message.setText("Veuillez donner ce numero au comptoir")
        # message.setInformativeText(f"<strong>Commande numero {self.numero}</strong>")
        message.setText(" Votre commande est validée !")
        message.resize(1024, 512)
        message.exec()

        print(self.path)
        # self.folder(f"{self.path}\\COMMANDE")
            
        with open(f"{self.path}\\commande.txt", "a") as text:
            for size in self.PRINT :
                # print(size)
                # text.write(f"#########{size}#########\n")
                for key, value in self.PRINT[size].items() :
                    if value > 0:
                        print(f"{size} --> {value}X_{key}")
                        text.write(f"{size} --> {value}X_{key}\n")
                        # self.folder(f"{self.path}\\{size}")
                        # copyfile(f"{self.path}\\{key}",
                        #         f"{self.path}\\{size}\\{value}X_{key}")
            print("#" * 32)
            print(f"{self.price}€\n")
            text.write("#" * 32)
            text.write(f"\n{self.price}€")
            text.write("\n" + "-" * 42 + "\n\n")
        # os.execl(sys.executable, os.path.abspath(__file__)
        # sys.exit(app.exec_())
        # subprocess.call([sys.executable, os.path.realpath(__file__)] + sys.argv[1:])
        self.price = 0.0
        self.ui.label_price.setText(str(self.price))
        

#############################################################
#                           MAIN                            #
#############################################################
if __name__ == "__main__":
    # QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
    app = QtWidgets.QApplication(sys.argv)

    ## SETUP STYLESHEET
    apply_stylesheet(app, theme='dark_blue.xml')

    ui = GUI()
    # ui.setWindowFlags(QtCore.Qt.FramelessWindowHint)
    # ui.showMaximized()
    ui.showFullScreen()
    # ui.resize(CONSTANT.RESOLUTION[0], CONSTANT.RESOLUTION[1])

    sys.exit(app.exec())
