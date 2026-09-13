from database import conectar

def agregar_libro(titulo, autor):

    print("Entrando a agregar_libro")

    conexion = conectar()

    print("Conexion:", conexion)

    if conexion is None:
        print("No se pudo conectar a MySQL")
        return False

    cursor = conexion.cursor()

    print("Cursor creado")

    # VALIDAR DUPLICADOS
    sql = """
        SELECT *
        FROM libros
        WHERE titulo = %s
    """

    print("Buscando duplicados")

    cursor.execute(sql, (titulo,))

    resultado = cursor.fetchone()

    print("Resultado duplicado:", resultado)

    if resultado:

        print("Libro duplicado")

        conexion.close()
        return False

    sql = """
        INSERT INTO libros (
            titulo,
            autor,
            disponible
        )
        VALUES (%s, %s, %s)
    """

    print("Ejecutando INSERT")

    cursor.execute(
        sql,
        (titulo, autor, True)
    )

    print("INSERT realizado")

    conexion.commit()

    print("COMMIT realizado")

    conexion.close()

    print("Conexion cerrada")

    return True

def obtener_libros():

    conexion = conectar()
    cursor = conexion.cursor(dictionary=True)

    cursor.execute(
        "SELECT * FROM libros"
    )

    libros = cursor.fetchall()

    conexion.close()

    return libros


def cambiar_estado(id_libro, estado):

    conexion = conectar()
    cursor = conexion.cursor()

    sql = """
        UPDATE libros
        SET disponible = %s
        WHERE id = %s
    """

    cursor.execute(
        sql,
        (estado, id_libro)
    )

    conexion.commit()
    conexion.close()


def buscar_libros(texto):

    conexion = conectar()
    cursor = conexion.cursor(dictionary=True)

    sql = """
        SELECT *
        FROM libros
        WHERE titulo LIKE %s
        OR autor LIKE %s
    """

    busqueda = f"%{texto}%"

    cursor.execute(
        sql,
        (busqueda, busqueda)
    )

    resultados = cursor.fetchall()

    conexion.close()

    return resultados


def eliminar_libro(id_libro):

    conexion = conectar()
    cursor = conexion.cursor()

    sql = """
        DELETE FROM libros
        WHERE id = %s
    """

    cursor.execute(sql, (id_libro,))

    conexion.commit()
    conexion.close()

def editar_libro(
    id_libro,
    nuevo_titulo,
    nuevo_autor
):

    conexion = conectar()
    cursor = conexion.cursor()

    sql = """
        UPDATE libros
        SET titulo = %s,
            autor = %s
        WHERE id = %s
    """

    cursor.execute(
        sql,
        (
            nuevo_titulo,
            nuevo_autor,
            id_libro
        )
    )

    conexion.commit()
    conexion.close()
