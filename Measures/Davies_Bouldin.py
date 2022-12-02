import numpy as np
def dist(x,y):
    return np.sum((x-y)**2)**0.5

def Davies_Bouldin_Index(arr,cluster_centres_list,pt_label_list):
    for k in range(2,10):
        cluster_centres = cluster_centres_list[k-2]
        pt_labels = pt_label_list[k-2]
        num_clusters = len(cluster_centres)
        index_value = []
        for i in range(num_clusters):
            dist_i = np.sum(np.sqrt(np.sum((arr[pt_labels == i] - cluster_centres[i])**2,axis = 1)))/arr[pt_labels == i].shape[0]
            maxfori = []
            for j in range(num_clusters):
                if i != j:
                    dist_j = np.sum(np.sqrt(np.sum((arr[pt_labels == j] - cluster_centres[j])**2,axis = 1)))/arr[pt_labels == j].shape[0]
                    maxfori.append((dist_i + dist_j)/dist(cluster_centres[i],cluster_centres[j]))
            maxofi = max(maxfori)
            index_value.append(maxofi)

        index_value = sum(index_value)
        print('Number of clusters:',k, 'Davies-Bouldin Index: ',index_value)
