import numpy as np


def density(pt,var,cl1,cl2):
    #combine the two clusters
    cl_union = np.row_stack((cl1,cl2))
    #distance between pt and cl_union
    dist_pt_clu = np.sum((cl_union-pt)**2,axis=1)**0.5
    dens_num = np.count_nonzero(dist_pt_clu<var)
    return dens_num

def scat_val(arr,cluster_centres_list,pt_label_list):
    data_std = np.std(arr,axis = 0)
    mod_datastd = np.sqrt(np.dot(data_std,data_std.T))
    scat_list = []
    for k in range(2,10):
        cluster_centres = cluster_centres_list[k - 2]
        pt_labels = pt_label_list[k-2]
        num_clusters = len(cluster_centres)
        num = 0
        for i in range(num_clusters):
            cluster_std = np.std(arr[pt_labels == i],axis = 0)
            num += np.sqrt(np.dot(cluster_std,cluster_std.T))
        num = num/num_clusters
        scat = num/mod_datastd
        scat_list.append(scat)
    return np.array(scat_list)

def dens_dw(arr,cluster_centres_list,pt_label_list):
    #square root of the sum of the norms of the variance vectors of each cluster
    densdw_list = []
    for j in range(2,10):
        cluster_centres=cluster_centres_list[j-2]
        pt_label=pt_label_list[j-2]
        intra_cl_var=0
        sum=0
        for i in range(j):
            #variance vectors of each cluster
            intra_cl_var += np.sqrt(np.sum(np.var(arr[pt_label==i],axis=0)))/j #radius of variance ball
        #densities for barycenters and their midpoint
        for i in range(j):
            # sum=0
            for k in range(j):
                if i!=k:
                    den_cli = density(cluster_centres[i],intra_cl_var,arr[pt_label==i],arr[pt_label==k]) #density of cli
                    den_clk = density(cluster_centres[k],intra_cl_var,arr[pt_label==i],arr[pt_label==k]) #density of clk
                    mid_pt = (cluster_centres[i]+cluster_centres[k])/2 #midpoint
                    den_mpt = density(mid_pt,intra_cl_var,arr[pt_label==i],arr[pt_label==k]) #denisty of midpoint
                    quotient = den_mpt/(np.maximum(den_cli,den_clk)) #quotient
                    sum+=quotient
            # print(quotient)
        dens_dw_ind = 2*sum/(j*(j-1))
        # print('Number of clusters:',j, 'Dens_dw Index: ',dens_dw_ind)
        densdw_list.append(dens_dw_ind)
    return np.array(densdw_list)
def s_dbw(arr,cluster_centres_list,pt_label_list):
    s_dbw = dens_dw(arr,cluster_centres_list,pt_label_list)+scat_val(arr,cluster_centres_list,pt_label_list)
    for j in range(2,10):
        print('Number of clusters:',j, 'S_Dbw:',s_dbw[j-2])
    return 
