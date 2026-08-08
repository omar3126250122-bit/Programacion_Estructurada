def existe_matricula(matricula, conexionBD):
    try:
        if conexionBD is not None:
            cursor = conexionBD.cursor()
            cursor.execute("SELECT matricula FROM usuarios WHERE matricula = %s", (matricula,))
            resultado = cursor.fetchone()
            return resultado is not None
        return False
    except:
        return False
    
def insertar(matricula, name, password, rol, conexionBD):
    try:
        if conexionBD is not None:
            cursor = conexionBD.cursor()
            cursor.execute("INSERT INTO usuarios (matricula, name, password, rol) VALUES (%s, %s, %s, %s)", (matricula, name, password, rol))
            conexionBD.commit()
            return True
        return False   
    except:
        return False

def consultar(conexionBD):
    try:
        if conexionBD is not None:
            cursor = conexionBD.cursor()
            cursor.execute("SELECT matricula, name, password, rol FROM usuarios")
            return cursor.fetchall()
        return []
    except:
        return []

def buscar(criterio, conexionBD):
    try:
        if conexionBD is not None:
            cursor = conexionBD.cursor()
            param_like = f"%{criterio}%"
            cursor.execute(
                "SELECT matricula, name, password, rol FROM usuarios WHERE matricula = %s OR name LIKE %s", 
                (criterio, param_like)
            )
            return cursor.fetchall()
        return []
    except:
        return [] 

def borrar(codigo, conexionBD):
    try:
        if conexionBD is not None:
            cursor = conexionBD.cursor()
            cursor.execute("DELETE FROM usuarios WHERE matricula = %s", (codigo,))
            conexionBD.commit()
            return True
        return False   
    except Exception:
        return False

def vaciar(conexionBD):
    try:
        if conexionBD is not None:
            cursor = conexionBD.cursor()
            cursor.execute("DELETE FROM usuarios")   
            conexionBD.commit()
            cursor.close()
            return True
        return False   
    except:
        return False

def actualizar(matricula, name, password, rol, conexionBD):
    try:
        if conexionBD is not None:
            cursor = conexionBD.cursor()
            cursor.execute(
                "UPDATE usuarios SET name = %s, password = %s, rol = %s WHERE matricula = %s",
                (name, password, rol, matricula)
            )
            conexionBD.commit()
            return True
        return False   
    except: 
        return False