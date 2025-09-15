import os
import glob

def clean_folder():
    # Folder paths
    folder_paths = [r"C:\ACT\公用核心\易仓\易仓日常下载\采购单合并",]
    # File types
    file_patterns = ['*.xlsx', '*.csv']

    # Process each folder
    for folder_path in folder_paths:
        print(f"\nProcessing folder: {folder_path}")
        
        files_to_delete = []
        for pattern in file_patterns:
            files_to_delete.extend(glob.glob(os.path.join(folder_path, pattern)))

        for file in files_to_delete:
            try:
                os.remove(file)
                print(f"Deleted: {file}")
            except Exception as e:
                print(f"Failed to delete: {file}, Reason: {e}")
'''
if __name__ == "__main__":
    clean_folder()
'''