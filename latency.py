def calculate_latency(cache_server_info, video_number, 
						endpoint_number, endpoint_datacenter_latency,
						endpoint_cache_latencies, request_number, 
						requests, cache_capacity):
	for request in requests:
		how_many_requests = request[0]
		request_endpoint = request[1]
		request_video_id = request[2]
		