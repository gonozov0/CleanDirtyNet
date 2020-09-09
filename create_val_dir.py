import os
import shutil 
from tqdm import tqdm

data_root = 'plates/'

train_dir = 'train'
val_dir = 'val'

class_names = ['cleaned', 'dirty']

for class_name in class_names:
    os.makedirs(os.path.join(data_root, val_dir, class_name), exist_ok=True)

for class_name in class_names:
    source_dir = os.path.join(data_root, train_dir, class_name)
    dest_dir = os.path.join(data_root, val_dir, class_name)
    for i, file_name in enumerate(tqdm(os.listdir(source_dir))):
        if i % 6 == 0:
            shutil.move(os.path.join(source_dir, file_name), os.path.join(dest_dir, file_name))