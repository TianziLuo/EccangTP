import os
import shutil
from pathlib import Path
from datetime import datetime
from config_paths import get_eccang_paths

paths = get_eccang_paths()

def copy_download(keywords=None):
    """
    Copy today's latest file for each keyword from downloads to target directory.
    """
    # Config directories
    download_dir = paths["downloads"]
    target_dir   = paths["copy_download"]

    # Default keywords 
    DEFAULT_KEYWORDS = [
        "shipment_order", 
        "product_csv", 
        "库存查询（库位）", 
        "产品库存", 
        "sku-relation", 
        "product-sku-relation"
    ]
    keywords = keywords or DEFAULT_KEYWORDS

    today_date = datetime.today().date()  

    for kw in keywords:
        matched_files = []

        # Search download_dir 
        for root, _, files in os.walk(download_dir):
            for file in files:
                if file.endswith((".csv", ".xls")) and kw in file:
                    full_path = Path(root) / file
                    mtime = datetime.fromtimestamp(full_path.stat().st_mtime).date()
                    if mtime == today_date:
                        matched_files.append(full_path)

        if not matched_files:
            print(f"⚠️ No files found for keyword '{kw}' modified today")
            continue

        # Take the most recently modified file for this keyword
        latest_file = max(matched_files, key=lambda f: f.stat().st_mtime)
        dest_path = target_dir / latest_file.name

        # Copy file to target directory
        shutil.copy2(latest_file, dest_path)
        print(f"✅ Copied (latest for '{kw}'): {latest_file.name} → {target_dir}")


'''
copy_download(["库存查询（库位）", "产品库存"])
'''
