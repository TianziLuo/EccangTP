import zipfile
from pathlib import Path
from datetime import datetime

def unzip():
    # ------ configs ------
    KEYWORDS = ["已映射关系列表", "未映射和待确认关系列表", "产品库存"]

    DOWNLOADS = Path.home() / "Downloads"

    # Find the most recent ZIP 
    def find_zip(keyword: str):
        today = datetime.today().date()

        matched_files = [
            f for f in DOWNLOADS.glob("*.zip")
            if keyword in f.name and datetime.fromtimestamp(f.stat().st_mtime).date() == today
        ]
        return max(matched_files, key=lambda f: f.stat().st_mtime) if matched_files else None

    def extract_single_file(zip_path: Path):
        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            namelist = zip_ref.namelist()
            zip_ref.extract(namelist[0], path=DOWNLOADS)
            print(f"✅ Extracted '{namelist[0]}' to: {DOWNLOADS.resolve()}")

    # Main func
    def main():
        for keyword in KEYWORDS:
            latest_zip = find_zip(keyword)
            if latest_zip:
                print(f"Found latest ZIP file: {latest_zip.name}")
                extract_single_file(latest_zip)
            else:
                print(f"❌ No ZIP file found for keyword: '{keyword}'")

    main()

'''
if __name__ == "__main__":
    unzip()
'''