import numpy as np

def dist(x,y):
    return np.sum((x-y)**2)**0.5
def dunn_index(arr,pt_label_list):
    for j in range(2,10):
        pt_label=pt_label_list[j-2]
        #minimum pairwise interclass distance and maximum pairwise intraclass distance
        min_interclass_dist = np.inf
        max_intraclass_dist = 0
        for i in range(j):
            #minimum pairwise interclass distance
            for k in range(j):
                if i!=k:
                    #distance between points of different clusters
                    dist_pt_pt = np.array([ dist( x, y ) for x, y in zip( arr[pt_label==i], arr[pt_label==k] )])
                    min_dist_pt_pt = np.min(dist_pt_pt)
                    if min_dist_pt_pt<min_interclass_dist:
                        min_interclass_dist = min_dist_pt_pt
        # print(min_dist_pt_pt)
            #maximum pairwise intraclass distance
            #distance between points of same cluster
            dist_intc = np.zeros((arr[pt_label==i].shape[0],arr[pt_label==i].shape[0]))
            for m in range(arr[pt_label==i].shape[0]):
                dist_intc[i] = np.sum((arr[pt_label==i][m]-arr[pt_label==i])**2,axis=1)**0.5
            max_dist_intc = np.max(dist_intc)
            if max_dist_intc>max_intraclass_dist:
                max_intraclass_dist = max_dist_intc
        # print(max_dist_intc)
        dunn_ind = min_interclass_dist/max_intraclass_dist
        print('Number of clusters:',j, 'Dunn Index: ',dunn_ind)
    return