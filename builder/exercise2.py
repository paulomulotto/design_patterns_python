class Class:
    def __init__(self, root_name):
        self.root_name = root_name
        self.fields = []
    
    def __str__(self):
        lines = [f'class {self.root_name}:']
        if not self.fields:
            lines.append('    pass')
        else:
            lines.append('    def __init__(self):')
            
            for field in self.fields:    
                lines.append('        ' + str(field))
        return '\n'.join(lines)


class Field:
    def __init__(self, name, value):
        self.name = name
        self.value = value
    
    def __str__(self):
        return f'self.{self.name} = {self.value}'


class CodeBuilder:
    def __init__(self, root_name):
        self.__class = Class(root_name)

    def add_field(self, name, value):
        self.__class.fields.append(Field(name, value))
        return self

    def __str__(self):
        return str(self.__class)



from unittest import TestCase, main
class Evaluate(TestCase):
    @staticmethod
    def preprocess(s=''):
        return s.strip().replace('\r\n', '\n')

    def test_empty(self):
        cb = CodeBuilder('Foo')
        self.assertEqual(
            self.preprocess(str(cb)),
            'class Foo:\n    pass'
        )

    def test_person(self):
        cb = CodeBuilder('Person').add_field('name', '""')\
                            .add_field('age', 0)
        self.assertEqual(
            self.preprocess(str(cb)),
            '''class Person:
    def __init__(self):
        self.name = ""
        self.age = 0'''
        )


main()



# cb = CodeBuilder('Person').add_field('name', '""')\
#                             .add_field('age', "0")
# print(cb)