import tkinter as tk
from tkinter import ttk
from tkinter.filedialog import askopenfilename
from PIL import Image, ImageTk
import cv2
import numpy as np
import joblib   # <-- scikit-learn model loader

root = tk.Tk()
root.configure(background="seashell2")
w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (w, h))
root.title("Road Pathole Detection")

lbl = tk.Label(root, text="Road Pathole Detection", font=('times', 35,' bold '),
               width=65, height=1, bg="Red3", fg="white")
lbl.place(x=0, y=0)

frame_alpr = tk.LabelFrame(root, text=" --Process-- ", width=220, height=350,
                           bd=5, font=('times', 14, ' bold '), bg="SeaGreen1")
frame_alpr.place(x=10, y=100)

fn = ""

def update_label(msg):
    result_label = tk.Label(root, text=msg, width=40, font=("bold", 25),
                            bg='bisque2', fg='black')
    result_label.place(x=300, y=420)

def openimage():
    global fn
    fileName = askopenfilename(title='Select image for Analysis',
                               filetypes=[("Image files", "*.jpg;*.png;*.jpeg")])
    fn = fileName
    if fn:
        img = Image.open(fn).resize((200, 200))
        imgtk = ImageTk.PhotoImage(img)
        img_label = tk.Label(root, text='Original', font=('times new roman', 20 ,'bold'),
                             image=imgtk, compound='bottom', height=250, width=250)
        img_label.image = imgtk
        img_label.place(x=300, y=100)

def convert_grey():
    global fn
    if not fn: return
    img = cv2.imread(fn, 1)
    gs = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    retval, threshold = cv2.threshold(gs, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

    for arr, title, xpos in [(gs, "Gray", 580), (threshold, "Binary", 880)]:
        im = Image.fromarray(arr)
        imgtk = ImageTk.PhotoImage(image=im)
        lbl = tk.Label(root, text=title, font=('times new roman', 20 ,'bold'),
                       image=imgtk, compound='bottom', height=250, width=250)
        lbl.image = imgtk
        lbl.place(x=xpos, y=100)

def test_model_proc(fn):
    # Load scikit-learn model
    model = joblib.load("road_model.pkl")   # <-- trained & saved separately
    img = Image.open(fn).resize((64, 64))
    img = np.array(img).reshape(1, -1)      # flatten for scikit-learn
    prediction = model.predict(img)[0]
    return "Pathole Detected" if prediction == 1 else "Pathole not Detected"

def test_model():
    global fn
    if fn:
        update_label("Model Testing Start...")
        result = test_model_proc(fn)
        update_label("Result: " + result)
        fn = ""
    else:
        update_label("Please Select Image For Prediction...")

def window():
    root.destroy()

# Buttons
tk.Button(frame_alpr, text="Select Image", command=openimage,
          width=15, height=1, font=('times', 15, ' bold ')).place(x=10, y=50)
tk.Button(frame_alpr, text="Image Preprocess", command=convert_grey,
          width=15, height=1, font=('times', 15, ' bold ')).place(x=10, y=120)
tk.Button(frame_alpr, text="Prediction", command=test_model,
          width=15, height=1, font=('times', 15, ' bold ')).place(x=10, y=190)
tk.Button(frame_alpr, text="Exit", command=window,
          width=15, height=1, font=('times', 15, ' bold '), bg="red", fg="white").place(x=10, y=260)

root.mainloop()

# train_model.py
import os
import numpy as np
from PIL import Image
from sklearn.ensemble import RandomForestClassifier
import joblib

# Path to your dataset folders
# Example: pothole images in "train/1", non-pothole images in "train/0"
data_dir = "train"

X = []
y = []

IMAGE_SIZE = 64

for label in ["0", "1"]:  # 0 = no pothole, 1 = pothole
    folder = os.path.join(data_dir, label)
    for fname in os.listdir(folder):
        if fname.lower().endswith((".jpg", ".png", ".jpeg")):
            path = os.path.join(folder, fname)
            img = Image.open(path).resize((IMAGE_SIZE, IMAGE_SIZE))
            arr = np.array(img).flatten()  # flatten for scikit-learn
            X.append(arr)
            y.append(int(label))

X = np.array(X)
y = np.array(y)

# Train a simple RandomForest classifier
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X, y)

# Save the model
joblib.dump(model, "road_model.pkl")
print("Model saved as road_model.pkl")
