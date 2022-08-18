from PyQt5.QtWidgets import QLabel, QPushButton, QApplication, QWidget, QMessageBox, QFrame, QLineEdit
from PyQt5.QtCore import Qt
from PyQt5 import QtWidgets
import sys
import random as r

class Game_2048(QWidget):
    def __init__(self):
        super().__init__()
        self.start()

    def start(self):
        self.setFixedSize(910, 606)
        self.setStyleSheet("font: 15pt \"Roboto\";background-color: white;color:black;background-color:lightblue;")
        self.setWindowTitle("2048 GAME")

        self.arrow_stl = "background-color:rgb(108, 108, 189);border-radius:10px;border:2px solid black;"

        self.Btn_1 = QPushButton(self)
        self.Btn_2 = QPushButton(self)
        self.Btn_3 = QPushButton(self)
        self.Btn_4 = QPushButton(self)
        self.Btn_5 = QPushButton(self)
        self.Btn_6 = QPushButton(self)
        self.Btn_7 = QPushButton(self)
        self.Btn_8 = QPushButton(self)
        self.Btn_9 = QPushButton(self)
        self.Btn_10 = QPushButton(self)
        self.Btn_11 = QPushButton(self)
        self.Btn_12 = QPushButton(self)
        self.Btn_13 = QPushButton(self)
        self.Btn_14 = QPushButton(self)
        self.Btn_15 = QPushButton(self)
        self.Btn_16 = QPushButton(self)
        self.Btn_17 = QPushButton(self)
        self.Btn_18 = QPushButton(self)
        self.Btn_19 = QPushButton(self)
        self.Btn_20 = QPushButton(self)
        self.Btn_21 = QPushButton(self)
        self.Btn_22 = QPushButton(self)
        self.Btn_23 = QPushButton(self)
        self.Btn_24 = QPushButton(self)
        self.Btn_25 = QPushButton(self)
        self.Up = QPushButton(self)
        self.Down = QPushButton(self)
        self.Right = QPushButton(self)
        self.Left = QPushButton(self)
        self.New_game = QPushButton(self)
        self.Records_show = QLabel(self)
        self.label = QLabel(self)
        self.label_2 = QLabel(self)
        self.Ball_l = QLabel(self)
        self.Ball_show = QLabel(self)
        self.line = QFrame(self)
        self.line_2 = QFrame(self)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)

        self.Btn_1.setGeometry(0, 10, 131, 111)
        self.Btn_2.setGeometry(140, 10, 131, 111)
        self.Btn_3.setGeometry(280, 10, 131, 111)
        self.Btn_4.setGeometry(420, 10, 131, 111)
        self.Btn_5.setGeometry(560, 10, 131, 111)
        self.Btn_6.setGeometry(0, 130, 131, 111)
        self.Btn_7.setGeometry(140, 130, 131, 111)
        self.Btn_8.setGeometry(280, 130, 131, 111)
        self.Btn_9.setGeometry(420, 130, 131, 111)
        self.Btn_10.setGeometry(560, 130, 131, 111)
        self.Btn_11.setGeometry(0, 250, 131, 111)
        self.Btn_12.setGeometry(140, 250, 131, 111)
        self.Btn_13.setGeometry(280, 250, 131, 111)
        self.Btn_14.setGeometry(420, 250, 131, 111)
        self.Btn_15.setGeometry(560, 250, 131, 111)
        self.Btn_16.setGeometry(0, 370, 131, 111)
        self.Btn_17.setGeometry(140, 370, 131, 111)
        self.Btn_18.setGeometry(280, 370, 131, 111)
        self.Btn_19.setGeometry(420, 370, 131, 111)
        self.Btn_20.setGeometry(560, 370, 131, 111)
        self.Btn_21.setGeometry(0, 490, 131, 111)
        self.Btn_22.setGeometry(140, 490, 131, 111)
        self.Btn_23.setGeometry(280, 490, 131, 111)
        self.Btn_24.setGeometry(420, 490, 131, 111)
        self.Btn_25.setGeometry(560, 490, 131, 111)
        self.label.setGeometry(710, 255, 191, 131)
        self.label_2.setGeometry(710, 130, 201, 25)
        self.line.setGeometry(690, 0, 20, 611)
        self.line_2.setGeometry(700, 100, 301, 16)
        self.Ball_l.setGeometry(700, 0, 211, 20)
        self.Ball_show.setGeometry(710, 29, 191, 61)
        self.Records_show.setGeometry(710, 160, 191, 81)
        self.New_game.setGeometry(710, 400, 191, 41)
        self.Up.setGeometry(775, 460, 60, 60)
        self.Left.setGeometry(710, 530, 60, 60)
        self.Down.setGeometry(775, 530, 60, 60)
        self.Right.setGeometry(840, 530, 60, 60)

        self.New_game.setStyleSheet("background-color:#333;color:white;border-radius:10px;border:1px solid #fff;")
        self.line.setStyleSheet("border-color: rgb(0, 0, 0);")
        self.label.setStyleSheet("font-size:15px;background-color:#999;background-color: yellow;border-radius:15px;border:1px solid #333;")
        self.Ball_show.setStyleSheet("border-radius:15px;border:1px solid #333;background-color:silver;")
        self.Records_show.setStyleSheet("border-radius:15px;border:1px solid #333;background-color:gold;")

        self.New_game.setText("New Game")
        self.label.setText("<center></center>")
        self.label_2.setText("<center><b>GOLDEN SCORE<b></center>")
        self.Records_show.setText("73132$")
        self.Ball_l.setText("<center><b>YOUR CASH</b></center>")
        self.Ball_show.setText("<center><b>0$</b></center>")
        self.Up.setStyleSheet(self.arrow_stl)
        self.Down.setStyleSheet(self.arrow_stl)
        self.Right.setStyleSheet(self.arrow_stl)
        self.Left.setStyleSheet(self.arrow_stl)
        self.score = 0
    
        self.btns = [[self.Btn_1, self.Btn_2, self.Btn_3, self.Btn_4, self.Btn_5],
                     [self.Btn_6, self.Btn_7, self.Btn_8, self.Btn_9, self.Btn_10],
                     [self.Btn_11, self.Btn_12, self.Btn_13, self.Btn_14, self.Btn_15], 
                     [self.Btn_16, self.Btn_17, self.Btn_18, self.Btn_19, self.Btn_20],
                     [self.Btn_21, self.Btn_22, self.Btn_23, self.Btn_24, self.Btn_25]
                    ]
        self.btn_clr = {' ':'white', '2':'orange', '4':'yellow', '8':'green', '16':'blue', '32':'purple', '64':'brown', '128':'rgb(0, 10, 104)', '256':'rgb(104, 0, 73)',
                        '512':'pink', '1024':'red', '2048':'aqua', '4096':'rgb(81, 100, 70)', '8192':'rgb(0, 0, 0)', '16384':'rgb(255, 0, 179)', '32768': 'rgb(0, 199, 106)',
                        '65536':'rgb(147, 255, 205)', '131072':'rgb(58, 52, 0)', '262144': 'rgb(32, 32, 58)', '524288':'rgb(26, 61, 50)', '1048576':'rgb(76, 0, 78)', 
                        '2097152':'rgba(46, 145, 0, 0.562)', '4194304':'rgba(96, 168, 153, 0.562)', '8388608':'#436860', '16777216':'#a18c00', '33554432':'#010431', '67108864':'#242215'}
        
        self.newGame()
        self.Up.setText('W ↑')
        self.Down.setText('S ↓')
        self.Right.setText('D →')
        self.Left.setText('← A')

        lst = r.choice(self.btns)
        btn = r.choice(lst)
        btn.setText('2')
        self.set_bgc()
        self.write_records()

        self.Up.setShortcut('w')
        self.Down.setShortcut('s')
        self.Right.setShortcut('d')
        self.Left.setShortcut('a')

        self.Up.clicked.connect(lambda: self.Play(self.Up))
        self.Down.clicked.connect(lambda: self.Play(self.Down))
        self.Right.clicked.connect(lambda: self.Play(self.Right))
        self.Left.clicked.connect(lambda: self.Play(self.Left))

        self.New_game.clicked.connect(self.newGame)


        self.sanoq = 0
        self.key = 'wwwasd'
        self.admin_key = ''

    def Play(self, btn):
        if btn == self.Up:
            self.admin_key += 'w'
            self.up(btn)
        elif btn == self.Down:
            self.admin_key += 's'
            self.down(btn)
        elif btn == self.Right:
            self.admin_key += 'd'
            self.right(btn)
        elif btn == self.Left:
            self.admin_key += 'a'
            self.left(btn)
            
        self.set_bgc()
        self.choose_num()
        self.Game_Over()
        
        if self.key in self.admin_key:
            self.Admin()

    def up(self, btn):
        for i in range(1, len(self.btns)):
            for j in range(len(self.btns)):
                if self.sanoq == 0 and self.btns[i][j].text() != ' ' and self.btns[i][j].text() == self.btns[i-1][j].text():
                    self.sanoq += 1
                    score = str(int(self.btns[i][j].text()) + int(self.btns[i-1][j].text()))
                    self.score += int(score)
                    self.btns[i-1][j].setText(score)
                    self.btns[i][j].setText(' ')
                    
                if self.btns[i][j].text() != ' ' and self.btns[i-1][j].text() == ' ':
                    self.btns[i-1][j].setText(self.btns[i][j].text())
                    self.btns[i][j].setText(' ')
                    self.up(btn)
        self.sanoq = 0
        self.Ball_show.setText(f"<center><b>{self.score} $</b></center>")

    def down(self, btn):
        for i in range(len(self.btns)-1):
            for j in range(len(self.btns)):
                if self.sanoq == 0 and self.btns[i][j].text() != ' ' and self.btns[i][j].text() == self.btns[i+1][j].text():
                    self.sanoq += 1
                    score = str(int(self.btns[i][j].text()) + int(self.btns[i+1][j].text()))
                    self.score += int(score)
                    self.btns[i+1][j].setText(score)
                    self.btns[i][j].setText(' ')

                if self.btns[i][j].text() != ' ' and self.btns[i+1][j].text() == ' ':
                    self.btns[i+1][j].setText(self.btns[i][j].text())
                    self.btns[i][j].setText(' ')
                    self.down(btn)
        self.sanoq = 0
        self.Ball_show.setText(f"<center><b>{self.score} $</b></center>")


    def right(self, btn):
        for i in range(len(self.btns)):
            for j in range(len(self.btns)-1):
                if self.sanoq == 0 and self.btns[i][j].text() != ' ' and self.btns[i][j].text() == self.btns[i][j+1].text():
                    self.sanoq += 1
                    score = str(int(self.btns[i][j].text()) + int(self.btns[i][j+1].text()))
                    self.score += int(score)
                    self.btns[i][j+1].setText(score)
                    self.btns[i][j].setText(' ')
                
                if self.btns[i][j].text() != ' ' and self.btns[i][j+1].text() == ' ':
                    self.btns[i][j+1].setText(self.btns[i][j].text())
                    self.btns[i][j].setText(' ')
                    self.right(btn)
        self.sanoq = 0
        self.Ball_show.setText(f"<center><b>{self.score} $</b></center>")

        
    def left(self, btn):
        for i in range(len(self.btns)):
            for j in range(1, len(self.btns)):
                if self.sanoq == 0 and self.btns[i][j].text() != ' ' and self.btns[i][j].text() == self.btns[i][j-1].text():
                    self.sanoq += 1
                    score = str(int(self.btns[i][j].text()) + int(self.btns[i][j-1].text()))
                    self.score += int(score)
                    self.btns[i][j-1].setText(score)
                    self.btns[i][j].setText(' ')

                if self.btns[i][j].text() != ' ' and self.btns[i][j-1].text() == ' ':
                    self.btns[i][j-1].setText(self.btns[i][j].text())
                    self.btns[i][j].setText(' ')
                    self.left(btn)
        self.sanoq = 0
        self.Ball_show.setText(f"<center><b>{self.score} $</b></center>")

        

    def set_bgc(self):
        for i in self.btns:
            for j in i:
                if j.text() in self.btn_clr:
                    self.btn_stl(j, self.btn_clr[j.text()])
                

    def btn_stl(self, btn, color='white'):
        col = '#fff'
        if color == 'yellow' or color == 'orange' or color == 'aqua' or color == 'rgb(147, 255, 205)'or color == 'pink':
            col = '#000'         
        btn.setStyleSheet(f"color:{col};font-size:25px;border-radius:15px;border:3px solid black;background-color:{color};margin:3px;")

    def choose_num(self):
        a = 0
        for i in self.btns:
            for j in i:
                if j.text() == ' ':
                    a += 1
        while a != 0:
            lst = r.choice(self.btns)
            btn = r.choice(lst)
            if btn.text() == ' ':
                btn.setText('2')
                self.set_bgc()
                return

    def newGame(self):
        for i in self.btns:
            for j in i:
                j.setText(' ')
                self.btn_stl(j)
        self.admin_key = ''
        self.score = 0
        self.Ball_show.setText(f"<center>{self.score} $</center>")
        self.choose_num()

    def Game_Over(self):
        a = 0
        for i in range(len(self.btns)-1):
            for j in range(len(self.btns)-1):
                if self.btns[i][j].text() == self.btns[i][j+1].text() or self.btns[i][j].text() == self.btns[i+1][j].text():
                    a += 1
        if a == 0:
            self.maximum = self.Find_Max() 
            clr_max = self.btn_clr[f'{self.maximum}']
            self.msg = QMessageBox(self)
            self.msg.setGeometry(500, 300, 800, 500)
            self.msg.setWindowTitle("GAME OVER")
            
            self.name_msg = QLineEdit(self.msg)
            self.name_msg.setGeometry(5, 230, 410, 50)
            self.name_msg.setStyleSheet('background-color:lightblue;border-radius:20px;border:2px solid black;color:blue;')
            self.name_msg.setPlaceholderText("Ismingizni kiriting...")
            self.name_msg.setAlignment(Qt.AlignCenter)

            self.ok = QPushButton("DONE", self.msg)
            self.ok.setGeometry(5, 320, 410, 50)
            self.ok.setStyleSheet('background-color:blue;border-radius:15px;border:2px solid black;color:white;')
            self.ok.clicked.connect(lambda: self.Done(self.name_msg))

            self.msg.setText(f"<center><h1>BARAKALLA !!!</h1><h3>MAX : {self.maximum} </h3><h3>Sizning to'plagan jami pullaringiz ... </h3><h1>{self.score} $</h1><br><br><center>")
            self.msg.show()
        self.write_records()
            


    def Admin(self):
        nums = [[2, 4, 8, 16, 64],
                [128, 256, 512, 1024, 2048], 
                [4096, 8192, 16384, 32768, 65536],
                [131072, 262144, 524288, 1048576, 2097152],
                [4194304, 8388608, 16777216, 33554432, 67108864]]
        for i in range(len(self.btns)):
            for j in range(len(self.btns)):
                self.btns[i][j].setText(str(nums[i][j]))
        self.set_bgc()
        self.Game_Over()

    def Find_Max(self):
        lst = []
        for i in range(len(self.btns)):
            for j in range(len(self.btns)):
                lst.append(int(self.btns[i][j].text()))
        return max(lst)

    def Done(self, name):
        name = name.text().strip()
        if name != '':
            with open('users.txt', 'r+') as f:
                if len(f.read().split()) == 0:
                    f.write(f"{name} {self.score} {self.maximum}")
                else:
                    f.write(f"\n{name} {self.score} {self.maximum}")
            self.newGame()
            self.msg.hide()
        else:
            self.ok.setStyleSheet('background-color:red;border-radius:15px;border:2px solid black;color:white;')
            self.name_msg.setStyleSheet('background-color:lightblue;border-radius:20px;border:2px solid black;color:red;')
        self.write_records()

    def write_records(self):
        with open('users.txt', 'r+') as f:
            txt = f.read().split('\n')
            if txt != ['']:
                best_score = []
                for i in range(len(txt)):
                    best_score.append(int(txt[i].split()[1]))
                a = 5 if len(txt) > 5 else len(txt)
                label_txt = ''
                for i in range(a):
                    label_txt += f" {i+1}) {txt[i].split(' ')[0].capitalize()} -- {txt[i].split(' ')[2]}<br>"
                self.label.setText(f"<br><b>{label_txt}<b>")
                self.Records_show.setText(f"<center><b>{max(best_score)} $</b></center>")

app = QApplication(sys.argv)
window = Game_2048()
window.show()
sys.exit(app.exec_())
