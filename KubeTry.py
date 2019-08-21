from kubernetes import client, config

config.load_kube_config()

PodIPlist = []
HostIPlist = []
PodIP = 0
HostIP = 0
dicOfIP = {}

v1 = client.CoreV1Api()
print("Listing pods with their IPs:")
ret = v1.list_namespaced_pod("man01-trn-test-01")
for i in ret.items:
    PodIP = i.status.pod_ip
    HostIP = i.status.host_ip
    PodIPlist.append(PodIP)
    HostIPlist.append(HostIP)

    dicOfIP.update({PodIP:HostIP})

    #print("%s" % (i.status.pod_ip))
    # \t%s\t%s i.metadata.namespace, i.metadata.name

#print(ret)
#print(PodIPlist, '\n', HostIPlist)
print(dicOfIP)
