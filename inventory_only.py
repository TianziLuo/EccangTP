from Eccang.xls2csv import xls2csv
from Eccang.unzip import unzip
from Eccang.rename import rename
from Eccang.copy_download import copy_download

def inv_only():
    unzip(["产品库存"])
    print("✔ Step 1 completed")
            
    xls2csv()
    print("✔ Step 2 completed")
            
    rename()
    print("✔ Step 3 completed")

    copy_download(["库存查询（库位）", "产品库存"])
    print("✔ Step 4 completed")