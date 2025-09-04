# Sistema de Gestión de Juguetería
Nuestro proyecto consiste en un Sistema de Gestión de Juguetería desarrollado en Python, una aplicación sencilla que utiliza Programación Orientada a Objetos para manejar diferentes tipos de juguetes con sus respectivas reglas de negocio.
## Descripción del Proyecto
Este proyecto implementa un sistema de inventario para una juguetería que permite gestionar tres tipos diferentes de juguetes:
- **Juguetes Electrónicos**: Con descuento máximo del 20%.
- **Juguetes Didácticos**: Con descuento máximo del 15%.
- **Juguetes Coleccionables**: Con descuento máximo del 4%
Cada tipo de juguete tiene sus propias reglas de descuento y hereda funcionalidades básicas de la clase padre `Juguete`.
### Pasos para Ejecutar
1. **Abre Visual Studio Code y clona el repositorio**:
   ```bash
   git clone https://github.com/PablitoRpoM205/Jugueteria
   cd Jugueteria
   ```

2. **Ejecuta el programa**:
   ```bash
   python3 main.py
   ```

3. **Navega por el menú**:
   - Opción 1: Ver inventario completo.
   - Opción 2: Vender juguetes.
   - Opción 3: Aplicar descuentos.
   - Opción 4: Salir del programa.

## Uso del Sistema

### Ejemplo de Uso

```bash
--- Menú Juguetería ---
1. Mostrar inventario
2. Vender juguete
3. Aplicar descuento
4. Salir
Elige una opción: 1

Robot - Precio: 100000 - Stock: 5
Lego - Precio: 350000 - Stock: 10
Funko - Precio: 60000 - Stock: 3
Carro - Precio: 200000 - Stock: 6
Rubik - Precio: 15000 - Stock: 18
Goku - Precio: 97000 - Stock: 2
```


## Estructura del Proyecto

```
jugueteria/
│
├── clases/
│   ├── juguete.py          # Clase padre para todos los tipos de juguetes
│   ├── electronico.py      # Juguetes electrónicos
│   ├── didactico.py        # Juguetes didácticos
│   ├── coleccionable.py    # Juguetes coleccionables
│   └── inventario.py       # Gestión del inventario
│
└── main.py                 # Archivo principal con el menú interactivo
└── README.md               # Documentación de la aplicación
```

## Características

### Funcionalidades Principales

- **Gestión de Inventario**: Visualización completa del stock disponible.
- **Sistema de Ventas**: Venta de juguetes con control de stock automático.
- **Aplicación de Descuentos**: Descuentos predeterminados según el tipo de juguete.
- **Validación de Datos**: Control de entrada de datos y manejo de errores.
- **Interfaz de Usuario**: Menú sencillo e interactivo por consola.

### Tipos de Juguetes y Descuentos

| Tipo | Descuento Máximo | Ejemplos |
|------|------------------|----------|
| Electrónico | 20% | Robot, Carro |
| Didáctico | 15% | Lego, Cubo de Rubik |
| Coleccionable | 4% | Funko, Goku |

## Instalación y Ejecución

### Requisitos

- Python 3.6 o superior.
- No se requieren dependencias externas.


### Venta de Juguetes

```bash
Elige una opción: 2
Nombre del juguete: Robot
Cantidad: 2
Se vendieron 2 Robot(s).
```

### Aplicación de Descuentos

```bash
Elige una opción: 3
Nombre del juguete: Lego
Porcentaje de descuento: 10
Se aplicó el descuento. El precio nuevo es: 315000.00
```
### Métodos Esenciales

- `get_nombre()`: Obtiene el nombre del juguete.
- `get_precio()`: Obtiene el precio actual.
- `get_stock()`: Obtiene la cantidad disponible.
- `vender(cantidad)`: Procesa la venta de juguetes.
- `aplicar_descuento(porcentaje)`: Aplica descuentos con validaciones específicas.

## Características Técnicas

- **Encapsulación**: Atributos privados con métodos getter.
- **Herencia**: Clases especializadas que extienden la funcionalidad base.
- **Polimorfismo**: Método `aplicar_descuento()` sobrescrito en cada subclase.
- **Validación de Datos**: Control de rangos y tipos de datos.
- **Manejo de Errores**: Mensajes informativos para el usuario.

## Autores
- Julián Esteban Álvarez Segura
- Juan Pablo Restrepo Muñoz

Instituto Tecnológico Metropolitano (ITM)

Período Académico: 2025-2

Desarrollado como proyecto educativo para demostrar conceptos de Programación Orientada a Objetos en Python.

¡Si te ha gustado nuestro proyecto, no olvides darle una estrella en GitHub!

¡Gracias!