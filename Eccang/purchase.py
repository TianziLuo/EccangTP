import os
import glob
import shutil
from pathlib import Path
from datetime import datetime
from config_paths import get_eccang_paths

paths = get_eccang_paths()

def clean_folder():
    """
    Delete old .xlsx / .csv files in the purchase_path directory.
    """
    folder_paths = paths["purchase_path"]
    if isinstance(folder_paths, (str, Path)):
        folder_paths = [Path(folder_paths)]

    file_patterns = ['*.xlsx', '*.csv']

    for folder_path in folder_paths:
        folder_path = Path(folder_path)
        if not folder_path.exists():
            print(f"Skipping (not found): {folder_path}")
            continue

        print(f"\n🧹 Cleaning folder: {folder_path}")
        files_to_delete = []
        for pattern in file_patterns:
            files_to_delete.extend(glob.glob(str(folder_path / pattern)))

        if not files_to_delete:
            print("No files to delete.")
            continue

        for file in files_to_delete:
            try:
                os.remove(file)
                print(f"Deleted: {file}")
            except Exception as e:
                print(f"Failed to delete: {file}, Reason: {e}")


def copy_purchase():
    """
    Copy today's purchase CSV files from downloads to purchase_path.
    """
    download_dir = Path(paths["downloads"])
    target_dirs = paths["purchase_path"]
    if isinstance(target_dirs, (str, Path)):
        target_dirs = [Path(target_dirs)]

    # Ensure target directories exist
    for td in target_dirs:
        td.mkdir(parents=True, exist_ok=True)

    keywords = ["purchase_orders"]
    today_files = []
    today_date = datetime.today().date()

    # Walk through the downloads folder
    for root, _, files in os.walk(download_dir):
        for file in files:
            if file.lower().endswith(".csv") and any(k in file.lower() for k in keywords):
                full_path = Path(root) / file
                mtime = datetime.fromtimestamp(full_path.stat().st_mtime).date()
                if mtime == today_date:
                    today_files.append(full_path)

    if today_files:
        for file_path in today_files:
            for td in target_dirs:
                dest_path = td / file_path.name
                try:
                    shutil.copy2(file_path, dest_path)
                    print(f"✅ Copied: {file_path.name} → {td}")
                except Exception as e:
                    print(f"❌ Failed to copy {file_path.name} → {td}, Reason: {e}")
    else:
        print(f"⚠️ No files found with keywords {keywords} modified today")
