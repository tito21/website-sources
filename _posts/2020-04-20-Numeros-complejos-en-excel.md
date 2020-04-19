---
layout: post
title: "Como usar numeros complejos en Excel"
slug: "numeros-complejos-excel"
date: 2020-04-20 22:00:00 -0300
categories: ["programacion", "excel", "numeros"]
tags: ["excel", "hojas de calculo", "numeros imaginarios", "numeros complejos"]
description: Tutorial de como usar numeros complejos en excel

---

En muchos casos los numeros reales no son suficientes y deben llegar los numeros
complejos para solucionar los problemas. Los numeros complejos extienden a
conjunto real $\mathbb{R}$ agregando una nueva dimension "imaginaria" o
complementaria perpendicular al eje principal.

# Números complejos y Excel

Excel soporta trabajar con numeros complejos interpretando celdas con un formato
tipo "1+1i" como el numero complejo correspondiste. También es posible usar "j"
como la unidad imaginaria (como es popular en ingeniería). Las funciones que
permiten trabajar con numeros complejos tienen el prefijo "IM". Por ejemplo

<style>
td:first-child, th:first-child {
    text-align: center;
    font-weight: bold;
    border-right: black solid;
}
table td, th {
    border-right: 2px grey solid;
    padding-right: 1em;

}
</style>

|   |  A  |     B          |  C  |
|---|-----|----------------|-----|
| 1 |1+1i |=IMABS(A1)      |     |
| 2 |0-1j |=IMARGUMENT(A2) |     |
| 3 |     |                |     |

|   |  A  |     B     |  C  |
|---|-----|-----------|-----|
| 1 |1+1i |  1.414214 |     |
| 2 |0-1j | -1.570796 |     |
| 3 |     |           |     |

Las funciones disponibles: `IMABS`, `IMARGUMENT`, `IMDIV`, `IMSUB`, `IMADD`,
`IMPRUDUCT`, `IMCOS`, `IMSIN`, `IMTAN`, otras agrando el prefijo `IM`.

## Importante

Lo que Excel usa es en realidad una celda de texto para guardar los numeros
complejos, lo que significa que no funcionan los operadores aritméticos simples
(`+`, `-`, `*` ni `/`) ni funciones que no tengan , tienes que usar las
funciones especializadas.