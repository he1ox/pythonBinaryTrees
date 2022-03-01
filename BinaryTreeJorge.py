#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ----------------------------------------------------------------------------
# Created By  : Jorge A. López
# Created Date: 24/02/2022
# version ='1.0'
# ---------------------------------------------------------------------------
""" Creación de arboles binarios en Python"""
# ---------------------------------------------------------------------------


class Nodo(object):
    dato = 0
    izquierdo = None
    derecho = None

    def __init__(self, valor, ramaIzq=None, ramaDer=None):
        self.dato = valor

        if ramaIzq is None and ramaDer is None:
            self.izquierdo = None
            self.derecho = None
        else:
            self.izquierdo = ramaIzq
            self.derecho = ramaDer

    def valorNodo(self):
        return self.dato

    def getSubArbolIzq(self):
        return self.izquierdo

    def getSubArbolDer(self):
        return self.derecho

    def nuevoValor(self, d):
        self.dato = d

    def setRamaIzq(self, n):
        self.izquierdo = n

    def setRamaDer(self, n):
        self.derecho = n


class Arbol(object):
    raiz = None

    def insertar(self, dato, padre: Nodo = None):
        if self.raiz is None:
            self.raiz = Nodo(dato)
        elif padre != None:
            if dato > padre.valorNodo():
                if padre.getSubArbolDer() is None:
                    padre.setRamaDer(Nodo(dato))
                else:
                    if padre.getSubArbolIzq() is None:
                        padre.setRamaIzq(Nodo(dato))
                    else:
                        self.insertar(dato, padre.getSubArbolIzq)

arbol = Arbol()
arbol.insertar(4)
arbol.insertar(2)
