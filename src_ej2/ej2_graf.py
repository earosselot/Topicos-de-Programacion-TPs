import matplotlib.pyplot as plt


def Sort(sub_li, elem):
    # ordena la lista de listas segun un elemento pasado como parametro (elem)

    return (sorted(sub_li, key=lambda x: x[elem]))

def get_item(list, item):
    """devuelve una lista con el enesimo elemento de cada lista de una lista (de listas)"""

    res = []
    for elem in list:
        res.append(elem[item])
    return res


with open('resultados.csv', 'r') as resultados:

    matriz_res = []

    for linea in resultados:
        linea = linea.strip('\n')
        camposDeLinea = linea.split(';')
        matriz_res.append(camposDeLinea)

    sort_res = Sort(matriz_res, 0)
    print(sort_res)


    # 8imagenes
    cant_resultados_por_imagen = int(len(sort_res) / 8)
    for i in range(0, len(sort_res), cant_resultados_por_imagen):
        res_por_imagen = sort_res[i:i+cant_resultados_por_imagen]

        thr = get_item(res_por_imagen, 1)
        t_gray = get_item(res_por_imagen, 2)
        t_blur = get_item(res_por_imagen, 3)

        plt.plot(thr, t_gray, label='gray')
        plt.plot(thr, t_blur, label='blur')

        plt.xlabel('threads')
        plt.ylabel('tiempo')

        plt.title(res_por_imagen[0][0])

        plt.show()

