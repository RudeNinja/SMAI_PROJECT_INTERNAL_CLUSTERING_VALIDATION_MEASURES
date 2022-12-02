import numpy as np
def b(cl1,cl2):
    #minimum distance of every point in cl1 to cl2
    min_dist = np.zeros(cl1.shape[0])
    for i in range(cl1.shape[0]):
        min_dist[i] = np.min(np.sum((cl1[i]-cl2)**2,axis=1)**0.5)
    return min_dist
def a(cl):
    #average distance of every point in cl to all other points in cl
    avg_dist = np.zeros(cl.shape[0])
    for i in range(cl.shape[0]):
        avg_dist[i] = np.sum(np.sum((cl[i]-cl)**2,axis=1)**0.5)/(cl.shape[0]-1)
    return avg_dist
def silhoutte_index(arr,cluster_centres_list,pt_label_list):
    for j in range(2,10):
        # cluster_centres = cluster_centres_list[j-2]
        pt_label=pt_label_list[j-2]
        #minimum pairwise interclass distance and average intraclass distance
        sum=0
        for i in range(j):
            #minimum pairwise interclass distance
            for k in range(j):
                if i!=k:
                    #distance between points of different clusters
                    min_dist_ik = b(arr[pt_label==i],arr[pt_label==k])
            # print(min_dist_ik.shape)
            #average distance of points of same cluster from each other
            avg_dist_ii = a(arr[pt_label==i])
            # print(avg_dist_ii.shape)
            sum+=np.sum((min_dist_ik-avg_dist_ii)/(np.maximum(min_dist_ik,avg_dist_ii))/arr[pt_label==i].shape[0])
        silhoutte_ind = sum/j
        print('Number of clusters:',j, 'Silhoutte Index: ',silhoutte_ind)
    return