import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def read_csv(file_path):
    return pd.read_csv(file_path)

def plot_data(data, x_column, y_column, log_x=False, log_y=False, label=None):
    x_data = data[x_column]
    y_data = data[y_column]

    if log_x:
        x_data = np.log(np.abs(x_data))
    if log_y:
        y_data = np.log(np.abs(y_data))

    plt.plot(x_data, y_data, linestyle='-', label=label)

def _plot_files_from_directory_level_1():
    directory_path = input("Enter the path to the directory containing CSV files: ")

    # List all CSV files in the directory
    files = [f for f in os.listdir(directory_path) if f.endswith('.csv')]

    if not files:
        print("No CSV files found in the directory.")
        return

    if len(files) == 1:
        file_path = os.path.join(directory_path, files[0])
        data = read_csv(file_path)
        print("Available columns:")
        print(data.columns)

        x_column = input("Enter the column name for the x-axis: ")
        y_column = input("Enter the column name for the y-axis: ")

        log_x = input("Apply logarithmic filter to x-axis? (yes/no): ").lower() == 'yes'
        log_y = input("Apply logarithmic filter to y-axis? (yes/no): ").lower() == 'yes'

        plt.figure(figsize=(10, 6))
        plot_data(data, x_column, y_column, log_x, log_y, label=files[0])
        plt.xlabel(x_column)
        plt.ylabel(y_column)
        plt.title(f'Plot of {y_column} vs {x_column} from {files[0]}')
        if log_x:
            plt.xlabel(f'Log(|{x_column}|)')
        if log_y:
            plt.ylabel(f'Log(|{y_column}|)')
        plt.grid(True)
        plt.legend()
        plt.show()
    else:
        print("Available CSV files:")
        for i, file in enumerate(files):
            print(f"{i + 1}. {file}")

        selected_files = input("Enter the numbers of the files you want to plot (separated by spaces): ").split()
        selected_files = [int(num) - 1 for num in selected_files]

        same_plot = input("Do you want to plot all selected files on the same plot? (yes/no): ").lower() == 'yes'

        # Load the first selected file to get column names
        first_file_path = os.path.join(directory_path, files[selected_files[0]])
        first_data = read_csv(first_file_path)
        print("Available columns:")
        print(first_data.columns)

        x_column = input("Enter the column name for the x-axis: ")
        y_column = input("Enter the column name for the y-axis: ")

        log_x = input("Apply logarithmic filter to x-axis? (yes/no): ").lower() == 'yes'
        log_y = input("Apply logarithmic filter to y-axis? (yes/no): ").lower() == 'yes'

        if same_plot:
            plt.figure(figsize=(10, 6))
            for index in selected_files:
                file_path = os.path.join(directory_path, files[index])
                data = read_csv(file_path)
                plot_data(data, x_column, y_column, log_x, log_y, label=files[index])
            plt.xlabel(x_column)
            plt.ylabel(y_column)
            plt.title(f'Plot of {y_column} vs {x_column}')
            if log_x:
                plt.xlabel(f'Log(|{x_column}|)')
            if log_y:
                plt.ylabel(f'Log(|{y_column}|)')
            plt.grid(True)
            plt.legend()
            plt.show()
        else:
            for index in selected_files:
                file_path = os.path.join(directory_path, files[index])
                data = read_csv(file_path)
                plt.figure(figsize=(10, 6))
                plot_data(data, x_column, y_column, log_x, log_y, label=files[index])
                plt.xlabel(x_column)
                plt.ylabel(y_column)
                plt.title(f'Plot of {y_column} vs {x_column} from {files[index]}')
                if log_x:
                    plt.xlabel(f'Log(|{x_column}|)')
                if log_y:
                    plt.ylabel(f'Log(|{y_column}|)')
                plt.grid(True)
                plt.legend()
                plt.show()

