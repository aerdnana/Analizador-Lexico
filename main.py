import re

file = open("read.py")

operador = {'+': 'op Suma', '-': 'op Resta', '*': 'op Multiplicacion',
            '/': 'op Division', '=': 'op Asignacion', '%': 'op Modulo',
            '==': 'op Igualdad',     '!=': 'op Diferencia',     '<': 'op Menor que',
            '>': 'op Mayor que', '<=': 'op Menor igual', '>=': 'op Mayor igual'}

operador_key = operador.keys()

tipoDato = {'int': 'integer', 'float': 'punto flotante',
            'char': 'character', 'str': 'String',
            'bool': 'Booleano'}
tipoDato_key = tipoDato.keys()

puntuacion =  {':': 'dos puntos', ';': 'punto y coma', '.': 'punto', ',': 'coma',
                '(': 'abre parentesis', ')':'cierra parentesis', '{': 'abre llave',
                '}':'cierra llave'}
puntuacion_key = puntuacion.keys()


TOKEN_PATTERN = re.compile(
    r'\".*?\"|\'.*?\''        # cadenas de texto
    r'|==|!=|<=|>='          # operadores dobles
    r'|[=+\-*/%<>]'          # operadores simples
    r'|[0-9]+(?:\.[0-9]+)?' # números (int y float)
    r'|[a-zA-Z_]\w*'         # identificadores
    r'|[():;,.\[\]{}]'       # puntuacion
)

a = file.read()
count = 0
program = a.split("\n")

for line in program:
    count = count + 1

    print(f"\nOperacion nro {count}\n", line)
    tokens = [t for t in TOKEN_PATTERN.findall(line) if t.strip() != '']
    print("Tokens:", tokens)

    print(f"Analizador lexico nro {count}\n")

    for token in tokens:
        if token in operador_key:
            print("  Operador          :", operador[token])
        elif token in tipoDato_key:
            print("  Tipo de dato      :", tipoDato[token])
        elif token in puntuacion_key:
            print("  Puntuación        :", puntuacion[token])

        elif re.fullmatch(r'[0-9]+\.[0-9]+', token):
            print("  Número flotante   :", token)
        elif re.fullmatch(r'[0-9]+', token):
            print("  Número entero     :", token)
        elif re.fullmatch(r'[0-9]+', token):
            print("  Número entero     :", token)
        elif re.fullmatch(r'[a-zA-Z_]\w*', token):
            print("  Identificador     :", token)
        else:
            print("  Token desconocido :", token)
        print("★・・・・・・・★・・・・・・・・★")