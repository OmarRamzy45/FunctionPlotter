import numpy as np
import matplotlib.pyplot as plt
import sys
from PySide2.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit, QMainWindow, QLabel, QVBoxLayout, QGridLayout, QHBoxLayout, QCheckBox, QFileDialog, QSizePolicy, QMessageBox
from PySide2.QtCore import QSize, Qt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from PySide2 import QtGui
from PySide2.QtGui import QFontMetrics, QFont, QIcon
from MainWindow import *

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowTitle("Function Plotter")
        self.setFixedSize(1200,1000) # make the window full screen
        self.setStyleSheet("background-color: #ACC8D7;") # change the window background color
        self.setWindowIcon(QtGui.QIcon('icon.png')) # change the window icon

    
        self.layout = QVBoxLayout() # main layout
        self.input_layouts = []  # list of layouts for the input fields
        self.layout_1 = QHBoxLayout() # layout for the checkboxes and the plot button
        self.layout_2 = QHBoxLayout() # layout for the restart and save buttons

        self.label = QLabel("Function Plotter") # add a label to the window
        self.label.setAlignment(Qt.AlignCenter) # center the label
        self.label.setStyleSheet("font-size: 80px; color: #1260CC; font-family: Times New Roman; font-weight: bold;") # change the label font and color
        self.label.setFixedHeight(100) # set the label height
        self.layout.addWidget(self.label) # add the label to the main layout
        
        self.add_input_widgets("Enter the Function:", self.layout) 
        self.add_input_widgets("Enter function minimum value:", self.layout)
        self.add_input_widgets("Enter function maximum value:", self.layout)

        self.grid_checkbox = self.add_checkbox("Show Grid", self.layout_1, self.update_plot_grid)
        self.axes_checkbox = self.add_checkbox("Show Axes", self.layout_1, self.update_plot_axes)
   
        self.plot_button = self.add_button("Plot", self.layout_1, self.plot)
        self.layout.addLayout(self.layout_1)

        self.figure = plt.figure()
        self.canvas = FigureCanvas(self.figure)
        self.layout.addWidget(self.canvas)

        self.restart_button = self.add_button("Plot Another Function", self.layout_2, self.restart)

        self.save_button = self.add_button("Save the plot", self.layout_2, self.save_image)
        self.layout.addLayout(self.layout_2)
        
        central_widget = QWidget()
        central_widget.setLayout(self.layout)
        self.setCentralWidget(central_widget)
    
    def add_input_widgets(self, label_text, layout):
        input_layout = QHBoxLayout()
        
        input_label = QLabel(label_text)
        input_label.setStyleSheet("color: #1260CC; font-weight: bold;")
        input_label.setFixedWidth(400)
        input_label.setAlignment(Qt.AlignCenter)
        font = input_label.font()
        font.setPointSize(13)
        input_label.setFont(font)
        line_edit = QLineEdit()
        line_edit.setStyleSheet("border-radius: 10px; padding: 10px; background-color: white;")
        line_edit.setFixedWidth(600)
        line_edit.setAlignment(Qt.AlignCenter)   
        input_layout.addWidget(input_label)
        input_layout.addWidget(line_edit)  
        layout.addLayout(input_layout)
        self.input_layouts.append((input_label, line_edit))

    def add_button(self, label_text, layout, function):
        button = QPushButton(label_text)
        button.clicked.connect(function)
        button.setStyleSheet("background-color: #1260CC;;border-radius: 10px; padding: 10px; color: white; font-weight: bold; font-size: 20px;")
        button.setFixedWidth(400)
        layout.addWidget(button)
        return button

    def add_checkbox(self, label_text, layout, function):
        checkbox = QCheckBox(label_text)
        checkbox.setStyleSheet("QCheckBox::indicator { width: 25px; height: 25px; }")
        checkbox.setStyleSheet("color: #1260CC; font-weight: bold; font-size: 20px;")
        checkbox.setFixedWidth(400)
        checkbox.stateChanged.connect(function)
        layout.addWidget(checkbox)
        return checkbox
    
    def plot(self):
        function = self.input_layouts[0][1].text()
        lower = float(self.input_layouts[1][1].text())
        upper = float(self.input_layouts[2][1].text())
        
        x = np.linspace(lower, upper, 1000)
        error_message = QMessageBox()
        try:
            y = eval(function.replace("^", "**"))
        except SyntaxError as e:
            error_message.setWindowTitle("Error!")
            error_message.setText("Error: Syntax Error in the function.")
            error_message.setIcon(QMessageBox.Critical)
            error_message.exec_()
            return
        except ZeroDivisionError as e:
            error_message.setWindowTitle("Error!")
            error_message.setText("Error: Division by zero in the function.")
            error_message.setIcon(QMessageBox.Critical)
            error_message.exec_()
            return
        except NameError as e:
            error_message.setWindowTitle("Error!")
            error_message.setText("Error: Invalid function.")
            error_message.setIcon(QMessageBox.Critical)
            error_message.exec_()
            return
        except Exception as e:
            error_message.setWindowTitle("Error!")
            error_message.setText("Error: Invalid function.")
            error_message.setIcon(QMessageBox.Critical)
            error_message.exec_()
            return
        
        self.figure.clear()
        plt.plot(x, y)
        plt.xlabel('x')
        plt.ylabel('y')
        plt.title(f'Function Plot for {function}')
        self.update_plot_grid()
        self.canvas.draw()
        
    def update_plot_grid(self):
        if self.grid_checkbox.isChecked():
            plt.grid(True)
        else:
            plt.grid(False)
        self.canvas.draw()

    def update_plot_axes(self): 
        if self.axes_checkbox.isChecked():
            plt.axhline(y=0, color='k')
            plt.axvline(x=0, color='k')
        else:
            plt.axhline(y=0, color='w')
            plt.axvline(x=0, color='w')
        self.canvas.draw()
    
    def restart(self):
        for label, line_edit in self.input_layouts:
            line_edit.clear()
        self.figure.clear()
        self.canvas.draw()
    
    def save_image(self):
        file_dialog = QFileDialog()
        file_path, _ = file_dialog.getSaveFileName(self, "Save Image", "", "PNG (*.png);;JPEG (*.jpg *.jpeg)")
        if file_path:
            self.figure.savefig(file_path, dpi=300)
            save_message = QMessageBox()
            save_message.setWindowTitle("Image Saved")
            save_message.setText(f"The image was saved successfully at:\n{file_path}")
            save_message.setIcon(QMessageBox.Information)
            save_message.exec_()

    def resizeEvent(self, event):
        super().resizeEvent(event)
        self.adjust_button_sizes()
    
    def adjust_button_sizes(self):
        font_metrics = QFontMetrics(self.font())
        plot_button_width = font_metrics.width(self.plot_button.text()) + 100
        restart_button_width = font_metrics.width(self.restart_button.text()) + 100
        save_button_width = font_metrics.width(self.save_button.text()) + 100
    
        self.plot_button.setFixedWidth(plot_button_width)
        self.restart_button.setFixedWidth(restart_button_width)
        self.save_button.setFixedWidth(save_button_width)
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
