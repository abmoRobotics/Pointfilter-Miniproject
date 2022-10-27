import vis_utils
import numpy as np

test_path = "./Dataset/Test/"
train_path = "./Dataset/Train/"
res_path = "./Dataset/Results/"

pc_noisy_path = test_path + "sphere_dev1.0938961202360427.npy"
pc_filtered_path = res_path + "sphere_dev1.0938961202360427_pred_iter_2.npy"

pc_input = train_path + "dodge_dev0.0.npy"
pc_input_noisy = train_path + "dodge_dev0.16997851507465497.npy"

pc_noisy = np.load(pc_input)
pc_filtered = np.load(pc_input_noisy)
print(pc_noisy)
print(pc_filtered)
vis_utils.visualize_np_pointcloud(pc_noisy)
vis_utils.visualize_np_pointcloud(pc_filtered)