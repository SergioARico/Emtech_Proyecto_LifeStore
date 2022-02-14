# coding=utf-8
# importar datos de lifestore_file
from lifestore_file import lifestore_products, lifestore_sales, lifestore_searches

"""
LifeStore_file data:
lifestore_products = [id_product, name, price, category, stock]
lifestore_sales = [id_sale, id_product, score (from 1 to 5), date, refund (1 true or 0 false)]
lifestore_searches = [id_search, id product]
"""
# registro de 2 usuarios y 2 contraseñas
usuarios_registrados = [["admin", "1234"],
                        ["sergio", "2708"]]
entrada = 1

while entrada == 1:
    print(
        "\n======================================================================================================================================\n"
        "--------------------------------------------------------  B I E N V E N I D O --------------------------------------------------------\n")
    # Mensaje de bienvenida al usuario
    print("Ingresa Usuario y Contraseña para Comenzar...\n")
    usuario = input("Usuario: ")
    contrasena = input("Contraseña: ")
    # Revisamos si el usuario y contraseña coincide con alguna de las almacenadas
    if (usuarios_registrados[0][0] == usuario and usuarios_registrados[0][1] == contrasena) or \
            (usuarios_registrados[1][0] == usuario and usuarios_registrados[1][1] == contrasena):
        # si coincide se comienza el analisis del proyecto
        """=================================================================
        ======================= Comienza el analisis =======================
        =================================================================="""


        def menores_ventas(ventas_categorias, lifestore_productos):
            i = 1
            for venta_categoria in ventas_categorias:
                for lifestore_producto in lifestore_productos:
                    if venta_categoria[1] == lifestore_producto[0] and i < 6:
                        # Comparo el id de la lista por categoria con el id de la lista de lifestore_product
                        # si coincide imprimo el ID y el nombre del producto
                        print("No.{} ID: {} Ventas:{} --> {}"
                              .format(i, venta_categoria[1], venta_categoria[0], lifestore_producto[1]))
                        i += 1


        def menores_busquedas(busquedas_categorias, lifestore_productos):
            i = 1
            for busqueda_categoria in busquedas_categorias:
                for lifestore_producto in lifestore_productos:
                    if busqueda_categoria[1] == lifestore_producto[0] and i < 11:
                        # Comparo el id de la lista por categoria con el id de la lista de lifestore_product
                        # si coincide imprimo el ID y el nombre del producto
                        print("No.{} ID: {} Busquedas:{} --> {}"
                              .format(i, busqueda_categoria[1], busqueda_categoria[0], lifestore_producto[1]))
                        i += 1


        # arreglo con id de productos
        id_productos = [lifestore_product[0] for lifestore_product in lifestore_products]

        """" ================ Listado con 5 productos MAYORES VENTAS ================"""

        # pasar a una lista el id de los productos vendidos sin devolucion
        productos_vendidos = [lifestore_sale[1] for lifestore_sale in lifestore_sales if lifestore_sale[4] == 0]
        compras_frec_id = []
        for id_producto in id_productos:  # lista con id de productos [1, 2, 3,...,96]
            compras_frec_id.append([productos_vendidos.count(id_producto), id_producto])
            # se agrega a lista compras_frec_id = [frecuencia de id_producto (de acuerdo al for) en productos vendidos, id_producto]

        # ordena la lista de de mayor a menor por la frecuencia de compra
        compras_frec_id = sorted(compras_frec_id, reverse=True)

        # Numero de productos mas vendidos a mostrar?
        num_mas_vendidos = 5
        ranking_productos_vendidos = []

        for compra_frec_id in compras_frec_id:
            for lifestore_product in lifestore_products:  # recorrere la lista de productos para cada compra_frec_id
                # si coinciden los id's tomamos frecuencia, id y nombre
                if compra_frec_id[1] == lifestore_product[0]:
                    ranking_productos_vendidos.append([compra_frec_id[0], compra_frec_id[1], lifestore_product[1]])
        print(
            "\n======================================================================================================================================\n"
            "----------------------------------------------------  TOP {} Productos MÁS VENDIDOS --------------------------------------------------                                \n"
            "======================================================================================================================================"
                .format(num_mas_vendidos))
        i = 1
        for ranking_producto_vendido in ranking_productos_vendidos:
            if i <= num_mas_vendidos:  # mostramos el numero de prod solicitados
                print("No.{} ID:{} Ventas:{} --> {}".format(i, ranking_producto_vendido[1], ranking_producto_vendido[0],
                                                            ranking_producto_vendido[2]))
                i += 1

        input("\nEnter para continuar....")  # Dar un momento al usuario a obervar la informacion y continuar

        """================ 10 Productos con MAYORES Busquedas================"""
        # lista con el id de los productos buscados
        busquedas_id = [lifestore_search[1] for lifestore_search in lifestore_searches]
        busquedas_frec_id = []

        for id_producto in id_productos:  # [1, 2, 3, 4, 5 ..., 96]
            # se agrega la frecuencia con la que se encuentra cada num en la lista de los id's buscados
            busquedas_frec_id.append([busquedas_id.count(id_producto), id_producto])
            # busquedas_frec_id = [frecuencia, id_product]

        busquedas_frec_id = sorted(busquedas_frec_id, reverse=True)

        # Num de Productos MAS buscados
        num_mas_buscados = 10
        print(
            "\n======================================================================================================================================\n"
            "----------------------------------------------------  TOP {} Productos MÁS BUSCADOS --------------------------------------------------                                \n"
            "======================================================================================================================================".format(
                num_mas_buscados))
        i = 1
        for busqueda_frec_id in busquedas_frec_id:
            for lifestore_product in lifestore_products:
                # Si coinciden los id's e i aun no alcanza el num de productos a mostrar
                if busqueda_frec_id[1] == lifestore_product[0] and i <= num_mas_buscados:
                    print("No.{} ID:{} Búsquedas:{} --> {}".format(i, busqueda_frec_id[1], busqueda_frec_id[0],
                                                                   lifestore_product[1]))
                    i += 1
                # darle un stop para continuar
        input("\nEnter para continuar....")

        """ ================ Por categoria, generar un listado con los 5 productos con menores ventas"""

        # Genero un arreglo unicamente con las categorias
        categorias = ["procesadores", "tarjetas de video", "tarjetas madre", "discos duros", "memorias usb",
                      "pantallas", "bocinas", "audifonos"]

        # Listas para guardar las ventas por categorias
        ventas_procesadores = []
        ventas_tarjetas_video = []
        ventas_tarjetas_madre = []
        ventas_discos_duros = []
        ventas_memorias_usb = []
        ventas_pantallas = []
        ventas_bocinas = []
        ventas_audifonos = []
        # Ordenar lista en forma Ascendente (Min a Max) antes de entrar al for
        compras_frec_id = sorted(compras_frec_id)

        for compra_frec_id in compras_frec_id:  # lista ordenada
            for lifestore_product in lifestore_products:
                if compra_frec_id[1] == lifestore_product[0]:  # Comparación de id
                    # Se ordenan las ventas por categoria y de menor a mayor (lista previamente ordenada)
                    if lifestore_product[3] == categorias[0]:
                        ventas_procesadores.append(compra_frec_id)
                    elif lifestore_product[3] == categorias[1]:
                        ventas_tarjetas_video.append(compra_frec_id)
                    elif lifestore_product[3] == categorias[2]:
                        ventas_tarjetas_madre.append(compra_frec_id)
                    elif lifestore_product[3] == categorias[3]:
                        ventas_discos_duros.append(compra_frec_id)
                    elif lifestore_product[3] == categorias[4]:
                        ventas_memorias_usb.append(compra_frec_id)
                    elif lifestore_product[3] == categorias[5]:
                        ventas_pantallas.append(compra_frec_id)
                    elif lifestore_product[3] == categorias[6]:
                        ventas_bocinas.append(compra_frec_id)
                    elif lifestore_product[3] == categorias[7]:
                        ventas_audifonos.append(compra_frec_id)

        # inicializo la variable en 1 para que inicialice el while
        categoria_seleccionada = 1
        while (categoria_seleccionada != 0):
            print(
                "\n======================================================================================================================================\n"
                "----------------------------------------------------  Productos con MENORES VENTAS --------------------------------------------------                                \n"
                "======================================================================================================================================\n")
            print(
                "Para Mostrar los productos con menores ventas por 'categoria', \nSelecciona la categoria de tu interes: ")
            print("(1) Procesadores\n"
                  "(2) Tarjetas de Video\n"
                  "(3) Tarjetas Madre\n"
                  "(4) Discos Duros\n"
                  "(5) Memorias USB\n"
                  "(6) Pantallas\n"
                  "(7) Bocinas\n"
                  "(8) Audifonos\n"
                  "(0) Continuar")
            categoria_seleccionada = int(input("Opcion: "))

            if categoria_seleccionada == 1:
                print("\n\nTOP 5 Productos con MENORES Ventas Categoria: {}\n".format(categorias[0]))
                menores_ventas(ventas_procesadores, lifestore_products)
                input("\nEnter para continuar")
            elif categoria_seleccionada == 2:
                print("\n\nTOP 5 Productos con MENORES Ventas Categoria: {}\n".format(categorias[1]))
                menores_ventas(ventas_tarjetas_video, lifestore_products)
                input("\nEnter para continuar")
            elif categoria_seleccionada == 3:
                print("\n\nTOP 5 Productos con MENORES Ventas Categoria: {}\n".format(categorias[2]))
                menores_ventas(ventas_tarjetas_madre, lifestore_products)
                input("\nEnter para continuar")
            elif categoria_seleccionada == 4:
                print("\n\nProductos con MENORES Ventas Categoria: {}\n".format(categorias[3]))
                menores_ventas(ventas_discos_duros, lifestore_products)
                input("\nEnter para continuar")
            elif categoria_seleccionada == 5:
                print("\n\nTOP 5 Productos con MENORES Ventas Categoria: {}\n".format(categorias[4]))
                menores_ventas(ventas_memorias_usb, lifestore_products)
                input("\nEnter para continuar")
            elif categoria_seleccionada == 6:
                print("\n\nTOP 5 Productos con MENORES Ventas Categoria: {}\n".format(categorias[5]))
                menores_ventas(ventas_pantallas, lifestore_products)
                input("\nEnter para continuar")
            elif categoria_seleccionada == 7:
                print("\n\nOP 5 Productos con MENORES Ventas Categoria: {}\n".format(categorias[6]))
                menores_ventas(ventas_bocinas, lifestore_products)
                input("\nEnter para continuar")
            elif categoria_seleccionada == 8:
                print("\n\nTOP 5 Productos con MENORES Ventas Categoria: {}\n".format(categorias[7]))
                menores_ventas(ventas_audifonos, lifestore_products)
                input("\nEnter para continuar")

        """ ================ Por categoria, generar un listado con los 10 productos con menores busquedas"""
        busquedas_procesadores = []
        busquedas_tarjetas_video = []
        busquedas_tarjetas_madre = []
        busquedas_discos_duros = []
        busquedas_memorias_usb = []
        busquedas_pantallas = []
        busquedas_bocinas = []
        busquedas_audifonos = []
        # Ordenar la lista de busquedas de menor a mayor
        busquedas_frec_id = sorted(busquedas_frec_id)

        for busqueda_frec_id in busquedas_frec_id:
            for lifestore_product in lifestore_products:
                if busqueda_frec_id[1] == lifestore_product[0]:  # Comparo el id de ambas listas
                    # Se ordenan las busquedas por categoria y de menor a mayor (lista previamente ordenada)
                    if lifestore_product[3] == categorias[0]:
                        busquedas_procesadores.append(busqueda_frec_id)
                    elif lifestore_product[3] == categorias[1]:
                        busquedas_tarjetas_video.append(busqueda_frec_id)
                    elif lifestore_product[3] == categorias[2]:
                        busquedas_tarjetas_madre.append(busqueda_frec_id)
                    elif lifestore_product[3] == categorias[3]:
                        busquedas_discos_duros.append(busqueda_frec_id)
                    elif lifestore_product[3] == categorias[4]:
                        busquedas_memorias_usb.append(busqueda_frec_id)
                    elif lifestore_product[3] == categorias[5]:
                        busquedas_pantallas.append(busqueda_frec_id)
                    elif lifestore_product[3] == categorias[6]:
                        busquedas_bocinas.append(busqueda_frec_id)
                    elif lifestore_product[3] == categorias[7]:
                        busquedas_audifonos.append(busqueda_frec_id)

        categoria_seleccionada = 1  # inicializo la variable en 1 para que inicialice el while
        while (categoria_seleccionada != 0):
            print(
                "\n======================================================================================================================================\n"
                "----------------------------------------------------  TOP 10 Productos MENOS BUSCADOS --------------------------------------------------\n"
                "======================================================================================================================================")
            print("\n\n\nPara Mostrar los productos con Menores Busquedas por Categoria, "
                "\nSelecciona la Categoria de tu interes: ")
            print("(1) Procesadores\n"
                  "(2) Tarjetas de Video\n"
                  "(3) Tarjetas Madre\n"
                  "(4) Discos Duros\n"
                  "(5) Memorias USB\n"
                  "(6) Pantallas\n"
                  "(7) Bocinas\n"
                  "(8) Audifonos\n"
                  "(0) Continuar")
            categoria_seleccionada = int(input("Opcion: "))

            if categoria_seleccionada == 1:
                print("\n\nTOP 10 Productos con MENORES Busquedas Categoria: {}\n".format(categorias[0]))
                menores_busquedas(busquedas_procesadores, lifestore_products)
                input("\nEnter para continuar")
            elif categoria_seleccionada == 2:
                print("\n\nTOP 10 Productos con MENORES Busquedas Categoria: {}\n".format(categorias[1]))
                menores_busquedas(busquedas_tarjetas_video, lifestore_products)
                input("\nEnter para continuar")
            elif categoria_seleccionada == 3:
                print("\n\nTOP 10 Productos con MENORES Busquedas Categoria: {}\n".format(categorias[2]))
                menores_busquedas(busquedas_tarjetas_madre, lifestore_products)
                input("\nEnter para continuar")
            elif categoria_seleccionada == 4:
                print("\n\nTOP 10 Productos con MENORES Busquedas Categoria: {}\n".format(categorias[3]))
                menores_busquedas(busquedas_discos_duros, lifestore_products)
                input("\nEnter para continuar")
            elif categoria_seleccionada == 5:
                print("\n\nTOP 10 Productos con MENORES Busquedas Categoria: {}\n".format(categorias[4]))
                menores_busquedas(busquedas_memorias_usb, lifestore_products)
                input("\nEnter para continuar")
            elif categoria_seleccionada == 6:
                print("\n\nTOP 10 Productos con MENORES Busquedas Categoria: {}\n".format(categorias[5]))
                menores_busquedas(busquedas_pantallas, lifestore_products)
                input("\nEnter para continuar")
            elif categoria_seleccionada == 7:
                print("\n\nTOP 10 Productos con MENORES Busquedas Categoria: {}\n".format(categorias[6]))
                menores_busquedas(busquedas_bocinas, lifestore_products)
                input("\nEnter para continuar")
            elif categoria_seleccionada == 8:
                print("\n\nTOP 10 Productos con MENORES Busquedas Categoria: {}\n".format(categorias[7]))
                menores_busquedas(busquedas_audifonos, lifestore_products)
                input("\nEnter para continuar")

        """ Productos por reseña en el Servicio """
        id_avgscores = []
        for id_producto in id_productos:
            # inicio las variables en 0
            frec = 0
            score = 0
            score_avg = 0.0
            for lifestore_sale in lifestore_sales:
                if id_producto == lifestore_sale[1]:
                    # si existe el id_producto en lifestore_sales entra si no, se queda con el anterior
                    frec += 1
                    id_temp = id_producto
                    score += lifestore_sale[2]
                    score_avg = round(float(score) / float(frec), 2)
            if frec > 0:
                id_avgscores.append([score_avg, id_temp, frec])

        id_avgscores = sorted(id_avgscores, reverse=True)

        print("\n\n==================== TOP 5 Productos con Mejor Score ====================")
        i = 1
        for id_avgscore in id_avgscores:
            for lifestore_product in lifestore_products:
                if id_avgscore[1] == lifestore_product[0] and i < 6:
                    print("No.{} ID:{} Ventas:{} Score:{} --> {}".format(i, lifestore_product[0], id_avgscore[2],
                                                                         id_avgscore[0], lifestore_product[1]))
                    i += 1

        id_avgscores = sorted(id_avgscores)
        print("\n==================== TOP 5 Productos con Peor Score ====================")
        i = 1
        for id_avgscore in id_avgscores:
            for lifestore_product in lifestore_products:
                if id_avgscore[1] == lifestore_product[0] and i < 6:
                    print(
                        "No.{} ID:{} Ventas:{} Score:{} --> {}".format(i, lifestore_product[0], id_avgscore[2],
                                                                       id_avgscore[0], lifestore_product[1]))
                    i += 1
        input("\nEnter para continuar")

        """ ================ Total de Ingresos, ingresos mensuales y promedio de ingreso  ================ """
        # Lista con id y fecha convertida en entero sin considerar productos con devolución
        id_dates = [
            [lifestore_sale[1], int(lifestore_sale[3][:2]), int(lifestore_sale[3][3:5]), int(lifestore_sale[3][6:])] for
            lifestore_sale in lifestore_sales if lifestore_sale[4] == 0]
        id_dates = sorted(id_dates, key=lambda id_date: id_date[2])

        # Agregar el precio de cada venta
        for id_date in id_dates:
            for lifestore_producto in lifestore_products:
                if id_date[0] == lifestore_producto[0]:
                    id_date.append(lifestore_producto[2])

        mes_frec_ventastotales = []
        for i in range(1, 13):  # Para recorrer del 1 al 12 (meses del año)
            acumulado = 0
            num_ventas = 0
            for id_date in id_dates:
                if id_date[2] == i and id_date[3] == 2020:  # revisa en que numero de mes esta y si es del año 2020
                    acumulado += id_date[4]  # Si las ventas son del mismo mes se acumula el costo de productos
                    num_ventas += 1  # frecuencia de ventas en el mes
            # si el mes de id_date != i, sale del condicional y guardamos en una lista el mes, num de ventas y
            # el acumulado de ventas
            if num_ventas > 0:
                mes_frec_ventastotales.append([i, num_ventas, acumulado, float(acumulado / num_ventas)])
            else:
                mes_frec_ventastotales.append([i, num_ventas, acumulado, 0])

        mes_frec_ventastotales = sorted(mes_frec_ventastotales,
                                        key=lambda mes_frec_ventastotal: mes_frec_ventastotal[1], reverse=True)
        print(
            "\n======================================================================================================================================\n"
            "--------------------------------------------------------------  Ventas por mes -------------------------------------------------------\n"
            "======================================================================================================================================\n")
        for mes_frec_ventastotal in mes_frec_ventastotales:
            print("Mes: {}, Num de ventas: {} ---> Total de ingreso en el mes: ${} ".format(mes_frec_ventastotal[0],
                                                                                            mes_frec_ventastotal[1],
                                                                                            mes_frec_ventastotal[2]))
        input("\nEnter para continuar")
        print(
            "\n======================================================================================================================================\n"
            "-----------------------------------------------------------  Ventas promedio por mes -------------------------------------------------\n"
            "======================================================================================================================================\n")
        for mes_frec_ventastotal in mes_frec_ventastotales:
            print("Mes: {} --> Promedio de Ingreso: ${} ".format(mes_frec_ventastotal[0],
                                                                 round(mes_frec_ventastotal[3], 2)))

        # Total de ingresos tomando el valor de las ventas mensuales
        total_ingresos = [mes_frec_ventastotal[2] for mes_frec_ventastotal in mes_frec_ventastotales]
        print("\n**********************************\n   Ingreso Total Anual: ${}".format(sum(total_ingresos)))
        print("**********************************")

        # terminamos el analisis y cambiamos el estado de entrada para que salga del bucle principal
        entrada = 0

    else:
        # Si no coincide el usuario y contraeña se le siguen dando oportunidades
        print("\n--------¡Usuario y/o Contraseña NO válidos!--------\n")
        continuar = input("¿Desea volver a intentar? s/n:")
        if continuar == "s" or continuar == "S":
            entrada = 1
        else:
            entrada = 0
