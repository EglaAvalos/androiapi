from mysql.connector import Error
from persistence.db import get_connection

class Encargado:
    def __init__(self, puesto, nombre, telefono=None):
        self.puesto = puesto
        self.nombre = nombre
        self.telefono = telefono

    @classmethod
    def get(cls):
        try:
            connection = get_connection()
            cursor = connection.cursor(dictionary=True)
            cursor.execute('SELECT id, puesto, nombre, telefono FROM encargados')
            return cursor.fetchall()
        except Error as ex:
            return str(ex)
        finally:
            cursor.close()
            connection.close()

    @classmethod
    def save(cls, encargado):
        try:
            connection = get_connection()
            cursor = connection.cursor()
            cursor.execute(
                'INSERT INTO encargados (puesto, nombre, telefono) VALUES (%s, %s, %s)',
                (encargado.puesto, encargado.nombre, encargado.telefono)
            )
            connection.commit()
            return cursor.lastrowid
        except Error as ex:
            return str(ex)
        finally:
            cursor.close()
            connection.close()
