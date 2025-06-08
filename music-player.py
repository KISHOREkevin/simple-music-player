
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import os

from PyQt5.QtMultimedia import QMediaContent, QMediaPlayer, QMediaPlaylist

class Ui_MainWindow(object):
    def __init__(self):
        self.playList=[]
        self.mediaplayer=QMediaPlayer()  
        self.mediaplaylist=QMediaPlaylist()
        self.mediaplayer.setPlaylist(self.mediaplaylist)
        self.mediaplayer.positionChanged.connect(self.setSliderPosition)
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(754, 523)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setStyleSheet("background-color:#1e1e2e;")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")

        self.fileBrowseBtn = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.fileBrowseBtn.setFont(font)
        self.fileBrowseBtn.setObjectName("fileBrowseBtn") 
        self.fileBrowseBtn.setStyleSheet("QPushButton{background-color: #45475a;color:white;outline:none;border:none;padding:5px;border-radius:5px} QPushButton::pressed{background-color:#7f849c;color:white;}")
        self.verticalLayout.addWidget(self.fileBrowseBtn)
        self.fileBrowseBtn.clicked.connect(self.filePicker)
       
        self.musicslist = QtWidgets.QListWidget(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.musicslist.setFont(font)
        self.musicslist.setObjectName("musicslist")
        self.musicslist.setStyleSheet("QListWidget{background-color:#45475a;color:white;margin:20px;padding:10px;border-radius:10px} QListWidget::item{padding:10px;border:none;margin:2px;} QListWidget::item:selected{background-color:#89b4fa;color:#1e1e2e;border-radius:10px;}")
        self.verticalLayout.addWidget(self.musicslist)
        self.musicslist.itemDoubleClicked.connect(self.singleSong)

        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        
        self.songInfo = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.songInfo.setFont(font)
        self.songInfo.setStyleSheet("background-color : #45475a;\n"
"padding: 10px;\n""border-radius: 5px;\n""color:white;")
        self.songInfo.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.songInfo.setObjectName("songInfo")
        self.verticalLayout_2.addWidget(self.songInfo)
        
        self.songSlider = QtWidgets.QSlider(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(17)
        self.songSlider.setFont(font)
        self.songSlider.setStyleSheet("QSlider{padding:20px 0px ;} QSlider::groove:horizontal{background-color:#89b4fa;height:2px;} QSlider::handle:horizontal{background: #89b4fa;width: 15px;height: 10px;margin: -5px 0; border-radius:20px;} QSlider::add-page:horizontal{ border: 1px solid #1e1e2e;background: #1e1e2e;height: 2px;border-radius: 4px;}")
        self.songSlider.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.songSlider.setObjectName("songSlider")
        self.verticalLayout_2.addWidget(self.songSlider)
        self.songSlider.setRange(0,0)
        self.songSlider.sliderMoved.connect(self.setSlider)
        

        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")

        self.prevBtn = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.prevBtn.setFont(font)
        self.prevBtn.setStyleSheet("QPushButton{background-color: #89b4fa;color:black;outline:none;border:none;padding:5px;border-radius:5px;} QPushButton::pressed{background-color:#1e1e2e;color:#89b4fa;}")
        self.prevBtn.setObjectName("prevBtn") 
        self.horizontalLayout.addWidget(self.prevBtn)
        self.prevBtn.clicked.connect(self.prevMusic)

        self.playBtn = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.playBtn.setFont(font)
        self.playBtn.setStyleSheet("QPushButton{background-color: #89b4fa;color:black;outline:none;border:none;padding:5px;border-radius:5px;} QPushButton::pressed{background-color:#1e1e2e;color:#89b4fa;}")
        self.playBtn.setObjectName("playBtn")
        self.horizontalLayout.addWidget(self.playBtn)
        self.playBtn.clicked.connect(self.playMusic)

        self.stopBtn = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.stopBtn.setFont(font)
        self.stopBtn.setStyleSheet("QPushButton{background-color: #89b4fa;color:black;outline:none;border:none;padding:5px;border-radius:5px;} QPushButton::pressed{background-color:#1e1e2e;color:#89b4fa;}")
        self.stopBtn.setObjectName("stopBtn")
        self.horizontalLayout.addWidget(self.stopBtn)
        self.stopBtn.clicked.connect(self.stopMusic)
        
        self.nextBtn = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.nextBtn.setFont(font)
        self.nextBtn.setStyleSheet("QPushButton{background-color: #89b4fa;color:black;outline:none;border:none;padding:5px;border-radius:5px;} QPushButton::pressed{background-color:#1e1e2e;color:#89b4fa;}")
        self.nextBtn.setObjectName("nextBtn")
        self.horizontalLayout.addWidget(self.nextBtn)
        self.nextBtn.clicked.connect(self.nextMusic)

        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.verticalLayout.addLayout(self.verticalLayout_2)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.playSingleSong()


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.fileBrowseBtn.setText(_translate("MainWindow", "⎙  Browse"))
        self.songInfo.setText(_translate("MainWindow", "No Song Loaded"))
        self.prevBtn.setText(_translate("MainWindow", "   ⏮   "))
        self.playBtn.setText(_translate("MainWindow", "   ▶   "))
        self.stopBtn.setText(_translate("MainWindow", "   ⏹   "))
        self.nextBtn.setText(_translate("MainWindow", "   ⏭   "))
        
    def singleSong(self,item):
        index = self.musicslist.row(item)
        self.mediaplaylist.setCurrentIndex(index)
        self.setSongInfo()
        self.playBtn.setText("   ⏸   ")
        self.mediaplayer.play()

    def setSlider(self,position):
        self.songSlider.setRange(0,self.mediaplayer.duration())
        self.mediaplayer.setPosition(position)
        self.songSlider.setValue(position)
    
    def setSliderPosition(self,position):
        self.songSlider.setRange(0,self.mediaplayer.duration())
        self.songSlider.setValue(position)

    def setSongInfo(self):
        self.songInfo.setText(os.path.basename(self.playList[self.mediaplaylist.currentIndex()]))
        
    def playMusic(self):
        if self.mediaplaylist.mediaCount() == 0:
            self.songInfo.setText("Select song to play")
        else:
            self.setSongInfo() 
            if self.mediaplayer.state() == 1:
                self.playBtn.setText("   ▶   ")
                self.mediaplayer.pause()
            else:
                self.playBtn.setText("   ⏸   ")
                self.mediaplayer.play()
         
    
        
    def prevMusic(self):
        if self.mediaplaylist.mediaCount() == 0:
            self.songInfo.setText("Select song to play")
        else: 
            current_index=self.mediaplaylist.currentIndex()
            if current_index > 0:
                self.mediaplaylist.setCurrentIndex(current_index-1)
                self.setSongInfo()
            else:
                self.mediaplaylist.setCurrentIndex(self.mediaplaylist.mediaCount() - 1 )
                self.setSongInfo()

    def nextMusic(self):
        if self.mediaplaylist.mediaCount() == 0:
            self.songInfo.setText("Select song to play")
        else:
            current_index=self.mediaplaylist.currentIndex()
            if current_index < (self.mediaplaylist.mediaCount()-1):
                self.mediaplaylist.setCurrentIndex(current_index+1)
                self.setSongInfo()
            else:
                self.mediaplaylist.setCurrentIndex(0)
                self.setSongInfo() 

    
    def stopMusic(self):
        if self.mediaplaylist.mediaCount() == 0:
            self.songInfo.setText("Select song to play")
        else:
            self.mediaplayer.stop()
            if self.mediaplayer.state() == 0:
                self.playBtn.setText("   ▶   ")

    def filePicker(self):
        file_dialog=QtWidgets.QFileDialog()
        file_dialog.setFileMode(QtWidgets.QFileDialog.ExistingFiles)
        file_dialog.setNameFilter("Audio Files (*.mp3 *.wav *.ogg *.flac);;All Files (*)")
        if file_dialog.exec_():
            self.playList.clear()
            self.musicslist.clear()
            self.mediaplaylist.clear()
            self.mediaplayer.stop()
            selectedFiles = file_dialog.selectedFiles()
            for file_path in selectedFiles:
                if os.path.exists(file_path):
                    self.playList.append(file_path)
                    self.musicslist.addItem("♫     "+ os.path.basename(file_path))
                    self.mediaplaylist.addMedia(QMediaContent(QtCore.QUrl.fromLocalFile(file_path)))
        self.mediaplaylist.setCurrentIndex(0)
        self.songInfo.setText("Song Loaded Lets play")
       

    def playSingleSong(self):
        if len(sys.argv) > 1 :
            if os.path.exists(sys.argv[1]):
                if sys.argv[1].find(os.path.expanduser("~")) == 0 :
                    file=sys.argv[1]
                else :
                    file = os.path.abspath(sys.argv[1])
                self.mediaplaylist.clear()
                self.playList.clear()
                self.playList.append(file)
                self.mediaplaylist.addMedia(QMediaContent(QtCore.QUrl.fromLocalFile(file)))
                self.mediaplaylist.setCurrentIndex(0)
                self.setSongInfo()
                self.playBtn.setText("   ⏸   ")
                self.musicslist.addItem("♫     "+ os.path.basename(file))
                self.mediaplayer.play() 
            else:
                print("File not exists")
                sys.exit()
            
            
                        

    
if __name__ == "__main__":
    app=QtWidgets.QApplication(sys.argv)
    mainWindow=QtWidgets.QMainWindow()
    ui=Ui_MainWindow()
    ui.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())

