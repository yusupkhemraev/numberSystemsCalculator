import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from ui import Ui_Form
import rc_rc
import math

app = QtWidgets.QApplication(sys.argv)

Form = QtWidgets.QWidget()
ui = Ui_Form()
ui.setupUi(Form)
Form.show()

############################ Global variables ##############################

symbol = ""
view_numbers = ""
num_1 = ""
nam_2 = ""

############################ Buttons Logic #################################

def btn_0():
	global view_numbers
	global num_1
	view_numbers = view_numbers + "0"
	ui.lineEdit.setText(view_numbers)
	num_1 = num_1 + "0"

ui.pushButton_0.clicked.connect(btn_0)

def btn_1():
	global view_numbers
	global num_1
	view_numbers = view_numbers + "1"
	ui.lineEdit.setText(view_numbers)
	num_1 = num_1 + "1"

ui.pushButton_1.clicked.connect(btn_1)

def btn_2():
	global view_numbers
	global num_1
	view_numbers = view_numbers + "2"
	ui.lineEdit.setText(view_numbers)
	num_1 = num_1 + "2"

ui.pushButton_2.clicked.connect(btn_2)

def btn_3():
	global view_numbers
	global num_1
	view_numbers = view_numbers + "3"
	ui.lineEdit.setText(view_numbers)
	num_1 = num_1 + "3"

ui.pushButton_3.clicked.connect(btn_3)

def btn_4():
	global view_numbers
	global num_1
	view_numbers = view_numbers + "4"
	ui.lineEdit.setText(view_numbers)
	num_1 = num_1 + "4"

ui.pushButton_4.clicked.connect(btn_4)

def btn_5():
	global view_numbers
	global num_1
	view_numbers = view_numbers + "5"
	ui.lineEdit.setText(view_numbers)
	num_1 = num_1 + "5"

ui.pushButton_5.clicked.connect(btn_5)

def btn_6():
	global view_numbers
	global num_1
	view_numbers = view_numbers + "6"
	ui.lineEdit.setText(view_numbers)
	num_1 = num_1 + "6"

ui.pushButton_6.clicked.connect(btn_6)

def btn_7():
	global view_numbers
	global num_1
	view_numbers = view_numbers + "7"
	ui.lineEdit.setText(view_numbers)
	num_1 = num_1 + "7"

ui.pushButton_7.clicked.connect(btn_7)

def btn_8():
	global view_numbers
	global num_1
	view_numbers = view_numbers + "8"
	ui.lineEdit.setText(view_numbers)
	num_1 = num_1 + "8"

ui.pushButton_8.clicked.connect(btn_8)

def btn_9():
	global view_numbers
	global num_1
	view_numbers = view_numbers + "9"
	ui.lineEdit.setText(view_numbers)
	num_1 = num_1 + "9"

ui.pushButton_9.clicked.connect(btn_9)

def btn_12():
	global view_numbers
	global num_1
	view_numbers = view_numbers + "A"
	ui.lineEdit.setText(view_numbers)
	num_1 = num_1 + "A"

ui.pushButton_12.clicked.connect(btn_12)

def btn_36():
	global view_numbers
	global num_1
	view_numbers = view_numbers + "B"
	ui.lineEdit.setText(view_numbers)
	num_1 = num_1 + "B"

ui.pushButton_36.clicked.connect(btn_36)

def btn_29():
	global view_numbers
	global num_1
	view_numbers = view_numbers + "C"
	ui.lineEdit.setText(view_numbers)
	num_1 = num_1 + "C"

ui.pushButton_29.clicked.connect(btn_29)

def btn_23():
	global view_numbers
	global num_1
	view_numbers = view_numbers + "D"
	ui.lineEdit.setText(view_numbers)
	num_1 = num_1 + "D"

ui.pushButton_23.clicked.connect(btn_23)

def btn_22():
	global view_numbers
	global num_1
	view_numbers = view_numbers + "E"
	ui.lineEdit.setText(view_numbers)
	num_1 = num_1 + "E"

ui.pushButton_22.clicked.connect(btn_22)

def btn_21():
	global view_numbers
	global num_1
	view_numbers = view_numbers + "F"
	ui.lineEdit.setText(view_numbers)
	num_1 = num_1 + "F"

ui.pushButton_21.clicked.connect(btn_21)

def BackSpace():
	global view_numbers
	global num_1
	view_numbers = view_numbers[0:-1]
	ui.lineEdit.setText(view_numbers)
	num_1 = num_1[0:-1]

ui.pushButton_BackSpace.clicked.connect(BackSpace)

def delete():
	global view_numbers
	global num_1
	global num_2
	global symbol
	symbol = ""
	view_numbers = ""
	num_1 = ""
	nam_2 = ""
	ui.lineEdit.setText(view_numbers)
	ui.resText.setText(view_numbers)

ui.pushButton_cn.clicked.connect(delete)

def percent():
	try:
		global view_numbers
		global num_1
		if "+" in view_numbers or "-" in view_numbers or "×" in view_numbers or "/" in view_numbers or "%" in view_numbers:
			pass
		else:
			num_1 = float(num_1)
			num_1 = num_1 * 0.01
			num_1 = str(num_1)
			view_numbers = num_1
			ui.lineEdit.setText(view_numbers)
	except:
		ui.lineEdit.setText('Введите цифру !')

ui.pushButton_19.clicked.connect(percent)

def factorial():
	global view_numbers
	global num_1
	if "+" in view_numbers or "-" in view_numbers or "×" in view_numbers or "/" in view_numbers or "%" in view_numbers:
		ui.lineEdit.setText("Ошибка")
	else:
		if float(view_numbers) <= 0:
			ui.lineEdit.setText("Число не положительное")
		else:
			try:
				fact = 1
				num_1 = int(num_1)
				for i in range(1, num_1 + 1):
					fact = fact * i

				num_1 = fact
				num_1 = str(num_1)
				view_numbers = num_1
				ui.lineEdit.setText(view_numbers)
			except:
				ui.lineEdit.setText("Число не целое")

ui.pushButton_10.clicked.connect(factorial)

def point():
	global view_numbers
	global num_1
	if "." in num_1:
		pass
	else:
		num_1 = num_1 + "."
		view_numbers = view_numbers + "."
		ui.lineEdit.setText(view_numbers)

ui.pushButton_14.clicked.connect(point)

def division():
	global view_numbers
	global num_1
	global num_2
	global symbol
	if "+" in view_numbers or "-" in view_numbers or "×" in view_numbers or "/" in view_numbers or "%" in view_numbers:
		pass
	else:
		view_numbers = view_numbers + "/"
		ui.lineEdit.setText(view_numbers)
		symbol = "/"
		num_2 = num_1
		num_1 = ""

ui.pushButton_20.clicked.connect(division)

def plus():
	global view_numbers
	global num_1
	global num_2
	global symbol
	if "+" in view_numbers or "-" in view_numbers or "×" in view_numbers or "/" in view_numbers or "%" in view_numbers:
		pass
	else:
		view_numbers = view_numbers + "+"
		ui.lineEdit.setText(view_numbers)
		symbol = "+"
		num_2 = num_1
		num_1 = ""

ui.pushButton_13.clicked.connect(plus)

def mult():
	global view_numbers
	global num_1
	global num_2
	global symbol
	if "+" in view_numbers or "-" in view_numbers or "×" in view_numbers or "/" in view_numbers or "%" in view_numbers:
		pass
	else:
		view_numbers = view_numbers + "×"
		ui.lineEdit.setText(view_numbers)
		symbol = "×"
		num_2 = num_1
		num_1 = ""

ui.pushButton.clicked.connect(mult)

def minus():
	global view_numbers
	global num_1
	global num_2
	global symbol
	if "+" in view_numbers or "-" in view_numbers or "×" in view_numbers or "/" in view_numbers or "%" in view_numbers:
		pass
	else:
		view_numbers = view_numbers + "-"
		ui.lineEdit.setText(view_numbers)
		symbol = "-"
		num_2 = num_1
		num_1 = ""

ui.pushButton_15.clicked.connect(minus)

def equally():
	global view_numbers
	global num_1
	global num_2
	global symbol
	if symbol == "+":
		num_1 = float(num_1)
		num_2 = float(num_2)
		answer = num_1 + num_2
		num_1 = answer
		answer = str(answer)
		ui.lineEdit.setText(answer)
		num_1 = str(num_1)
		num_2 = str(num_2)
		view_numbers = num_1
		answer = ""
	elif symbol == "-":
		num_1 = float(num_1)
		num_2 = float(num_2)
		answer = num_2 - num_1
		num_1 = answer
		answer = str(answer)
		ui.lineEdit.setText(answer)
		num_1 = str(num_1)
		num_2 = str(num_2)
		view_numbers = num_1
		answer = ""
	elif symbol == "×":
		num_1 = float(num_1)
		num_2 = float(num_2)
		answer = num_1 * num_2
		num_1 = answer
		answer = str(answer)
		ui.lineEdit.setText(answer)
		num_1 = str(num_1)
		num_2 = str(num_2)
		view_numbers = num_1
		answer = ""
	elif symbol == "/":
		num_1 = float(num_1)
		num_2 = float(num_2)
		answer = num_2 / num_1
		num_1 = answer
		answer = str(answer)
		ui.lineEdit.setText(answer)
		num_1 = str(num_1)
		num_2 = str(num_2)
		view_numbers = num_1
		answer = ""
	else:
		ui.lineEdit.setText("Ошибка! Знак не выбран !")

ui.pushButton_16.clicked.connect(equally)

############################### RadioButtons ###################################

def getResult():
        try:
        	if ui.radioButton.isChecked():
	            lineNum1 = ui.lineEdit.text()
	            lineNum2 = int(ui.radioButton.text())
	            res = int(lineNum1, lineNum2)

	        elif ui.radioButton_2.isChecked():
	            lineNum1 = ui.lineEdit.text()
	            lineNum2 = int(ui.radioButton_2.text())
	            res = int(lineNum1, lineNum2)

	        elif ui.radioButton_3.isChecked():
	            lineNum1 = ui.lineEdit.text()
	            lineNum2 = int(ui.radioButton_3.text())
	            res = int(lineNum1, lineNum2)

	        elif ui.radioButton_4.isChecked():
	            lineNum1 = ui.lineEdit.text()
	            lineNum2 = int(ui.radioButton_4.text())
	            res = int(lineNum1, lineNum2)

	        else: lineNum2 = ''

############################ Second RadioButtons ################################

        	if ui.radioButton_5.isChecked():
	            res = bin(res)
	            res = str(res).replace('0b' ,'')
	            ui.resText.setText(str(res.upper()))

	        elif ui.radioButton_6.isChecked():
	            res = oct(res)
	            res = str(res).replace('0o' ,'')
	            ui.resText.setText(str(res.upper()))

	        elif ui.radioButton_7.isChecked():
	            res = dec(res)
	            res = str(res).replace('0d' ,'')
	            ui.resText.setText(str(res.upper()))

	        elif ui.radioButton_8.isChecked():
	            res = hex(res)
	            res = str(res).replace('0x' ,'')
	            ui.resText.setText(str(res.upper()))

	        else: ui.resText.setText('Выберите систему счисления !')

        except:
            ui.lineEdit.setText('Введите коректные данные !')

ui.btnResult.clicked.connect(getResult)


sys.exit(app.exec_())
