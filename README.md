# Function Plotter

## Description
Function Plotter is a simple Python application that allows users to plot mathematical functions and customize the appearance of the generated plot. The application is built using PySide2 (Qt for Python) for the GUI and matplotlib for plotting.

## Features

- Enter a mathematical function and its range to generate a plot.
- The following operators are supported: + - / * ^. 
- Customize the plot appearance by enabling/disabling the grid and axes.
- Save the generated plot as an image (PNG or JPEG).
- Error handling for invalid input with a message box.

## Prerequisites

Before running the Function Plotter application, make sure you have the following installed:

- Python 3
- PySide2 library
- NumPy library
- Matplotlib library

You can install the required libraries using `pip`:

```bash
pip install PySide2 numpy matplotlib pytest pytest-qt
``` 

## Testing
Automated tests are implemented using pytest and pytest-qt. To run the tests, navigate to the project directory and run the following command:

```bash
python3.8 -m pytest test_function_plotter.py
```

# Examples
example for plotting (x^2 + 2x + 1) from -10 to 10
![plot](Examples/plot.png)




