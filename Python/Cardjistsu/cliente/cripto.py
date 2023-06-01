from math import ceil
###################################################################################################
def encriptar(msg : bytearray) -> bytearray:
    a = bytearray()
    b = bytearray()
    c = bytearray()
    for i in range(0, len(msg), 3):
        a.extend(msg[i].to_bytes(1, byteorder='little'))
    for i in range(1, len(msg), 3):
        b.extend(msg[i].to_bytes(1, byteorder='little'))
    for i in range(2, len(msg), 3):
        c.extend(msg[i].to_bytes(1, byteorder='little'))
    suma = 0
    suma += int.from_bytes(a[0].to_bytes(1, 'little'), 'little')
    suma += int.from_bytes(c[len(c) - 1].to_bytes(1, 'little'), 'little')
    if len(b) % 2 == 0:
        index1 = int(len(b) / 2)
        suma += int.from_bytes(b[index1 - 1].to_bytes(1,'little'), byteorder='little')
        suma += int.from_bytes(b[index1].to_bytes(1,'little'), byteorder='little')
    if len(b) % 2 != 0:
        index1 = ceil(len(b) / 2)
        suma += int.from_bytes(b[index1 - 1].to_bytes(1,'little'), byteorder='little')
    bytes_encriptados = bytearray()
    if suma % 2 == 0:
        bytes_encriptados.extend(b'\x00')
        bytes_encriptados.extend(c)
        bytes_encriptados.extend(a)
        bytes_encriptados.extend(b)
    else:
        bytes_encriptados.extend(b'\x01')
        bytes_encriptados.extend(a)
        bytes_encriptados.extend(c)
        bytes_encriptados.extend(b)
    # Completar con el proceso de encriptación
    return bytes_encriptados


def desencriptar(msg : bytearray) -> bytearray:
    # Completar con el proceso de desencriptación
    if len(msg) > 0:
        mensaje_desencriptado = bytearray()
        a_d = bytearray()
        b_d = bytearray()
        c_d = bytearray()
        largo_c = 0
        largo_b = 0
        largo_a = 0
        for i in range(1, len(msg), 3):
            largo_a += 1
        for i in range(2, len(msg), 3):
            largo_b += 1
        for i in range(3, len(msg), 3):
            largo_c += 1
        if msg[0].to_bytes(1, byteorder='little') == b'\x00':
            for i in range(1 ,1 + largo_c):
                c_d.extend(msg[i].to_bytes(1, byteorder='little'))
            for i in range(largo_c + largo_a + 1,(largo_c + largo_a + 1) + largo_b):
                b_d.extend(msg[i].to_bytes(1, byteorder='little'))
            for i in range(largo_c + 1,largo_c + largo_a + 1):
                a_d.extend(msg[i].to_bytes(1, byteorder='little'))
            if largo_a == largo_b == largo_c:
                for i in range(int(len(msg) / 3)):
                    mensaje_desencriptado.extend(a_d[i].to_bytes(1, 'little'))
                    mensaje_desencriptado.extend(b_d[i].to_bytes(1, 'little'))
                    mensaje_desencriptado.extend(c_d[i].to_bytes(1, 'little'))
            if largo_b > largo_c and largo_a == largo_b:
                for i in range(largo_c):
                    mensaje_desencriptado.extend(a_d[i].to_bytes(1, 'little'))
                    mensaje_desencriptado.extend(b_d[i].to_bytes(1, 'little'))
                    mensaje_desencriptado.extend(c_d[i].to_bytes(1, 'little'))
                mensaje_desencriptado.extend(a_d[largo_a - 1].to_bytes(1, 'little'))
                mensaje_desencriptado.extend(b_d[largo_b - 1].to_bytes(1, 'little'))
            if largo_a > largo_b:
                for i in range(largo_b):
                    mensaje_desencriptado.extend(a_d[i].to_bytes(1, 'little'))
                    mensaje_desencriptado.extend(b_d[i].to_bytes(1, 'little'))
                    mensaje_desencriptado.extend(c_d[i].to_bytes(1, 'little'))
                mensaje_desencriptado.extend(a_d[largo_a - 1].to_bytes(1, 'little'))
        elif msg[0].to_bytes(1, byteorder='little') == b'\x01':
            for i in range(largo_a + 1, (largo_a + 1) + largo_c):
                c_d.extend(msg[i].to_bytes(1, byteorder='little'))
            for i in range((largo_c + largo_a) + 1, (largo_c + largo_a + 1) + largo_b):
                b_d.extend(msg[i].to_bytes(1, byteorder='little'))
            for i in range(1, 1 + largo_a):
                a_d.extend(msg[i].to_bytes(1, byteorder='little'))
            if largo_a == largo_b == largo_c:
                for i in range(int(len(msg) / 3)):
                    mensaje_desencriptado.extend(a_d[i].to_bytes(1, 'little'))
                    mensaje_desencriptado.extend(b_d[i].to_bytes(1, 'little'))
                    mensaje_desencriptado.extend(c_d[i].to_bytes(1, 'little'))
            if largo_b > largo_c and largo_a == largo_b:
                for i in range(largo_c):
                    mensaje_desencriptado.extend(a_d[i].to_bytes(1, 'little'))
                    mensaje_desencriptado.extend(b_d[i].to_bytes(1, 'little'))
                    mensaje_desencriptado.extend(c_d[i].to_bytes(1, 'little'))
                mensaje_desencriptado.extend(a_d[largo_a - 1].to_bytes(1, 'little'))
                mensaje_desencriptado.extend(b_d[largo_b - 1].to_bytes(1, 'little'))
            if largo_a > largo_b:
                for i in range(largo_b):
                    mensaje_desencriptado.extend(a_d[i].to_bytes(1, 'little'))
                    mensaje_desencriptado.extend(b_d[i].to_bytes(1, 'little'))
                    mensaje_desencriptado.extend(c_d[i].to_bytes(1, 'little'))
                mensaje_desencriptado.extend(a_d[largo_a - 1].to_bytes(1, 'little'))
        return mensaje_desencriptado
    else:
        return b""

if __name__ == "__main__":
    # Testear encriptar

    msg_original = bytearray(b'\x05\x08\x03\x02\x04\x03\x05\x09\x05\x09\x01')
    msg_esperado = bytearray(b'\x01\x05\x02\x05\x09\x03\x03\x05\x08\x04\x09\x01')
    


    msg_encriptado = encriptar(msg_original) #hacer copy paste del cripto del server
    if msg_encriptado != msg_esperado:
        print("[ERROR] Mensaje escriptado erroneamente")
    else:
        print("[SUCCESSFUL] Mensaje escriptado correctamente")
    
    # Testear desencriptar
    msg_desencriptado = desencriptar(msg_esperado)
    if msg_desencriptado != msg_original: #cambiar a mensaje original
        print("[ERROR] Mensaje descencriptado erroneamente")
    else:
        print("[SUCCESSFUL] Mensaje descencriptado correctamente")
