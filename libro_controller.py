# Modificación realizada en feature/version1
# Modificación realizada en feature/version2
# Modificación realizada en feature/version3
from libro_model import (
    agregar_libro,
    obtener_libros,
    cambiar_estado,
    buscar_libros,
    eliminar_libro,
    editar_libro
)

from log_controller import guardar_log


def registrar_libro(titulo, autor):

    if titulo and autor:

        resultado = agregar_libro(
            titulo,
            autor
        )

        if resultado:

            guardar_log(
                f"Libro agregado: {titulo}"
            )

            return True

        return False

    return False


def listar_libros():

    return obtener_libros()


def prestar_libro(id_libro):

    cambiar_estado(id_libro, False)

    guardar_log(
        f"Libro prestado ID {id_libro}"
    )


def devolver_libro(id_libro):

    cambiar_estado(id_libro, True)

    guardar_log(
        f"Libro devuelto ID {id_libro}"
    )


def buscar_libro(texto):

    return buscar_libros(texto)


def borrar_libro(id_libro):

    eliminar_libro(id_libro)

    guardar_log(
        f"Libro eliminado ID {id_libro}"
    )

def editar_datos_libro(
    id_libro,
    nuevo_titulo,
    nuevo_autor
):

    editar_libro(
        id_libro,
        nuevo_titulo,
        nuevo_autor
    )

    guardar_log(
        f"Libro editado ID {id_libro}"
    )