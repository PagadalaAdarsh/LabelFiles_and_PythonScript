import cv2
import os

# --- Paths (update if needed) ---
video_path = "C:/Users/adars/Downloads/FireTruckRecording_Resolution.mp4"     
labels_dir = r"C:\Users\adars\Downloads\Updated_Yolo_Truck\obj_train_data"
names_path = r"C:\Users\adars\Downloads\Updated_Yolo_Truck\obj.names"
output_video_path = "C:/Users/adars/Downloads/output_labeled_video.mp4"

# --- Load class names ---
class_names = []
with open(names_path, 'r') as f:
    class_names = [line.strip() for line in f.readlines()]

# --- Colors for bounding boxes ---
colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (0, 255, 255), 
          (255, 0, 255), (128, 0, 0), (0, 128, 0), (0, 0, 128), (128, 128, 0)]

# --- Video setup ---
cap = cv2.VideoCapture(video_path)
if not cap.isOpened():
    print("❌ Error: Could not open input video.")
    exit()

frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = cap.get(cv2.CAP_PROP_FPS)

fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter(output_video_path, fourcc, fps, (frame_width, frame_height))

frame_number = 0

while True:
    ret, frame = cap.read()
    if not ret:
        break

    label_filename = f"frame_{frame_number:06d}.txt"
    label_path = os.path.join(labels_dir, label_filename)

    if os.path.exists(label_path):
        with open(label_path, 'r') as f:
            for line in f:
                parts = line.strip().split()
                if len(parts) == 5:
                    class_id, x_center, y_center, width, height = map(float, parts)
                    class_id = int(class_id)

                    # Convert YOLO to pixel coords
                    x1 = int((x_center - width / 2) * frame_width)
                    y1 = int((y_center - height / 2) * frame_height)
                    x2 = int((x_center + width / 2) * frame_width)
                    y2 = int((y_center + height / 2) * frame_height)

                    color = colors[class_id % len(colors)]
                    label = class_names[class_id] if class_id < len(class_names) else f"class_{class_id}"

                    # Draw box and label
                    cv2.rectangle(frame, (x1, y1), (x2, y2), color, 2)
                    cv2.putText(frame, label, (x1, max(y1 - 10, 0)), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)

    out.write(frame)
    frame_number += 1

cap.release()
out.release()
cv2.destroyAllWindows()

print(f"✅ Labeled video saved at: {output_video_path}")
