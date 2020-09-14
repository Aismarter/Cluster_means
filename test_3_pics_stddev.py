from Analysis.hist_analysis import *
import os
import time
from utils.tools import *
from utils.read_excels import *

path = "files/Seg_Means_Stddev_Output_informations.xls"
seg_sheet = "Worksheet_seg_means"
sttdev_sheet = "Worksheet_seg_stddev"
std_content = re.get_info4col(path,sttdev_sheet,2,2,[1376,146])
draw_single_num(std_content,"StdDev")