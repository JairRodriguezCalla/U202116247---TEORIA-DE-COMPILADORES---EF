; archivo_generado.ll

; Declaraciones globales
@result = global i32 0 ; Variable global para almacenar el resultado

; Función principal
define i32 @main() {
entry:
  ; Asignación
  store i32 42, i32* @result ; Asigna 42 a la variable global result

  ; Comparación
  %x_val = load i32, i32* @result ; Carga el valor de la variable global result
  %cmp = icmp eq i32 %x_val, 42 ; Compara el valor con 42

  ; Estructura de control
  br i1 %cmp, label %if_block, label %if_else_block

if_block:
  ; Bloque if
  ret i32 1 ; Retorna 1 si la condición es verdadera
  br label %if_end

if_else_block:
  ; Bloque else
  ret i32 0 ; Retorna 0 si la condición es falsa
  br label %if_end

if_end:
  ; Fin de la estructura de control
  ret i32 0 ; Retorna un valor (puede ser cualquier valor, ya que es un ejemplo simple)
}
