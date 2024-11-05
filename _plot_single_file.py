
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def read_csv(file_path):
    return pd.read_csv(file_path)

def plot_data(data, x_column, y_column, log_x=False, log_y=False):
    plt.figure(figsize=(10, 6))

    x_data = data[x_column]
    y_data = data[y_column]

    if log_x:
        x_data = np.log(np.abs(x_data))
    if log_y:
        y_data = np.log(np.abs(y_data))

    plt.plot(x_data, y_data, marker='o', linestyle='-')

    plt.xlabel(x_column)
    plt.ylabel(y_column)
    plt.title(f'Plot of {y_column} vs {x_column}')

    if log_x:
        plt.xlabel(f'Log(|{x_column}|)')
    if log_y:
        plt.ylabel(f'Log(|{y_column}|)')

    plt.grid(True)
    plt.show()

def find_minima(data, x_column, y_column, log_x=False, log_y=False):
    x_data = data[x_column]
    y_data = data[y_column]

    if log_x:
        x_data = np.log(np.abs(x_data))
    if log_y:
        y_data = np.log(np.abs(y_data))

    positive_minima = []
    negative_minima = []

    for i in range(1, len(x_data) - 1):
        if y_data[i] < y_data[i - 1] and y_data[i] < y_data[i + 1]:
            if x_data[i] > 0:
                positive_minima.append((x_data[i], y_data[i]))
            else:
                negative_minima.append((x_data[i], y_data[i]))

    positive_minima.sort(key=lambda x: x[1])
    negative_minima.sort(key=lambda x: x[1])

    return positive_minima[:2], negative_minima[:2]

def plot_minima(data, x_column, y_column, positive_minima, negative_minima, log_x=False, log_y=False):
    plt.figure(figsize=(10, 6))

    x_data = data[x_column]
    y_data = data[y_column]

    if log_x:
        x_data = np.log(np.abs(x_data))
    if log_y:
        y_data = np.log(np.abs(y_data))

    plt.plot(x_data, y_data, marker='o', linestyle='-')

    for x, y in positive_minima:
        plt.plot(x, y, 'ro')  # Red circle for positive minima
    for x, y in negative_minima:
        plt.plot(x, y, 'bo')  # Blue circle for negative minima

    plt.xlabel(x_column)
    plt.ylabel(y_column)
    plt.title(f'Plot of {y_column} vs {x_column} with Minima')

    if log_x:
        plt.xlabel(f'Log(|{x_column}|)')
    if log_y:
        plt.ylabel(f'Log(|{y_column}|)')

    plt.grid(True)
    plt.show()

def _plot_single_file():
    # User inputs
    file_path = input("Enter the path to the CSV file: ")
    data = read_csv(file_path)

    print("Available columns:")
    print(data.columns)

    x_column = input("Enter the column name for the x-axis: ")
    y_column = input("Enter the column name for the y-axis: ")

    log_x = input("Apply logarithmic filter to x-axis? (yes/no): ").lower() == 'yes'
    log_y = input("Apply logarithmic filter to y-axis? (yes/no): ").lower() == 'yes'

    plot_data(data, x_column, y_column, log_x, log_y)

    positive_minima, negative_minima = find_minima(data, x_column, y_column, log_x, log_y)

    print("Positive Minima:")
    for x, y in positive_minima:
        print(f"({x}, {y})")

    print("Negative Minima:")
    for x, y in negative_minima:
        print(f"({x}, {y})")

    if len(positive_minima) >= 2:
        diff_positive = positive_minima[1][1] - positive_minima[0][1]
        print(f"Difference between first two positive minima: {diff_positive}")

    if len(negative_minima) >= 2:
        diff_negative = negative_minima[1][1] - negative_minima[0][1]
        print(f"Difference between first two negative minima: {diff_negative}")

    if len(positive_minima) > 0 and len(negative_minima) > 0:
        diff_cross = positive_minima[0][1] - negative_minima[0][1]
        print(f"Difference between dominant positive and negative minima: {diff_cross}")

    plot_minima(data, x_column, y_column, positive_minima, negative_minima, log_x, log_y)
