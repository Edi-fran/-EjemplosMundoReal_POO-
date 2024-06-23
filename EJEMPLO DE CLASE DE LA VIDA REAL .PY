"""
Este programa modela un sistema de gestión de una biblioteca utilizando principios de Programación Orientada a Objetos (POO). 
El programa define dos clases principales: Libro y Biblioteca. La clase Libro representa un libro individual con atributos 
como título, autor, ISBN y disponibilidad. La clase Biblioteca gestiona una colección de libros y proporciona métodos para 
agregar, modificar, eliminar, prestar y devolver libros.

El programa incluye un menú interactivo que permite al usuario seleccionar opciones para interactuar con la biblioteca. 
El menú se presenta en un bucle infinito hasta que el usuario elige salir. Las opciones disponibles en el menú son:

1. Agregar libro: Permite al usuario agregar un nuevo libro a la biblioteca.
2. Mostrar libros disponibles: Muestra todos los libros que están disponibles en la biblioteca.
3. Modificar libro: Permite al usuario modificar los detalles de un libro existente.
4. Eliminar libro: Permite al usuario eliminar un libro de la biblioteca.
5. Prestar libro: Marca un libro como prestado si está disponible.
6. Devolver libro: Marca un libro como disponible si estaba prestado.
7. Salir: Termina el programa.

Cada opción del menú solicita al usuario la entrada necesaria (como título, autor, ISBN) y llama a las funciones correspondientes 
de la clase Biblioteca o Libro para realizar la acción deseada.
"""

class Libro:
    def __init__(self, titulo, autor, isbn):
        """
        Inicializa un nuevo libro.

        :param titulo: Título del libro.
        :param autor: Autor del libro.
        :param isbn: ISBN del libro.
        """
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.disponible = True

    def prestar(self):
        """
        Marca el libro como prestado si está disponible.
        """
        if self.disponible:
            self.disponible = False
            print(f"El libro '{self.titulo}' ha sido prestado.")
        else:
            print(f"El libro '{self.titulo}' no está disponible.")

    def devolver(self):
        """
        Marca el libro como disponible.
        """
        if not self.disponible:
            self.disponible = True
            print(f"El libro '{self.titulo}' ha sido devuelto.")
        else:
            print(f"El libro '{self.titulo}' ya estaba disponible.")


class Biblioteca:
    def __init__(self, nombre):
        """
        Inicializa una nueva biblioteca.

        :param nombre: Nombre de la biblioteca.
        """
        self.nombre = nombre
        self.libros = []

    def agregar_libro(self, libro):
        """
        Agrega un nuevo libro a la biblioteca.

        :param libro: Objeto de la clase Libro.
        """
        self.libros.append(libro)
        print(f"El libro '{libro.titulo}' ha sido agregado a la biblioteca.")

    def mostrar_libros_disponibles(self):
        """
        Muestra todos los libros disponibles en la biblioteca.
        """
        print("Libros disponibles:")
        for libro in self.libros:
            if libro.disponible:
                print(f"Título: {libro.titulo}, Autor: {libro.autor}, ISBN: {libro.isbn}")

    def modificar_libro(self, isbn, nuevo_titulo=None, nuevo_autor=None):
        """
        Modifica los detalles de un libro existente.

        :param isbn: ISBN del libro a modificar.
        :param nuevo_titulo: Nuevo título del libro.
        :param nuevo_autor: Nuevo autor del libro.
        """
        for libro in self.libros:
            if libro.isbn == isbn:
                if nuevo_titulo:
                    libro.titulo = nuevo_titulo
                if nuevo_autor:
                    libro.autor = nuevo_autor
                print(f"El libro con ISBN {isbn} ha sido modificado.")
                return
        print(f"No se encontró el libro con ISBN {isbn}.")

    def eliminar_libro(self, isbn):
        """
        Elimina un libro de la biblioteca.

        :param isbn: ISBN del libro a eliminar.
        """
        for libro in self.libros:
            if libro.isbn == isbn:
                self.libros.remove(libro)
                print(f"El libro con ISBN {isbn} ha sido eliminado.")
                return
        print(f"No se encontró el libro con ISBN {isbn}.")


def menu():
    biblioteca = Biblioteca("Biblioteca Central")
    while True:
        print("\nMenú de Biblioteca")
        print("1. Agregar libro")
        print("2. Mostrar libros disponibles")
        print("3. Modificar libro")
        print("4. Eliminar libro")
        print("5. Prestar libro")
        print("6. Devolver libro")
        print("7. Salir")
        opcion = input("Elige una opción: ")

        if opcion == '1':
            titulo = input("Título del libro: ")
            autor = input("Autor del libro: ")
            isbn = input("ISBN del libro: ")
            libro = Libro(titulo, autor, isbn)
            biblioteca.agregar_libro(libro)
        elif opcion == '2':
            biblioteca.mostrar_libros_disponibles()
        elif opcion == '3':
            isbn = input("ISBN del libro a modificar: ")
            nuevo_titulo = input("Nuevo título (dejar en blanco para no cambiar): ")
            nuevo_autor = input("Nuevo autor (dejar en blanco para no cambiar): ")
            biblioteca.modificar_libro(isbn, nuevo_titulo or None, nuevo_autor or None)
        elif opcion == '4':
            isbn = input("ISBN del libro a eliminar: ")
            biblioteca.eliminar_libro(isbn)
        elif opcion == '5':
            isbn = input("ISBN del libro a prestar: ")
            for libro in biblioteca.libros:
                if libro.isbn == isbn:
                    libro.prestar()
                    break
            else:
                print(f"No se encontró el libro con ISBN {isbn}.")
        elif opcion == '6':
            isbn = input("ISBN del libro a devolver: ")
            for libro in biblioteca.libros:
                if libro.isbn == isbn:
                    libro.devolver()
                    break
            else:
                print(f"No se encontró el libro con ISBN {isbn}.")
        elif opcion == '7':
            break
        else:
            print("Opción no válida. Inténtalo de nuevo.")


# Ejemplo de uso
if __name__ == "__main__":
    menu()
