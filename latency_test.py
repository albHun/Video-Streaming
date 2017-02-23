from latency import calculate_latency


cache_server_info = [[2], [3, 1], [0, 1]]
endpoint_connections = [[0, 2, 1], []]
endpoint_datacenter_latency = [1000, 500]
endpoint_cache_latencies = [{0:100, 2:200, 1:300}, {} ]
requests = [[3, 0, 1500], [0, 1, 1000], [4, 0, 500], [1, 0, 1000]]
print(calculate_latency(cache_server_info, endpoint_connections, endpoint_datacenter_latency,
						endpoint_cache_latencies, requests))