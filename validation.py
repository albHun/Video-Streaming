from inout import load_data
import numpy as np

# cache_storage is a list of caches with already stored data
# video_size is a list of videos with their sizes in MB
# new_storing_command is a tuple of (video_id, cache_id)

def validate(cache_storage, video_size, new_storing_command, data_config, video_config, endpoints, endpoint_connections, endpoint_datacenter_latency, requests):
	# data_config, video_config, endpoints, endpoint_connections, endpoint_datacenter_latency, requests = load_data("me_at_the_zoo.in")
	stored = [ video_size[video] for video in cache_storage[new_storing_command[1]]]
	used_space = np.sum(stored)
	capacity = data_config["cache_size"]
	# print(video_size[new_storing_command[0]], used_space, capacity)
	if (video_size[new_storing_command[0]] + used_space) > capacity:
		# print("f")
		return False
	# print("t")
	return True
