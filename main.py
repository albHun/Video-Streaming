from io import load_data
from validation import validate
from latency import calculate_latency

data_config, video_config, endpoints, requests = load_data("kitten.in")

best_result = 0
best_methods = list()
for i in range(0, 10):
	cache_info = [[] * data_config["caches"]]
	for request in requests:
		request_endpoint = request[1]
		request_video_id = request[0]
		connected = False
		endpoint = endpoints[request_endpoint]
		for cache in endpoint:
			videos_stored = cache_info[cache]
			if request_video_id in videos_stored:
				connected = True
				break
		if connected == False:
			for cache in endpoint:
				if validate(cache_info, video_config[request_video_id], (request_video_id, cache)):
					connected = True
					cache_info[cache].append(request_video_id)
					break
			
	result = calculate_latency(cache_info, )

