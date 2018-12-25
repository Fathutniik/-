from PyQt5.QtWidgets import QApplication, QMainWindow, QMenuBar, QMenu, QAction, QFileDialog
from PyQt5.QtGui import QIcon, QImage, QPainter, QPen
from PyQt5.QtCore import Qt, QPoint
import sys



class Window(QMainWindow): #создаём окно, в котором и будет находиться Paint
    def __init__(self):
        super().__init__()

        top = 400 #задаём размеры окна
        left = 400
        width = 800
        height = 600

        icon = 'icons/paint.png'

        self.setWindowTitle('Paint Application')
        self.setGeometry(top, left, width, height)
        self.setWindowIcon(QIcon(icon))

        self.image = QImage(self.size(), QImage.Format_RGB32)
        self.image.fill(Qt.white)

        self.drawing = False
        self.brushSize = 2
        self.brushColor = Qt.black

        self.lastPoint = QPoint()


        mainMenu = self.menuBar() #создаём кнопки для выбора цвета, размера кисти, сохранения файла и очищения холста
        fileMenu = mainMenu.addMenu('Файл')
        brushMenu = mainMenu.addMenu('Размер')
        brushColor = mainMenu.addMenu('Цвет')


        saveAction = QAction(QIcon('icons/save.png'), 'Сохранить', self)
        saveAction.setShortcut('Ctrl+S')
        fileMenu.addAction(saveAction)
        saveAction.triggered.connect(self.save)

        clearAction = QAction(QIcon('icons/clear.png'), 'Очистить', self)
        clearAction.setShortcut('Ctrl+C')
        fileMenu.addAction(clearAction)
        clearAction.triggered.connect(self.clear)

        threepxAction = QAction(QIcon('icons/threepx.png'), '3px', self)
        threepxAction.setShortcut('Ctrl+T')
        brushMenu.addAction(threepxAction)
        threepxAction.triggered.connect(self.threePx)

        fivepxAction = QAction(QIcon('icons/fivepx.png'), '5px', self)
        fivepxAction.setShortcut('Ctrl+F')
        brushMenu.addAction(fivepxAction)
        fivepxAction.triggered.connect(self.fivePx)

        sevenpxAction = QAction(QIcon('icons/sevenpx.png'), '7px', self)
        sevenpxAction.setShortcut('Ctrl+S')
        brushMenu.addAction(sevenpxAction)
        sevenpxAction.triggered.connect(self.sevenPx)

        ninepxAction = QAction(QIcon('icons/ninepx.png'), '9px', self)
        ninepxAction.setShortcut('Ctrl+N')
        brushMenu.addAction(ninepxAction)
        ninepxAction.triggered.connect(self.ninePx)

        blackAction = QAction(QIcon('icons/black.png'), 'Черный', self)
        blackAction.setShortcut('Ctrl + B')
        brushColor.addAction(blackAction)
        blackAction.triggered.connect(self.blackColor)

        redAction = QAction(QIcon('icons/red.png'), 'Красный', self)
        redAction.setShortcut('Ctrl + W')
        brushColor.addAction(redAction)
        redAction.triggered.connect(self.redColor)

        greenAction = QAction(QIcon('icons/green.png'), 'Зеленый', self)
        greenAction.setShortcut('Ctrl + G')
        brushColor.addAction(greenAction)
        greenAction.triggered.connect(self.greenColor)

        yellowAction = QAction(QIcon('icons/yellow.png'), 'Желтый', self)
        yellowAction.setShortcut('Ctrl + H')
        brushColor.addAction(yellowAction)
        yellowAction.triggered.connect(self.yellowColor)

        whiteAction = QAction(QIcon('icons/white.png'), 'Ластик', self)
        whiteAction.setShortcut('Ctrl + J')
        brushColor.addAction(whiteAction)
        whiteAction.triggered.connect(self.whiteColor)



    def mousePressEvent(self, event): #создаём функции, чтобы рисовать на холсте
        if event.button() == Qt.LeftButton:
            self.drawing = True
            self.lastPoint = event.pos()


    def mouseMoveEvent(self, event):
        if (event.buttons() & Qt.LeftButton) & self.drawing:
            painter = QPainter(self.image)
            painter.setPen(QPen(self.brushColor, self.brushSize, Qt.SolidLine, Qt.RoundCap, Qt.RoundJoin))
            painter.drawLine(self.lastPoint, event.pos())
            self.lastPoint = event.pos()
            self.update()

    def mouseReleaseEvent(self, event):
        if event.button == Qt.LeftButton:
            self.drawing = False



    def paintEvent(self, event):
        canvasPainter = QPainter(self)
        canvasPainter.drawImage(self.rect(), self.image, self.image.rect())



    def save(self): #создаём функцию для сохранения файла в формате PNG
        filePath,_ = QFileDialog.getSaveFileName(self, 'Save Image', '', 'PNG (*.png);;JPEG(*.jpg)')
        if filePath == '':
            return
        self.image.save(filePath)

    def clear(self):
        self.image.fill(Qt.white)
        self.update()

    def threePx(self):
        self.brushSize = 3

    def fivePx(self):
        self.brushSize = 5

    def sevenPx(self):
        self.brushSize = 7

    def ninePx(self):
        self.brushSize = 9

    def blackColor(self):
        self.brushColor = Qt.black

    def redColor(self):
        self.brushColor = Qt.red

    def greenColor(self):
        self.brushColor = Qt.green

    def yellowColor(self):
        self.brushColor = Qt.yellow


    def whiteColor(self):
        self.brushColor = Qt.white

if __name__ == '__main__': #создаём приложение
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    app.exec()


