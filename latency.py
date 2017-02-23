def calculate_latency(cache_server_info, endpoint_connections, endpoint_datacenter_latency,
						endpoint_cache_latencies, requests):
	total_latency = 0
	total_requests = 0
	original_latency = 0

	for request in requests:
		print(request)
		how_many_requests = request[2]
		request_endpoint = request[1]
		request_video_id = request[0]

		total_requests += how_many_requests
		streamed = False

		connected_caches = endpoint_connections[request_endpoint]
		connected_caches = sorted(connected_caches, 
			key = lambda cache: endpoint_cache_latencies[request_endpoint][cache])
		for cache in connected_caches:
			if request_video_id in cache_server_info[cache]:
				total_latency += how_many_requests * endpoint_cache_latencies[request_endpoint][cache]
				streamed = True
				break
		if streamed == False:
			total_latency += how_many_requests * endpoint_datacenter_latency[request_endpoint]
			

		original_latency += how_many_requests * endpoint_datacenter_latency[request_endpoint]

	return (original_latency - total_latency) / total_requests