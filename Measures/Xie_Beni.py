import numpy as np

def Xie_Beni_Index(arr,cluster_centres_list,pt_label_list):
    n = arr.shape[0]
    for k in range(2,10):
        cluster_centres = cluster_centres_list[k - 2]
        pt_labels = pt_label_list[k-2]
        num_clusters = len(cluster_centres)
        num = 0
        mini_ij = np.inf
        for i in range(num_clusters):
            num += np.sum(np.sum((arr[pt_labels == i] - cluster_centres[i])**2,axis = 1))
            mini_i = np.sort(np.sum((cluster_centres - cluster_centres[i])**2,axis = 1))[1]
            if mini_i < mini_ij:
                mini_ij = mini_i
        index_value = num/mini_ij
        print('Number of clusters:',k, 'Xie Beni Index: ',index_value)
