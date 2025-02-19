import math
import pandas as pd
import matplotlib.pyplot as plt

# ===================================================
# FUNÇÃO PARA CÁLCULO DE DISTÂNCIA GEOGRÁFICA
# ===================================================
def haversine(lat1, lon1, lat2, lon2):
    R = 6371  # Raio da Terra em km
    dlat = math.radians(lat2 - lat1)
    dlon = math.radians(lon2 - lon1)
    a = (math.sin(dlat / 2) ** 2 + math.cos(math.radians(lat1)) *
         math.cos(math.radians(lat2)) * (math.sin(dlon / 2) ** 2))
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    return R * c

# ===================================================
# DADOS GEOGRÁFICOS (EXPANDIDO E RENOMEADO)
# ===================================================
start_vertices = {
    'A': (-7.742, 109.017),
    'B': (-7.733, 109.019),
    'C': (-7.728, 109.017),
    'D': (-7.725, 109.023),
    'E': (-7.716, 109.030),
    'F': (-7.708, 109.033),
    'G': (-7.702, 109.041),
    'H': (-7.694, 109.056),
}

end_vertices = {
    'I': (-7.690, 109.065),  # Mais longe
    'J': (-7.710, 109.048),  # Mais perto
}
intersections = {
    '1': (-7.740, 109.018),  # Rua1_AvA
    '2': (-7.738, 109.019),  # Rua1_AvB
    '3': (-7.736, 109.020),  # Rua1_AvC
    '4': (-7.734, 109.021),  # Rua1_AvD
    '5': (-7.735, 109.020),  # Rua2_AvA
    '6': (-7.733, 109.021),  # Rua2_AvB
    '7': (-7.731, 109.022),  # Rua2_AvC
    '8': (-7.729, 109.023),  # Rua2_AvD
    '9': (-7.730, 109.025),  # Rua3_AvA
    '10': (-7.728, 109.026), # Rua3_AvB
    '11': (-7.726, 109.027), # Rua3_AvC
    '12': (-7.724, 109.028), # Rua3_AvD
    '13': (-7.725, 109.028), # Rua4_AvA
    '14': (-7.723, 109.029), # Rua4_AvB
    '15': (-7.721, 109.030), # Rua4_AvC
    '16': (-7.719, 109.031), # Rua4_AvD
    '17': (-7.720, 109.032), # Rua5_AvA
    '18': (-7.718, 109.033), # Rua5_AvB
    '19': (-7.716, 109.034), # Rua5_AvC
    '20': (-7.714, 109.035), # Rua5_AvD
    '21': (-7.715, 109.036), # Rua6_AvA
    '22': (-7.713, 109.037), # Rua6_AvB
    '23': (-7.711, 109.038), # Rua6_AvC
    '24': (-7.709, 109.039), # Rua6_AvD
    '25': (-7.710, 109.040), # Rua7_AvA
    '26': (-7.708, 109.041), # Rua7_AvB
    '27': (-7.706, 109.042), # Rua7_AvC
    '28': (-7.704, 109.043), # Rua7_AvD
    '29': (-7.703, 109.041), # Rua8_AvA
    '30': (-7.701, 109.042), # Rua8_AvB
    '31': (-7.700, 109.044), # Rua8_AvC
    '32': (-7.698, 109.046), # Rua8_AvD
    '33': (-7.697, 109.048), # Rua9_AvA
    '34': (-7.696, 109.050), # Rua9_AvB
    '35': (-7.695, 109.052), # Rua9_AvC
    '36': (-7.694, 109.054), # Rua9_AvD
    '37': (-7.693, 109.056), # Rua10_AvA
    '38': (-7.692, 109.058), # Rua10_AvB
    '39': (-7.691, 109.060), # Rua10_AvC
    '40': (-7.690, 109.062), # Rua10_AvD

    '41': (-7.741, 109.022),  # Adicionadas interseções extras
    '42': (-7.739, 109.024),
    '43': (-7.737, 109.026),
    '44': (-7.732, 109.028),
    '45': (-7.727, 109.030),
    '46': (-7.722, 109.032),
    '47': (-7.717, 109.036),
    '48': (-7.712, 109.039),
    '49': (-7.707, 109.043),
    '50': (-7.705, 109.045),
    '51': (-7.700, 109.047),
    '52': (-7.695, 109.055),
}

# Dicionário de conexões (Grafo Esparso)
connections = {
    'A': ['1'],
    'B': ['6'],
    'C': ['5'],
    'D': ['11'],
    'E': ['19'],
    'F': ['26'],
    'G': ['29'],
    'H': ['37'],

    '1':  ['2', '5', 'A', '41'],
    '2':  ['1', '3', '6', '41'],
    '3':  ['2', '4', '7', '42'],
    '4':  ['3', '8', '42'],
    '5':  ['1', '6', '9', 'C'],
    '6':  ['2', '5', '7', '10', 'B'],
    '7':  ['3', '6', '8', '11'],
    '8':  ['4', '7', '12', '44'],
    '9':  ['5', '10', '13', '42'],
    '10': ['6', '9', '11', '14', '43'],
    '11': ['7', '10', '12', '15', 'D'],
    '12': ['8', '11', '16', '44'],
    '13': ['9', '14', '17', '45'],
    '14': ['10', '13', '15', '18'],
    '15': ['11', '14', '16', '19'],
    '16': ['12', '15', '20', '46'],
    '17': ['13', '18', '21', '46'],
    '18': ['14', '17', '19', '22', '45'],
    '19': ['15', '18', '20', '23', 'E'],
    '20': ['16', '19', '24', '47'],
    '21': ['17', '22', '25', '47'],
    '22': ['18', '21', '23', '26'],
    '23': ['19', '22', '24', '27', '48'],
    '24': ['20', '23', '28', '48'],
    '25': ['21', '26', '29', '49'],
    '26': ['22', '25', '27', '30', 'F'],
    '27': ['23', '26', '28', '31', '49'],
    '28': ['24', '27', '32', '50'],
    '29': ['25', '30', 'G', '33', '50'],
    '30': ['26', '29', '31', '34'],
    '31': ['27', '30', '32', '35'],
    '32': ['28', '31', '36', '51'],
    '33': ['29', '34', '37', '51'],
    '34': ['30', '33', '35', '38'],
    '35': ['31', '34', '36', '39'],
    '36': ['32', '35', '40', '52'],
    '37': ['33', '38', 'H'],
    '38': ['34', '37', '39'],
    '39': ['35', '38', '40'],
    '40': ['36', '39', 'I'],
    '41': ['1', '2', '5'],
    '42': ['3', '4', '9'],
    '43': ['10','11'],
    '44': ['8', '12'],
    '45': ['13', '18'],
    '46': ['16', '17'],
    '47': ['20', '21'],
    '48': ['23', '24'],
    '49': ['25', '27'],
    '50': ['28', '29', 'J'],
    '51': ['32', '33'],
    '52': ['36'],


    'I': ['40'],  # Conexão com o abrigo I
    'J': ['50']   # Conexão com o abrigo J
}
# Validação de nós (importante para garantir que não há erros de digitação)
all_nodes = set(start_vertices.keys()) | set(end_vertices.keys()) | set(intersections.keys())
for node, neighbors in connections.items():
    if node not in all_nodes:
        print(f"Erro: Nó '{node}' em connections não encontrado: {node}")
        exit()
    for neighbor in neighbors:
        if neighbor not in all_nodes:
            print(f"Erro: Vizinho '{neighbor}' de '{node}' não encontrado: {neighbor}")
            exit()

# ===================================================
# CONSTRUÇÃO DO GRAFO
# ===================================================
graph = {}

def get_coordinates(node):
    if node in start_vertices:
        return start_vertices[node]
    elif node in end_vertices:
        return end_vertices[node]
    elif node in intersections:
        return intersections[node]
    else:
        return None  # Nó não existe

for node in connections:
    graph[node] = {}
    coord1 = get_coordinates(node)
    if coord1 is None:
        print(f"Aviso: Nó {node} sem coordenadas.")
        continue
    for neighbor in connections[node]:
        coord2 = get_coordinates(neighbor)
        if coord2 is None:
            print(f"Aviso: Vizinho {neighbor} de {node} sem coordenadas.")
            continue
        distance = haversine(coord1[0], coord1[1], coord2[0], coord2[1])
        graph[node][neighbor] = distance

# ===================================================
# ALGORITMO DE DIJKSTRA
# ===================================================
def dijkstra(graph, start, end):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    unvisited = list(graph.keys())
    previous = {}

    while unvisited:
        current_node = min(unvisited, key=lambda node: distances[node])
        current_dist = distances[current_node]

        if current_node == end:
            path = []
            while current_node in previous:
                path.insert(0, current_node)
                current_node = previous[current_node]
            path.insert(0, start)
            return (current_dist, path)

        unvisited.remove(current_node)

        for neighbor, weight in graph[current_node].items():
            if neighbor in distances and distances[neighbor] > current_dist + weight:
                distances[neighbor] = current_dist + weight
                previous[neighbor] = current_node
    return (float('inf'), [])

# ===================================================
# FUNÇÃO PARA PLOTAR AS ROTAS
# ===================================================
def plotar_rota(caminho, titulo, start_vertices, intersections, end_vertices):
    if not caminho:
        print(f"Caminho vazio para {titulo}")
        return

    # 1. Coletar TODAS as coordenadas
    all_lats = []
    all_lons = []
    all_labels = []  # Para os rótulos de todos os pontos

    # Vértices iniciais
    for node, (lat, lon) in start_vertices.items():
        all_lats.append(lat)
        all_lons.append(lon)
        all_labels.append(node)

    # Interseções
    for node, (lat, lon) in intersections.items():
        all_lats.append(lat)
        all_lons.append(lon)
        all_labels.append(node)

    # Vértices finais
    for node, (lat, lon) in end_vertices.items():
        all_lats.append(lat)
        all_lons.append(lon)
        all_labels.append(node)


    # 2. Coordenadas do *caminho* (para plotagem destacada)
    caminho_lats, caminho_lons = [], []
    for no in caminho:
        if no in start_vertices:
            lat, lon = start_vertices[no]
        elif no in intersections:
            lat, lon = intersections[no]
        elif no in end_vertices:
            lat, lon = end_vertices[no]
        else:
            continue  # Se o nó não for encontrado, pula
        caminho_lons.append(lon)
        caminho_lats.append(lat)

    # 3. Configurar o gráfico
    plt.figure(figsize=(14, 10))  # Ajustei o tamanho

    # 4. Plotar *TODOS* os pontos (fundo)
    plt.plot(all_lons, all_lats, 'k.', markersize=5, label='Todos os Pontos')  # 'k.' = pontos pretos

    # 5. Adicionar rótulos a *TODOS* os pontos (opcional, mas recomendado)
    for lon, lat, label in zip(all_lons, all_lats, all_labels):
        plt.annotate(label, (lon, lat), textcoords="offset points",
                     xytext=(0, 3), ha='center', fontsize=5, color='gray') #fonte e cor diferentes



    # 6. Plotar a linha da rota (destacada)
    plt.plot(caminho_lons, caminho_lats, 'b-', marker='o', markersize=7, linewidth=2.5, label='Rota')

    # 7. Destacar início e fim do *caminho*
    plt.plot(caminho_lons[0], caminho_lats[0], 'go', markersize=10, label='Início')
    plt.plot(caminho_lons[-1], caminho_lats[-1], 'ro', markersize=10, label='Destino')

    # 8. Adicionar rótulos ao *caminho* (destacados)
    for i, (lon, lat) in enumerate(zip(caminho_lons, caminho_lats)):
        plt.annotate(caminho[i], (lon, lat), textcoords="offset points",
                     xytext=(0, 8), ha='center', fontsize=9, color='blue') #fonte maior, outra cor

    plt.xlabel('Longitude')
    plt.ylabel('Latitude')
    plt.title(titulo)
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(f'rota_{titulo}.png')
    plt.close()

# ===================================================
# GERAÇÃO DA PLANILHA EXCEL
# ===================================================
def gerar_planilha_excel():
    dados = []
    colunas = [
        "Vértice Inicial",
        "Distância para I (km)",
        "Caminho para I",
        "Distância para J (km)",
        "Caminho para J"
    ]

    for vertice in start_vertices:
        linha = [vertice]

        distancia_i, caminho_i = dijkstra(graph, vertice, 'I')
        plotar_rota(caminho_i, f"Rota de {vertice} para I", start_vertices, intersections, end_vertices)
        linha.extend([distancia_i, " → ".join(caminho_i)])

        distancia_j, caminho_j = dijkstra(graph, vertice, 'J')
        plotar_rota(caminho_j, f"Rota de {vertice} para J", start_vertices, intersections, end_vertices)
        linha.extend([distancia_j, " → ".join(caminho_j)])

        dados.append(linha)

    df = pd.DataFrame(dados, columns=colunas)
    df['Distância para I (km)'] = df['Distância para I (km)'].round(2)
    df['Distância para J (km)'] = df['Distância para J (km)'].round(2)

    writer = pd.ExcelWriter('resultados_evacuacao_complexo.xlsx', engine='xlsxwriter')
    df.to_excel(writer, index=False, sheet_name='Rotas')

    workbook = writer.book
    worksheet = writer.sheets['Rotas']
    formatos = {
        'header': workbook.add_format({'bold': True}),
        'caminhos': workbook.add_format({'text_wrap': True})
    }
    worksheet.set_column('A:A', 15)
    worksheet.set_column('B:B', 22)
    worksheet.set_column('C:C', 80, formatos['caminhos'])
    worksheet.set_column('D:D', 22)
    worksheet.set_column('E:E', 80, formatos['caminhos'])

    writer.close()

# ===================================================
# EXECUÇÃO
# ===================================================
if __name__ == "__main__":
    gerar_planilha_excel()
    print("Planilha gerada: resultados_evacuacao_complexo.xlsx")