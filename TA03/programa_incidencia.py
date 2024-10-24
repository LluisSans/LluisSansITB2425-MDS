import xml.etree.ElementTree as ET
from datetime import datetime

def leer_incidencias(fichero):
    # Cargar y parsear el archivo XML
    try:
        tree = ET.parse(fichero)
        root = tree.getroot()
    except ET.ParseError:
        print("Error al parsear el archivo XML. Asegúrate de que esté bien formado.")
        return [], [], [], []

    # Listas para almacenar los datos
    noms_i_cognoms = []
    correus_electronics = []
    datas_de_la_incidencia = []
    nivells_urgencia = []

    # Extraer información de cada registro
    for record in root.findall('record'):
        nom = record.find('NOM_I_COGNOMS')
        correu = record.find('CORREU_ELECTRONIC')
        data = record.find('DATA_DE_LA_INCIDENCIA')
        nivell = record.find('NIVELL_URGENCIA')

        if nom is not None:
            noms_i_cognoms.append(nom.text)
        if correu is not None:
            correus_electronics.append(correu.text)
        if data is not None and data.text:  # Verificar que data.text no sea None ni vacío
            try:
                # Convertir la cadena de fecha a un objeto datetime
                data_obj = datetime.strptime(data.text, "%d/%m/%Y")
                datas_de_la_incidencia.append(data_obj)
            except ValueError:
                print(f"Fecha inválida: {data.text}. No se añadirá a la lista.")
                datas_de_la_incidencia.append(None)  # Agregar None si hay un error en la fecha
        else:
            datas_de_la_incidencia.append(None)  # Agregar None si no hay fecha

        if nivell is not None:
            nivells_urgencia.append(nivell.text)

    return noms_i_cognoms, correus_electronics, datas_de_la_incidencia, nivells_urgencia

def mostrar_incidencias(noms, correus, datas, nivells):
    fecha_inicio = datetime(2024, 9, 1)  # 1 de septiembre de 2024
    fecha_hoy = datetime.now()  # Fecha actual

    # Combinar las listas en una lista de tuplas
    incidencias = list(zip(noms, correus, datas, nivells))

    # Filtrar y ordenar las incidencias
    incidencias_validas = [
        (nom, correu, fecha, nivell) for nom, correu, fecha, nivell in incidencias
        if fecha is not None and fecha_inicio <= fecha <= fecha_hoy  # Filtrar None
    ]

    # Definir un orden para NIVELL_URGENCIA
    orden_urgencia = {'Molt Urgent': 1, 'Urgent': 2, 'Poc Urgent': 3}

    # Ordenar las incidencias primero por NIVELL_URGENCIA y luego por fecha
    incidencias_validas.sort(key=lambda x: (orden_urgencia.get(x[3], 4), x[2]))  # Usar 4 para nivells no especificados

    # Mostrar la información ordenada
    print(
        f"{'NOM_I_COGNOMS':<20} \t {'CORREU_ELECTRONIC':<30} \t {'DATA_DE_LA_INCIDENCIA':<20} \t {'NIVELL_URGENCIA':<15}")
    print("-" * 108)

    for nom, correu, fecha, nivell in incidencias_validas:
        fecha_str = fecha.strftime("%d/%m/%Y")
        print(f"{nom:<20} \t {correu:<30} \t {fecha_str:<20} \t {nivell:<15}")

if __name__ == "__main__":
    fichero_xml = '/home/lluis.sans.7e6/PycharmProjects/LluisSansITB2425-MDS/TA03/incidencies.xml'
    try:
        noms, correus, datas, nivells = leer_incidencias(fichero_xml)
        if noms:  # Solo mostrar si hay datos
            mostrar_incidencias(noms, correus, datas, nivells)
        else:
            print("No se encontraron incidencias.")
    except FileNotFoundError:
        print(f"No se encontró el archivo: {fichero_xml}")
    except Exception as e:
        print(f"Ocurrió un error: {e}")
