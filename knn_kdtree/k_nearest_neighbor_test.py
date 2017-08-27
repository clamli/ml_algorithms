from kdtree import KDTree
import numpy as np

#### test for create tree and print tree
test_sample = np.array([[7,2], [5,4], [9,6], [2,3], [4,7], [8,1]])
kd_tree = KDTree()
kd_tree.build_tree(input_data=test_sample, sel_feature=0, tree_node = None)
kd_tree.print_tree()

#### test for search closest neighbor
point = np.array([[2.1, 3.1]])
min_dist, min_dist_pnt = kd_tree.search_neighbor(point)
print "minimum distance: ", min_dist
print "minimum point: ", min_dist_pnt
point = np.array([[2, 4.5]])
min_dist, min_dist_pnt = kd_tree.search_neighbor(point)
print "minimum distance: ", min_dist
print "minimum point: ", min_dist_pnt