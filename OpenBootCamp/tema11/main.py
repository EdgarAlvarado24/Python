import getpass
import sqlite3

def main():
    crear_usuario(5, "maria", "mariados")
def main2():
    username = input("Nombre de usuario: ")
    password = getpass.getpass("Contraseña: ")

    if verifica_credenciales(username, password):
        print("Login Correcto")
    else:
        print("Login Incorrecto")
def verifica_credenciales(username, password):
    conn = sqlite3.connect('miaplicacion.db')
    cursor = conn.cursor()

    query = f"SELECT id from users WHERE username='{username}' AND password='{password}'"
    print("Query a ejecutar: ", query)
    rows = cursor.execute(query)
    data = rows.fetchone()

    cursor.close()
    conn.close()

def crear_usuario(identificador, usuario, clave):
    conn = sqlite3.connect('miaplicacion.db', isolation_level=None)
    cursor = conn.cursor()

    query = '''INSERT INTO users (id, username, password) VALUES (?, ?, ?)'''
    cursor.execute(query, (identificador, usuario, clave))

    conn.commit()
    cursor.close()
    conn.close()

if __name__ == '__main__':
    main()