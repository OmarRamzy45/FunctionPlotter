import sys
import pytest
from PySide2.QtWidgets import QApplication
from function_plotter import MainWindow

@pytest.fixture
def app(qtbot):
    application = QApplication(sys.argv) # Create the application
    yield application # Tests will run here
    application.quit() # Exit the application

def test_invalid_function(app, qtbot):
    window = MainWindow() # Create the main window
    qtbot.addWidget(window) # Add the widget to the qtbot for testing

    # Set up invalid function input
    qtbot.keyClicks(window.input_layouts[0][1], "x^")

    # Click the plot button
    qtbot.mouseClick(window.plot_button, Qt.LeftButton)

    # Assert that an error message is displayed
    assert window.error_label.text() == "Error: Invalid syntax in the function."

