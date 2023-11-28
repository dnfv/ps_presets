import os
import shutil
import json
from tkinter import Tk, Label, Entry, Button, filedialog, Frame, N, S, E, W

class FileCopyApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Aplikasi Preset Photoshop")

        # Load configuration if available
        self.load_configuration()

        # Set the initial size of the window
        root.geometry("900x450")  # You can adjust the width and height as needed

        # Bind the <Destroy> event to the save_configuration method
        root.protocol("WM_DELETE_WINDOW", self.on_close)        

        self.target_path_label = Label(root, text="Photoshop Settings:")
        self.target_path_label.grid(row=0, column=0, padx=10, pady=10, sticky=W)
        self.target_path_entry = Entry(root)
        self.target_path_entry.grid(row=0, column=1, padx=10, pady=10, sticky=W+E)
        self.target_path_button = Button(root, text="Browse", command=self.browse_target_path)
        self.target_path_button.grid(row=0, column=2, padx=10, pady=10)

        self.path1_label = Label(root, text="Path 1:")
        self.path1_label.grid(row=1, column=0, padx=10, pady=10, sticky=W)
        self.path1_entry = Entry(root)
        self.path1_entry.grid(row=1, column=1, padx=10, pady=10, sticky=W+E)
        self.path1_button = Button(root, text="Browse", command=self.browse_path1)
        self.path1_button.grid(row=1, column=2, padx=10, pady=10)

        self.path2_label = Label(root, text="Path 2:")
        self.path2_label.grid(row=2, column=0, padx=10, pady=10, sticky=W)
        self.path2_entry = Entry(root)
        self.path2_entry.grid(row=2, column=1, padx=10, pady=10, sticky=W+E)
        self.path2_button = Button(root, text="Browse", command=self.browse_path2)
        self.path2_button.grid(row=2, column=2, padx=10, pady=10)

        self.path3_label = Label(root, text="Path 3:")
        self.path3_label.grid(row=3, column=0, padx=10, pady=10, sticky=W)
        self.path3_entry = Entry(root)
        self.path3_entry.grid(row=3, column=1, padx=10, pady=10, sticky=W+E)
        self.path3_button = Button(root, text="Browse", command=self.browse_path3)
        self.path3_button.grid(row=3, column=2, padx=10, pady=10)

        self.path4_label = Label(root, text="Path 4:")
        self.path4_label.grid(row=4, column=0, padx=10, pady=10, sticky=W)
        self.path4_entry = Entry(root)
        self.path4_entry.grid(row=4, column=1, padx=10, pady=10, sticky=W+E)
        self.path4_button = Button(root, text="Browse", command=self.browse_path4)
        self.path4_button.grid(row=4, column=2, padx=10, pady=10)

        self.path5_label = Label(root, text="Backup Location:")
        self.path5_label.grid(row=5, column=0, padx=10, pady=10, sticky=W)
        self.path5_entry = Entry(root)
        self.path5_entry.grid(row=5, column=1, padx=10, pady=10, sticky=W+E)
        self.path5_button = Button(root, text="Browse", command=self.browse_path5)
        self.path5_button.grid(row=5, column=2, padx=10, pady=10)

        self.path6_label = Label(root, text="Path 6:")
        self.path6_label.grid(row=6, column=0, padx=10, pady=10, sticky=W)
        self.path6_entry = Entry(root)
        self.path6_entry.grid(row=6, column=1, padx=10, pady=10, sticky=W+E)
        self.path6_button = Button(root, text="Browse", command=self.browse_path6)
        self.path6_button.grid(row=6, column=2, padx=10, pady=10)

        self.path7_label = Label(root, text="Path 7:")
        self.path7_label.grid(row=7, column=0, padx=10, pady=10, sticky=W)
        self.path7_entry = Entry(root)
        self.path7_entry.grid(row=7, column=1, padx=10, pady=10, sticky=W+E)
        self.path7_button = Button(root, text="Browse", command=self.browse_path7)
        self.path7_button.grid(row=7, column=2, padx=10, pady=10)

        # Initialize Entry widgets with saved values
        self.target_path_entry.insert(0, self.config.get("target_path", ""))
        self.path1_entry.insert(0, self.config.get("path1", ""))
        self.path2_entry.insert(0, self.config.get("path2", ""))
        self.path3_entry.insert(0, self.config.get("path3", ""))
        self.path4_entry.insert(0, self.config.get("path4", ""))
        self.path5_entry.insert(0, self.config.get("path5", ""))
        self.path6_entry.insert(0, self.config.get("path6", ""))
        self.path7_entry.insert(0, self.config.get("path7", ""))

        # Add similar widgets for Path 2 and Path 3

        # Create a frame for the buttons
        button_frame = Frame(root)
        button_frame.grid(row=8, column=0, columnspan=3, pady=10)

        self.copy_button1 = Button(button_frame, text="Path 1 Act", command=lambda: self.copy_and_replace(1))
        self.copy_button1.grid(row=0, column=0, padx=10)

        self.copy_button2 = Button(button_frame, text="Path 2 Act", command=lambda: self.copy_and_replace(2))
        self.copy_button2.grid(row=0, column=1, padx=10)

        self.copy_button3 = Button(button_frame, text="Path 3 Act", command=lambda: self.copy_and_replace(3))
        self.copy_button3.grid(row=0, column=2, padx=10)

        self.copy_button4 = Button(button_frame, text="Path 4 Act", command=lambda: self.copy_and_replace(4))
        self.copy_button4.grid(row=0, column=3, padx=10)

        self.copy_button5 = Button(button_frame, text="Settings -> Backup", command=lambda: self.backup_settings(5))
        self.copy_button5.grid(row=0, column=4, padx=10)

        self.copy_button6 = Button(button_frame, text="Path 6 Act", command=lambda: self.copy_and_replace(6))
        self.copy_button6.grid(row=1, column=0, padx=10)

        self.copy_button7 = Button(button_frame, text="Path 7 Act", command=lambda: self.copy_and_replace(7))
        self.copy_button7.grid(row=1, column=1, padx=10)

        # Configure column to expand
        root.columnconfigure(1, weight=1)  # column 1 contains the entry fields

    def load_configuration(self):
        # Load configuration from a file
        config_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "config.json")
        try:
            with open(config_path, "r") as config_file:
                self.config = json.load(config_file)
        except FileNotFoundError:
            # If the file is not found, initialize with default values
            self.config = {}
    
    def save_configuration(self):
        # Save configuration to a file
        config_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "config.json")
        with open(config_path, "w") as config_file:
            json.dump({
                "target_path": self.target_path_entry.get(),
                "path1": self.path1_entry.get(),
                "path2": self.path2_entry.get(),
                "path3": self.path3_entry.get(),
                "path4": self.path4_entry.get(),
                "path5": self.path5_entry.get(),
                "path6": self.path6_entry.get(),
                "path7": self.path7_entry.get(),
            }, config_file)

        print("Configuration saved.")
        
    def browse_target_path(self):
        folder_selected = filedialog.askdirectory()
        self.target_path_entry.delete(0, 'end')
        self.target_path_entry.insert(0, folder_selected)
        self.save_configuration()

    def browse_path1(self):
        folder_selected = filedialog.askdirectory()
        self.path1_entry.delete(0, 'end')
        self.path1_entry.insert(0, folder_selected)
        self.save_configuration()

    def browse_path2(self):
        folder_selected = filedialog.askdirectory()
        self.path2_entry.delete(0, 'end')
        self.path2_entry.insert(0, folder_selected)
        self.save_configuration()

    def browse_path3(self):
        folder_selected = filedialog.askdirectory()
        self.path3_entry.delete(0, 'end')
        self.path3_entry.insert(0, folder_selected)
        self.save_configuration()

    def browse_path4(self):
        folder_selected = filedialog.askdirectory()
        self.path4_entry.delete(0, 'end')
        self.path4_entry.insert(0, folder_selected)
        self.save_configuration()

    def browse_path5(self):
        folder_selected = filedialog.askdirectory()
        self.path5_entry.delete(0, 'end')
        self.path5_entry.insert(0, folder_selected)
        self.save_configuration()
    
    def browse_path6(self):
        folder_selected = filedialog.askdirectory()
        self.path6_entry.delete(0, 'end')
        self.path6_entry.insert(0, folder_selected)
        self.save_configuration()

    def browse_path7(self):
        folder_selected = filedialog.askdirectory()
        self.path7_entry.delete(0, 'end')
        self.path7_entry.insert(0, folder_selected)
        self.save_configuration()

    # Add similar functions for browsing Path 2 and Path 3

    def copy_and_replace(self, path_number):
        target_path = self.target_path_entry.get()
        source_path = getattr(self, f"path{path_number}_entry").get()

        try:
            for root, dirs, files in os.walk(source_path):
                relative_path = os.path.relpath(root, source_path)
                target_folder = os.path.join(target_path, relative_path)
                os.makedirs(target_folder, exist_ok=True)
                for file in files:
                    source_file = os.path.join(root, file)
                    target_file = os.path.join(target_folder, file)
                    shutil.copy2(source_file, target_file)
            print(f"Files copied from Path {path_number} to Target Path.")
        except Exception as e:
            print(f"Error copying files: {e}")

    def backup_settings(self, path_number):
        source_path = self.target_path_entry.get()
        target_path = folder_selected = filedialog.askdirectory()

        try:
            for root, dirs, files in os.walk(source_path):
                relative_path = os.path.relpath(root, source_path)
                target_folder = os.path.join(target_path, relative_path)
                os.makedirs(target_folder, exist_ok=True)
                for file in files:
                    source_file = os.path.join(root, file)
                    target_file = os.path.join(target_folder, file)
                    shutil.copy2(source_file, target_file)
            print(f"PS Settings has been copied to Backup")
        except Exception as e:
            print(f"Error copying files: {e}")

    def on_close(self):
        # Callback function to handle the window closing event
        self.save_configuration()
        self.root.destroy()

if __name__ == "__main__":
    root = Tk()
    app = FileCopyApp(root)
    root.mainloop()
