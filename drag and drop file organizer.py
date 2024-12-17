    # UI Components
    Label(self, text="Drag and drop files below:", font=("Arial", 14)).pack(pady=10)
    self.drop_area = Label(self, text="Drop files here", bg="lightgray", width=50, height=10, relief="sunken")
    self.drop_area.pack(pady=10)
    self.drop_area.drop_target_register(DND_FILES)
    self.drop_area.dnd_bind("<Drop>", self.add_files)
    
    Button(self, text="Start Sorting", command=self.sort_files, bg="green", fg="white").pack(pady=10)
    Button(self, text="Exit", command=self.quit, bg="red", fg="white").pack(pady=10)

def add_files(self, event):
    # Add dropped files to the list
    dropped_files = self.split_files(event.data)
    self.files.extend(dropped_files)
    messagebox.showinfo("Files Added", f"Added {len(dropped_files)} files!")

@staticmethod
def split_files(file_data):
    # Handle multiple file paths
    return file_data.split(" ")

def sort_files(self):
    if not self.files:
        messagebox.showwarning("No Files", "No files to organize. Drag and drop files first.")
        return

    # Define file categories
    categories = {
        "Images": [".png", ".jpg", ".jpeg", ".gif"],
        "Documents": [".pdf", ".docx", ".txt"],
        "Videos": [".mp4", ".avi"],
        "Music": [".mp3", ".wav"]
    }

    # Create directories and move files
    for file in self.files:
        file_extension = os.path.splitext(file)[1].lower()
        moved = False
        for category, extensions in categories.items():
            if file_extension in extensions:
                self.move_file(file, category)
                moved = True
                break

        if not moved:
            self.move_file(file, "Others")

    messagebox.showinfo("Sorting Complete", "Files have been organized successfully!")
    self.files = []

@staticmethod
def move_file(file, folder_name):
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)
    shutil.move(file, os.path.join(folder_name, os.path.basename(file)))
