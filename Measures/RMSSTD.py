
import numpy as np
def RMSSTD(X1,cluster_centres_list,pt_label_list):
  for j in range(2,10):
    # kmeans = KMeans(n_clusters=j).fit(X1)
    # cluster_centres = kmeans.cluster_centers_
    # pt_label = kmeans.labels_
    ni_arr = np.zeros((j,1))
    var = 0
    for i in range(j):
      ni_arr[i] = np.count_nonzero(pt_label_list[j-2]==i)
      sum_ni = np.sum(ni_arr)
      var += (np.sum((X1[pt_label_list[j-2]==i]-cluster_centres_list[j-2][i])**2)/(2*sum_ni))
    rmsstd = var**(0.5)
    print('Number of Clusters:',j,' 𝑅𝑀𝑆𝑆𝑇𝐷:',rmsstd)
  return