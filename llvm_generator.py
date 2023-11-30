# llvm_generator.py
from llvmlite import ir, binding

import ctypes  # Añade esta importación para el manejo de tipos de funciones en ctypes

def generate_llvm_code():
    # Inicializa LLVM
    binding.initialize()
    binding.initialize_native_target()
    binding.initialize_native_asmprinter()

    # Crea el módulo LLVM
    module = ir.Module(name="my_module")

    # Crea el motor de ejecución JIT
    target_machine = binding.Target.from_default_triple().create_target_machine()
    backing_mod = binding.parse_assembly("")
    engine = binding.create_mcjit_compiler(backing_mod, target_machine)

    # Crea el tipo de función para funciones que devuelven int
    int_type = ir.IntType(32)
    func_type = ir.FunctionType(int_type, [])

    # Crea la función main
    main_func = ir.Function(module, func_type, name="main")
    entry_block = main_func.append_basic_block(name="entry")
    builder = ir.IRBuilder(entry_block)

    # Agrega código para asignación
    x = builder.alloca(int_type, name="x")
    builder.store(ir.Constant(int_type, 42), x)

    # Agrega código para if statement
    cond = builder.icmp_signed('==', builder.load(x), ir.Constant(int_type, 42), name="if.cond")
    if_block = main_func.append_basic_block("if.block")
    if_else_block = main_func.append_basic_block("if.else.block")
    end_block = main_func.append_basic_block("if.end")
    builder.cbranch(cond, if_block, if_else_block)

    builder.position_at_end(if_block)
    builder.branch(end_block)

    builder.position_at_end(if_else_block)
    builder.branch(end_block)

    builder.position_at_end(end_block)

    # Imprime el código LLVM generado
    print(str(module))

    # Compila y ejecuta el código LLVM
    engine.add_module(module)
    engine.finalize_object()
    engine.run_static_constructors()

    # Obtiene el puntero a la función y la llama
    main_ptr = engine.get_function_address("main")
    func = ctypes.CFUNCTYPE(ctypes.c_int)(main_ptr)
    result = func()

    print("Result:", result)

if __name__ == "__main__":
    generate_llvm_code()

