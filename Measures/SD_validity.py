import numpy as np

def SD_validity_index(arr,cluster_centres_list,pt_label_list):
    data_std = np.std(arr,axis = 0)
    mod_datastd = np.sqrt(np.dot(data_std,data_std.T))
    for k in range(2,10):
        cluster_centres = cluster_centres_list[k - 2]
        pt_labels = pt_label_list[k-2]
        num_clusters = len(cluster_centres)
        num_scat = 0
        inv_dist = 0
        max_ij = 0
        min_ij = np.inf
        for i in range(num_clusters):
            den = 0
            cluster_std = np.std(arr[pt_labels == i],axis = 0)
            num_scat += np.sqrt(np.dot(cluster_std,cluster_std.T))

            dist_ij = sorted(np.sqrt(np.sum((cluster_centres - cluster_centres[i])**2,axis = 1)))
            den += np.sum(dist_ij)
            inv_dist += 1/den

            maxval = dist_ij[-1]
            minval = dist_ij[1]
            if max_ij < maxval:
                max_ij = maxval
            if min_ij > minval:
               min_ij = minval

        num_scat = num_scat/num_clusters
        scat = num_scat/mod_datastd
        index_value = (max_ij/min_ij)*inv_dist + scat
        print('Number of clusters:',k, 'SD Validity Index: ',index_value)
