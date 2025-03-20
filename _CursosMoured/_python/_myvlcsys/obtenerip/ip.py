import dns.resolver
import os
##name = "myvlcsys.com"
print("")
print("********************************")
name= input("Ingrese ip o dominio a resolver configuración: ")
print("********************************")
print("")

for qtype in ["A", "AAAA", "MX", "NS", "TXT", "SOA"]:
    answer = dns.resolver.resolve(name, qtype, raise_on_no_answer=False)
    if answer.rrset is not None:
        print(answer.rrset)


## nuevo

response = os.system("ping -c 1 " + name)


if response == 0:
    print (name + ' responde al ping.')
else:
    print (name + ' NO responde al ping.')


os.system("net user")