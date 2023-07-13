import numpy as np
import matplotlib.pyplot as plt
import sys
from PySide2.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit, QMainWindow, QLabel, QVBoxLayout, QGridLayout, QHBoxLayout, QCheckBox, QFileDialog, QSizePolicy
from PySide2.QtCore import QSize, Qt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from PySide2 import QtGui
from PySide2.QtGui import QFontMetrics, QFont, QIcon

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowTitle("Function Plotter")
        # make the window full screen
        self.setFixedSize(1200,1000)

        # change the window background color
        self.setStyleSheet("background-color: #ACC8D7;")
        
        # change the window icon
        self.setWindowIcon(QtGui.QIcon('icon.png'))

        self.layout = QVBoxLayout()
        self.input_layouts = []
        self.layout_1 = QHBoxLayout()
        self.layout_2 = QHBoxLayout()

        # add a label to the window
        self.label = QLabel("Function Plotter")
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setStyleSheet("font-size: 80px; color: #1260CC; font-family: Times New Roman; font-weight: bold;")
        self.label.setFixedHeight(100)
        self.layout.addWidget(self.label)
        
        self.configure_input_widgets("Enter the Function:", self.layout)
        self.configure_input_widgets("Enter function minimum value:", self.layout)
        self.configure_input_widgets("Enter function maximum value:", self.layout)

        self.grid_checkbox = QCheckBox("Display Grid")
        self.grid_checkbox.stateChanged.connect(self.update_plot_grid)
        self.grid_checkbox.setStyleSheet("QCheckBox::indicator { width: 25px; height: 25px; }")
        self.grid_checkbox.setStyleSheet("color: #1260CC; font-weight: bold; font-size: 20px;")
        self.grid_checkbox.setFixedWidth(400)
        self.layout_1.addWidget(self.grid_checkbox)

        self.axes_checkbox = QCheckBox("Display axes")
        self.axes_checkbox.stateChanged.connect(self.update_plot_axes)
        self.axes_checkbox.setStyleSheet("QCheckBox::indicator { width: 25px; height: 25px; }")
        self.axes_checkbox.setStyleSheet("color: #1260CC; font-weight: bold; font-size: 20px;")
        self.axes_checkbox.setFixedWidth(400)
        self.layout_1.addWidget(self.axes_checkbox)
   
        self.plot_button = QPushButton("Plot")
        self.plot_button.clicked.connect(self.plot)
        self.plot_button.setStyleSheet("background-color: #1260CC;;border-radius: 10px; padding: 10px; color: white; font-weight: bold; font-size: 20px;")
        self.plot_button.setFixedWidth(400)

        self.layout_1.addWidget(self.plot_button)
        self.layout.addLayout(self.layout_1)

        self.figure = plt.figure()
        self.canvas = FigureCanvas(self.figure)
        self.layout.addWidget(self.canvas)
        
        self.restart_button = QPushButton("Plot Another Function")
        self.restart_button.clicked.connect(self.restart)
        self.restart_button.setStyleSheet("background-color: #1260CC;;border-radius: 10px; padding: 10px; color: white; font-weight: bold; font-size: 20px;")
        self.layout_2.addWidget(self.restart_button)

        self.save_button = QPushButton("Save Image")
        self.save_button.clicked.connect(self.save_image)
        self.save_button.setStyleSheet("background-color: #1260CC;;border-radius: 10px; padding: 10px; color: white; font-weight: bold; font-size: 20px;")
        self.layout_2.addWidget(self.save_button)
        self.layout.addLayout(self.layout_2)
        
        central_widget = QWidget()
        central_widget.setLayout(self.layout)
        self.setCentralWidget(central_widget)
    
    def configure_input_widgets(self, label_text, layout):
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
    
    def plot(self):
        function = self.input_layouts[0][1].text()
        lower = float(self.input_layouts[1][1].text())
        upper = float(self.input_layouts[2][1].text())
        
        x = np.linspace(lower, upper, 1000)
        y = eval(function.replace("^", "**"))        

        self.figure.clear()
        plt.plot(x, y)
        plt.xlabel('x')
        plt.ylabel('y')
        plt.title('Function Plot')
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
            self.plot()
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
            message_box = QMessageBox()
            message_box.setWindowTitle("Image Saved")
            message_box.setText(f"The image was saved successfully at:\n{file_path}")
            message_box.setIcon(QMessageBox.Information)
            message_box.exec_()

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
