import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class CALC_GUI(QWidget):
    
    data = '0'
    base_option = 'DEC'
    #number = ''
    result = '0'
    prev_op = '+'
    
    def __init__(self):
        super(CALC_GUI,self).__init__()
        
        self.setFixedSize(400,500)
        self.setWindowTitle("Calculator")
        
        self.main_layout = QVBoxLayout(self)
        self.v_layout = QVBoxLayout()
        self.v_layout.setAlignment(Qt.AlignCenter)
        
        self.main_layout.setAlignment(Qt.AlignCenter)
        self.main_layout.addLayout(self.v_layout)
        
        self.main_layout.addStretch()
        
        self.display()
        
        self.setLayout(self.main_layout)
        self.setContentsMargins(10,260,10,10)
        self.show()
    
    def display(self):
        self.display_layout = QGridLayout()
        
        self.header = QLabel("Programmer Calculator", self)
        self.header.setGeometry(25,0,200,30)
        self.header.setFont(QFont('Decorative', 9))
        
        self.number_data = QLineEdit(self)
        self.number_data.setGeometry(25,30,350,30)
        self.number_data.setEnabled(False)
        self.number_data.setAlignment(Qt.AlignRight)
        self.number_data.setStyleSheet("color: black")
        self.number_data.setFont(QFont('Decorative', 9))
        
        self.number_line = QLabel(self)
        self.number_line.setGeometry(25,65,350,30)
        self.number_line.setEnabled(False)
        self.number_line.setAlignment(Qt.AlignRight)
        self.number_line.setStyleSheet("color: black")
        self.number_line.setNum(0)
        self.number_line.setFont(QFont('Decorative', 9))
        
        self.hex_select = QLineEdit(self)
        self.hex_select.setGeometry(20,105,5,10)
        self.hex_select.setStyleSheet("background-color: #F0F0F0 ; border: #F0F0F0")
        self.hex_select.setEnabled(False)
        
        self.hex_btn = QPushButton("HEX", self)
        self.hex_btn.setGeometry(25,95,50,25)
        self.hex_btn.setStyleSheet("border: none")
        self.hex_value = QLabel(self)
        self.hex_value.setGeometry(90,95,285,25)
        self.hex_value.setEnabled(False)
        self.hex_value.setStyleSheet("color: black")
        self.hex_value.setText('0')
        self.hex_btn.clicked.connect(self.hex_btn_clicked)
        
        self.dec_select = QLineEdit(self)
        self.dec_select.setGeometry(20,135,5,10)
        self.dec_select.setStyleSheet("background-color: #F0F0F0 ; border: #F0F0F0")
        self.dec_select.setEnabled(False)
        
        self.dec_btn = QPushButton("DEC", self)
        self.dec_btn.setGeometry(25,125,50,25)
        self.dec_btn.setStyleSheet("border: none")
        self.dec_value = QLabel(self)
        self.dec_value.setGeometry(90,125,285,25)
        self.dec_value.setEnabled(False)
        self.dec_value.setStyleSheet("color: black")
        self.dec_value.setNum(0)
        self.dec_btn.clicked.connect(self.dec_btn_clicked)
        
        self.oct_select = QLineEdit(self)
        self.oct_select.setGeometry(20,165,5,10)
        self.oct_select.setStyleSheet("background-color: #F0F0F0 ; border: #F0F0F0")
        self.oct_select.setEnabled(False)
        
        self.oct_btn = QPushButton("OCT", self)
        self.oct_btn.setGeometry(25,155,50,25)
        self.oct_btn.setStyleSheet("border: none")
        self.oct_value = QLabel(self)
        self.oct_value.setGeometry(90,155,285,25)
        self.oct_value.setEnabled(False)
        self.oct_value.setStyleSheet("color: black")
        self.oct_value.setNum(0)
        self.oct_btn.clicked.connect(self.oct_btn_clicked)
        
        self.bin_select = QLineEdit(self)
        self.bin_select.setGeometry(20,195,5,10)
        self.bin_select.setStyleSheet("background-color: #F0F0F0 ; border: #F0F0F0")
        self.bin_select.setEnabled(False)
        
        self.bin_btn = QPushButton("BIN", self)
        self.bin_btn.setGeometry(25,185,50,25)
        self.bin_btn.setStyleSheet("border: none")
        self.bin_value = QLabel(self)
        self.bin_value.setWordWrap(True)
        self.bin_value.setGeometry(90,185,285,50)
        self.bin_value.setEnabled(False)
        self.bin_value.setStyleSheet("color: black")
        self.bin_value.setNum(0)
        self.bin_btn.clicked.connect(self.bin_btn_clicked)
        
        self.logic = QComboBox(self)
        self.logic.setGeometry(25,240,120,30)
        logic_list = ["Bitwise", "AND", "OR", "NOT", "NAND", "NOR", "XOR",]
        self.logic.addItems(logic_list)
        
        self.operation = QComboBox(self)
        self.operation.setGeometry(150,240,225,30)
        operation_list = ["Bit Shift", "Arithmetic Shift", "Logical Shift", "Rotate Circular Shift", "Rotate Through Carry Circular Shift"]
        self.operation.addItems(operation_list)
        
        self.btn_0 = QPushButton("0", self)
        self.btn_0.setFont(QFont('Decorative', 9))
        self.btn_0.clicked.connect(lambda digit:self.btn_click(0))
        
        self.btn_1 = QPushButton("1", self)
        self.btn_1.setFont(QFont('Decorative', 9))
        self.btn_1.clicked.connect(lambda digit:self.btn_click(1))
        
        self.btn_2 = QPushButton("2", self)
        self.btn_2.setFont(QFont('Decorative', 9))
        self.btn_2.clicked.connect(lambda digit:self.btn_click(2))
        
        self.btn_3 = QPushButton("3", self)
        self.btn_3.setFont(QFont('Decorative', 9))
        self.btn_3.clicked.connect(lambda digit:self.btn_click(3))
        
        self.btn_4 = QPushButton("4", self)
        self.btn_4.setFont(QFont('Decorative', 9))
        self.btn_4.clicked.connect(lambda digit:self.btn_click(4))
        
        self.btn_5 = QPushButton("5", self)
        self.btn_5.setFont(QFont('Decorative', 9))
        self.btn_5.clicked.connect(lambda digit:self.btn_click(5))
        
        self.btn_6 = QPushButton("6", self)
        self.btn_6.setFont(QFont('Decorative', 9))
        self.btn_6.clicked.connect(lambda digit:self.btn_click(6))
        
        self.btn_7 = QPushButton("7", self)
        self.btn_7.setFont(QFont('Decorative', 9))
        self.btn_7.clicked.connect(lambda digit:self.btn_click(7))

        self.btn_8 = QPushButton("8", self)
        self.btn_8.setFont(QFont('Decorative', 9))
        self.btn_8.clicked.connect(lambda digit:self.btn_click(8))
        
        self.btn_9 = QPushButton("9", self)
        self.btn_9.setFont(QFont('Decorative', 9))
        self.btn_9.clicked.connect(lambda digit:self.btn_click(9))
        
        self.btn_A = QPushButton("A", self)
        self.btn_A.setFont(QFont('Decorative', 9))
        self.btn_A.setEnabled(False)    
        self.btn_A.clicked.connect(lambda digit:self.btn_click(10))
        
        self.btn_B = QPushButton("B", self)
        self.btn_B.setFont(QFont('Decorative', 9))
        self.btn_B.setEnabled(False)
        self.btn_B.clicked.connect(lambda digit:self.btn_click(11))
        
        self.btn_C = QPushButton("C", self)
        self.btn_C.setFont(QFont('Decorative', 9))
        self.btn_C.setEnabled(False)
        self.btn_C.clicked.connect(lambda digit:self.btn_click(12))
        
        self.btn_D = QPushButton("D", self)
        self.btn_D.setFont(QFont('Decorative', 9))
        self.btn_D.setEnabled(False)
        self.btn_D.clicked.connect(lambda digit:self.btn_click(13))
        
        self.btn_E = QPushButton("E", self)
        self.btn_E.setFont(QFont('Decorative', 9))
        self.btn_E.setEnabled(False)
        self.btn_E.clicked.connect(lambda digit:self.btn_click(14))
        
        self.btn_F = QPushButton("F", self)
        self.btn_F.setFont(QFont('Decorative', 9))
        self.btn_F.setEnabled(False)
        self.btn_F.clicked.connect(lambda digit:self.btn_click(15))
        
        self.btn_add = QPushButton("+", self)
        self.btn_add.setFont(QFont('Decorative', 9))
        self.btn_add.clicked.connect(self.btn_add_click)
        
        self.btn_sub = QPushButton("-", self)
        self.btn_sub.setFont(QFont('Decorative', 9))
        self.btn_sub.clicked.connect(self.btn_sub_click)
        
        self.btn_mul = QPushButton("*", self)
        self.btn_mul.setFont(QFont('Decorative', 9))
        self.btn_mul.clicked.connect(self.btn_mul_click)
        
        self.btn_div = QPushButton("/", self)
        self.btn_div.setFont(QFont('Decorative', 9))
        self.btn_div.clicked.connect(self.btn_div_click)
        
        self.btn_perc = QPushButton("%", self)
        self.btn_perc.setFont(QFont('Decorative', 9))
        #self.btn_perc.clicked.connect(self.btn_perc_click)
        
        self.btn_pos_neg = QPushButton("+/-", self)
        self.btn_pos_neg.setFont(QFont('Decorative', 9))
        #self.btn_pos_neg.clicked.connect(self.btn_pos_neg_click)
        
        self.btn_dec = QPushButton(".", self)
        self.btn_dec.setFont(QFont('Decorative', 9))
        self.btn_dec.clicked.connect(self.btn_dec_click)
        
        self.btn_equal = QPushButton("=", self)
        self.btn_equal.setFont(QFont('Decorative', 9))
        #self.btn_equal.clicked.connect(self.btn_equal_click)
        
        self.btn_lbracket = QPushButton("(", self)
        self.btn_lbracket.setFont(QFont('Decorative', 9))
        #self.btn_lbracket.clicked.connect(self.btn_lbracket_click)
        
        self.btn_rbracket = QPushButton(")", self)
        self.btn_rbracket.setFont(QFont('Decorative', 9))
        #self.btn_rbracket.clicked.connect(self.btn_rbracket_click)
        
        self.btn_clear = QPushButton("CLEAR", self)
        self.btn_clear.setFont(QFont('Decorative', 9))
        self.btn_clear.clicked.connect(self.btn_clear_click)
        
        self.btn_backspace = QPushButton("BACKSPACE", self)
        self.btn_backspace.setFont(QFont('Decorative', 5))
        self.btn_backspace.clicked.connect(self.btn_backspace_click)
        
        self.btn_lshift = QPushButton("<<", self)
        self.btn_lshift.setFont(QFont('Decorative', 9))
        #self.btn_lshift.clicked.connect(self.btn_lshift_click)
        
        self.btn_rshift = QPushButton(">>", self)
        self.btn_rshift.setFont(QFont('Decorative', 9))
        #self.btn_rshift.clicked.connect(self.btn_rshift_click)
        
        self.display_layout.addWidget(self.btn_F, 6,0)
        self.display_layout.addWidget(self.btn_pos_neg, 6,1)
        self.display_layout.addWidget(self.btn_0, 6,2)
        self.display_layout.addWidget(self.btn_dec, 6,3)
        self.display_layout.addWidget(self.btn_equal, 6,4)
        self.display_layout.addWidget(self.btn_E, 5,0)
        self.display_layout.addWidget(self.btn_1, 5,1)
        self.display_layout.addWidget(self.btn_2, 5,2)
        self.display_layout.addWidget(self.btn_3, 5,3)
        self.display_layout.addWidget(self.btn_add, 5,4)
        self.display_layout.addWidget(self.btn_D, 4,0)
        self.display_layout.addWidget(self.btn_4, 4,1)
        self.display_layout.addWidget(self.btn_5, 4,2)
        self.display_layout.addWidget(self.btn_6, 4,3)
        self.display_layout.addWidget(self.btn_sub, 4,4)
        self.display_layout.addWidget(self.btn_C, 3,0)
        self.display_layout.addWidget(self.btn_7, 3,1)
        self.display_layout.addWidget(self.btn_8, 3,2)
        self.display_layout.addWidget(self.btn_9, 3,3)
        self.display_layout.addWidget(self.btn_mul, 3,4)
        self.display_layout.addWidget(self.btn_B, 2,0)
        self.display_layout.addWidget(self.btn_lbracket, 2,1)
        self.display_layout.addWidget(self.btn_rbracket, 2,2)
        self.display_layout.addWidget(self.btn_perc, 2,3)
        self.display_layout.addWidget(self.btn_div, 2,4)
        self.display_layout.addWidget(self.btn_A, 1,0)
        self.display_layout.addWidget(self.btn_lshift, 1,1)
        self.display_layout.addWidget(self.btn_rshift, 1,2)
        self.display_layout.addWidget(self.btn_clear, 1,3)
        self.display_layout.addWidget(self.btn_backspace, 1,4)
        
        self.v_layout.addLayout(self.display_layout)
    
    def conversion(self, option, data):
        if option == 'HEX':
            self.hex_conv(data)
        elif option == 'DEC':
            self.dec_conv(data)
        elif option == 'OCT':
            self.oct_conv(data)
        elif option == 'BIN':
            self.bin_conv(data)
    
    def hex_conv(self, data):
        value = data
        self.number_line.setText(str(value))
        
        self.hex_value.setText(str(value))
        dec_data = int(value, 16)
        self.dec_value.setText(str(dec_data))
        oct_data = oct(int(value, 16)).split('o')[-1]
        self.oct_value.setText(str(oct_data))
        bin_data = bin(int(value, 16)).split('b')[-1]
        self.bin_value.setText(str(bin_data))

    def dec_conv(self, data):
        value = int(data)
        self.number_line.setText(str(value))
        
        hex_data = hex(value).split('x')[-1].upper()
        self.hex_value.setText(str(hex_data))
        self.dec_value.setText(str(value))
        oct_data = oct(value).split('o')[-1]
        self.oct_value.setText(str(oct_data))
        bin_data = bin(value).split('b')[-1]
        self.bin_value.setText(str(bin_data))
    
    def oct_conv(self, data):
        value = data
        self.number_line.setText(str(value))
        
        hex_data = hex(int(value, 8)).split('x')[-1].upper()
        self.hex_value.setText(str(hex_data))
        dec_data = int(value, 8)
        self.dec_value.setText(str(dec_data))
        self.oct_value.setText(str(value))
        bin_data = bin(int(value, 8)).split('b')[-1]
        self.bin_value.setText(str(bin_data))
   
    def bin_conv(self, data):
        value = data
        self.number_line.setText(str(value))
        
        hex_data = hex(int(value, 2)).split('x')[-1].upper()
        self.hex_value.setText(str(hex_data))
        dec_data = int(value, 2)
        self.dec_value.setText(str(dec_data))
        oct_data = oct(int(value, 2)).split('o')[-1]
        self.oct_value.setText(str(oct_data))
        self.bin_value.setText(str(value))

    def btn_click(self, i):
        value = hex(i).split('x')[-1].upper()
        
        if self.number_data.text() == '':
            if (self.number_line.text() == '0') and (len(self.number_line.text()) < 20):
                self.data = str(value)
                self.conversion(self.base_option, self.data)
            elif (self.number_line.text() != '0') and (len(self.number_line.text()) < 20):
                self.data = self.data + str(value)
                self.conversion(self.base_option, self.data)
            elif (self.number_line.text() != '0') and (len(self.number_line.text()) > 20):
                self.conversion(self.base_option, self.data)
        else:
            if (self.current_value == self.data) and (len(self.number_line.text()) < 20):
                self.number_line.setText('0')
                self.data = str(value)
                self.conversion(self.base_option, self.data)
            elif (self.current_value != self.data) and (len(self.number_line.text()) < 20):
                self.data = self.data + str(value)
                self.conversion(self.base_option, self.data)
            elif (self.number_line.text() != '0') and (len(self.number_line.text()) > 20):
                self.conversion(self.base_option, self.data)

    def btn_dec_click(self):
        if self.number_line.text() == '0':
            self.number_line.setText('0')
        else:
            self.data = self.data + ''
            self.number_line.setText(self.data)
    
    def btn_clear_click(self):
        self.number_data.setText('')
        self.number_line.setText('0')
        self.hex_value.setText('0')
        self.dec_value.setText('0')
        self.oct_value.setText('0')
        self.bin_value.setText('0')
        self.result = '0'
        #self.number_1 = '0'
        #self.number_2 = '0'

    def btn_backspace_click(self):
        if self.number_line.text() == '0':
            self.data = '0'
            self.number_line.setText(self.data)
        else:
            self.data = self.number_line.text()
            self.data = self.data[0:(len(self.data)-1)]
            self.number_line.setText(self.data)
            
            if len(self.data) == 0:
                self.number_line.setText('0')
                self.hex_value.setText('0')
                self.dec_value.setText('0')
                self.oct_value.setText('0')
                self.bin_value.setText('0')

    def hex_btn_clicked(self):
        self.base_option = 'HEX'
        self.number_line.setText(self.hex_value.text())
        self.alphabet_status(1)
        self.number_status(1)
        self.hex_select.setStyleSheet("background-color: blue; border: blue")
        self.dec_select.setStyleSheet("background-color: #F0F0F0 ; border: #F0F0F0")
        self.oct_select.setStyleSheet("background-color: #F0F0F0 ; border: #F0F0F0")
        self.bin_select.setStyleSheet("background-color: #F0F0F0 ; border: #F0F0F0")

    def dec_btn_clicked(self):
        self.base_option = 'DEC'
        self.number_line.setText(self.dec_value.text())
        self.alphabet_status(0)
        self.number_status(1)
        self.hex_select.setStyleSheet("background-color: #F0F0F0 ; border: #F0F0F0")
        self.dec_select.setStyleSheet("background-color: blue; border: blue")
        self.oct_select.setStyleSheet("background-color: #F0F0F0 ; border: #F0F0F0")
        self.bin_select.setStyleSheet("background-color: #F0F0F0 ; border: #F0F0F0")

    def oct_btn_clicked(self):
        self.base_option = 'OCT'
        self.number_line.setText(self.oct_value.text())
        self.alphabet_status(0)
        self.number_status(1)
        self.btn_8.setEnabled(False)
        self.btn_9.setEnabled(False)
        self.hex_select.setStyleSheet("background-color: #F0F0F0 ; border: #F0F0F0")
        self.dec_select.setStyleSheet("background-color: #F0F0F0 ; border: #F0F0F0")
        self.oct_select.setStyleSheet("background-color: blue; border: blue")
        self.bin_select.setStyleSheet("background-color: #F0F0F0 ; border: #F0F0F0")

    def bin_btn_clicked(self):
        self.base_option = 'BIN'
        self.number_line.setText(self.bin_value.text())
        self.alphabet_status(0)
        self.number_status(0)
        self.hex_select.setStyleSheet("background-color: #F0F0F0 ; border: #F0F0F0")
        self.dec_select.setStyleSheet("background-color: #F0F0F0 ; border: #F0F0F0")
        self.oct_select.setStyleSheet("background-color: #F0F0F0 ; border: #F0F0F0")
        self.bin_select.setStyleSheet("background-color: blue; border: blue")

    def alphabet_status(self, status):
        if status == 1:
            self.btn_A.setEnabled(True)
            self.btn_B.setEnabled(True)
            self.btn_C.setEnabled(True)
            self.btn_D.setEnabled(True)
            self.btn_E.setEnabled(True)
            self.btn_F.setEnabled(True)
        else:
            self.btn_A.setEnabled(False)
            self.btn_B.setEnabled(False)
            self.btn_C.setEnabled(False)
            self.btn_D.setEnabled(False)
            self.btn_E.setEnabled(False)
            self.btn_F.setEnabled(False)
    
    def number_status(self, status):
        if status == 1:
            self.btn_2.setEnabled(True)
            self.btn_3.setEnabled(True)
            self.btn_4.setEnabled(True)
            self.btn_5.setEnabled(True)
            self.btn_6.setEnabled(True)
            self.btn_7.setEnabled(True)
            self.btn_8.setEnabled(True)
            self.btn_9.setEnabled(True)
        else:
            self.btn_2.setEnabled(False)
            self.btn_3.setEnabled(False)
            self.btn_4.setEnabled(False)
            self.btn_5.setEnabled(False)
            self.btn_6.setEnabled(False)
            self.btn_7.setEnabled(False)
            self.btn_8.setEnabled(False)
            self.btn_9.setEnabled(False)
    
    def btn_add_click(self):
        #self.result = int(self.result) + int(self.data)
        self.action(self.result, self.data, self.prev_op)
        if self.number_data.text() == '':
            self.number_data.setText(self.number_line.text() + ' ' + self.btn_add.text())
        else:
            self.number_data.setText(self.number_data.text() + ' ' + self.data + ' ' + self.btn_add.text())
        self.update(self.btn_add.text(), self.result, self.data)
    
    def btn_sub_click(self):
        self.action(self.result, self.data, self.prev_op)
        if self.number_data.text() == '':
            self.number_data.setText(self.number_line.text() + ' ' + self.btn_sub.text())
        else:
            self.number_data.setText(self.number_data.text() + ' ' + self.data + ' ' + self.btn_sub.text())
        self.update(self.btn_sub.text(), self.result, self.data)
    
    def btn_mul_click(self):
        self.action(self.result, self.data, self.prev_op)
        if self.number_data.text() == '':
            self.number_data.setText(self.number_line.text() + ' ' + self.btn_mul.text())
        else:
            self.number_data.setText(self.number_data.text() + ' ' + self.data + ' ' + self.btn_mul.text())
        self.update(self.btn_mul.text(), self.result, self.data)
    
    def btn_div_click(self):
        self.action(self.result, self.data, self.prev_op)
        if self.number_data.text() == '':
            self.number_data.setText(self.number_line.text() + ' ' + self.btn_div.text())
        else:
            self.number_data.setText(self.number_data.text() + ' ' + self.data + ' ' + self.btn_div.text())
        self.update(self.btn_div.text(), self.result, self.data)
    
    def update(self, prev_op, result, data):
        self.prev_op = prev_op
        self.number_line.setText(str(self.result))
        self.current_value = self.data
    
    def action(self, no_1, no_2, operand):
        if self.base_option == 'HEX':
            if self.result != self.number_line.text():
                if operand == '+':
                    self.result = str(hex(int(no_1, 16) + int(no_2, 16))).split('x')[-1].upper()
                if operand == '-':
                    self.result = str(hex(int(no_1, 16) - int(no_2, 16))).split('x')[-1].upper()
                if operand == '*':
                    self.result = str(hex(int(no_1, 16) * int(no_2, 16))).split('x')[-1].upper()
                if operand == '/':
                    self.result = str(hex(int(int(no_1, 16) / int(no_2, 16)))).split('x')[-1].upper()
        if self.base_option == 'DEC':
            if self.result != self.number_line.text():
                if operand == '+':
                    self.result = str(int(no_1) + int(no_2))
                if operand == '-':
                    self.result = str(int(no_1) - int(no_2))
                if operand == '*':
                    self.result = str(int(no_1) * int(no_2))
                if operand == '/':
                    self.result = str(int(int(no_1) / int(no_2)))
        if self.base_option == 'OCT':
            if self.result != self.number_line.text():
                if operand == '+':
                    self.result = str(oct(int(no_1, 8) + int(no_2, 8))).split('o')[-1]
                if operand == '-':
                    self.result = str(oct(int(no_1, 8) - int(no_2, 8))).split('o')[-1]
                if operand == '*':
                    self.result = str(oct(int(no_1, 8) * int(no_2, 8))).split('o')[-1]
                if operand == '/':
                    self.result = str(oct(int(int(no_1, 8) / int(no_2, 8)))).split('o')[-1]
        if self.base_option == 'BIN':
            if self.result != self.number_line.text():
                if operand == '+':
                    self.result = str(bin(int(no_1, 2) + int(no_2, 2))).split('b')[-1]
                if operand == '-':
                    self.result = str(bin(int(no_1, 2) - int(no_2, 2))).split('b')[-1]
                if operand == '*':
                    self.result = str(bin(int(no_1, 2) * int(no_2, 2))).split('b')[-1]
                if operand == '/':
                    self.result = str(bin(int(int(no_1, 2) / int(no_2, 2)))).split('b')[-1]
        self.conversion(self.base_option, self.result)

if __name__ == "__main__":
    
    app = QApplication(sys.argv)
    GUI = CALC_GUI()
    sys.exit(app.exec_())