import os
import shutil
from pathlib import Path
from config_paths import get_tp_paths

def rename_DXM():
    paths = get_tp_paths()
    source_dir = Path(paths["downloads"])
    target_dir = Path(paths["core_dxm"])
    
    keywords = ["pandianshuju"]
    new_filename = "店小秘 盘点下载 源文件.xlsx"

    for keyword in keywords:
        latest_file = None
        latest_mtime = 0

        for root, _, files in os.walk(source_dir):
            for file in files:
                if file.endswith(".xlsx") and keyword in file:
                    full_path = Path(root) / file
                    mtime = full_path.stat().st_mtime
                    if mtime > latest_mtime:
                        latest_mtime = mtime
                        latest_file = full_path

        if latest_file:
            dest_path = target_dir / new_filename
            shutil.copy2(latest_file, dest_path)
            print(f"✅ Copied and renamed to: {dest_path}")
        else:
            print(f"⚠️ No file found containing '{keyword}'")
'''
if __name__ == "__main__":
    rename_DXM()
'''