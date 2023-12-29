# Функция сортировки
def tpl_sort(tpl):
    if any([type(x) != int for x in tpl]):
        return tpl
    return tuple(sorted(tpl))
tpl = (6, 3, -1, 8, 4, 10, -5)
print(tpl_sort(tpl))