import random

import sympy
from django.db import models

from .meta import Problem

# To je demonstracijski primer razreda nalog za reševanje sistemov linearnih enačb, ki so sicer v nekoliko drugačni obliki že vključene v razred Linearne enačbe

def nakljucen_sistem_enacb(st_spremenljivk, najmanjsi, najvecji):
    A = sympy.matrices.Matrix(st_spremenljivk, st_spremenljivk, nakljucen_seznam(st_spremenljivk**2, najmanjsi, najvecji))
    x = sympy.matrices.Matrix(st_spremenljivk, 1, nakljucen_seznam(st_spremenljivk, najmanjsi, najvecji))
    b = A*x
    return A, x, b

def nakljucen_seznam(dolzina, najmanjsi, najvecji):
    seznam = []
    while len(seznam) < dolzina:
        element = random.randint(najmanjsi, najvecji)
        seznam.append(element)
    return seznam


class SistemEnacbZDvemaSpremenljivkama(Problem):
    """Problem za izračun rešitve sistema linearnih enačb z dvema spremenljivkama."""

    default_instruction = "Poišči rešitev sistema enačb $@enacba1$, $@enacba2$."
    default_solution = "$x = @x$, $y = @y$."

    najmanjsa_vrednost = models.SmallIntegerField(
        "najmanjša vrednost",
        help_text="Najmanjša možna vrednost koeficienta v enačbi",
        default=-19,
    )

    najvecja_vrednost = models.SmallIntegerField(
        "največja vrednost",
        help_text="Največja možna vrednost koeficienta v enačbi",
        default=19,
    )

    class Meta:
        verbose_name = "Sistemi enačb / iskanje rešitve sistema linearnih enačb z dvema spremenljivkama"

    def generate(self):
        A, x, b = nakljucen_sistem_enacb(2, self.najmanjsa_vrednost, self.najvecja_vrednost)
        self.validate(A.det() != 0)
        self.validate(self.najmanjsa_vrednost <= b[0] <= self.najvecja_vrednost)
        self.validate(self.najmanjsa_vrednost <= b[1] <= self.najvecja_vrednost)

        X = sympy.symbols('x')
        Y = sympy.symbols('y')
        enacba1 = sympy.Eq(A[0,0]*X + A[0,1]*Y, b[0])
        enacba2 = sympy.Eq(A[1,0]*X + A[1,1]*Y, b[1])

        return {
            "enacba1": sympy.latex(enacba1),
            "enacba2": sympy.latex(enacba2),
            "x": x[0],
            "y": x[1],
        }
    
    class SistemEnacbSTremiSpremenljivkami(Problem):
        """Problem za izračun rešitve sistema linearnih enačb s tremi spremenljivkami."""

        default_instruction = "Poišči rešitev sistema enačb $@enacba1$, $@enacba2$, $@enacba3$."
        default_solution = "$x = @x$, $y = @y$, $z = @z$."

        najmanjsa_vrednost = models.SmallIntegerField(
            "najmanjša vrednost",
            help_text="Najmanjša možna vrednost koeficienta in rešitve",
            default=-19,
        )

        najvecja_vrednost = models.SmallIntegerField(
            "največja vrednost",
            help_text="Največja možna vrednost koeficienta in rešitve",
            default=19,
        )

        class Meta:
            verbose_name = "Sistemi enačb / iskanje rešitve sistema linearnih enačb s tremi spremenljivkami"

        def generate(self):
            A, x, b = nakljucen_sistem_enacb(3, self.najmanjsa_vrednost, self.najvecja_vrednost)
            self.validate(A.det() != 0)
            self.validate(self.najmanjsa_vrednost <= b[0] <= self.najvecja_vrednost)
            self.validate(self.najmanjsa_vrednost <= b[1] <= self.najvecja_vrednost)
            self.validate(self.najmanjsa_vrednost <= b[2] <= self.najvecja_vrednost)

            X = sympy.symbols('x')
            Y = sympy.symbols('y')
            Z = sympy.symbols('z')
            enacba1 = sympy.Eq(A[0,0]*X + A[0,1]*Y + A[0,2]*Z, b[0])
            enacba2 = sympy.Eq(A[1,0]*X + A[1,1]*Y + A[1,2]*Z, b[1])
            enacba3 = sympy.Eq(A[2,0]*X + A[2,1]*Y + A[2,2]*Z, b[2])

            return {
                "enacba1": sympy.latex(enacba1),
                "enacba2": sympy.latex(enacba2),
                "enacba3": sympy.latex(enacba3),
                "x": x[0],
                "y": x[1],
                "z": x[2],
            }