import sys
from server import Servidor
from utils import data_json

if __name__ == "__main__":
    HOST = data_json("HOST")
    PORT = data_json("PORT")
    servidor = Servidor(HOST, PORT)
    
    try:
        while True:
            input("[Presione Ctrl+C para cerrar]".center(82, "+") + "\n")
    except ConnectionError:
        print("No se pudo inicializar el servidor".center(80, " "))
        sys.exit()
    except KeyboardInterrupt:
        print("\n\n")
        print("Cerrando servidor...".center(80, " "))
        print("".center(82, "-"))
        print("".center(82, "-") + "\n")
        servidor.server_sock.close()
        sys.exit()