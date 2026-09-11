import sys
import math

from PyQt6.QtWidgets import QApplication, QWidget, QLineEdit, QGridLayout, QVBoxLayout, QPushButton


app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle("Smart Calculator - Aoudi Edition")
window.resize(400, 550)

# خلفية النافذة
window.setStyleSheet("background-color: #F3E8E6;")


# شاشة العرض
display = QLineEdit()
display.setFixedHeight(60)
display.setReadOnly(True)

display.setStyleSheet("""
    background-color: #FFFFFF;
    color: #4A2C2A;
    font-size: 26px;
    padding: 10px;
    border: 2px solid #C8A39A;
    border-radius: 8px;
""")


# =========================
# دوال الأزرار
# =========================

def number_clicked(n):
    display.setText(display.text() + n)


def operation_clicked(op):
    display.setText(display.text() + op)


def clear():
    display.setText("")


def backspace():
    text = display.text()
    display.setText(text[:-1])


def toggle_sign():
    text = display.text()

    if text:
        if text.startswith("-"):
            display.setText(text[1:])
        else:
            display.setText("-" + text)


def percent():
    text = display.text()

    if text:
        try:
            display.setText(str(float(text) / 100))
        except:
            display.setText("Error")


def sqrt():
    text = display.text()

    if text:
        try:
            display.setText(str(math.sqrt(float(text))))
        except:
            display.setText("Error")


def square():
    text = display.text()

    if text:
        try:
            display.setText(str(float(text) ** 2))
        except:
            display.setText("Error")


def calculate():
    text = display.text()

    try:
        result = eval(text)
        display.setText(str(result))
    except:
        display.setText("Error")


# =========================
# تصميم الواجهة
# =========================

layout = QVBoxLayout()
layout.addWidget(display)

grid = QGridLayout()


buttons = [
    ("7", 0, 0), ("8", 0, 1), ("9", 0, 2), ("/", 0, 3),
    ("4", 1, 0), ("5", 1, 1), ("6", 1, 2), ("*", 1, 3),
    ("1", 2, 0), ("2", 2, 1), ("3", 2, 2), ("-", 2, 3),
    ("0", 3, 0), ("C", 3, 1), ("=", 3, 2), ("+", 3, 3),

    ("⌫", 4, 0), ("±", 4, 1), ("%", 4, 2), ("√", 4, 3),
    ("x²", 5, 0)
]


for text, row, col in buttons:

    button = QPushButton(text)

    # الشكل الأساسي للأزرار
    button.setStyleSheet("""
        background-color: #C8A39A;
        color: white;
        font-size: 20px;
        border-radius: 10px;
        padding: 10px;
    """)


    # أزرار العمليات
    if text in ["+", "-", "*", "/", "%", "√", "x²"]:
        button.setStyleSheet("""
            background-color: #7A4F4A;
            color: white;
            font-size: 20px;
            border-radius: 10px;
        """)


    # زر =
    if text == "=":
        button.setStyleSheet("""
            background-color: #4A2C2A;
            color: white;
            font-size: 22px;
            border-radius: 12px;
        """)


    # ربط الأزرار بالدوال

    if text.isdigit():
        button.clicked.connect(
            lambda checked, n=text: number_clicked(n)
        )

    elif text in ["+", "-", "*", "/"]:
        button.clicked.connect(
            lambda checked, op=text: operation_clicked(op)
        )

    elif text == "=":
        button.clicked.connect(calculate)

    elif text == "C":
        button.clicked.connect(clear)

    elif text == "⌫":
        button.clicked.connect(backspace)

    elif text == "±":
        button.clicked.connect(toggle_sign)

    elif text == "%":
        button.clicked.connect(percent)

    elif text == "√":
        button.clicked.connect(sqrt)

    elif text == "x²":
        button.clicked.connect(square)


    grid.addWidget(button, row, col)



layout.addLayout(grid)

window.setLayout(layout)


window.show()

sys.exit(app.exec())