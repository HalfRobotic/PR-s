import socket

nom_host = socket.gethostname()
dir_ip = socket.gethostbyname(nom_host)

print(f"El nom del teu ordinador es: {nom_host}")
print(f"La direccion IP es: {dir_ip}")
