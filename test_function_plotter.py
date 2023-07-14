import sys
import pytest
from PySide2.QtWidgets import QApplication
from main import MainWindow

@pytest.fixture
def app(qtbot):
    application = QApplication(sys.argv)
    yield application
    application.quit()

def test_plot_button(app, qtbot):
    window = MainWindow()
    qtbot.addWidget(window)

    # Set up initial values
    qtbot.keyClicks(window.input_layouts[0][1], "x**2")
    qtbot.keyClicks(window.input_layouts[1][1], "0")
    qtbot.keyClicks(window.input_layouts[2][1], "10")

    # Click the plot button
    qtbot.mouseClick(window.plot_button, Qt.LeftButton)

    # Assert that the plot is displayed
    assert window.figure.axes

def test_restart_button(app, qtbot):
    window = MainWindow()
    qtbot.addWidget(window)

    # Set up initial values
    qtbot.keyClicks(window.input_layouts[0][1], "x**2")
    qtbot.keyClicks(window.input_layouts[1][1], "0")
    qtbot.keyClicks(window.input_layouts[2][1], "10")

    # Click the plot button
    qtbot.mouseClick(window.plot_button, Qt.LeftButton)

    # Click the restart button
    qtbot.mouseClick(window.restart_button, Qt.LeftButton)

    # Assert that the input fields are cleared and the plot is cleared
    assert window.input_layouts[0][1].text() == ""
    assert window.input_layouts[1][1].text() == ""
    assert window.input_layouts[2][1].text() == ""
    assert not window.figure.axes
