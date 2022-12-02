import numpy as np
def I_index(arr,cluster_centres_list,pt_label_list):
    #distance between dataset centre and each point
    data_centre = np.sum(arr,axis = 0)/arr.shape[0]
    dist_dc_pt = np.sum((arr - data_centre)**2,axis = 1)**0.5
    sum_dist_dc_pt = np.sum(dist_dc_pt)
    print(sum_dist_dc_pt)
    #distance of clusters from each other
    for j in range(2,10):
        cluster_centres = cluster_centres_list[j-2]
        dist_cc = np.zeros((j,j))
        sum_dist_pt_cc=0
        for i in range(j):
            dist_cc[i] = np.sum((cluster_centres[i]-cluster_centres)**2,axis=1)**0.5
            #distance between point and its cluster centre
            dist_pt_cc = np.sum((arr[pt_label_list[j-2]==i]-cluster_centres[i])**2,axis = 1)**0.5
            #sum of all such distances
            sum_dist_pt_cc += np.sum(dist_pt_cc)
        max_sep = np.max(dist_cc)
        I = (sum_dist_dc_pt*max_sep/(j*sum_dist_pt_cc))**2
        print('Number of clusters:',j, 'I Index: ',I)
    return
