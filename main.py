from inout import *
from validation import validate
from latency import calculate_latency

filename = "videos_worth_spreading.in"

data_config, video_config, endpoints, endpoint_connections, endpoint_datacenter_latency, requests = load_data(filename)
# print(data_config["caches"])

best_result = 0
best_methods = list()
for i in range(0, 1):
	cache_info = [[]] * data_config["caches"]
	for request in requests:
		request_endpoint = request[1]
		request_video_id = request[0]
		connected = False
		endpoint = endpoints[request_endpoint]
		for cache in endpoint.keys() :
			if cache != "datacentre":
				videos_stored = cache_info[cache]
				if request_video_id in videos_stored:
					connected = True
					break
		if connected == False:
			for cache in endpoint:
				if cache != "datacentre":
					if validate(cache_info, video_config, (request_video_id, cache), data_config, video_config, endpoints, endpoint_connections, endpoint_datacenter_latency, requests) == True:
						connected = True
						cache_info[cache].append(request_video_id)
						# print("cache", cache, request_video_id)
						break

	result = calculate_latency(cache_info, endpoint_connections, endpoint_datacenter_latency,
		endpoints, requests)
	if result > best_result:
		best_methods = cache_info
		best_result = result
print(best_methods, best_result)
output_data(best_methods, "out.txt")
