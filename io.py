""" Module for loading and outputting data """


def load_data(filename):


    """
        Data returned: data_config, video_config, endpoints, requests

        each endpoint is dictionary with the cache_id being the key and the latency being the value, 
        the latency datacentre is stored in a key "datacentre"

        each request is a list of tuples: (video_id, endpoint_id, number of requests for the video)
    """


    # config line loaded
    raw_data = open(filename).readlines()
    # split all the lines
    for i in range(len(raw_data) ):
        line = raw_data[i]
        raw_data[i] = line.split()
        for j in range(len(raw_data[i])):
            v = raw_data[i][j]
            raw_data[i][j] = int(v)
    
    line0 = raw_data[0]
    data_config = {
        "videos": line0[0],
        "endpoints": line0[1],
        "requests": line0[2],
        "caches":  line0[3],
        "cache_size": line0[4]
    }

    #video info loaded
    video_config = raw_data[1]

    # delete first two lines
    del raw_data[0]
    del raw_data[0]

    endpoints = list()
    cache_connections = 0
    datacentre_latency = 0
    index = 0
    endpoint_count = 0
    #load endpoint data
    while endpoint_count < data_config["endpoints"]:
        #end point config line 
        line0 = raw_data[index]
        endpoint = dict()
        endpoint["datacentre"] = line0[0]
        cache_connections = line0[1]

        #for each cache config
        for j in range(index + 1, index + cache_connections + 1):
            line = raw_data[j] # line = {cache_id} {latency}
            endpoint[line[0]] = line[1]
        
        endpoints.append(endpoint)
        index += cache_connections + 1
        endpoint_count +=1
    

    # load requests data
    requests = list()
    for i in range(index, len(raw_data)):
        line = raw_data[i]
        requests.append( (line[0], line[1], line[2]) )

    return data_config, video_config, endpoints, requests


def output_data(caches, filename):
    """
        Prints the output data to file 
        caches structure: list of videos to be stored into a server specified by the key
        eg: test_caches = [
                    [2],    // server 0 stores video 2
                    [3,1],  // server 1 stored videos 3 and 1
                    [0,1]   //Cache server 2 contains videos 0 and 1.
                ]
    """
    cache_count = len(caches)
    data = str(cache_count) + "\n"
    for i in range(len(caches)):
        data += str(i) + " "
        for j in range(len(caches[i])):
            data += str( caches[i][j] ) + " "
        data += "\n"
    with open(filename, "w") as text_file:
	    text_file.write(data)


# print(load_data("me_at_the_zoo.in"))

# test_caches = [
#     [2],
#     [3,1],
#     [0,1]
# ]
# output_data(test_caches, "test.out")