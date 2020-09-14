from Analysis.hist_analysis import *
import os
import time
from utils.tools import *

pics_path = "pics/normal/"



if __name__ == '__main__':

    list_img = os.listdir(pics_path)
    hists = []
    n = 0

    for img in list_img:
        # print(img)
        img = pics_path + img
        p1 = tl.pictures(img)
        # p2 = tl.pictures1(path)
        st = time.time()
        img_list = p1.seg_pictures()
        ed = time.time()
        print("cost :", ed -st )
        hist = Get_HIST(img_list)
        for i in range(len(hist)):
            hists.append(hist[i])
        n += 1
        print("pics:", n)
    # print(hists)
    draw_single_num(hists)

