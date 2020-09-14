
import numpy as np
from sklearn.cluster import MeanShift, estimate_bandwidth, KMeans

def MeanShift_process(content):

    # #############################################################################
    # Generate sample data
    # centers = [[1, 1], [-1, -1], [1, -1]]
    X = content.reshape(-1,1)
    # X = content
    # #############################################################################
    # Compute clustering with MeanShift

    # The following bandwidth can be automatically detected using
    bandwidth = estimate_bandwidth(X, quantile=0.2, n_samples=500)

    ms = MeanShift(bandwidth=bandwidth, bin_seeding=True)
    ms.fit(X)
    labels = ms.labels_
    print(len(labels),len(X))

    cluster_centers = ms.cluster_centers_
    # for i in range(len(labels)):
    #     print(i , "label: ",labels[i] , "Culster: ", cluster_centers[labels[i]] )

    labels_unique = np.unique(labels)
    n_clusters_ = len(labels_unique)

    print("number of estimated clusters : %d" % n_clusters_)
    print(cluster_centers)
    return labels,cluster_centers


def Kmeans_process(content):
    X = content.reshape(-1, 1)
    # Kmeans
    import time
    print("Kmeans")
    st = time.time()
    km = KMeans(n_clusters=3, max_iter=100)
    km.fit(X)
    et = time.time()
    print(et-st)
    KM_labels = km.labels_
    print(len(KM_labels),len(X))
    km_cluster_centers = km.cluster_centers_
    print(km_cluster_centers)
    cluster_centers = km.cluster_centers_
    for i in range(len(KM_labels)):
        print(i , "label: ",KM_labels[i] , "Culster: ", cluster_centers[KM_labels[i]] )
    return KM_labels,cluster_centers

