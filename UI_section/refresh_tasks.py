import time
from utils.open_excel_utils import open_excel_file
from utils.SKU_mapping import SKU_out
from utils.copy_file_utils import copy_file_to_dirs
from config_paths import get_refresh_paths

paths = get_refresh_paths()


downloads = paths["downloads"]
core_1_8 = paths["core_1_8"]
core_1_85 = paths["core_1_85"]
core_3_1 = paths["core_3_1"]
core_4_1 = paths["core_4_1"]
core_1_6 = paths["core_1_6"]
sku_mapping = paths["sku_mapping"]
core_eccang = paths["core_eccang"]
core_1_2 = paths["core_1_2"]
core_2_6 = paths["core_2_6"]
core_2_9 = paths["core_2_9"]
core_5_1 = paths["core_5_1"]
core_5_2 = paths["core_5_2"]
core_5_3 = paths["core_5_3"]


def step_1_1(): 
    open_excel_file(core_1_8)
    time.sleep(30)
    open_excel_file(core_1_85)

def step_1_2(): open_excel_file(core_3_1)
def step_1_3(): open_excel_file(core_4_1)
def step_2_1(): open_excel_file(core_1_6)

def step_2_2():
    SKU_out()
    time.sleep(20)
    copy_file_to_dirs(str(sku_mapping), [str(core_eccang)])

def step_3_1(): open_excel_file(core_1_2)
def step_3_2(): open_excel_file(core_2_6)
def step_3_3(): open_excel_file(core_2_9)
def step_3_4(): open_excel_file(core_5_1)
def step_3_5(): open_excel_file(core_5_2)
def step_3_6(): open_excel_file(core_5_3)
