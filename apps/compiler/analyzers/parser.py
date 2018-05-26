import apps.compiler.analyzers.ply.yacc as yacc
import os
import codecs

from apps.compiler.analyzers.lexer import tokens, analizadorLexico, lexer_results

parser_results = []
parser_log = []
variables = {}

precedence = (
    ('right', 'ASIGNACION'),
    ('left', 'IGUAL', 'DIFERENTE'),
    ('left', 'MAYOR_QUE', 'MAYOR_IGUAL', 'MENOR_QUE', 'MENOR_IGUAL'),
    ('left', 'SUMA', 'RESTA'),
    ('left', 'MULTIPLICACION', 'DIVISION', 'MODULO'),
    ('left', 'NEGAR'),
    ('left', 'POTENCIA'),
    ('right', 'NEGATIVO'),
)

def p_declaracionAsignacion(t):
    'declaracion : IDENTIFICADOR ASIGNACION expresion'
    variables[t[1]] = t[3]

def p_declaracionExpresion(t):
    'declaracion : expresion'
    t[0] = t[1]

def p_declaracionFuncion(t):
    'declaracion : FUNCION IDENTIFICADOR PARENTESIS_IZQUIERDO  PARENTESIS_DERECHO PUNTO_COMA'
    # t[0] = "Declaracion de la funcion -> "+t[2]

def p_condicionalSi(t):
    'declaracion : SI expresion PUNTO_COMA'
    # t[0] = "Condicional Si -> "+str(t[2])

def p_condicionalSino(t):
    'declaracion : SINO PUNTO_COMA'
    # t[0] = "Condicional Sino -> "

def p_imprimir(t):
    '''
        declaracion : IMPRIMIR expresion
            | IMPRIMIR LITERAL
    '''
    t[0] = t[2]

def p_leer(t):
    'declaracion : LEER PARENTESIS_IZQUIERDO PARENTESIS_DERECHO'
    # t[0] = " Expera de datos por terminal"


def p_expresionOperacion(t):
    '''
        expresion :  expresion SUMA expresion
            | expresion RESTA expresion
            | expresion MULTIPLICACION expresion
            | expresion DIVISION expresion
            | expresion POTENCIA expresion
            | expresion MODULO expresion
    '''

    if t[2] == '+':
        t[0] = t[1] + t[3]
    elif t[2] == '-':
        t[0] = t[1] - t[3]
    elif t[2] == '*':
        t[0] = t[1] * t[3]
    elif t[2] == '/':
        t[0] = t[1] / t[3]
    elif t[2] == '%':
        t[0] = t[1] % t[3]
    elif t[2] == '^':
        i = t[3]
        t[0] = t[1]
        while i > 1:
            t[0] *= t[1]
            i -= 1

def p_expresionEnteroNegativo(t):
    'expresion : RESTA expresion %prec NEGATIVO'
    t[0] = -t[2]

def p_grupoExpresiones(t):
    '''
    expresion  : PARENTESIS_IZQUIERDO expresion PARENTESIS_DERECHO
                | LLAVE_IZQUIERDA expresion LLAVE_DERECHA
                | CORCHETE_IZQUIERDO expresion CORCHETE_DERECHO
    '''
    t[0] = t[2]

def p_expresionLogica(t):
    '''
    expresion : expresion MENOR_QUE expresion
        | expresion MAYOR_QUE expresion
        | expresion MENOR_IGUAL expresion
        | expresion MAYOR_IGUAL expresion
        | expresion IGUAL expresion
        | expresion DIFERENTE expresion
        | PARENTESIS_IZQUIERDO expresion PARENTESIS_DERECHO MENOR_QUE PARENTESIS_IZQUIERDO expresion PARENTESIS_DERECHO
        | PARENTESIS_IZQUIERDO expresion PARENTESIS_DERECHO MAYOR_QUE PARENTESIS_IZQUIERDO expresion PARENTESIS_DERECHO
        | PARENTESIS_IZQUIERDO expresion PARENTESIS_DERECHO MENOR_IGUAL PARENTESIS_IZQUIERDO expresion PARENTESIS_DERECHO
        | PARENTESIS_IZQUIERDO expresion PARENTESIS_DERECHO MAYOR_IGUAL PARENTESIS_IZQUIERDO expresion PARENTESIS_DERECHO
        | PARENTESIS_IZQUIERDO expresion PARENTESIS_DERECHO IGUAL PARENTESIS_IZQUIERDO expresion PARENTESIS_DERECHO
        | PARENTESIS_IZQUIERDO expresion PARENTESIS_DERECHO DIFERENTE PARENTESIS_IZQUIERDO expresion PARENTESIS_DERECHO
    '''
    if t[2] == "<<": t[0] = t[1] < t[3]
    elif t[2] == ">>": t[0] = t[1] > t[3]
    elif t[2] == "<::": t[0] = t[1] <= t[3]
    elif t[2] == ">::": t[0] = t[1] >= t[3]
    elif t[2] == ":::": t[0] = t[1] is t[3]
    elif t[2] == ":-:": t[0] = t[1] != t[3]
    elif t[3] == "<<":
        t[0] = t[2] < t[4]
    elif t[2] == ">>":
        t[0] = t[2] > t[4]
    elif t[3] == "<::":
        t[0] = t[2] <= t[4]
    elif t[3] == ">::":
        t[0] = t[2] >= t[4]
    elif t[3] == ":::":
        t[0] = t[2] is t[4]
    elif t[3] == ":-:":
        t[0] = t[2] != t[4]

def p_expresionBooleana(t):
    '''
    expresion   : expresion Y expresion
                | expresion O expresion
                | expresion NEGAR expresion
                | PARENTESIS_IZQUIERDO expresion Y expresion PARENTESIS_DERECHO
                | PARENTESIS_IZQUIERDO expresion O expresion PARENTESIS_DERECHO
                | PARENTESIS_IZQUIERDO expresion NEGAR expresion PARENTESIS_DERECHO
    '''
    if t[2] == "yy":
        t[0] = t[1] and t[3]
    elif t[2] == "oo":
        t[0] = t[1] or t[3]
    elif t[2] == "neg":
        t[0] =  t[1] is not t[3]
    elif t[3] == "yy":
        t[0] = t[2] and t[4]
    elif t[3] == "oo":
        t[0] = t[2] or t[4]
    elif t[3] == "neg":
        t[0] =  t[2] is not t[4]

def p_expresionEntero(t):
    'expresion : ENTERO'
    t[0] = t[1]

def p_expresionCadena(t):
    'expresion : COMILLA_DOBLE expresion COMILLA_DOBLE'
    t[0] = t[2]

def p_expresionIdentificador(t):
    'expresion : IDENTIFICADOR'
    try:
        t[0] = variables[t[1]]
    except LookupError:
        # global parser_results
        mensaje = "En la linea {} -> \"{}\" no definido.".format(t.lexer.lineno,t[1])
        # parser_results.append(mensaje)
        # print(mensaje)
        t[0] = 0


def p_error(t):
    global parser_results
    if t:
        mensaje = "Linea {} -> Error sintactico de tipo {} en el valor \"{}\"".format(str(nlinea_leida), str(t.type), str(t.value))
        # print(mensaje)
    else:
        mensaje = "Error sintactico {} (desconocido)".format(t)
        # print(mensaje)
    parser_results.append(mensaje)

parser = yacc.yacc()

nlinea_leida = 0

def ejecucion_linea_por_linea(codigo):
    global resultado_gramatica
    global nlinea_leida
    parser_results.clear()
    nlinea_leida = 0
    for lineaCodigo in codigo.splitlines():
        nlinea_leida = nlinea_leida + 1
        if lineaCodigo:
            resultado = parser.parse(lineaCodigo)
            if resultado:
                salida = "Linea {} -> {}".format(str(nlinea_leida), str(resultado))
                parser_results.append(salida)
        else:
            # print("linea de codigo vacia")
            pass
    # print("result: ", parser_results)
    # print('\n'.join(parser_results))
    return parser_results

# nombreArchivo =  'operaciones.slx'
# ruta = str(os.getcwd())+"/archivos/"+nombreArchivo
# fp = codecs.open(ruta,"r","utf-8")
# codigoArchivo = fp.read()
# fp.close()

# resultado_analisis = ejecucion_linea_por_linea(codigoArchivo)

# analizadorLexico.input(codigoArchivo)
# plylex_results = []
#
# while True:
#     tkn = analizadorLexico.token()
#     if not tkn : break
#     import copy
#     plylex_results.append(copy.copy(str(tkn)))
#
#
# if plylex_results:
#     print("============ply LEX===================")
#     print('\n'.join(plylex_results))

# if lexer_results:
#     cont = 0
#     mitad = len(lexer_results)/2
#     for i in reversed(lexer_results):
#         cont = cont + 1
#         if cont <= mitad: lexer_results.pop(0)
#         else: break
#     print("============LEXER===================")
#     print('\n'.join(lexer_results))
