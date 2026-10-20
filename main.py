def calcular_medidas(base:float, altura:float) -> tuple[float, float]:
    """
    :param base: Se introduce la base.
    :param altura: Se introduce la altura.
    :return: Resultado de area y perímetro.
    """
    area:float = base * altura
    perimetro:float = (base + altura)* 2
    return area, perimetro

def determinar_forma(base:float, altura:float) -> str:
    """
    :param base: Se introduce la base.
    :param altura: Se introduce la altura.
    :return: Da de resultado su forma geométrica.
    """
    forma:str = "Vertical"
    
    if base == altura:
        forma = "Cuadrado"
    elif base > altura:
        forma = "Horizontal"
    
    return forma

def main():
    base = float(input("Introduce la base: "))
    altura = float(input("Introduce la altura: "))

    if base <= 0 or altura <= 0:
        print("La base o la altura es menor a 0")

    else:
        resultado = calcular_medidas(base, altura)
        tipo = determinar_forma(base, altura)

        print(f"Forma: {tipo}")
        print(f"Área: {resultado[0]}cm²")
        print(f"Perímetro: {resultado[1]}cm")      
if __name__ == "__main__":
    main()