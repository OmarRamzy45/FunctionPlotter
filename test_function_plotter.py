import pytest
import numpy as np
from PySide2.QtWidgets import QApplication
from main import MainWindow
from PySide2.QtWidgets import QLineEdit, QPushButton, QCheckBox
from PySide2.QtCore import Qt
import matplotlib.pyplot as plt  # Import the plt module to access the grid setting

def test_plot(qtbot):
    # Test the plot is shown correctly
    # Arrange
    window = MainWindow()
    window.show()
    qtbot.addWidget(window)
    function_input = window.input_layouts[0][1]
    min_input = window.input_layouts[1][1]
    max_input = window.input_layouts[2][1]
    plot_button = window.plot_button
    plot = window.figure
    # Act
    function_input.setText("x**2")
    min_input.setText("-10")
    max_input.setText("10")
    qtbot.mouseClick(plot_button, Qt.LeftButton)
    # Assert
    assert function_input.text() == "x**2"
    assert min_input.text() == "-10" 
    assert max_input.text() == "10"
    assert plot_button.isEnabled() == True
    assert function_input.isEnabled() == True
    assert min_input.isEnabled() == True
    assert max_input.isEnabled() == True
    assert plot != None # check if the plot is not empty

def test_plot_with_invalid_input(qtbot):
    # Test the plot is not shown when the input is invalid
    # Arrange
    window = MainWindow()
    window.show()
    qtbot.addWidget(window)
    function_input = window.input_layouts[0][1]
    min_input = window.input_layouts[1][1]
    max_input = window.input_layouts[2][1]
    plot_button = window.plot_button
    plot = window.figure
    # Act
    function_input.setText("x**")
    min_input.setText("10")
    max_input.setText("-10")
    qtbot.mouseClick(plot_button, Qt.LeftButton)
    # Assert
    assert not plot.axes # check if the plot is empty
    assert window.error_message.text() == "Error: Syntax Error in the function." 

def test_plot_with_zero_division(qtbot):
    # Test the plot is not shown when the input is invalid
    # Arrange
    window = MainWindow()
    window.show()
    qtbot.addWidget(window)
    function_input = window.input_layouts[0][1]
    min_input = window.input_layouts[1][1]
    max_input = window.input_layouts[2][1]
    plot_button = window.plot_button
    plot = window.figure
    # Act
    function_input.setText("x/0")
    min_input.setText("10")
    max_input.setText("-10")
    qtbot.mouseClick(plot_button, Qt.LeftButton)
    # Assert
    assert not plot.axes # check if the plot is empty
    assert window.error_message.text() == "Error: Division by zero in the function."

def test_grid(qtbot):
    # Test the grid is shown correctly
    # Arrange
    window = MainWindow()
    window.show()
    qtbot.addWidget(window)
    grid_checkbox = window.grid_checkbox
    plot = window.figure
    # Act
    grid_checkbox.setChecked(True)
    # Update the plot after checking the grid checkbox
    window.update_plot_grid()
    # Assert
    assert grid_checkbox.isChecked() == True
    # Check if grid is shown
    assert plt.rcParams['axes.grid'] == True


def test_axes(qtbot):
    # Test the axes are shown correctly
    # Arrange
    window = MainWindow()
    window.show()
    qtbot.addWidget(window)
    axes_checkbox = window.axes_checkbox
    plot = window.figure
    # Act
    axes_checkbox.setChecked(True)
    # Assert
    assert axes_checkbox.isChecked() == True
    assert plt.rcParams['axes.spines.left'] == True
    assert plt.rcParams['axes.spines.bottom'] == True
    assert plt.rcParams['axes.spines.top'] == True
    assert plt.rcParams['axes.spines.right'] == True

def test_reset(qtbot):
    # Test the reset button works correctly
    # Arrange
    window = MainWindow()
    window.show()
    qtbot.addWidget(window)
    function_input = window.input_layouts[0][1]
    min_input = window.input_layouts[1][1]
    max_input = window.input_layouts[2][1]
    plot_button = window.plot_button
    restart_button = window.restart_button
    plot = window.figure
    # Act
    function_input.setText("x**2")
    min_input.setText("-10")
    max_input.setText("10")
    qtbot.mouseClick(plot_button, Qt.LeftButton)
    qtbot.mouseClick(restart_button, Qt.LeftButton)
    # Assert
    assert function_input.text() == ""
    assert min_input.text() == "" 
    assert max_input.text() == ""
    assert not plot.axes # check if the plot is empty
