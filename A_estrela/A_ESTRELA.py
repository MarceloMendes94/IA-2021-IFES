from operator import itemgetter
import sys
def custo(linha,coluna,alvo):
  #receber um vetor
  custo_linha = alvo[0] - linha
  if custo_linha < 0:
    custo_linha = custo_linha*-1

  custo_coluna = alvo[1] - coluna
  if custo_coluna < 0:
    custo_coluna = custo_coluna*-1
  
  return custo_coluna+ custo_linha

def vizinho(linha,coluna,alvo,MAP):
  adj=[]
  #verificando linha
  if linha > 0 and MAP[linha-1][coluna] != 1:
    adj.append(
        ([linha-1,coluna],custo(linha-1,coluna,alvo),MAP[linha-1][coluna]) )
    
  if linha+1 < len(MAP) and MAP[linha+1][coluna] != 1: 
    adj.append(
        ([linha+1,coluna],custo(linha+1,coluna,alvo),MAP[linha+1][coluna]) )

  #verificando coluna
  if coluna > 0 and MAP[linha][coluna-1] != 1:
    adj.append(
        ([linha,coluna-1],custo(linha,coluna-1,alvo),MAP[linha][coluna-1]) )

  if coluna+1< len(MAP[0]) and MAP[linha][coluna+1] != 1:
    adj.append(
        ([linha,coluna+1],custo(linha,coluna+1,alvo),MAP[linha][coluna+1])  )
  
  #fazer um teste aqui  
  adj = sorted(adj, key=itemgetter(1))
  for i in range(len(adj)):
    if adj[i][0] == alvo:
      adj.insert(0, adj[i]) 
      adj.pop(i+1)

  return adj

def ler_grid(arquivo):
    grid = [ [int(x) for x in  i[:-1].split(" ")]  for i in open(arquivo, "r").readlines() ]
    return grid

def set_alvo(linha,coluna):
    return [linha,coluna,[linha,coluna]]

def set_inicio(linha,coluna):
    return [linha,coluna,[linha,coluna]]

def pathfinding(MAP,inicio,alvo):
    lst_aberta, lst_fechada = [],[]
    lst_fechada.append(inicio)
    linha,coluna = inicio
    lst_aberta = vizinho(linha,coluna,alvo,MAP)
    aux = 0
    escolha = inicio
    while (escolha != alvo):
        achou = False
        for elem in lst_aberta:
            if elem[0] not in lst_fechada:
                escolha = elem[0]
                linha,coluna = escolha  
                lst_fechada.append(escolha)
                achou = True
                break

        if achou == False:
            aux = aux + 1
            escolha = lst_fechada[-aux:][0]
            linha,coluna = escolha
        else:
            if aux !=0 : 
                #limpar N coisos
                lst_fechada =lst_fechada[:-aux]
                aux = 0
                lst_fechada.append(escolha)
        lst_aberta = vizinho(linha,coluna,alvo,MAP)
    return lst_fechada

def pathdraw(MAP,lst):
  for i in lst:
    MAP[i[0]][i[1]]= 8
  return MAP

def main(arquivo,lst1,lst2):
  """
  onde:
  arquivo é o arquivo do grid
  lst1 é o inicio
  lst2 é o alvo
  """
  
  MAP = ler_grid(arquivo)
  linha_i, coluna_i, inicio = set_inicio(lst1[0],lst1[1])
  linha_f, coluna_f, alvo   = set_alvo(lst2[0],lst2[1])
  path = pathfinding(MAP,inicio,alvo)

  MAP2 = MAP
  MAP2 = pathdraw(MAP2,path)
  print("A saida é preeenchida com 8 \n")
  for i in MAP2:
    print(i)
  print(f"\n{path}")  

  return True

if __name__ == "__main__":
    if(len(sys.argv)!=4):
      print(f"{28*'#'}\nParametros errados\n{28*'#'}\nentre em com:\n> python3 A_ESTRELA.py grid.txt [0,0] [12,12]\n\n")
    else:
      main(
        sys.argv[1],
        [int(i) for i in sys.argv[2][1:-1].split(',')],
        [int(i) for i in sys.argv[3][1:-1].split(',')]
        )
    
