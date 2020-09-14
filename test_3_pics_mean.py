from Analysis.hist_analysis import *
import os
import time
from utils.tools import *
from utils.read_excels import *

path = "files/Seg_Means_Stddev_Output_informations.xls"
seg_sheet = "Worksheet_seg_means"
sttdev_sheet = "Worksheet_seg_stddev"

seg_content = re.get_info4col(path,seg_sheet,2,1,[1376,146])



# print(len(seg_content))
# print(std_content)
draw_single_num(seg_content,"Means")