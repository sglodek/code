import re
import subprocess

tracert2 = ["""
 1  142.232.221.254  1.891 ms  1.883 ms  1.928 ms
 2  142.232.24.123  0.944 ms  0.997 ms  0.993 ms
 3  142.232.38.94  0.438 ms  0.439 ms  0.431 ms
 4  * 142.232.38.133  0.623 ms  0.600 ms
 5  192.68.70.22  0.920 ms  1.028 ms  1.005 ms
 6  134.87.0.74  2.250 ms  2.251 ms  2.233 ms
 7  199.212.24.64  1.761 ms  1.798 ms  1.993 ms
 8  206.81.82.189  5.880 ms  5.876 ms  5.802 ms
 9  207.231.242.20  5.071 ms  5.239 ms  5.213 ms
10  108.170.245.113  5.289 ms *  5.387 ms
11  108.170.237.189  5.031 ms 216.239.63.189  5.455 ms 209.85.250.59  5.520 ms
12  8.8.8.8  5.370 ms  5.261 ms  5.251 ms
""",
"""
 1  142.232.221.254  1.216 ms  1.254 ms  1.286 ms
 2  142.232.24.123  1.052 ms  1.155 ms  1.149 ms
 3  142.232.38.94  0.437 ms  0.435 ms  0.427 ms
 4  142.232.38.133  0.607 ms *  0.589 ms
 5  192.68.70.22  0.946 ms  0.920 ms  0.924 ms
 6  134.87.0.74  2.225 ms  2.057 ms  2.046 ms
 7  199.212.24.64  2.026 ms  2.059 ms  2.047 ms
 8  206.81.82.189  5.609 ms  5.749 ms  5.650 ms
 9  207.231.242.20  59.001 ms  58.877 ms  58.884 ms
10  * 108.170.245.113  5.186 ms  5.192 ms
11  209.85.243.9  5.268 ms  5.096 ms  5.131 ms
12  216.58.216.174  5.279 ms  5.455 ms  5.439 ms
"""]
addresses_to_check = ["8.8.8.8", "yahoo.com", "google.com", "osnews.com", "facebook.com"]
tracert = []
for address in addresses_to_check:
    route = subprocess.run("traceroute -n " + address, universal_newlines=True, stdout=subprocess.PIPE, shell=True)
    tracert.append(route.stdout.splitlines())

router_dict = {}
for route in tracert:
    previous = None
    for hop in route:
        if hop.startswith("traceroute") == False:
            hop_num = re.search(r'\d{1,2}',hop).group()
            matched = re.findall(r'\d{1,3}[.]\d{1,3}[.]\d{1,3}[.]\d{1,3}', hop)
            for match in matched:
                router_dict.setdefault(match, {"hop": 1, "count" : 0, "previous" : None})
                router_dict[match]["hop"] = hop_num
                router_dict[match]["count"] += 1
                router_dict[match]["previous"] = previous
                previous = match

for router in router_dict:
    rt = """
        ip: {}
        hop: {}
        count: {}
        previous: {}
        """.format(router, router_dict[router]["hop"], router_dict[router]["count"], router_dict[router]["previous"])
    print(rt)

