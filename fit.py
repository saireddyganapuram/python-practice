import tkinter as tk
from tkinter import filedialog, messagebox, simpledialog  # Import simpledialog
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

class FitnessTrackerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Personalized Fitness Tracker")

        # UI components
        self.label = tk.Label(root, text="Upload a CSV File with Fitness Data")
        self.label.pack(pady=10)

        self.upload_button = tk.Button(root, text="Browse File", command=self.browse_file)
        self.upload_button.pack(pady=5)

        self.add_entry_button = tk.Button(root, text="Add Daily Entry", command=self.add_daily_entry)
        self.add_entry_button.pack(pady=5)

        self.view_data_button = tk.Button(root, text="View Fitness Data", command=self.view_fitness_data)
        self.view_data_button.pack(pady=5)

        self.plot_steps_button = tk.Button(root, text="Plot Steps", command=self.plot_steps)
        self.plot_steps_button.pack(pady=5)

        self.plot_calories_button = tk.Button(root, text="Plot Calories", command=self.plot_calories)
        self.plot_calories_button.pack(pady=5)

        self.plot_workout_button = tk.Button(root, text="Plot Workout Duration", command=self.plot_workout_duration)
        self.plot_workout_button.pack(pady=5)

        self.filepath = None
        self.fitness_data = None

    def browse_file(self):
        # Open file dialog to select a CSV file
        self.filepath = filedialog.askopenfilename(
            title="Open CSV File",
            filetypes=[("CSV Files", "*.csv")]
        )
        if self.filepath:
            self.label.config(text=f"Selected File: {self.filepath}")
            self.fitness_data = pd.read_csv(self.filepath)

    def add_daily_entry(self):
        if self.fitness_data is None:
            messagebox.showerror("Error", "Please select a file first!")
            return

        # Get user input for a new daily entry
        date = datetime.now().strftime("%Y-%m-%d")
        steps = int(self._prompt_user("Enter steps taken:"))
        calories = int(self._prompt_user("Enter calories burned:"))
        workout_duration = int(self._prompt_user("Enter workout duration (minutes):"))

        # Add new entry to DataFrame
        new_entry = pd.DataFrame({
            "Date": [date],
            "Steps": [steps],
            "Calories": [calories],
            "WorkoutDuration": [workout_duration]
        })
        self.fitness_data = pd.concat([self.fitness_data, new_entry], ignore_index=True)

        # Save updated data to CSV
        self.fitness_data.to_csv(self.filepath, index=False)
        messagebox.showinfo("Entry Added", "Your daily entry has been added successfully!")

    def _prompt_user(self, prompt):
        # Helper function to prompt the user for input
        return simpledialog.askstring("Input", prompt)

    def view_fitness_data(self):
        if self.fitness_data is None:
            messagebox.showerror("Error", "Please select a file first!")
            return

        # Display the first 10 rows of the fitness data
        fitness_text = self.fitness_data.tail(10).to_string(index=False)
        messagebox.showinfo("Fitness Data", fitness_text)

    def plot_steps(self):
        if self.fitness_data is None:
            messagebox.showerror("Error", "Please select a file first!")
            return

        # Plot steps over time
        plt.figure(figsize=(10, 6))
        plt.plot(self.fitness_data['Date'], self.fitness_data['Steps'], marker='o', color='blue')
        plt.title("Steps Over Time")
        plt.xlabel("Date")
        plt.ylabel("Steps")
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()

    def plot_calories(self):
        if self.fitness_data is None:
            messagebox.showerror("Error", "Please select a file first!")
            return

        # Plot calories over time
        plt.figure(figsize=(10, 6))
        plt.plot(self.fitness_data['Date'], self.fitness_data['Calories'], marker='o', color='green')
        plt.title("Calories Burned Over Time")
        plt.xlabel("Date")
        plt.ylabel("Calories")
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()

    def plot_workout_duration(self):
        if self.fitness_data is None:
            messagebox.showerror("Error", "Please select a file first!")
            return

        # Plot workout duration over time
        plt.figure(figsize=(10, 6))
        plt.plot(self.fitness_data['Date'], self.fitness_data['WorkoutDuration'], marker='o', color='red')
        plt.title("Workout Duration Over Time")
        plt.xlabel("Date")
        plt.ylabel("Workout Duration (minutes)")
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()

# Run the application
if __name__ == "__main__":
    root = tk.Tk()
    app = FitnessTrackerApp(root)
    root.mainloop()
