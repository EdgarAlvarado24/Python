import sqlite3

def main():
    usarname = input("Nombre de usuario: ")
    password = getpass.getpass("Contrasena: ")

    if verificacion_credenciales(usarname, password):
        print("login Correcto")
    else:
        print("Login Incorrecto")
def verificacion_credenciales(usarname, password):
    conn = sqlite3.connect('miaplicacion.db')
    cursor = conn.cursor()

    query = f"SELECT id FROM users WHERE usarname={usarname} AND password={password}"
    print("Query a ejecutar: ", query)
    rows = cursor.execute(query)
    data = rows.fetchone()
    print("data es", type(data))
    cursor.close()
    conn.close()

if __name__ == '__main__':
    main()