import os
import hashlib
import pandas as pd
from datasets import load_dataset
from PIL import Image
import imagehash

SEED = 42
os.makedirs("splits", exist_ok=True)

print("Pobieranie zbioru Beans (ibean)...")
dataset = load_dataset("AI-Lab-Makerere/beans")

splits = ["train", "validation", "test"]
records = []
split_filenames = {
    "train": "splits/train_ids.txt",
    "validation": "splits/validation_ids.txt",
    "test": "splits/final_test_ids.txt"
}

for split_name in splits:
    split_data = dataset[split_name]
    id_list = []
    
    for idx, sample in enumerate(split_data):
        img: Image.Image = sample["image"]
        label = sample["labels"]
        class_name = split_data.features["labels"].int2str(label)
        
        sample_id = f"{split_name}_{idx:04d}_{class_name}"
        id_list.append(sample_id)
        
        img_bytes = img.tobytes()
        records.append({
            "sample_id": sample_id,
            "split": split_name,
            "label_id": label,
            "class_name": class_name,
            "width": img.width,
            "height": img.height,
            "channels": len(img.getbands()),
            "md5": hashlib.md5(img_bytes).hexdigest(),
            "phash": str(imagehash.phash(img))
        })
    
    out_file = split_filenames[split_name]
    with open(out_file, "w", encoding="utf-8") as f:
        for s_id in id_list:
            f.write(f"{s_id}\n")
    print(f"Zapisano {len(id_list)} identyfikatorow do {out_file}")

df = pd.DataFrame(records)

print("\n" + "="*50)
print("WYNIKI AUDYTU:")
print("="*50)

print("\n1. Rozklad klas:")
print(pd.crosstab(df["split"], df["class_name"], margins=True))

print("\n2. Wymiary obrazow:")
print(f"Szerokosc: {df['width'].unique()}, Wysokosc: {df['height'].unique()}, Kanaly: {df['channels'].unique()}")

print("\n3. Braki danych:")
print(df.isnull().sum())

md5_counts = df["md5"].value_counts()
exact_dupes = md5_counts[md5_counts > 1]
print(f"\n4. Dokladne duplikaty (MD5): {len(exact_dupes)}")

print("\n5. Sprawdzanie podobienstwa miedzy podzialami (pHash <= 2)...")
leakage_count = 0
for i in range(len(df)):
    for j in range(i + 1, len(df)):
        if df.iloc[i]["split"] != df.iloc[j]["split"]:
            h1 = imagehash.hex_to_hash(df.iloc[i]["phash"])
            h2 = imagehash.hex_to_hash(df.iloc[j]["phash"])
            if (h1 - h2) <= 2:
                print(f"Podejrzenie: {df.iloc[i]['sample_id']} <-> {df.iloc[j]['sample_id']} [d={h1-h2}]")
                leakage_count += 1

print(f"Liczba podejrzanych par miedzy podzialami: {leakage_count}")