import heapq
from collections import defaultdict, Counter

class NodoHuffman:
    def __init__(self, simbolo, frecuencia):
        self.simbolo = simbolo
        self.frecuencia = frecuencia
        self.izquierda = None
        self.derecha = None

    def __lt__(self, otro):
        return self.frecuencia < otro.frecuencia

def construir_arbol_huffman(frecuencias):
    heap = [NodoHuffman(simbolo, frecuencia) for simbolo, frecuencia in frecuencias.items()]
    heapq.heapify(heap)
    
    while len(heap) > 1:
        nodo_izquierdo = heapq.heappop(heap)
        nodo_derecho = heapq.heappop(heap)
        
        nodo_padre = NodoHuffman(None, nodo_izquierdo.frecuencia + nodo_derecho.frecuencia)
        nodo_padre.izquierda = nodo_izquierdo
        nodo_padre.derecha = nodo_derecho
        
        heapq.heappush(heap, nodo_padre)
    
    return heap[0]

def construir_tabla_codigos(arbol_huffman, codigo_actual="", tabla_codigos={}):
    if arbol_huffman is not None:
        if arbol_huffman.simbolo is not None:
            tabla_codigos[arbol_huffman.simbolo] = codigo_actual
        construir_tabla_codigos(arbol_huffman.izquierda, codigo_actual + "0", tabla_codigos)
        construir_tabla_codigos(arbol_huffman.derecha, codigo_actual + "1", tabla_codigos)
    return tabla_codigos

def comprimir(texto):
    frecuencias = dict(Counter(texto))
    arbol_huffman = construir_arbol_huffman(frecuencias)
    tabla_codigos = construir_tabla_codigos(arbol_huffman)
    
    codigo_comprimido = ''.join(tabla_codigos[simbolo] for simbolo in texto)
    
    return codigo_comprimido, arbol_huffman

def descomprimir(codigo_comprimido, arbol_huffman):
    texto_descomprimido = ""
    nodo_actual = arbol_huffman
    
    for bit in codigo_comprimido:
        if bit == '0':
            nodo_actual = nodo_actual.izquierda
        else:
            nodo_actual = nodo_actual.derecha
        
        if nodo_actual.simbolo is not None:
            texto_descomprimido += nodo_actual.simbolo
            nodo_actual = arbol_huffman
    
    return texto_descomprimido

# Ejemplo de uso
if __name__ == "__main__":
    texto_original = "abracadabra"
    codigo_comprimido, arbol = comprimir(texto_original)
    print("Texto original:", texto_original)
    print("Código comprimido:", codigo_comprimido)
    texto_descomprimido = descomprimir(codigo_comprimido, arbol)
    print("Texto descomprimido:", texto_descomprimido)
