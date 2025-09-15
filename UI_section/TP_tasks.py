import time
from utils.open_excel_utils import open_excel_file
from utils.copy_file_utils import copy_file_to_dirs
from utils.create_file_utils import generate_tp_csv, update_inventory_excel
from utils.TP_upload_utils import teapplix_upload
from utils.download_rename import rename_DXM
from config_paths import get_tp_paths

paths = get_tp_paths()

downloads = paths["downloads"]
core_1_1 = paths["core_1_1"]
core_2_1 = paths["core_2_1"]
tp_template = paths["tp_template"]
tp_output = downloads / paths["tp_output"]
core_tp = paths["core_tp"]
tp_skuinv = paths["tp_skuinv"]
inv_upload = paths["inv_upload"]
dxm_excel = paths["dxm_excel"]
dxm_template = paths["dxm_template"]
dxm_output = downloads / paths["dxm_output"]
core_dxm = paths["core_dxm"]

def step_1_1(): open_excel_file(core_1_1)
def step_2_1(): open_excel_file(core_2_1)

def step_2_2():
    generate_tp_csv(core_2_1, "易仓进TP", tp_template, tp_output)
    time.sleep(1)
    teapplix_upload("wayfaircolourtree","wayfair.colourtree@gmail.com","Colourtree168!!", str(tp_output))
    time.sleep(1)
    teapplix_upload("colourtree","colourtreeusa@gmail.com","Colourtree168!", str(tp_output))
    time.sleep(2)
    copy_file_to_dirs(str(tp_output), [str(core_tp)])
    time.sleep(2)
    open_excel_file(tp_skuinv)

def step_2_3(): copy_file_to_dirs(str(tp_skuinv), [str(inv_upload)])

def step_3_1():
    rename_DXM()
    time.sleep(1)
    open_excel_file(dxm_excel)

def step_3_3():
    update_inventory_excel(dxm_excel, "盘点", dxm_template, dxm_output)
    time.sleep(20)
    copy_file_to_dirs(str(dxm_output), [str(core_dxm)])
