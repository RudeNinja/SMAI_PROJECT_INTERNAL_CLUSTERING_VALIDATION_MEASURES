import numpy as np
def calinski_harabasz_index(arr,cluster_centres_list,pt_label_list):
    n=arr.shape[0]
    for j in range(2,10):
        #calculate distance between cluster centres and dataset cluster
        cluster_centres = cluster_centres_list[j-2]
        data_centre = np.sum(arr,axis = 0)/arr.shape[0]
        #distance between cluster centres and dataset centre
        dist_cc_dc = np.sum((cluster_centres - data_centre)**2,axis = 1)
        # print(dist_cc_dc)
        numerator = 0
        denominator = 0
        for i in range(j):
            #numerator
            num_pt = np.count_nonzero(pt_label_list[j-2]==i)
            numerator+=num_pt*dist_cc_dc[i]/(j-1)
            #denominator
            #distance between each point and its cluster centre
            dist_pt_cc = np.sum((arr[pt_label_list[j-2]==i]-cluster_centres[i])**2,axis = 1)
            denominator+=np.sum(dist_pt_cc)/(n-j)
        cal_har_index = numerator/denominator
        print('Number of clusters:',j, 'Calinski-Harabasz Index: ',cal_har_index)
    return    
