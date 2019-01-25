import re
import string


class Garden(object):
    def __init__(self, diagram, students=None):
        self.students = students
        self.diagram = diagram
        self.list_of_students = "Alice", "Bob", "Charlie", "David", "Eve", "Fred", "Ginny", "Harriet",\
                                "Ileana", "Joseph", "Kincaid", "Larry"
        self.mydict = {
        "V": "Violets",
        "R": "Radishes",
        "G": "Grass",
        "C": "Clover"
    }

    def plants(self, students):

        n = self.get_element_index(students)
        first_element = (n * 2) - 2
        second_element = (n * 2) - 1

        rows_columns = re.split("\n", self.diagram)
        rows = list(rows_columns[0])  # RVGV
        column = list(rows_columns[1])  # GCRV
        result = (self.mydict[rows[first_element]], self.mydict[rows[second_element]],
                        self.mydict[column[first_element]],
                        self.mydict[column[second_element]])

        return list(result)

    def get_element_index(self, children):
        if children in self.list_of_students:
            names = list(string.ascii_uppercase[:22])
            for index, childName in enumerate(children):
                for i, alphabets in enumerate(names):
                    if childName[index] == names[i]:
                        i = i+1
                        return i
        elif children in self.students:
                namess = sorted(self.students[1][0])
                for indexx, childNames in enumerate(children):
                    for j, alphabetss in enumerate(namess):
                        if childNames[indexx] == namess[j]:
                            indexx = indexx+1
                    return indexx


# another way
class Garden(object):
    kids_default = ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Fred', 'Ginny',
            'Harriet', 'Ileana', 'Joseph', 'Kincaid', 'Larry']
    plants_mapping = {'C': 'Clover',
                      'G': 'Grass',
                      'V': 'Violets',
                      'R': 'Radishes'}

    def __init__(self, diagram, students=kids_default):
        self.possession = {}
        row1, row2 = diagram.split()
        for i, student in enumerate(students):
            try:
                self.possession[student] = [row1[2*i], row1[2*i+1], row2[2*i], row2[2*i+1]]
            except IndexError:
                break

    def plants(self, student):
        return list(map(lambda x: self.plants_mapping[x], self.possession[student]))











