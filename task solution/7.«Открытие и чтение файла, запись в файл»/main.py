import os
from pprint import pprint


def read_cookbook():
    BASE_PATH = os.getcwd()
    LOG_DIR = 'Files'
    LOG_FILE = 'cook_book.txt'
    FULL_LOG_PATH = os.path.join(BASE_PATH, LOG_DIR, LOG_FILE)
    cook_book = {}
    with open(FULL_LOG_PATH, 'r', encoding='utf-8') as f:
        for line in f:
            dish_name = line.strip()
            count = int(f.readline())
            ing_list = list()
            for item in range(count):
                ingrs = {}
                ingr = f.readline().strip()
                ingrs['ingredient_name'], ingrs['quantity'], ingrs['measure'] = ingr.split('|')
                ingrs['quantity'] = int(ingrs['quantity'])
                ing_list.append(ingrs)
            f.readline()
            cook_book[dish_name] = ing_list
    return cook_book


def get_shop_list_by_dishes(dishes, person_count):
    ingr_list = dict()
    for dish_name in dishes:  # итерируем список полученных блюд
        if dish_name in cook_book:
            for ings in cook_book[dish_name]:  # итерируем ингридиенты в блюде
                meas_quan_list = dict()
                if ings['ingredient_name'] not in ingr_list:
                    meas_quan_list['measure'] = ings['measure']
                    meas_quan_list['quantity'] = ings['quantity'] * person_count
                    ingr_list[ings['ingredient_name']] = meas_quan_list
                else:
                    ingr_list[ings['ingredient_name']]['quantity'] = ingr_list[ings['ingredient_name']]['quantity'] + \
                                                                     ings['quantity'] * person_count

        else:
            print(f'\n"Такого блюда нет в списке!"\n')
    return ingr_list


def rewrite_file(path1=None, path2=None, path3=None):
    if path1 or path2 or path3 is None:
        # path1 = '1.txt'
        BASE_PATH1 = os.getcwd()
        LOG_DIR1 = 'Files'
        LOG_FILE1 = '1.txt'
        path1 = os.path.join(BASE_PATH1, LOG_DIR1, LOG_FILE1)
        # path2 = '2.txt'
        BASE_PATH2 = os.getcwd()
        LOG_DIR2 = 'Files'
        LOG_FILE2 = '2.txt'
        path2 = os.path.join(BASE_PATH2, LOG_DIR2, LOG_FILE2)
        # path3 = '3.txt'
        BASE_PATH3 = os.getcwd()
        LOG_DIR3 = 'Files'
        LOG_FILE3 = '3.txt'
        path3 = os.path.join(BASE_PATH3, LOG_DIR3, LOG_FILE3)
        os.chdir('Files')
        outout_file = "rewrite_file.txt"
        file1_path = os.path.join(os.getcwd(), path1)
        file2_path = os.path.join(os.getcwd(), path2)
        file3_path = os.path.join(os.getcwd(), path3)
        with open(file1_path, 'r', encoding='utf-8') as f1:
            file1 = f1.readlines()
        with open(file2_path, 'r', encoding='utf-8') as f2:
            file2 = f2.readlines()
        with open(file3_path, 'r', encoding='utf-8') as f3:
            file3 = f3.readlines()
        with open(outout_file, 'w', encoding='utf-8') as f_total:

            if len(file1) < len(file2) and len(file1) < len(file3):
                f_total.write(path1 + '\n')
                f_total.write(str(len(file1)) + '\n')
                f_total.writelines(file1)
                f_total.write('\n')
            elif len(file2) < len(file1) and len(file2) < len(file3):
                f_total.write(path2 + '\n')
                f_total.write(str(len(file2)) + '\n')
                f_total.writelines(file2)
                f_total.write('\n')
            elif len(file3) < len(file1) and len(file3) < len(file2):
                f_total.write(path3 + '\n')
                f_total.write(str(len(file3)) + '\n')
                f_total.writelines(file3)
                f_total.write('\n')
            if len(file2) > len(file1) > len(file3) or len(file2) < len(file1) < len(
                    file3):
                f_total.write(path1 + '\n')
                f_total.write(str(len(file1)) + '\n')
                f_total.writelines(file1)
                f_total.write('\n')
            elif len(file1) > len(file2) > len(file3) or len(file2) > len(file1) and len(file2) < len(
                    file3):
                f_total.write(path2 + '\n')
                f_total.write(str(len(file2)) + '\n')
                f_total.writelines(file2)
                f_total.write('\n')
            elif len(file1) > len(file3) > len(file2) or len(file3) > len(file1) and len(file3) < len(
                    file2):
                f_total.write(path3 + '\n')
                f_total.write(str(len(file3)) + '\n')
                f_total.writelines(file3)
                f_total.write('\n')
            if len(file1) > len(file2) and len(file1) > len(file3):
                f_total.write(path1 + '\n')
                f_total.write(str(len(file1)) + '\n')
                f_total.writelines(file1)
            elif len(file2) > len(file1) and len(file2) > len(file3):
                f_total.write(path2 + '\n')
                f_total.write(str(len(file2)) + '\n')
                f_total.writelines(file2)
            elif len(file3) > len(file1) and len(file3) > len(file2):
                f_total.write(path3 + '\n')
                f_total.write(str(len(file3)) + '\n')
                f_total.writelines(file3)
    else:
        print('Давай лучше без параметров')
    return


filename = "cook_book.txt"
cook_book = read_cookbook()
print('Задание 1------------------------------------------------------------')
print(cook_book)
print('Задание 2------------------------------------------------------------')
pprint(get_shop_list_by_dishes(dishes=['Запеченный картофель', 'Омлет'], person_count=2))
print('Задание 3------------------------------------------------------------')
BASE_PATH_REW = os.getcwd()
LOG_DIR_REW = 'Files'
LOG_FILE_REW = 'rewrite_file.txt'
FULL_LOG_PATH_REW = os.path.join(BASE_PATH_REW, LOG_DIR_REW, LOG_FILE_REW)

with open(FULL_LOG_PATH_REW, 'r', encoding='utf-8') as f:
    print(f.read())
