def insertar(id_usuario, id_libro, fecha_prestamo, fecha_devolucion, estado, observaciones, conexionBD):
    try:
        if conexionBD is not None:
            cursor = conexionBD.cursor()
            cursor.execute(
                "INSERT INTO prestamos VALUES (NULL, %s, %s, %s, %s, %s, %s)",
                (id_usuario, id_libro, fecha_prestamo, fecha_devolucion, estado, observaciones)
            )
            conexionBD.commit()
            return True
        else:
            return False
    except Exception:
        return False

def consultar(conexionBD):
    try:
        if conexionBD is not None:
            cursor = conexionBD.cursor()
            cursor.execute("""
                SELECT
                    p.id_prestamo,
                    u.name,
                    l.nombre,
                    p.fecha_prestamo,
                    p.fecha_devolucion,
                    p.estado,
                    p.observaciones
                FROM prestamos p
                INNER JOIN usuarios u ON p.id_usuario = u.matricula
                INNER JOIN libros l ON p.id_libro = l.codigo
            """)
            return cursor.fetchall()
        else:
            return []
    except Exception:
        return []

def consultarAlumno(matricula, conexionBD):
    try:
        if conexionBD is not None:
            cursor = conexionBD.cursor()
            query = """
                SELECT 
                    p.id_prestamo,
                    u.name AS usuario,
                    l.nombre AS libro,
                    DATE_FORMAT(p.fecha_prestamo, '%Y-%m-%d') AS f_prestamo,
                    DATE_FORMAT(p.fecha_devolucion, '%Y-%m-%d') AS f_devolucion,
                    p.estado,
                    p.observaciones
                FROM Prestamos p
                INNER JOIN usuarios u ON p.id_usuario = u.matricula
                INNER JOIN libros l ON p.id_libro = l.codigo
                WHERE p.id_usuario = %s
            """
            cursor.execute(query, (str(matricula).strip(),)) # Forzamos a convertir matricula a string limpio
            resultados = cursor.fetchall()
            cursor.close()
            return resultados
        return []
    except Exception as e:
        print(f"\n[DEBUG ERROR SQL]: {e}")  # <-- Esto te mostrará el error exacto en consola
        input()
        return []

def buscar(prestamo, conexionBD):
    try:
        if conexionBD is not None:
            cursor = conexionBD.cursor()
            cursor.execute("""
                SELECT 
                    id_prestamo, 
                    id_usuario, 
                    id_libro, 
                    fecha_prestamo, 
                    fecha_devolucion, 
                    estado, 
                    observaciones 
                FROM prestamos 
                WHERE id_prestamo = %s OR id_usuario = %s
            """, (prestamo, prestamo))
            return cursor.fetchall()
        else:
            return []
    except Exception:
        return []

def buscarAlumno(prestamo, conexionBD):
    try:
        if conexionBD is not None:
            cursor = conexionBD.cursor()
            cursor.execute("""
                SELECT 
                    id_prestamo, 
                    id_usuario, 
                    id_libro, 
                    fecha_prestamo, 
                    fecha_devolucion, 
                    estado, 
                    observaciones 
                FROM prestamos 
                WHERE id_usuario = %s
            """, (prestamo,))
            return cursor.fetchall()
        else:
            return []
    except Exception:
        return []

def buscarID(prestamo, conexionBD):
    try:
        if conexionBD is not None:
            cursor = conexionBD.cursor()
            cursor.execute("""
                SELECT 
                    id_prestamo, 
                    id_usuario, 
                    id_libro, 
                    fecha_prestamo, 
                    fecha_devolucion, 
                    estado, 
                    observaciones 
                FROM prestamos 
                WHERE id_prestamo = %s
            """, (prestamo,))
            return cursor.fetchall()
        else:
            return []
    except Exception:
        return []

def borrar(id_prestamo, conexionBD):
    try:
        if conexionBD is not None:
            cursor = conexionBD.cursor()
            cursor.execute("DELETE FROM prestamos WHERE id_prestamo = %s", (id_prestamo,))
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
            cursor.execute("SET FOREIGN_KEY_CHECKS = 0")
            cursor.execute("DELETE FROM prestamos")
            cursor.execute("SET FOREIGN_KEY_CHECKS = 1")
            conexionBD.commit()
            return True
        else:
            return False
    except Exception:
        return False

def actualizar(id_prestamo, id_usuario, id_libro, fecha_prestamo, fecha_devolucion, estado, observaciones, conexionBD):
    try:
        if conexionBD is not None:
            cursor = conexionBD.cursor() 
            cursor.execute("""
                UPDATE prestamos
                SET
                    id_usuario = %s,
                    id_libro = %s,
                    fecha_prestamo = %s,
                    fecha_devolucion = %s,
                    estado = %s,
                    observaciones = %s
                WHERE id_prestamo = %s
            """, (id_usuario, id_libro, fecha_prestamo, fecha_devolucion, estado, observaciones, id_prestamo))
            conexionBD.commit()
            return True
        else:
            return False
    except Exception:
        return False