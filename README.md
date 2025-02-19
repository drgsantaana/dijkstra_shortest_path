# The Shortest Path Finder for Tsunami Evacuation - Implementação em Python

Este projeto implementa uma versão simplificada e adaptada da lógica apresentada no artigo *"The Shortest Path Finder for Tsunami Evacuation Strategy using Dijkstra Algorithm"* para a disciplina de Técnicas de Programação, ministrada pela professora Natalia Camilo. O projeto foi desenvolvido pelo aluno Daniel Reis.

## Objetivo

Aplicar o algoritmo de Dijkstra para encontrar as rotas mais curtas entre pontos de origem (simulando residências e locais de trabalho) e pontos de evacuação (abrigos seguros) em um cenário hipotético de tsunami. O projeto utiliza dados geográficos simplificados (latitude e longitude) para representar um mapa da área e calcula as distâncias entre os pontos usando a fórmula de Haversine.

## Estrutura do Projeto

* **`main.py`**: Arquivo principal com o código para:
  * Definir os dados geográficos (vértices iniciais, finais e interseções).
  * Definir as conexões entre os nós do grafo.
  * Construir o grafo a partir dos dados e conexões.
  * Implementar o algoritmo de Dijkstra para encontrar o caminho mais curto.
  * Gerar uma planilha Excel (`resultados_evacuacao_complexo.xlsx`) com os resultados.
  * Gerar imagens PNG (`rota_...png`) mostrando os caminhos encontrados em um mapa.

## Dependências

* **Python 3**: Certifique-se de ter o Python 3 instalado em seu sistema.
* **Bibliotecas:**
  * `pandas`: Para manipulação de dados e geração da planilha Excel.
  * `matplotlib`: Para plotagem dos mapas com as rotas.
  * `xlsxwriter`: Para escrever a planilha em formato Excel.
  * `math`: Funções matemáticas (incluído por padrão no Python).

## Instalação das Dependências

Execute o seguinte comando para instalar as bibliotecas necessárias:

```bash
pip install pandas matplotlib xlsxwriter
```

## Como Executar

1. Clone o repositório (ou faça o download do código):

   ```bash
   git clone <URL_do_repositório>
   ```
   (Substitua `<URL_do_repositório>` pela URL correta do repositório, se aplicável. Ou baixe os arquivos do projeto manualmente.)

2. Navegue até o diretório do projeto:

   ```bash
   cd <caminho_para_o_diretorio_do_projeto>
   ```

3. Execute o script principal:

   ```bash
   python main.py
   ```

## Resultados

Após a execução, o script gerará:

* Uma planilha Excel chamada `resultados_evacuacao_complexo.xlsx` no diretório do projeto, contendo as distâncias e os caminhos mais curtos de cada ponto de origem até os abrigos.
* Imagens PNG (ex: `rota_CasaA_para_I.png`) mostrando os caminhos mais curtos sobrepostos a um mapa com todos os pontos do grafo.

## Estrutura do Grafo

O grafo é definido por:

* **`start_vertices`**: Dicionário contendo os pontos de origem com suas coordenadas (latitude, longitude).
* **`end_vertices`**: Dicionário com os pontos de evacuação e suas coordenadas.
* **`intersections`**: Dicionário com as interseções/nós do grafo e suas coordenadas.
* **`connections`**: Dicionário que define as conexões entre os nós. A chave é um nó, e o valor é uma lista de nós conectados diretamente a ele.

## Observações Importantes

* **Grafo Esparso:** As conexões são definidas manualmente, simulando uma rede viária mais realista.
* **Ajuste das Conexões:** Modifique o dicionário `connections` para criar rotas alternativas ou adicionar/remover ruas.
* **Coordenadas:** Ajuste as coordenadas para simular diferentes áreas.
* **Validação:** O código inclui validação para garantir que todos os nós em `connections` existam nos dicionários de coordenadas.

## Customização

* **Adicionar/Remover Pontos:** Modifique os dicionários `start_vertices`, `end_vertices` e `intersections` conforme necessário.
* **Modificar Conexões:** Ajuste o dicionário `connections` para testar diferentes cenários.
* **Visualização:** Os labels, cores e outros aspectos das imagens podem ser modificados.

Este projeto fornece uma base sólida para explorar o algoritmo de Dijkstra e sua aplicação em problemas de planejamento de rotas de evacuação. Sinta-se à vontade para modificar e expandir o código para atender às suas necessidades e explorar diferentes cenários.