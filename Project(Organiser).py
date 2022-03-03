from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QLineEdit, QComboBox
from PyQt5.QtGui import QFont,QIntValidator,QIcon
from PyQt5.QtCore import QTimer
import googletrans
import requests
import sys

#mainWindow(done)
class window1(QWidget):
    def __init__(self):
        super().__init__()
        self.ui()
    def ui(self):
        self.calc = QPushButton("Калькулятор",self)
        self.calc.resize(200,50)
        self.calc.move(3,70)
        self.calc.clicked.connect(self.cal)

        self.trans = QPushButton("Переводчик", self)
        self.trans.move(3,120)
        self.trans.resize(200, 50)
        self.trans.clicked.connect(self.tran)

        self.tim = QPushButton("Таймер", self)
        self.tim.move(3,170)
        self.tim.resize(200, 50)
        self.tim.clicked.connect(self.ti)

        self.conv = QPushButton("Конвертер",self)
        self.conv.move(3,220)
        self.conv.resize(200,50)
        self.conv.clicked.connect(self.con)

        #label
        self.l = QLabel("ОРГАНАЙЗЕР",self)
        self.l.resize(206,20)
        self.l.move(37,20)
        self.l.setFont(QFont("Century Gothic", 15))
        self.l.show()
        # window
        self.setFixedSize(206, 270)
        self.move(600,250)
        self.setWindowTitle("Organiser")
        self.setWindowIcon(QIcon("OrganiserLogo.png"))
        self.show()

    def cal(self):
        w2.show()
        w1.close()

    def tran(self):
        w3.show()
        w1.close()

    def ti(self):
        w4.show()
        w1.close()

    def con(self):
        w5.show()
        w1.close()

#calc(done)
class window2(QWidget):
    def __init__(self):
        super().__init__()
        self.UI()

    def UI(self):
        #stylesheet(done)
        self.setStyleSheet('''QPushButton{
                                background-color: #DCDCDC;
                                border: 1px solid;
                                border-color: #808080;
                                border-radius: 5px;
                                }
                              QPushButton:hover{
                                background:#D3D3D3;
                                }
                              QPushButton:pressed{
                                background:#C0C0C0;
                                }
                              window2{
                                background: #DCDCDC;
                                }
                              QLineEdit{
                                background: rgb(250,250,250);


        }''')

        #pole
        self.pole = QLineEdit(self)
        self.pole.resize(400, 180)
        self.pole.setReadOnly(True)
        self.pole.setFont(QFont("Arial",30))

        # buttons
        self.bb = QPushButton("<—",self)
        self.bb.resize(30,30)
        self.bb.clicked.connect(self.back)

        self.b1 = QPushButton('1', self)
        self.b1.move(1, 390)
        self.b1.resize(100, 70)
        self.b1.clicked.connect(self.p1)

        self.b2 = QPushButton('2', self)
        self.b2.move(101, 390)
        self.b2.resize(100, 70)
        self.b2.clicked.connect(self.p2)

        self.b3 = QPushButton('3', self)
        self.b3.move(201, 390)
        self.b3.resize(100, 70)
        self.b3.clicked.connect(self.p3)

        self.b4 = QPushButton('4', self)
        self.b4.move(1, 320)
        self.b4.resize(100, 70)
        self.b4.clicked.connect(self.p4)

        self.b5 = QPushButton('5', self)
        self.b5.move(101, 320)
        self.b5.resize(100, 70)
        self.b5.clicked.connect(self.p5)

        self.b6 = QPushButton('6', self)
        self.b6.move(201, 320)
        self.b6.resize(100, 70)
        self.b6.clicked.connect(self.p6)

        self.b7 = QPushButton('7', self)
        self.b7.move(1, 250)
        self.b7.resize(100, 70)
        self.b7.clicked.connect(self.p7)

        self.b8 = QPushButton('8', self)
        self.b8.move(101, 250)
        self.b8.resize(100, 70)
        self.b8.clicked.connect(self.p8)

        self.b9 = QPushButton('9', self)
        self.b9.move(201, 250)
        self.b9.resize(100, 70)
        self.b9.clicked.connect(self.p9)

        self.b0 = QPushButton('0', self)
        self.b0.move(101, 460)
        self.b0.resize(100, 70)
        self.b0.clicked.connect(self.p0)

        self.br = QPushButton('=', self)
        self.br.move(201, 460)
        self.br.resize(100, 70)

        self.br.clicked.connect(self.eq)

        self.bp = QPushButton('+', self)
        self.bp.move(301, 250)
        self.bp.resize(100, 70)
        self.bp.setStyleSheet('''QPushButton{
                              background: #FFFFFF
                            }
                            QPushButton:hover{
                              background: #F5F5F5
                            }
                            QPushButton:pressed{
                              background: #e6e6e6

                }''')
        self.bp.clicked.connect(self.pp)

        self.bm = QPushButton('-', self)
        self.bm.move(301, 320)
        self.bm.resize(100, 70)
        self.bm.setStyleSheet('''QPushButton{
                              background: #FFFFFF
                            }
                            QPushButton:hover{
                              background: #F5F5F5
                            }
                            QPushButton:pressed{
                              background: #e6e6e6

                }''')
        self.bm.clicked.connect(self.pm)

        self.bu = QPushButton('*', self)
        self.bu.move(301, 390)
        self.bu.resize(100, 70)
        self.bu.clicked.connect(self.pu)
        self.bu.setStyleSheet('''QPushButton{
                              background: #FFFFFF
                            }
                            QPushButton:hover{
                              background: #F5F5F5
                            }
                            QPushButton:pressed{
                              background: #e6e6e6

                }''')

        self.bd = QPushButton('/', self)
        self.bd.move(301, 460)
        self.bd.resize(100, 70)
        self.bd.setStyleSheet('''QPushButton{
                              background: #FFFFFF
                            }
                            QPushButton:hover{
                              background: #F5F5F5
                            }
                            QPushButton:pressed{
                              background: #e6e6e6

                }''')
        self.bd.clicked.connect(self.pd)

        self.bdl = QPushButton('Del', self)
        self.bdl.move(301, 180)
        self.bdl.resize(100, 70)
        self.bdl.setStyleSheet('''QPushButton{
                              background: #FFFFFF
                            }
                            QPushButton:hover{
                              background: #F5F5F5
                            }
                            QPushButton:pressed{
                              background: #e6e6e6

                }''')
        self.bdl.clicked.connect(self.ud)

        self.bpn = QPushButton('.',self)
        self.bpn.move(1,460)
        self.bpn.resize(100,70)
        self.bpn.clicked.connect(self.ppn)

        self.bpr = QPushButton('%',self)
        self.bpr.move(201,180)
        self.bpr.resize(100,70)
        self.bpr.setStyleSheet('''QPushButton{
                              background: #FFFFFF
                            }
                            QPushButton:hover{
                              background: #F5F5F5
                            }
                            QPushButton:pressed{
                              background: #e6e6e6

                }''')
        self.bpr.clicked.connect(self.ppr)

        self.bsk1 = QPushButton('(',self)
        self.bsk1.move(1,180)
        self.bsk1.resize(100,70)
        self.bsk1.setStyleSheet('''QPushButton{
                              background: #FFFFFF
                            }
                            QPushButton:hover{
                              background: #F5F5F5
                            }
                            QPushButton:pressed{
                              background: #e6e6e6

                }''')
        self.bsk1.clicked.connect(self.psk1)

        self.bsk2 = QPushButton(')',self)
        self.bsk2.move(101,180)
        self.bsk2.resize(100,70)
        self.bsk2.setStyleSheet('''QPushButton{
                              background: #FFFFFF
                            }
                            QPushButton:hover{
                              background: #F5F5F5
                            }
                            QPushButton:pressed{
                              background: #e6e6e6

                }''')
        self.bsk2.clicked.connect(self.psk2)

        #window
        self.setWindowIcon(QIcon("Calclogo.png"))
        self.setWindowTitle("Calculator")
        self.setFixedSize(402, 530)
        self.move(600, 250)
        self.close()

    def ud(self):
        self.pole.clear()

    def psk1(self):
        self.pole.insert('(')

    def psk2(self):
        self.pole.insert(')')

    def ppr(self):
        self.pole.insert('%')

    def ppn(self):
        self.pole.insert('.')

    def p1(self):
        self.pole.insert('1')

    def p2(self):
        self.pole.insert('2')

    def p3(self):
        self.pole.insert('3')

    def p4(self):
        self.pole.insert('4')

    def p5(self):
        self.pole.insert('5')

    def p6(self):
        self.pole.insert('6')

    def p7(self):
        self.pole.insert('7')

    def p8(self):
        self.pole.insert('8')

    def p9(self):
        self.pole.insert('9')

    def p0(self):
        self.pole.insert('0')

    def pp(self):
        self.pole.insert(' + ')

    def pm(self):
        self.pole.insert(' - ')

    def pu(self):
        self.pole.insert(' * ')

    def pd(self):
        self.pole.insert(' / ')

    def eq(self):
        t = self.pole.text()
        answ = str(eval(t))
        self.pole.setText(answ)

    def back(self):
        w2.close()
        w1.show()

#translator(done)
class window3(QWidget):
    def __init__(self):
        super().__init__()
        self.translator = googletrans.Translator()
        self.UI()

    def UI(self):
        # comboboxes
        self.combo1 = QComboBox(self)
        self.s = googletrans.LANGUAGES
        self.combo1.addItems(self.s.values())
        self.combo1.resize(90, 25)
        self.combo1.setStyleSheet('''QComboBox{
                                       color: #FFFFF0;
                                       border-radius: 0px;
                                       border:2px solid #00A5BB;
                                       background:#00B9D3;
        }''')
        self.combo1.move(200, 35)

        self.combo2 = QComboBox(self)
        self.combo2.addItems(self.s.values())
        self.combo2.resize(90, 25)
        self.combo2.setStyleSheet('''QComboBox{
                                       color: #FFFFF0;
                                       border-radius: 0px;
                                       border:2px solid #00A5BB;
                                       background:#00B9D3
        }''')
        self.combo2.move(200, 70)

        # lines
        self.l1 = QLineEdit(self)
        self.l1.move(5, 35)
        self.l1.resize(190, 25)

        self.l2 = QLineEdit(self)
        self.l2.move(5, 70)
        self.l2.resize(190, 25)

        # buttons
        self.b = QPushButton("Перевести", self)
        self.b.move(110, 102)
        self.b.resize(60, 20)
        self.b.setStyleSheet('''QPushButton{
                                  background: #00B9D3;
                                  color: #FFFFF0;
                                  border:2px solid #00A5BB;
                                  font: 11px ;
                                  }
                                QPushButton:hover{
                                  background: #00C7E3;
                                  }
                                QPushButton:pressed{
                                  background: #00B3CB;



        }''')
        self.b.clicked.connect(self.trans)

        self.bb = QPushButton("<—",self)
        self.bb.resize(30,30)
        self.bb.clicked.connect(self.back)

        #window
        self.setFixedSize(300, 130)
        self.move(600,250)
        self.setWindowIcon(QIcon("translatelogo.png"))
        self.setWindowTitle("Translator")
        self.close()

    def back(self):
        w3.close()
        w1.show()

    def trans(self):
        n = self.combo1.currentText()
        d = self.combo2.currentText()

        for i in self.s:
            if n == self.s[i]:
                sr = i
        for i in self.s:
            if d == self.s[i]:
                ds = i

        w = self.l1.text()
        r = self.translator.translate(w, src=sr, dest=ds).text
        self.l2.setText(r)
        
#timer(done)
class window4(QWidget):
    def __init__(self):
        super().__init__()
        self.timer = QTimer()
        self.starT = False
        self.UI()
        self.nUpdate()

    def UI(self):
        #buttons
        self.start = QPushButton("Старт",self)
        self.start.resize(100,40)
        self.start.move(90,150)
        self.start.clicked.connect(self.starting)
        self.start.show()

        self.pause = QPushButton("Пауза",self)
        self.pause.resize(100,40)
        self.pause.move(200,150)
        self.pause.clicked.connect(self.pausing)
        self.pause.show()

        self.bb = QPushButton("<—",self)
        self.bb.resize(30,30)
        self.bb.clicked.connect(self.back)

        #validator
        self.val =QIntValidator()

        #lables
        self.h = QLabel("h = ", self)
        self.h.move(60,90)
        self.h.resize(20,15)
        self.h.show()

        self.m = QLabel("m = ", self)
        self.m.move(160,90)
        self.m.resize(20,15)
        self.m.show()

        self.s = QLabel("s = ", self)
        self.s.move(260,90)
        self.s.resize(20,15)
        self.s.show()

        #pola
        self.hw = QLineEdit(self)
        self.hw.move(80,90)
        self.hw.resize(50,15)
        self.hw.setValidator(self.val)

        self.mw = QLineEdit(self)
        self.mw.move(180,90)
        self.mw.resize(50,15)
        self.mw.setValidator(self.val)

        self.sw = QLineEdit(self)
        self.sw.move(280,90)
        self.sw.resize(50,15)
        self.sw.setValidator(self.val)

        #window
        self.move(600,250)
        self.setWindowIcon(QIcon("timerlogo.png"))
        self.setFixedSize(400,200)
        self.setWindowTitle("Timer")
        self.close()

    def starting(self):
        self.starT = True
        self.hw.setReadOnly(True)
        self.mw.setReadOnly(True)
        self.sw.setReadOnly(True)

    def pausing(self):
        self.starT = False
        self.hw.setReadOnly(False)
        self.mw.setReadOnly(False)
        self.sw.setReadOnly(False)

    def back(self):
        w4.close()
        w1.show()


    def nUpdate(self):
        if self.starT == True:
            if self.hw.text() == "":
                h = 0
                self.hw.setText("00")
            else:
                    h = int(self.hw.text())
            if self.mw.text() == "":
                m = 0
                self.mw.setText("00")
            else:
                m = int(self.mw.text())
            if self.sw.text() == "":
                s = 0
                self.sw.setText("00")
            else:
                s = int(self.sw.text())

            if  s > 0:
                s -= 1
                if s < 10:
                    self.sw.setText("0" + str(s))
                else:
                    self.sw.setText(str(s))

            elif s == 0 and m > 0:
                s = 59
                m -= 1
                if m < 10:
                    self.mw.setText(str(m))
                else:
                    self.sw.setText("0" + str(m))
                self.sw.setText(str(s))

            elif s == 0 and m == 0 and h > 0:
                s = 59
                m = 59
                h -= 1
                if h < 10:
                    self.hw.setText("0" + str(h))
                else:
                    self.hw.setText(str(h))

                self.mw.setText(str(m))
                self.sw.setText(str(s))
            else:
                self.starT = False
                self.hw.setReadOnly(False)
                self.mw.setReadOnly(False)
                self.sw.setReadOnly(False)
                QMessageBox.information(self, "ZA WARUDO", "Time has stopped working.")
        self.timer.singleShot(1000, self.nUpdate)

#converter(done)
class window5(QWidget):
    def __init__(self):
        super().__init__()
        link = "https://www.cbr-xml-daily.ru/daily_json.js"
        data = requests.get(link)

        self.forexUS = float(data.json()['Valute']['USD']['Value'])
        self.forexEU = float(data.json()['Valute']['EUR']['Value'])
        self.forexBY = float(data.json()['Valute']['BYN']['Value'])
        self.ui()

    def ui(self):
        #buttons
        self.bb = QPushButton("<—",self)
        self.bb.resize(30,30)
        self.bb.clicked.connect(self.back)

        self.bc = QPushButton("Конвертировать", self)
        self.bc.resize(100,20)
        self.bc.setStyleSheet('''QPushButton{
                                   color: #FFFFF0;
                                   border-radius: 0px;
                                   border:2px solid #D76C00;
                                   background:#FF8000;
                                   }
                                 QPushButton:hover{
                                   color: #FFFFF0;
                                   border-radius: 0px;
                                   border:2px solid #D76C00;
                                   background:#FF9123;
                                   }
        }''')
        self.bc.clicked.connect(self.calculation)
        self.bc.move(100,120)

        # comboboxes
        self.combo1 = QComboBox(self)
        self.combo1.resize(90, 25)
        self.s = ['EUR','USD',"BYN",'RUB']
        self.combo1.addItems(self.s)
        self.combo1.setStyleSheet('''QComboBox{
                                               color: #FFFFF0;
                                               border-radius: 0px;
                                               border:2px solid #D76C00;
                                               background:#FF8000;
                }''')
        self.combo1.move(200, 35)

        self.combo2 = QComboBox(self)
        self.combo2.resize(90, 25)
        self.combo2.addItems(self.s)
        self.combo2.setStyleSheet('''QComboBox{
                                               color: #FFFFF0;
                                               border-radius: 0px;
                                               border:2px solid #D76C00;
                                               background:#FF8000
                }''')
        self.combo2.move(200, 70)

        # lines
        self.l1 = QLineEdit(self)
        self.l1.move(5, 35)
        self.l1.resize(190, 25)

        self.l2 = QLineEdit(self)
        self.l2.move(5, 70)
        self.l2.resize(190, 25)

        #window
        self.setWindowTitle("Converter")
        self.setWindowIcon(QIcon("converterlogo.png"))
        self.move(600,250)
        self.setFixedSize(300,150)
        self.close()

    def back(self):
        w5.close()
        w1.show()

    def calculation(self):
        #EURO
        if self.combo1.currentText() == "EUR" and self.combo2.currentText() == "BYN" :
            self.l2.setText(str(round(self.forexEU / self.forexBY // 0.001 / 1000 * float(self.l1.text()), 2)))

        elif self.combo1.currentText() == "EUR" and self.combo2.currentText() == "USD":
            self.l2.setText(str(round(self.forexEU / self.forexUS // 0.001 / 1000 * float(self.l1.text()), 2)))

        elif self.combo1.currentText() == "EUR" and self.combo2.currentText() == "RUB":
            self.l2.setText(str(round(self.forexEU / 1 // 0.001 / 1000 * float(self.l1.text()), 2)))

        elif self.combo1.currentText() == "EUR" and self.combo2.currentText() == "EUR":
            self.l2.setText(self.l1.text())

        #DOLLAR
        elif self.combo1.currentText() == "USD" and self.combo2.currentText() == "BYN" :
            self.l2.setText(str(round(self.forexUS / self.forexBY // 0.001 / 1000 * float(self.l1.text()), 2)))

        elif self.combo1.currentText() == "USD" and self.combo2.currentText() == "USD":
            self.l2.setText(self.l1.text())

        elif self.combo1.currentText() == "USD" and self.combo2.currentText() == "RUB":
            self.l2.setText(str(round(self.forexUS / 1 // 0.001 / 1000 * float(self.l1.text()), 2)))

        elif self.combo1.currentText() == "USD" and self.combo2.currentText() == "EUR":
            self.l2.setText(str(round(self.forexUS / self.forexEU // 0.001 / 1000 * float(self.l1.text()), 2)))

        #BELRUBLE
        elif self.combo1.currentText() == "BYN" and self.combo2.currentText() == "BYN" :
            self.l2.setText(self.l1.text())

        elif self.combo1.currentText() == "BYN" and self.combo2.currentText() == "USD":
            self.l2.setText(str(round(self.forexBY / self.forexUS // 0.001 / 1000 * float(self.l1.text()), 2)))

        elif self.combo1.currentText() == "BYN" and self.combo2.currentText() == "RUB":
            self.l2.setText(str(round(self.forexBY / 1 // 0.001 / 1000 * float(self.l1.text()), 2)))

        elif self.combo1.currentText() == "BYN" and self.combo2.currentText() == "EUR":
            self.l2.setText(str(round(self.forexBY / self.forexEU // 0.001 / 1000 * float(self.l1.text()), 2)))

        #RUSRUBLE
        elif self.combo1.currentText() == "RUB" and self.combo2.currentText() == "BYN" :
            self.l2.setText(str(round(1 / self.forexBY // 0.001 / 1000 * float(self.l1.text()), 2)))

        elif self.combo1.currentText() == "RUB" and self.combo2.currentText() == "USD":
            self.l2.setText(str(round(1 / self.forexUS // 0.001 / 1000 * float(self.l1.text()), 2)))

        elif self.combo1.currentText() == "RUB" and self.combo2.currentText() == "RUB":
            self.l2.setText(self.l1.text())

        elif self.combo1.currentText() == "RUB" and self.combo2.currentText() == "EUR":
            self.l2.setText(str(round(1 / self.forexEU // 0.001 / 1000 * float(self.l1.text()), 2)))

program = QApplication(sys.argv)
w1 = window1()
w2 = window2()
w3 = window3()
w4 = window4()
w5 = window5()

sys.exit(program.exec_())