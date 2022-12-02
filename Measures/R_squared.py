
import numpy as np
def r_squared(arr,cluster_centres_list,pt_label_list):
    for j in range(2,10):
        # kmeans = KMeans(n_clusters=j).fit(arr)
        # cluster_centres = kmeans.cluster_centers_
        # sample_labels = kmeans.labels_
        data_centre = np.sum(arr,axis = 0)

        TSS = arr - data_centre
        TSS = np.sum(np.sum(TSS**2,axis = 1))

        SSE = 0
        labels_count = np.zeros(j)
        for i in range(j):
            SSE += np.sum((arr[pt_label_list[j-2] == i] - cluster_centres_list[j-2][i])**2) #(j-2) because j starts from 2 and index starts from 0

        RS = (TSS - SSE)/TSS
        print('Number of clusters:',j, 'RS: ',RS)
    return

