import re
import subprocess

addresses_to_check = ["8.8.8.8", "yahoo.com", "google.com", "osnews.com", "facebook.com"]
tracert = []
for address in addresses_to_check:
    print("Tracing " + address + "...")
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
