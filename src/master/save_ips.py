

def save_ips_name(name):

    data = open("cache/nodes.txt","w")
    data.write(str(name.decode())+"\n")
    data.close()

    

