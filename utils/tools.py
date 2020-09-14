import numpy as np
import cv2
import matplotlib.pyplot as plt

def get_cord(index):
        col = index // 6
        row = index % 6
        return col,row


def resize_arr_picsize(labels):
        pic_arr=np.zeros(shape=(6,24))
        for i in range(len(labels)):
                c,r =get_cord(i)
                # print(r,c)
                pic_arr[r][c] = labels[i]
        return pic_arr

def pics_info(pic_arr,cls_centers):
        edge = 40
        q = 2
        coord = []
        for h in range(len(pic_arr)):
                n = 0
                for w in range(len(pic_arr[h])):
                        n += 1
                        print(h, w)
                        print(int(pic_arr[h][w]))
                        print(h*600 + edge,w*300 + edge,h*600 + 600-edge, w * 300 + 300-edge)
                        val = int(pic_arr[h][w])
                        cls = int(cls_centers[val])
                        x1,y1,x2,y2 = w*300 + edge ,h*600 + edge,w*300 + 300-edge, h * 600 + 600-edge
                        coord.append([x1+edge*q,y1+edge*q,x2+edge*q,y2+edge*q,val,cls])
        print(len(coord),coord)
        return coord


def get_calcHist(img):
        hist = cv2.calcHist([img],[0],None,[256],[0,256])
        # hist, bins = np.histogram(img.flatten(),256,[0,256])
        return hist


def draw_plot(x,y):
        # plt.savefig(saved_path)
        plt.figure(1)
        plt.scatter(x, y)
        plt.show()


def draw_single_num(data_list,Name):
    unique_data = np.unique(data_list)

    resdata = []
    for ii in unique_data:
        resdata.append(data_list.count(ii))

    fig = plt.figure(Name)
    plt.bar(unique_data, resdata)
    # plt.savefig(output_path + "Analysis2_Mean_Loss.jpg")
    plt.show()


class pictures():
        def __init__(self,img_path):
                self.img_path = img_path
                self.saved_path = "/home/sycv/workspace/Cluster_means/outputs/hist_line10_"
                self.img = cv2.imread(self.img_path)
        def draw(self,X,coord):
                self.coord = coord
                list_name = self.img_path.split("/")
                print(list_name[-1])
                col = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (0, 255, 255), (255, 0, 255)]
                max = 0
                for coord_info in self.coord:
                        print(coord_info)
                        if coord_info[4] > max:
                                max = coord_info[4]
                        cv2.rectangle(self.img, (coord_info[0], coord_info[1]), (coord_info[2], coord_info[3]),
                                      col[coord_info[4]], X)
                        cv2.putText(self.img, str(coord_info[5]), (coord_info[0] + 50, coord_info[1] + 500),
                                    cv2.FONT_HERSHEY_SIMPLEX, 5, (0, 0, 0), 5)
                saved_path = self.saved_path  + "cls"+str(max+1) +  "_"
                cv2.namedWindow("show", cv2.WINDOW_FREERATIO)
                cv2.imshow("show", self.img)
                cv2.imwrite(saved_path+list_name[-1],self.img)
                cv2.waitKey(500)

        def seg_pictures(self):
                edge = 40
                q = 2
                self.img_list = []
                # print("seg_picture!!!!!!!!!!!!!!!!1")
                for h in range(24):

                        n = 0
                        for w in range(6):
                                n += 1

                                x1, y1, x2, y2 = h * 300 + edge, w * 600 + edge, h * 300 + 300 - edge, w * 600 + 600 - edge
                                # print(y1, y2, x1, x2)
                                seg_pics = self.img[y1 + edge * q:y2 + edge * q,x1 + edge * q:x2 + edge * q]
                                # seg_pics = self.img[y1 :y2 , x1:x2]
                                self.img_list.append(seg_pics)
                                # cv2.imshow("seg",seg_pics)
                                # cv2.waitKey(50)


class pictures1(pictures):
        def __init__(self,img_path):
                super().__init__(img_path)
                self.saved_path = "/home/sycv/workspace/Cluster_means/outputs/hist_line-1_"
        def draw(self,X,coord):
                self.coord = coord
                super().draw(X,coord)



