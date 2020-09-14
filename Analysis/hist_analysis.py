from utils import  read_excels as re
import matplotlib.pyplot as plt
import utils.tools  as tl
import numpy as np
import seaborn as sns
#
# path = "files/Seg_Means_Stddev_Output_informations.xls"
# seg_sheet = "Worksheet_seg_means"
# sttdev_sheet = "Worksheet_seg_stddev"
#
# seg_content = re.get_info4col(path,seg_sheet,2,539,[540,146])
# std_content = re.get_info4col(path,sttdev_sheet,2,539,[540,146])

# path = "/home/sycv/workspace/Cluster_means/pics/1PH6723025430271.jpg"


def Get_HIST(img_list):
    hist_seg_pics,hist_seg  = [],[]
    for img in img_list:
        hist = tl.get_calcHist(img)
        hist = hist.flatten()
        hist_seg.append(hist)
        p = 0
        for i in range(len(hist)):
            # print(len(hist))
            p += i*hist[i] #/256/len(hist)
        hist_seg_pics.append(int(p/1000))
    # print(len(hist_seg_pics))
    # print(hist_seg_pics)
    hist_seg_pics = np.array(hist_seg_pics)
    return  hist_seg_pics



def draw_hist_heatmap(hist_seg):

    data = np.array(hist_seg)
    f, ax = plt.subplots()
    ax = sns.heatmap(data)
    plt.show()

# # std_content,seg_content= np.array(std_content),np.array(seg_content)
# print(len(seg_content))
# print(len(std_content))
# np.set_printoptions(suppress=True)
# data_x = np.empty(shape=(144,2))
# for i in range(len(std_content)):
#     data_x[i][0] = hist_seg_pics[i]
#     data_x[i][1] = std_content[i]
# print(data_x)
# # data_x =data_x.T
#
# #####################################################################
# #####################################################################
# #####################################################################
#
# import numpy as np
# from sklearn.covariance import EllipticEnvelope
# from sklearn.svm import OneClassSVM
# # import matplotlib.pyplot as plt
# import matplotlib.font_manager
# from sklearn.datasets import load_wine
#
# # Define "classifiers" to be used
# classifiers = {
#     "Empirical Covariance": EllipticEnvelope(support_fraction=1.,
#                                              contamination=0.25),
#     "Robust Covariance (Minimum Covariance Determinant)":
#     EllipticEnvelope(contamination=0.4),
#     "OCSVM": OneClassSVM(nu=0.2, gamma=0.005)}
# colors = ['m', 'g', 'b']
# legend1 = {}
# legend2 = {}
#
# # Get data
# # X1 = load_wine()['data'][:, [1, 2]]  # two clusters
# # print(type(X1))
# # print(X1.shape)
# # print(X1)
# # print(type(X1))
# X1 = data_x
# print(X1[:, 0])
# print(X1[:, 1])
# # Learn a frontier for outlier detection with several classifiers
# xx1, yy1 = np.meshgrid(np.linspace(0, 370, 500), np.linspace(0, 50, 200))
# print(xx1,yy1)
# for i, (clf_name, clf) in enumerate(classifiers.items()):
#     plt.figure(1)
#     clf.fit(X1)
#     Z1 = clf.decision_function(np.c_[xx1.ravel(), yy1.ravel()])
#     print(Z1)
#     Z1 = Z1.reshape(xx1.shape)
#     legend1[clf_name] = plt.contour(
#         xx1, yy1, Z1, levels=[0], linewidths=2, colors=colors[i])
#     # legend1[clf_name] = plt.contour(
#     #     xx1, yy1, Z1,  linewidths=2, colors=colors[i])
#
# legend1_values_list = list(legend1.values())
# legend1_keys_list = list(legend1.keys())

# Plot the results (= shape of the data points cloud)
# plt.figure(1)  # two clusters
# plt.title("Outlier detection on a real data set (stddev hist)")
# plt.scatter(X1[:, 0], X1[:, 1], color='black')
# bbox_args = dict(boxstyle="round", fc="0.8")
# arrow_args = dict(arrowstyle="->")
# plt.annotate("outlying points", xy=(4, 2),
#              xycoords="data", textcoords="data",
#              xytext=(3, 1.25), bbox=bbox_args, arrowprops=arrow_args)
#
# plt.legend((legend1_values_list[0].collections[0],
#             legend1_values_list[1].collections[0],
#             legend1_values_list[2].collections[0]),
#            (legend1_keys_list[0], legend1_keys_list[1], legend1_keys_list[2]),
#            loc="upper center",
#            prop=matplotlib.font_manager.FontProperties(size=11))
# plt.ylabel("ash")
# plt.xlabel("malic_acid")
#
# #######################################################################
# ############################################################################
# plt.savefig("outputs/stddev_hist.png")
# plt.figure(1)
# for n in range(len(hist_seg)):
#     print("numbei is:" , n)
#     for m in range(len(hist_seg[n])):
#         print(m)
#         plt.scatter(n, m, label=hist_seg[n][m],)
# plt.show()




