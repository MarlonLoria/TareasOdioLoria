def operation_selector(num1, num2, op):
    resultado = None
    # Verificación valores num1 y num2, correspondan a enteros
    if not isinstance(num1, int) or not isinstance(num2, int):
        return -50, resultado
    if isinstance(num1, bool) or isinstance(num2, bool):
        return -50, resultado
    # Verificación valor op corresponda a un str
    if not isinstance(op, str):
        return -60, resultado
    # Verificación valor op corresponda a un operador valido
    if op not in ['+', '-', '*', '&']:
        return -70, resultado
    # Aplicación de la operación
    if op == '+':
        resultado = num1 + num2
    elif op == '-':
        resultado = num1 - num2
    elif op == '*':
        resultado = num1 * num2
    elif op == '&':
        resultado = num1 & num2
    return 0, resultado


def calculo_promedio(lista_valores):
    resultado = None
    # Verificación del tamaño de la lista
    if len(lista_valores) > 10:
        return -90, resultado
    # Verificación valores correspondan a números
    for i in range(len(lista_valores)):
        if not isinstance(lista_valores[i], (int, float)):
            return -80, resultado
        if isinstance(lista_valores[i], bool):
            return -80, resultado
    # Calculo de promedio
    resultado = sum(lista_valores)/len(lista_valores)
    return 0, resultado
