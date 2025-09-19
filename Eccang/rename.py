import shutil
from datetime import datetime
from config_paths import get_eccang_paths

paths = get_eccang_paths()

def rename():
    def get_filename():
        downloads = paths["downloads"]
        prefix = "产品库存"  
        today = datetime.today().date()

        # Find today's zip files starting with prefix
        matched_files = [
            f for f in downloads.glob("*.zip")
            if f.name.startswith(prefix) and datetime.fromtimestamp(f.stat().st_mtime).date() == today
        ]
        if not matched_files:
            print(f"❌ No zip file found starting with '{prefix}' (today)")
            return None

        # Take the most recently modified file
        latest = max(matched_files, key=lambda f: f.stat().st_mtime)

        # Remove extension and last 3 characters
        name_without_ext = latest.stem
        trimmed_name = name_without_ext[:-3]

        print(f"✅ Saved filename base: {trimmed_name}")
        return trimmed_name

    def rename_unzip_file(new_name: str):
        downloads = paths["downloads"]
        today = datetime.today().date()

        # Find today's unzipped files containing 'product_inventory'
        matched_files = [
            f for f in downloads.iterdir()
            if f.is_file() and "product_inventory" in f.name
            and datetime.fromtimestamp(f.stat().st_mtime).date() == today
        ]
        if not matched_files:
            print("❌ No file found containing 'product_inventory' (today)")
            return

        # Take the most recently modified file
        latest_file = max(matched_files, key=lambda f: f.stat().st_mtime)

        # Construct new filename while keeping extension
        new_file = downloads / f"{new_name}{latest_file.suffix}"

        # Rename file
        shutil.move(str(latest_file), str(new_file))
        print(f"✅ Renamed: {latest_file.name} → {new_file.name}")

    def main():
        filename_str = get_filename()
        if filename_str:
            rename_unzip_file(filename_str)

    main()


'''
if __name__ == "__main__":
    rename()
'''
