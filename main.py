import numpy as np
import matplotlib.pyplot as plt
import sys
from PySide2.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit, QMainWindow, QLabel, QVBoxLayout, QGridLayout, QHBoxLayout, QCheckBox, QFileDialog, QSizePolicy, QMessageBox
from PySide2.QtCore import QSize, Qt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from PySide2 import QtGui
from PySide2.QtGui import QFontMetrics, QFont, QIcon

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowTitle("Function Plotter")
        self.setFixedSize(1200, 1000)  # Set the window size to a fixed size
        self.setStyleSheet("background-color: #ACC8D7;")  # Set the window background color
        self.setWindowIcon(QtGui.QIcon('icon.png'))  # Set the window icon

        self.layout = QVBoxLayout()  # Main layout to hold all other layouts
        self.input_layouts = []  # List to store input field layouts
        self.layout_1 = QHBoxLayout()  # Layout for the checkboxes and the plot button
        self.layout_2 = QHBoxLayout()  # Layout for the restart and save buttons

        self.label = QLabel("Function Plotter")  # Create a label for the window
        self.label.setAlignment(Qt.AlignCenter)  # Center-align the label text
        self.label.setStyleSheet("font-size: 80px; color: #1260CC; font-family: Times New Roman; font-weight: bold;")  # Set the label font and color
        self.label.setFixedHeight(100)  # Set the fixed height for the label
        self.layout.addWidget(self.label)  # Add the label to the main layout

        # Add input fields and labels to the main layout
        self.add_input_widgets("Enter the Function:", self.layout)
        self.add_input_widgets("Enter function minimum value:", self.layout)
        self.add_input_widgets("Enter function maximum value:", self.layout)

        # Add checkboxes for grid and axes visibility and their corresponding functions
        self.grid_checkbox = self.add_checkbox("Show Grid", self.layout_1, self.update_plot_grid)
        self.axes_checkbox = self.add_checkbox("Show Axes", self.layout_1, self.update_plot_axes)

        # Add the "Plot" button to the layout and connect it to the "plot" function
        self.plot_button = self.add_button("Plot", self.layout_1, self.plot)
        self.layout.addLayout(self.layout_1)  # Add layout_1 to the main layout

        # Create a matplotlib figure and add it to the window as a canvas
        self.figure = plt.figure()
        self.canvas = FigureCanvas(self.figure)
        self.layout.addWidget(self.canvas)  # Add the canvas to the main layout

        # Add "Plot Another Function" and "Save the Plot" buttons with their corresponding functions
        self.restart_button = self.add_button("Plot Another Function", self.layout_2, self.restart)
        self.save_button = self.add_button("Save the plot", self.layout_2, self.save_image)
        self.layout.addLayout(self.layout_2)  # Add layout_2 to the main layout

        # Create QMessageBox to show error messages
        self.error_message = QMessageBox()

        # Create QFileDialog to select file path for image saving
        self.file_dialog = QFileDialog()

        # Create a central widget and set it as the main window's central widget
        central_widget = QWidget()
        central_widget.setLayout(self.layout)
        self.setCentralWidget(central_widget)

    def add_input_widgets(self, label_text, layout):
        # Function to add input field and label to a given layout
        input_layout = QHBoxLayout()

        # Create the input label and set its style
        input_label = QLabel(label_text)
        input_label.setStyleSheet("color: #1260CC; font-weight: bold;")
        input_label.setFixedWidth(400)  # Set the fixed width for the label
        input_label.setAlignment(Qt.AlignCenter)  # Center-align the label text
        font = input_label.font()
        font.setPointSize(13)  # Set the font size for the label text
        input_label.setFont(font)

        # Create the line edit (input field) and set its style and fixed width
        line_edit = QLineEdit()
        line_edit.setStyleSheet("border-radius: 10px; padding: 10px; background-color: white;")
        line_edit.setFixedWidth(600)

        # Center-align the input field text
        line_edit.setAlignment(Qt.AlignCenter)

        # Add the label and input field to the input layout
        input_layout.addWidget(input_label)
        input_layout.addWidget(line_edit)

        # Add the input layout to the given main layout
        layout.addLayout(input_layout)

        # Add the label and input field as a tuple to the input_layouts list
        self.input_layouts.append((input_label, line_edit))

    def add_button(self, label_text, layout, function):
        # Function to add a button with the given label text and connect it to a given function
        button = QPushButton(label_text)
        button.clicked.connect(function)

        # Set the button's style (background color, font, etc.)
        button.setStyleSheet("background-color: #1260CC;;border-radius: 10px; padding: 10px; color: white; font-weight: bold; font-size: 20px;")
        button.setFixedWidth(250)  # Set the fixed width for the button
        layout.addWidget(button)  # Add the button to the given layout
        return button

    def add_checkbox(self, label_text, layout, function):
        # Function to add a checkbox with the given label text and connect it to a given function
        checkbox = QCheckBox(label_text)

        # Set the checkbox style (indicator size, color, etc.)
        checkbox.setStyleSheet("QCheckBox::indicator { width: 25px; height: 25px; }")
        checkbox.setStyleSheet("color: #1260CC; font-weight: bold; font-size: 20px;")
        checkbox.setFixedWidth(400)  # Set the fixed width for the checkbox
        checkbox.stateChanged.connect(function)  # Connect the checkbox state change to the function
        layout.addWidget(checkbox)  # Add the checkbox to the given layout
        return checkbox

    def plot(self):
        # Function to plot the given function within the specified range
        function = self.input_layouts[0][1].text()
        lower = float(self.input_layouts[1][1].text())
        upper = float(self.input_layouts[2][1].text())

        # Check for division by zero in the function input
        if "/ 0" in function or "/0" in function:
            # Show error message if the function contains division by zero
            self.error_message.setWindowTitle("Error!")
            self.error_message.setText("Error: Division by zero in the function.")
            self.error_message.setIcon(QMessageBox.Critical)
            self.error_message.exec_()
            return

        x = np.linspace(lower, upper, 1000)  # Generate x values for the plot

        try:
            # Evaluate the function to get y values for the plot
            y = eval(function.replace("^", "**"))
        except SyntaxError as e:
            # Show error message if there is a syntax error in the function
            self.error_message.setWindowTitle("Error!")
            self.error_message.setText("Error: Syntax Error in the function.")
            self.error_message.setIcon(QMessageBox.Critical)
            self.error_message.exec_()
            return
        except NameError as e:
            # Show error message if there is an invalid function
            self.error_message.setWindowTitle("Error!")
            self.error_message.setText("Error: Invalid function.")
            self.error_message.setIcon(QMessageBox.Critical)
            self.error_message.exec_()
        except Exception as e:
            # Show error message for any other exceptions
            self.error_message.setWindowTitle("Error!")
            self.error_message.setText("Error: Invalid function.")
            self.error_message.setIcon(QMessageBox.Critical)
            self.error_message.exec_()
            return

        # Clear the previous plot and create a new one with the new data
        self.figure.clear()
        plt.plot(x, y)
        plt.xlabel('x')  # Set x-axis label
        plt.ylabel('y')  # Set y-axis label
        plt.title(f'Function Plot for {function}')  # Set the plot title with the function
        self.update_plot_grid()  # Update the plot grid based on the checkbox state
        self.canvas.draw()  # Redraw the canvas to display the updated plot

    def update_plot_grid(self):
        # Function to update the plot grid based on the state of the grid checkbox
        if self.grid_checkbox.isChecked():
            plt.rcParams['axes.grid'] = True  # Add this line to update the grid setting
            plt.grid(True)  # Show grid if the checkbox is checked
        else:
            plt.rcParams['axes.grid'] = False  # Add this line to update the grid setting
            plt.grid(False)  # Hide grid if the checkbox is unchecked
        self.canvas.draw()  # Redraw the canvas to display the updated plot

    def update_plot_axes(self):
        # Function to update the plot axes based on the state of the axes checkbox
        if self.axes_checkbox.isChecked():
            plt.axhline(y=0, color='k')  # Show horizontal axis line if the checkbox is checked
            plt.axvline(x=0, color='k')  # Show vertical axis line if the checkbox is checked
        else:
            plt.axhline(y=0, color='w')  # Hide horizontal axis line if the checkbox is unchecked
            plt.axvline(x=0, color='w')  # Hide vertical axis line if the checkbox is unchecked
        self.canvas.draw()  # Redraw the canvas to display the updated plot

    def restart(self):
        # Function to clear all input fields and the previous plot
        for label, line_edit in self.input_layouts:
            line_edit.clear()  # Clear all input fields
        self.figure.clear()  # Clear the previous plot
        self.canvas.draw()  # Redraw the canvas to display the cleared plot

    def save_image(self):
        # Function to save the plot as an image
        file_path, _ = self.file_dialog.getSaveFileName(self, "Save Image", "", "PNG (*.png);;JPEG (*.jpg *.jpeg)")
        if file_path:
            self.figure.savefig(file_path, dpi=300)  # Save the plot to the specified file path with 300 DPI
            # Show a message box to inform the user that the image was saved successfully
            save_message = QMessageBox()
            save_message.setWindowTitle("Image Saved")
            save_message.setText(f"The image was saved successfully at:\n{file_path}")
            save_message.setIcon(QMessageBox.Information)
            save_message.exec_()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
