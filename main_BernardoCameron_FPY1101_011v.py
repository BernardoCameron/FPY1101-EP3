import funciones_BernardoCameron_FPY1101_011v as fn

libros = [{"Titulo": "Alas de Hierro", "Autor": "Rebecca Yarros", "Año de publicacion": "2024", "SKU": "ALASDE-REB-2024", "Estado": "Disponible"}, {"Titulo": "La sombra de la Sirena", "Autor": "Camilla Lackberg", "Año de publicacion": "2003", "SKU": "LASOMB-CAM-2003", "Estado": "Disponible"}]
prestamos = []



while True:
    print("Bienvenido")
    print("Ingrese alguna de las opciones")
    print("1. Registrar libro")
    print("2. Prestar Libro")
    print("3. Listar todos los libros")
    print("4. Imprimir reporte de prestamos")
    print("5. Salir del programa")

    op = input("Ingrese una opcion (1-5): ")

    if op == "1":
        print("Registrar libro")
        fn.registrarLibro(libros)
    elif op == "2":
        print("Prestar libro")
        fn.prestarLibro(libros, prestamos)
    elif op == "3":
        print("Listar libros")
        fn.listarLibros(libros)
    elif op == "4":
        print("Imprimir reporte")
        fn.imprimirReportePrestamos(prestamos)
    elif op == "5":
        print("Programa finalizado...")
        print("Desarrollado por Bernardo Cameron")
        print("RUN: 19.277.900-6")
        break


