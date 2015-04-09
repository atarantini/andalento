"""
andalento should check your internet connection latency with various internet
server providers that have speedtest servers
"""
import random
import json
from time import time

import requests


def latency(host, samples=5):
    """
    Measure server latency downloading an empty file (latency.txt). Take
    a number of samples, discard the slowest one and average the results.

    :param host:    String with the hostname where the speedtest is hosted
    :param samples: Integer with the number of samples to take

    :return:        Integer with the latency, in milliseconds or False
                    if was unable to connect
    """
    times = []
    slowest = 0
    for i in range(samples):
        total_start_time = time()
        try:
            requests.get("http://{}/speedtest/latency.txt?x={}".format(
                host,
                str(random.random())
            ), headers={'Connection': 'Keep-Alive'})
        except(requests.exceptions.ConnectionError, TypeError):
            return False
        request_time = time() - total_start_time
        times.append(request_time)
        if request_time > slowest:
            slowest = request_time
    times.remove(slowest)

    return int(round(sum(times) * 1000 / 4))

if __name__ == "__main__":
    # Get the list of servers
    servers = json.load(open("servers-AR.json"))

    # Make the tests
    results = []
    for server in servers:
        host = server.get("-host")
        ms = latency(host)
        if ms:
            results.append((ms, host, server.get("-name"), server.get("-sponsor")))

    # Return the results ordered: lower latency first
    results.sort()
    c = 1
    for ms, host, name, sponsor in results:
        print "{}) {}/{} ({}): {}ms".format(c, name, sponsor, host, ms)
        c += 1