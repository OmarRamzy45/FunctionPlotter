import sys
import pytest
from PySide2.QtWidgets import QApplication
from PySide2.QtTest import QTest
from PySide2.QtCore import Qt
from main import MainWindow

@pytest.fixture
def app(qtbot):
    application = QApplication(sys.argv)
    yield application
    application.quit()


def test_valid_input_plot(app, qtbot):
    window = MainWindow()
    qtbot.addWidget(window)

    # Set up valid function input
    qtbot.keyClicks(window.input_layouts[0][1], "x^2")

    # Set up valid min and max values
    qtbot.keyClicks(window.input_layouts[1][1], "-5")
    qtbot.keyClicks(window.input_layouts[2][1], "5")

    # Click the plot button
    qtbot.mouseClick(window.plot_button, Qt.LeftButton)

    # Assert that no error message is displayed
    assert not window.error_label.text()

    # Assert that the plot appears on the canvas
    assert window.canvas.figure.get_axes()

    # Check if the plot is a line plot
    assert all(isinstance(item, plt.Line2D) for item in window.canvas.figure.get_axes()[0].get_children())


def test_grid_checkbox(app, qtbot):
    window = MainWindow()
    qtbot.addWidget(window)

    # Check if the grid is initially off
    assert not window.grid_checkbox.isChecked()

    # Click the grid checkbox
    qtbot.mouseClick(window.grid_checkbox, Qt.LeftButton)

    # Check if the grid is turned on
    assert window.grid_checkbox.isChecked()

    # Click the grid checkbox again
    qtbot.mouseClick(window.grid_checkbox, Qt.LeftButton)

    # Check if the grid is turned off again
    assert not window.grid_checkbox.isChecked()


def test_axes_checkbox(app, qtbot):
    window = MainWindow()
    qtbot.addWidget(window)

    # Check if the axes are initially off
    assert not window.axes_checkbox.isChecked()

    # Click the axes checkbox
    qtbot.mouseClick(window.axes_checkbox, Qt.LeftButton)

    # Check if the axes are turned on
    assert window.axes_checkbox.isChecked()

    # Click the axes checkbox again
    qtbot.mouseClick(window.axes_checkbox, Qt.LeftButton)

    # Check if the axes are turned off again
    assert not window.axes_checkbox.isChecked()
