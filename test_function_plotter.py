import pytest
import numpy as np
from PySide2.QtWidgets import QApplication
from main import MainWindow
from PySide2.QtWidgets import QLineEdit, QPushButton, QCheckBox
from PySide2.QtCore import Qt

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
    # Act
    function_input.setText("x**2")
    min_input.setText("-10")
    max_input.setText("10")
    qtbot.mouseClick(plot_button, Qt.LeftButton)
    # Assert
    assert plot_button.text() == "Plot"
    assert function_input.text() == "x**2"
    assert min_input.text() == "-10"
    assert max_input.text() == "10"
    assert plot_button.isEnabled() == True
    assert function_input.isEnabled() == True
    assert min_input.isEnabled() == True
    assert max_input.isEnabled() == True

def test_restart(qtbot):
    # Test the restart function
    # Arrange
    window = MainWindow()
    window.show()
    qtbot.addWidget(window)
    function_input = window.input_layouts[0][1]
    min_input = window.input_layouts[1][1]
    max_input = window.input_layouts[2][1]
    plot_button = window.plot_button
    restart_button = window.restart_button
    # Act
    function_input.setText("x**2")
    min_input.setText("-10")
    max_input.setText("10")
    qtbot.mouseClick(plot_button, Qt.LeftButton)
    qtbot.mouseClick(restart_button, Qt.LeftButton)
    # Assert
    assert plot_button.text() == "Plot"
    assert function_input.text() == ""
    assert min_input.text() == ""
    assert max_input.text() == ""
    assert plot_button.isEnabled() == True
    assert function_input.isEnabled() == True
    assert min_input.isEnabled() == True
    assert max_input.isEnabled() == True

# def test_save_image(qtbot):
#     # Test the save_image function
#     # Arrange
#     window = MainWindow()
#     window.show()
#     qtbot.addWidget(window)
#     function_input = window.input_layouts[0][1]
#     min_input = window.input_layouts[1][1]
#     max_input = window.input_layouts[2][1]
#     plot_button = window.plot_button
#     save_button = window.save_button
#     # Act
#     function_input.setText("x**2")
#     min_input.setText("-10")
#     max_input.setText("10")
#     qtbot.mouseClick(plot_button, Qt.LeftButton)
#     qtbot.mouseClick(save_button, Qt.LeftButton)
#     # Assert
#     assert plot_button.text() == "Plot"
#     assert function_input.text() == "x**2"
#     assert min_input.text() == "-10"
#     assert max_input.text() == "10"
#     assert plot_button.isEnabled() == True
#     assert function_input.isEnabled() == True
#     assert min_input.isEnabled() == True
#     assert max_input.isEnabled() == True

# def test_plot_with_invalid_function(qtbot):
#     # Test the plot function with invalid function
#     # Arrange
#     window = MainWindow()
#     window.show()
#     qtbot.addWidget(window)
#     function_input = window.input_layouts[0][1]
#     min_input = window.input_layouts[1][1]
#     max_input = window.input_layouts[2][1]
#     plot_button = window.plot_button
#     # Act
#     function_input.setText("x**")
#     min_input.setText("-10")
#     max_input.setText("10")
#     qtbot.mouseClick(plot_button, Qt.LeftButton)
#     # Assert
#     assert plot_button.text() == "Plot"
#     assert function_input.text() == "x**"
#     assert min_input.text() == "-10"
#     assert max_input.text() == "10"
#     assert plot_button.isEnabled() == True
#     assert function_input.isEnabled() == True
#     assert min_input.isEnabled() == True
#     assert max_input.isEnabled() == True

# def test_plot_with_invalid_min(qtbot):
#     # Test the plot function with invalid min
#     # Arrange
#     window = MainWindow()
#     window.show()
#     qtbot.addWidget(window)
#     function_input = window.input_layouts[0][1]
#     min_input = window.input_layouts[1][1]
#     max_input = window.input_layouts[2][1]
#     plot_button = window.plot_button
#     # Act
#     function_input.setText("x**2")
#     min_input.setText("a")
#     max_input.setText("10")
#     qtbot.mouseClick(plot_button, Qt.LeftButton)
#     # Assert
#     assert plot_button.text() == "Plot"
#     assert function_input.text() == "x**2"
#     assert min_input.text() == "a"
#     assert max_input.text() == "10"
#     assert plot_button.isEnabled() == True
#     assert function_input.isEnabled() == True
#     assert min_input.isEnabled() == True
#     assert max_input.isEnabled() == True

# def test_plot_with_invalid_max(qtbot):
#     # Test the plot function with invalid max
#     # Arrange
#     window = MainWindow()
#     window.show()
#     qtbot.addWidget(window)
#     function_input = window.input_layouts[0][1]
#     min_input = window.input_layouts[1][1]
#     max_input = window.input_layouts[2][1]
#     plot_button = window.plot_button
#     # Act
#     function_input.setText("x**2")
#     min_input.setText("-10")
#     max_input.setText("a")
#     qtbot.mouseClick(plot_button, Qt.LeftButton)
#     # Assert
#     assert plot_button.text() == "Plot"
#     assert function_input.text() == "x**2"
#     assert min_input.text() == "-10"
#     assert max_input.text() == "a"
#     assert plot_button.isEnabled() == True
#     assert function_input.isEnabled() == True
#     assert min_input.isEnabled() == True
#     assert max_input.isEnabled() == True

# def test_plot_grid(qtbot):
#     # Test the plot function with grid
#     # Arrange
#     window = MainWindow()
#     window.show()
#     qtbot.addWidget(window)
#     function_input = window.input_layouts[0][1]
#     min_input = window.input_layouts[1][1]
#     max_input = window.input_layouts[2][1]
#     grid_checkbox = window.grid_checkbox
#     plot_button = window.plot_button
#     # Act
#     function_input.setText("x**2")
#     min_input.setText("-10")
#     max_input.setText("10")
#     qtbot.mouseClick(grid_checkbox, Qt.LeftButton)
#     qtbot.mouseClick(plot_button, Qt.LeftButton)
#     # Assert
#     assert plot_button.text() == "Plot"
#     assert grid_checkbox.isChecked() == True
#     assert function_input.text() == "x**2"
#     assert min_input.text() == "-10"
#     assert max_input.text() == "10"
#     assert plot_button.isEnabled() == True
#     assert function_input.isEnabled() == True
#     assert min_input.isEnabled() == True
#     assert max_input.isEnabled() == True
#     assert grid_checkbox.isEnabled() == True

# def test_plot_axes(qtbot):
    # # Test the plot function with axes
    # # Arrange
    # window = MainWindow()
    # window.show()
    # qtbot.addWidget(window)
    # function_input = window.input_layouts[0][1]
    # min_input = window.input_layouts[1][1]
    # max_input = window.input_layouts[2][1]
    # axes_checkbox = window.axes_checkbox
    # plot_button = window.plot_button
    # # Act
    # function_input.setText("x**2")
    # min_input.setText("-10")
    # max_input.setText("10")
    # qtbot.mouseClick(axes_checkbox, Qt.LeftButton)
    # qtbot.mouseClick(plot_button, Qt.LeftButton)
    # # Assert
    # assert plot_button.text() == "Plot"
    # assert axes_checkbox.isChecked() == True
    # assert function_input.text() == "x**2"
    # assert min_input.text() == "-10"
    # assert max_input.text() == "10"
    # assert plot_button.isEnabled() == True
    # assert function_input.isEnabled() == True
    # assert min_input.isEnabled() == True
    # assert max_input.isEnabled() == True
    # assert axes_checkbox.isEnabled() == True