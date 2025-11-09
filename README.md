# 🗜️ Smart File Zipper & Unzipper  
*A DAA (Design and Analysis of Algorithms) Project by [Your Name]*

---

## 📘 Introduction
The **Smart File Zipper & Unzipper** is a desktop-based Python application that enables users to **compress and extract files or folders** easily.  
It combines **algorithmic efficiency** (using Python’s built-in ZipFile module) with an interactive **Tkinter GUI**, making it a practical implementation of **file compression algorithms** taught under **DAA**.

---

## 🎯 Objectives
- To apply algorithmic principles in real-world file compression.
- To design a user-friendly GUI for file zipping and unzipping.
- To improve storage efficiency and file transfer performance.
- To demonstrate how time and space complexities impact compression processes.

---

## 📚 Literature Review
File compression is a classic algorithmic problem that reduces data size using redundancy elimination techniques.  
Common algorithms like **Huffman Encoding**, **LZ77**, and **Deflate** form the basis for tools like ZIP and GZIP.  
In this project, we use **Python’s ZipFile module**, which internally applies these optimized algorithms efficiently.

---

## ⚙️ Requirements

### Software Requirements
- **Python 3.8+**
- **Tkinter**
- **Pillow (PIL)**
- **OS & ZipFile (built-in libraries)**

### Hardware Requirements
- Minimum 4 GB RAM  
- 200 MB free disk space  
- Windows/Linux/MacOS

---

## 🧩 Implementation

### Step 1: Interface Design
Tkinter was used to create an interactive GUI.  
The interface includes:
- Buttons for *Select File*, *Zip*, *Unzip*, and *Exit*  
- A *progress bar* to visualize compression progress  
- Dynamic background image that auto-resizes

### Step 2: Algorithm Workflow
```python
if os.path.isfile(selected_path):
    zipf.write(selected_path, os.path.basename(selected_path))
else:
    for foldername, subfolders, filenames in os.walk(selected_path):
        for filename in filenames:
            zipf.write(file_path, arcname)
