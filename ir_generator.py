class IRCommand:
    def __init__(self, operation, arguments):
        self.operation = operation
        self.arguments = arguments

    def __str__(self):
        return f"{self.operation} {', '.join(map(str, self.arguments))}"

class IRGenerator:
    def __init__(self):
        self.ir_code = []

    def add_assignment(self, var_name, var_value):
        ir_command = IRCommand("ASSIGN", [var_name, var_value])
        self.ir_code.append(ir_command)

    def add_if_statement(self, condition, then_commands):
        ir_command = IRCommand("IF", [condition, then_commands])
        self.ir_code.append(ir_command)

    # Agrega otras funciones según sea necesario

    def save_ir_code(self, file_name):
        with open(file_name, "w") as file:
            for ir_command in self.ir_code:
                file.write(str(ir_command) + '\n')

if __name__ == "__main__":
    ir_generator = IRGenerator()

    # Agrega comandos IR según la lógica de tu script
    ir_generator.add_assignment("x", "10")
    ir_generator.add_if_statement("x > 5", ["print('x es mayor que 5')"])

    # Guarda el código IR en un archivo
    ir_generator.save_ir_code("output.ir")
