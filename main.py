from ultralytics import YOLO  # If you don't have ultralytics, install it by typing "pip install ultralytics" on the terminal and hit enter

MODEL_PATH = "./License-Plate-Detector/results/runs/detect/train/weights/best.pt"  # Specify absolute path to last.pt or best.pt

MODEL = YOLO(MODEL_PATH)

results = MODEL(source='check the possible options in the source list', save=True, show_labels=True, save_crop=True)