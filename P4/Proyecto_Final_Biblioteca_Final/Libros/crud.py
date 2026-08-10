def insertar(nombre, autor, editorial, idioma, conexionBD):
    try:
        if conexionBD is not None:
            cursor = conexionBD.cursor()
            cursor.execute(
                "INSERT INTO libros VALUES (NULL, %s, %s, %s, %s)", 
                (nombre, autor, editorial, idioma)
            )
            conexionBD.commit()
            return True
        else:
            return False   
    except: 
        return False 

def consultar(conexionBD):
    try:
        if conexionBD is not None:
            cursor = conexionBD.cursor()
            cursor.execute("SELECT * FROM libros")
            return cursor.fetchall()
        else:
            return []
    except:
        return []  

def buscar(libro, conexionBD):
    try:
        if conexionBD is not None:
            cursor = conexionBD.cursor()
            cursor.execute(
                "SELECT * FROM libros WHERE nombre = %s OR codigo = %s", 
                (libro, libro)
            )
            return cursor.fetchall()
        else:
            return []
    except:
        return [] 

def borrar(codigo, conexionBD):
    try:
        if conexionBD is not None:
            cursor = conexionBD.cursor()
            cursor.execute("DELETE FROM libros WHERE codigo = %s", (codigo,))
            conexionBD.commit()
            return True
        else:
            return False
    except Exception:
        return False
    
def vaciar(conexionBD):
    try:
        if conexionBD is not None:
            cursor = conexionBD.cursor()
            cursor.execute("DELETE FROM libros")
            conexionBD.commit()
            cursor.close()
            return True
        else:
            return False   
    except:
        return False

def actualizar(codigo, libro, autor, editorial, idioma, conexionBD):
    try:
        if conexionBD is not None:
            cursor = conexionBD.cursor()
            cursor.execute(
                "UPDATE libros SET nombre = %s, autor = %s, editorial = %s, idioma = %s WHERE codigo = %s",
                (libro, autor, editorial, idioma, codigo)
            )
            conexionBD.commit()
            return True
        else:
            return False   
    except: 
        return False