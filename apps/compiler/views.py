from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse_lazy

import os
import codecs
from apps.compiler.analyzers.lexer import *
from apps.compiler.analyzers.parser import *

def compile(request, context):

    # nombreArchivo =  'operaciones.slx'
    # ruta = str(os.getcwd())+"/apps/compiler/codes/"+nombreArchivo
    # fp = codecs.open(ruta,"r","utf-8")
    # codigo = fp.read()
    # fp.close()
    # codigo = request.POST['code']
    codigo = limpiarBasura(request.POST['code'])

    global lexer_results
    lexer_results.clear()
    # global analizadorLexico
    # analizadorLexico = lex.lex()
    plylex_results = []

    resultado_analisis = ejecucion_linea_por_linea(codigo)

    import copy
    backup = copy.copy(lexer_results)
    analizadorLexico.input(codigo)
    lexer_results = copy.copy(backup)

    while True:
        tkn = analizadorLexico.token()
        if not tkn : break
        import copy
        plylex_results.append(copy.copy(str(tkn)))

    if resultado_analisis:
        print("============PARSER===================")
        print('\n'.join(resultado_analisis))
    if lexer_results:
        # print("\n".join(lexer_results))
        # cont = 0
        # mitad = len(lexer_results)/2
        # for i in reversed(lexer_results):
        #     cont = cont + 1
        #     if cont <= mitad: lexer_results.pop(0)
        #     else: break
        print("============LEXER===================")
        print('\n'.join(lexer_results))
    if plylex_results:
        print("============ply LEX===================")
        # print('\n'.join(plylex_results))


    if request.POST['compilations']:
        compilations = int(request.POST['compilations']) + 1
    else:
        compilations = 1
    context.setdefault("compilations", compilations)

    context.setdefault("code", codigo)
    context.setdefault("parser_results", parser_results)
    context.setdefault("lexer_results", lexer_results)
    context.setdefault("plylex_results", plylex_results)
    return render(request, 'page/compiler.html', context)


def limpiarBasura(codigo):
    lineasDeCodigo = codigo.splitlines()
    nlineas = len(lineasDeCodigo)

    for linea in reversed(lineasDeCodigo):
        if not linea: lineasDeCodigo.pop()
        else : break

    return '\n'.join(lineasDeCodigo)
