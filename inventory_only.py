from Eccang.unzip import unzip
from Eccang.copy_download import copy_download

def inv_only():
    unzip(["产品库存"])
    print("✔ Step 1 completed")
            
    copy_download(["库存查询（库位）", "产品库存"])
    print("✔ Step 3 completed")