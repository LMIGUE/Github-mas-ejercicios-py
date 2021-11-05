aclNum = int(input("Cual es el número de la ACL IPV4 ? "))
if aclNum >= 1 and aclNum <= 99:
    print("Este es un ACL IPv4 estándar.")
elif aclNum >=100 and aclNum <= 199:
    print("Este es una ACL IPv4 extendida")
else:
    print("Esta ACL IPv4 no es extendida ni estandar .")
