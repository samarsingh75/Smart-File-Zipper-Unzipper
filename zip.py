import os
import zipfile
import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from PIL import Image, ImageTk  # for background image

# ------------- MAIN APP CLASS -----------------
class FileZipperApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Smart File Zipper & Unzipper")
        self.root.geometry("800x500")
        self.root.minsize(700, 400)
        self.root.config(bg="#1e1e2e")

        # ----- Background Image -----
        self.bg_image_original = Image.open(r"C:\Users\srija\Projc\background.png")
        self.bg_photo = ImageTk.PhotoImage(self.bg_image_original)
        self.bg_label = tk.Label(root, image=self.bg_photo)
        self.bg_label.place(x=0, y=0, relwidth=1, relheight=1)
        self.bg_label.lower()

        # Bind resize event to auto-fit image
        self.root.bind("<Configure>", self.resize_background)

        # ---------- Project Title ----------
        tk.Label(root,
                 text="🗜️ File Compression & Extraction Utility",
                 font=("Segoe UI", 20, "bold"),
                 bg="#000000", fg="#00ffff",  # cyan title on black strip
                 pady=10).pack(fill="x")

        # ---------- Center Frame ----------
        center_frame = tk.Frame(root, bg="#1a1a1a")
        center_frame.place(relx=0.5, rely=0.5, anchor="center")

        tk.Label(center_frame, text="Smart File Zipper / Unzipper",
                 font=("Segoe UI", 18, "bold"), bg="#1a1a1a", fg="#ffffff").pack(pady=10)

        # Buttons Frame
        frame = tk.Frame(center_frame, bg="#1a1a1a")
        frame.pack(pady=10)

        style = ttk.Style()
        style.configure("TButton", font=("Segoe UI", 11, "bold"), padding=6)

        ttk.Button(frame, text="Select File / Folder", command=self.select_file).grid(row=0, column=0, padx=10, pady=10)
        ttk.Button(frame, text="Zip", command=self.zip_files).grid(row=0, column=1, padx=10, pady=10)
        ttk.Button(frame, text="Unzip", command=self.unzip_file).grid(row=0, column=2, padx=10, pady=10)
        ttk.Button(frame, text="Exit", command=root.quit).grid(row=0, column=3, padx=10, pady=10)

        # Progress Bar
        self.progress = ttk.Progressbar(center_frame, length=500, mode='determinate')
        self.progress.pack(pady=20)

        # Status Label
        self.status_label = tk.Label(center_frame, text="No file selected.",
                                     font=("Segoe UI", 12), bg="#1a1a1a", fg="#cccccc")
        self.status_label.pack(pady=10)

        self.selected_path = ""

    # ------------ Auto resize background ---------------
    def resize_background(self, event):
        new_width = event.width
        new_height = event.height
        resized = self.bg_image_original.resize((new_width, new_height), Image.LANCZOS)
        self.bg_photo = ImageTk.PhotoImage(resized)
        self.bg_label.config(image=self.bg_photo)
        self.bg_label.image = self.bg_photo  # prevent garbage collection

    # ------------ SELECT FILE / FOLDER ---------------
    def select_file(self):
        path = filedialog.askopenfilename(title="Select File or Folder")
        if not path:
            path = filedialog.askdirectory(title="Select Folder")
        if path:
            self.selected_path = path
            self.status_label.config(text=f"Selected: {path}")

    # ------------ ZIP FUNCTION ---------------
    def zip_files(self):
        if not self.selected_path:
            messagebox.showwarning("Warning", "Please select a file or folder first.")
            return

        output_path = filedialog.asksaveasfilename(defaultextension=".zip",
                                                   filetypes=[("ZIP files", "*.zip")],
                                                   title="Save Compressed File As")
        if not output_path:
            return

        self.progress["value"] = 0
        self.status_label.config(text="Zipping in progress...")

        try:
            with zipfile.ZipFile(output_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
                if os.path.isfile(self.selected_path):
                    zipf.write(self.selected_path, os.path.basename(self.selected_path))
                else:
                    for foldername, subfolders, filenames in os.walk(self.selected_path):
                        for filename in filenames:
                            file_path = os.path.join(foldername, filename)
                            arcname = os.path.relpath(file_path, os.path.dirname(self.selected_path))
                            zipf.write(file_path, arcname)
                            self.progress["value"] += 5
                            self.root.update_idletasks()

            self.progress["value"] = 100
            self.status_label.config(text=f"✅ File successfully zipped to: {output_path}")
            messagebox.showinfo("Success", f"File successfully zipped!\nSaved at:\n{output_path}")

        except Exception as e:
            messagebox.showerror("Error", f"Zipping failed!\n{e}")

    # ------------ UNZIP FUNCTION ---------------
    def unzip_file(self):
        file_path = filedialog.askopenfilename(title="Select ZIP File", filetypes=[("ZIP files", "*.zip")])
        if not file_path:
            return

        extract_path = filedialog.askdirectory(title="Select Destination Folder")
        if not extract_path:
            return

        self.progress["value"] = 0
        self.status_label.config(text="Unzipping in progress...")

        try:
            with zipfile.ZipFile(file_path, 'r') as zip_ref:
                zip_ref.extractall(extract_path)
                for i in range(0, 101, 10):
                    self.progress["value"] = i
                    self.root.update_idletasks()

            self.status_label.config(text=f"✅ Files extracted to: {extract_path}")
            messagebox.showinfo("Success", f"Files successfully extracted to:\n{extract_path}")

        except Exception as e:
            messagebox.showerror("Error", f"Unzipping failed!\n{e}")

# ------------- RUN APP -----------------
if __name__ == "__main__":
    root = tk.Tk()
    app = FileZipperApp(root)
    root.mainloop()
