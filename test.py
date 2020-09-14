from utils import read_excels as re
from utils import cluster_means as cm
from utils import tools as tl
import time

import numpy as np
np.set_printoptions(suppress=True)

path = "files/Seg_Means_Stddev_Output_informations.xls"
seg_sheet = "Worksheet_seg_means"




content = re.get_info4col(path,seg_sheet,2,539,[540,146])
print(content)
content = np.array(content)

path = "/home/sycv/workspace/Cluster_means/pics/1PH6723025430406.jpg"
p1 = tl.pictures(path)
p2 = tl.pictures1(path)


p1.seg_pictures()
hist_seg_pics = []
for img in p1.img_list:
    hist = tl.get_calcHist(img)
    hist = hist.flatten()
    p = 0
    for i in range(len(hist)):
        p += (i*hist[i])/256/len(hist)
    hist_seg_pics.append(p)
print(len(hist_seg_pics))
print(hist_seg_pics)
hist_seg_pics = np.array(hist_seg_pics)

st = time.time()
ms_labels,ms_cls_centers = cm.MeanShift_process(hist_seg_pics)
et = time.time()
print("ms",et-st)
km_labels,km_cls_centers = cm.Kmeans_process(hist_seg_pics)

print(type(ms_labels))
print(type(km_labels))

# print((ms_labels))
# print((km_labels))
ms_p = tl.resize_arr_picsize(ms_labels)
km_p = tl.resize_arr_picsize(km_labels)

# print("ms: \n", ms_p)
# print("km: \n", km_p)

km_coord_info = tl.pics_info(km_p,km_cls_centers)
ms_coord_info = tl.pics_info(ms_p,ms_cls_centers)

p1.draw(10,coord=ms_coord_info)
p2.draw(-1,coord=ms_coord_info)
p1.draw(10,coord=km_coord_info)
p2.draw(-1,coord=km_coord_info)

