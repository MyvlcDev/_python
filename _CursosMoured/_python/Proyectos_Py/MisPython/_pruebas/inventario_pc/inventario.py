# importing the required modules

import platform


print("[+] Arquitectura :", platform.architecture()[0])
print("[+] Prcoesador :", platform.machine())
## print("[+] Operating System Release :", platform.release())
print("[+] Sistema Operativo :",platform.system())
print("[+]  Version Sistema Operativo :", platform.version())
print("[+] Node: " + platform.node())
print("[+] Plataforma :", platform.platform())
print("[+] Procesador :",platform.processor())