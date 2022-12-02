import numpy as np
def modified_hubert_statistic(arr,cluster_centres_list,pt_label_list):
    n=arr.shape[0]
    for j in range(2,10):
        # kmeans = KMeans(n_clusters=j).fit(arr)
        # cluster_centres_list = kmeans.cluster_centers_
        # pt_label_list = kmeans.labels_#.reshape(arr.shape[0],1)
        # print(arr[pt_label==1])
        pt_dist = np.zeros((n,n))
        cl_dist = np.zeros((n,n))
        for i in range(n):
            #calculate distance of one point to all other points
            pt_dist[i] = np.sum((arr[i]-arr)**2,axis=1)
        #replace each point with its cluster
        arr1 = np.zeros(arr.shape)
        for i in range(j):
            arr1[pt_label_list[j-2]==i]=cluster_centres_list[j-2][i]
        for i in range(n):
            #calculate distance of one point's cluster to all other points' cluster
            cl_dist[i] = np.sum((arr1[i]-arr1)**2,axis=1)**0.5
        mod_hubert_stat = 2*np.sum(pt_dist*cl_dist)/(n*(n-1))
        print('Number of clusters:',j, 'Modified Hubert Statistic: ',mod_hubert_stat)
    return 
