Sim, em Python é possível integrar código de baixo nível, como **C** e **Assembly**, para melhorar o desempenho de certas partes do programa ou acessar diretamente o hardware. Isso pode ser feito de várias maneiras:

1. **Extensões em C/C++**: Python permite criar extensões em C/C++ que podem ser chamadas diretamente de código Python. Isso é feito com ferramentas como **Cython**, **ctypes**, **cffi**, e **CPython API**.
2. **Código Assembly**: É mais raro, mas podemos usar Assembly em Python de forma indireta ao incorporá-lo em bibliotecas C.

### 1. Usar código em C com `ctypes`

A biblioteca `ctypes` permite carregar bibliotecas C e chamar funções diretamente de Python. Primeiro, criamos uma biblioteca em C e depois chamamos suas funções em Python.

#### Exemplo com `ctypes`

1. **Criar uma biblioteca C**: Vamos criar um ficheiro `calculadora.c` com funções básicas.

   ```c
   // calculadora.c
   #include <stdio.h>

   int soma(int a, int b) {
       return a + b;
   }

   int subtracao(int a, int b) {
       return a - b;
   }
   ```

2. **Compilar a biblioteca**: No terminal, compile o código C como uma biblioteca partilhada:

   ```bash
   gcc -shared -o calculadora.so -fPIC calculadora.c
   ```

   Em Windows, o comando seria algo como:

   ```bash
   gcc -shared -o calculadora.dll calculadora.c
   ```

3. **Usar a biblioteca em Python**:

   ```python
   # principal.py
   import ctypes

   # Carregar a biblioteca
   calculadora = ctypes.CDLL('./calculadora.so')  # No Windows, './calculadora.dll'

   # Configurar os tipos de retorno das funções
   calculadora.soma.restype = ctypes.c_int
   calculadora.subtracao.restype = ctypes.c_int

   # Usar as funções
   resultado_soma = calculadora.soma(10, 5)
   resultado_subtracao = calculadora.subtracao(10, 5)

   print("Soma:", resultado_soma)          # Saída: Soma: 15
   print("Subtração:", resultado_subtracao) # Saída: Subtração: 5
   ```

### 2. Usar código em C com `cffi`

A biblioteca `cffi` é outra maneira de chamar funções C em Python. Ela permite uma interação mais detalhada e é útil para acessar estruturas complexas de C.

1. **Criar a biblioteca C** (mesmo código `calculadora.c` do exemplo anterior).

2. **Compilar a biblioteca** (como visto anteriormente).

3. **Usar `cffi` em Python**:

   ```python
   # principal.py
   from cffi import FFI

   ffi = FFI()

   # Declarar as funções C que queremos usar
   ffi.cdef("""
       int soma(int a, int b);
       int subtracao(int a, int b);
   """)

   # Carregar a biblioteca
   calculadora = ffi.dlopen('./calculadora.so')  # No Windows, './calculadora.dll'

   # Usar as funções
   resultado_soma = calculadora.soma(10, 5)
   resultado_subtracao = calculadora.subtracao(10, 5)

   print("Soma:", resultado_soma)          # Saída: Soma: 15
   print("Subtração:", resultado_subtracao) # Saída: Subtração: 5
   ```

### 3. Usar Assembly com Python (via C)

Python não possui suporte direto para Assembly, mas podemos usar Assembly em funções C e depois chamá-las em Python usando `ctypes` ou `cffi`.

1. **Criar um código C com Assembly embutido**:

   ```c
   // assembly_func.c
   #include <stdio.h>

   int soma(int a, int b) {
       int resultado;
       __asm__ ("add %1, %2; mov %2, %0"
                : "=r"(resultado)       // Saída
                : "r"(a), "r"(b)        // Entradas
                );
       return resultado;
   }
   ```

2. **Compilar o código C para uma biblioteca**:

   ```bash
   gcc -shared -o assembly_func.so -fPIC assembly_func.c
   ```

3. **Usar a biblioteca em Python**:

   ```python
   # principal.py
   import ctypes

   # Carregar a biblioteca
   assembly_func = ctypes.CDLL('./assembly_func.so')  # No Windows, './assembly_func.dll'

   # Configurar o tipo de retorno da função
   assembly_func.soma.restype = ctypes.c_int

   # Usar a função
   resultado = assembly_func.soma(10, 5)
   print("Resultado (Assembly):", resultado)  # Saída: Resultado (Assembly): 15
   ```

### 4. Criar Extensões com Cython

O **Cython** compila o código Python para código C, permitindo o uso de tipos de dados C e o acesso direto a bibliotecas C.

1. **Criar um ficheiro `.pyx`**:

   ```python
   # calculadora.pyx
   cdef int soma(int a, int b):
       return a + b

   cdef int subtracao(int a, int b):
       return a - b
   ```

2. **Criar o setup para compilar com Cython**:

   ```python
   # setup.py
   from setuptools import setup
   from Cython.Build import cythonize

   setup(
       ext_modules=cythonize("calculadora.pyx")
   )
   ```

3. **Compilar o módulo Cython**:

   ```bash
   python setup.py build_ext --inplace
   ```

4. **Usar o módulo compilado em Python**:

   ```python
   # principal.py
   import calculadora

   print("Soma:", calculadora.soma(10, 5))          # Saída: Soma: 15
   print("Subtração:", calculadora.subtracao(10, 5)) # Saída: Subtração: 5
   ```

Essas técnicas permitem integrar Python com código de baixo nível, oferecendo uma flexibilidade significativa e controle sobre o desempenho.
