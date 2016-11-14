class Customer:
    name = ''
    services = []
    smd = []

    def __init__(self, name, services, smd):
        self.name = name
        self.services = services
        self.smd = smd

customers = {89163523116: Customer('Глеб', ['Интернет', 'Умный дом', 'Прохождение стажировки'], ['термостат', 'свет'])}
customers.update({2: Customer('Глеб', ['Интернет Yota', 'Умный дом', 'Прохождение стажировки'], ['термостат', 'свет'])})
customers.update({1: Customer('Юрий Туржанский', ['Интернет', 'Умный дом', 'Управление стажировкой'], ['Термостат', 'Свет'])})
customers.update({89166487610: Customer('Юрий Туржанский', ['Интернет', 'Умный дом', 'Управление стажировкой'], ['Термостат', 'Свет'])})

