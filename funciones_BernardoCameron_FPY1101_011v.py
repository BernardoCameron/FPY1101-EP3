import datetime as fecha

def registrarLibro(libros):
    try:
        titulo = input("Ingrese el titulo del libro: ").upper()
        autor = input("Ingrese el autor del libro: ").upper()
        anio = input("Ingrese el año de publicacion del libro: ").upper()
        if titulo == "" or autor == "" or anio == "":
            print("Debe ingresar todos los datos")
            titulo = input("Ingrese el titulo del libro: ").upper()
            autor = input("Ingrese el autor del libro: ").upper()
            anio = input("Ingrese el año de publicacion del libro: ").upper()

        sku = titulo.replace(" ", "")[:6] + "-" + autor[:3] + "-" + anio
        libro = {
            "Titulo": titulo,
            "Autor": autor,
            "Año de publicacion": anio,
            "SKU": sku,
            "Estado": "Disponible"
        }
        libros.append(libro)
        print("Libro registrado con exito")
    except:
        print("Error al registrar el libro")




def prestarLibro(libros, prestamos):

    nombre = input("Ingrese el nombre del usuario: ").upper()
    sku = input("Ingrese el SKU del libro: ").upper()

    for libro in libros:
        if sku == libro["SKU"] and libro["Estado"] == "Disponible":
            libro["Estado"] = "Prestado"
            print("Gracias por pedir tu libro")
            prestamo = {
                "Nombre": nombre,
                "SKU": sku,
                "Fecha": fecha.datetime.now()
            }
            prestamos.append(prestamo)
            break
    else:
        print("Libro no disponible")


def listarLibros(libros):
    print("listas")
    print(f"\tTITULO\t\tAUTOR\t\tAÑO DE PUBLICACION\t\tSKU")
    for libro in libros:
        print(f"{libro["Titulo"]}\t\t{libro["Autor"]}\t\t{libro["Año de publicacion"]}\t\t{libro["SKU"]}")

def imprimirReportePrestamos(prestamos):
    
    with open("reporte_prestamos.txt", "w") as file:
        file.write("USUARIO\t\t\tTITULO\t\t\tFECHA\n")
        for prestamo in prestamos:
            file.write(f"{prestamo["Nombre"]}\t\t{prestamo["SKU"]}\t\t{prestamo["Fecha"]}\n")

