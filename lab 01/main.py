import sys
import cmath
# Получение коэффициентов от пользователя
def get_coef(index, str):
    # попытка считать коэф. из командной строки
    try:
        coef_str = sys.argv[index]
        # ввод коэф. с клаавиатуры
    except:
        print(str)
        coef_str = input()
    while True:
        try:
            # перевод стринга в действительное число
            float(coef_str)
            break
        except:
            coef_str = input()
    coef = float(coef_str)
    return coef

def get_roots(a,b,c):
    answr = []
    #расчет дискрименанта
    D = b*b - 4*(a*c)
    #расчет корней
    if D == 0:
        root = -b/(2.0*a)
        answr.append(root)
    elif D > 0.0:
        sqD = cmath.sqrt(D)
        root1 = (-b + sqD)/(2.0*a)
        root2 = (-b - sqD)/(2.0*a)
        answr.append(root1)
        answr.append(root2)
    return answr

def main():
    a = get_coef(1, 'Введите коэффициент А:')
    b = get_coef(2, 'Введите коэффициент B:')
    c = get_coef(3, 'Введите коэффициент C:')
    roots = get_roots(a,b,c)
    len_roots = len(roots)
    #вывод корней
    if len_roots == 0:
        print('Нет Корней.')
    if len_roots == 1:
        print('Единственный корень уравнения: {}'.format(roots[0]))
    if len_roots == 2:
        print('Два корня уравнения: {} и {}'.format(roots[0],roots[1]))
#для запуска кода из командной строки
if __name__ == "__main__":
    main()