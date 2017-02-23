from io import load_data
import numpy as np

# cache_storage is a list of caches with already stored data
# video_size is a list of videos with their sizes in MB
# new_storing_command is a tuple of (video_id, cache_id)

def validate(cache_storage, video_size, new_storing_command):
	used_space = np.sum(cache_storage[new_storing_command[1]])
	capacity = data_config["cache_size"]
	if video_size(new_storing_command[0]) + used_space > capacity:
		return False
	return True
