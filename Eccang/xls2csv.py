import os
from pathlib import Path
from config_paths import get_eccang_paths

paths = get_eccang_paths()

def xls2csv():
    # Set the target folder path
    folder_path = paths["downloads"]

    # Find all matching files
    matched_files = []
    for filename in os.listdir(folder_path):
        if "库存查询（库位）" in filename and filename.lower().endswith('.xls'):
            full_path = os.path.join(folder_path, filename)
            matched_files.append((full_path, os.path.getmtime(full_path)))

    # If there are matching files, find the most recent one
    if matched_files:
        # Sort by modification time 
        matched_files.sort(key=lambda x: x[1], reverse=True)
        latest_file = matched_files[0][0]

        # Construct .csv 
        new_path = os.path.splitext(latest_file)[0] + '.csv'

        try:
            os.rename(latest_file, new_path)
            print(f"✅ Latest file renamed to CSV:\n{latest_file} → {new_path}")
        except Exception as e:
            print(f"❌ Rename failed: {e}")
    else:
        print("📌 No .xls file found containing '库存查询（库位）'")

'''
if __name__ == "__main__":
    rename()
'''