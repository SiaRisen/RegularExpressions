import csv
import re


def csv_reader():
    with open("phonebook_raw.csv", encoding="utf-8") as f:
        rows = csv.reader(f, delimiter=",")
        personal_data = list(rows)
        return personal_data


def get_data(personal_data):
    for el in personal_data:
        name = ' '.join(el[0:3]).strip().split(' ')
        name = name + [''] * (3 - len(name))
        el[:3] = name[:3]

        phone_rep = re.sub(r"(\+7|8)\W*(\d{3})\W*(\d{3})[\s-]*(\d{2})[\s-]*(\d{2})", r"+7(\2)\3-\4-\5", el[5])
        phone = re.sub(r"\(*доб.\s*(\d{4})\)*", r"доб.\1", phone_rep)
        el[5] = phone
    return personal_data


def get_sort_data(personal_data):
    sort_data = []
    sort_data.append(personal_data[0])
    element_list = []
    for i in range(1, len(personal_data)):
        element = personal_data[i]
        identical = [j for j, jj in enumerate(personal_data) if jj[:2] == element[:2]]
        merge_el = [''] * len(element)
        for el in identical:
            if el not in element_list:
                merge_el = get_general(personal_data[el], merge_el)
                element_list.append(el)
        if ''.join(merge_el) != '':
            sort_data.append(merge_el)
    return sort_data


def get_general(data, elem):
    person_list = []
    for i in range(len(elem)):
        if elem[i] == '':
            person_list.append(data[i])
        else:
            person_list.append(data[i])
    return person_list


def csv_writer(sort_data):
    with open("phonebook.csv", "w", encoding="UTF-8") as f:
        datawriter = csv.writer(f, delimiter=',')
        datawriter.writerows(sort_data)


if __name__ == "__main__":
    personal_data = get_data(csv_reader())
    sort_data = get_sort_data(personal_data)
    csv_writer(sort_data)
