class Indent:
    size = 2
    
class FieldElement:
    def __init__(self, name='', valor=''):
        self.name = name
        self.valor = valor
        
        
    def __str__(self):
        return f'{self.name} = {self.valor}'
    
    
class CodeElement:
    def __init__(self, root_name=''):
        self.root_name = root_name
        self.fields = []
        
    
    def __str(self, indent=0):
        lines = []
        
        lines.append(f'class {self.root_name}:')
        i = ' ' * (indent+1*Indent.size)
        if self.fields:
            lines.append(f'{i}def __init__(self):')
        else:
            lines.append(f'{i}pass')
            
        # fields
        i = ' ' * (indent+2*Indent.size)
        for field in self.fields:
            lines.append(f'{i}{field}')
        
        return '\n'.join(lines)
        
        
    def __str__(self):
        return self.__str()

        
        

class CodeBuilder:
    def __init__(self, root_name):
        self.code_element = CodeElement(root_name)


    def add_field(self, _type, name):
        self.code_element.fields.append(
            FieldElement(_type, name)
        )
        return self
        
    def clear(self):
        self.code_element = CodeElement(root_name=self.code_element.root_name)
        
    def __str__(self):
        return str(self.code_element)



cb = CodeBuilder('Person').add_field('name', '""')\
                            .add_field('age', "0")
print(cb)