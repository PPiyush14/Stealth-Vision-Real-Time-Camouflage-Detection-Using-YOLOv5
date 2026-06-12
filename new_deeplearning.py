import zipfile
import os

zip_path = (r"E:\Projects\Deep Learning\Camouflage_Detection\Dataset\camouflage detection.v1i.yolov5pytorch.zip")
extract_dir = "dataset"

# Extract ZIP
with zipfile.ZipFile(zip_path, 'r') as zip_ref:
    zip_ref.extractall(extract_dir)

print("✅ Extracted to:", extract_dir)

# Print directory tree
for root, dirs, files in os.walk(extract_dir):
    level = root.replace(extract_dir, "").count(os.sep)
    indent = " " * 4 * level
    print(f"{indent}{os.path.basename(root)}/")
    sub_indent = " " * 4 * (level + 1)
    for f in files:
        print(f"{sub_indent}{f}")
updated_yaml = """
train: C:/Users/cl502_19/Downloads/dataset/train/images
val: C:/Users/cl502_19/Downloads/dataset/valid/images
test: C:/Users/cl502_19/Downloads/dataset/test/images

nc: 1

names: ['camouflage']

"""

with open("dataset/data.yaml", "w") as f:
    f.write(updated_yaml.strip())

print("✅ data.yaml updated")
import os
os.environ["WANDB_DISABLED"] = "true"



os.system("python train.py --img 640 --batch 32 --epochs 100 --data C:/Users/cl502_19/Downloads/dataset/data.yaml --weight yolov5l.pt --cache --workers 4")

 # for testing - python "E:\Projects\Deep Learning\Model VS\yolov5\detect.py" --weights "E:\Projects\Deep Learning\Model VS\yolov5\best.pt" --img 640 --conf 0.25 --source "C:\Users\piyus\Downloads\test1.jpg"
