Prueba Técnica Odoo - Retail Promotions

Instrucciones de instalación

1. Ya el repositorio contiene el nombre del módulo. Si se descarga como un zip en teoría el nombre debería ser 'retail_promotions-master'. 
Puede descargarlo de esa forma o con git dentro de una carpeta en los addons de Odoo. La versión utilizada para la prueba es la versión 18.

2. Una vez descargado en una carpeta, debe guardarla en la carpeta de addons extras de odoo. Esa carpeta (la de adddons extras) 
debe estar especificada en el archivo de configuración de Odoo para que pueda detectarla.

3. Tras haber especificado la carpeta de addons extras puede instalar el módulo dentro del apartado de Apps de Odoo (actualizando la lista de aplicaciones), 
el módulo depende del módulo de ventas base de Odoo (sale), la prueba se realizó en un entorno donde únicamente se instaló ese módulo oficial, no obstante, 
cuando se instaló a su vez se instalaron otros módulos base de Odoo, pero el módulo de la prueba solo necesita el módulo sale.

Para ver los cambios que trae el módulo puede ingresar en el apartado de ventas (Sales), ahí saldrá una opción llamada Promociones donde se verán reflejadas 
las promociones que se encuentren activas o inactivas, al ser la primera vez que ingresa no verá ninguna, si pulsa el botón de new (Nuevo), podrá 
crear una promoción con los campos especificados en la pdf, cuenta con validaciones para verificar si el porcentaje de descuento se encuentra entre 0 y 100 
y si la fecha de cierre ingresada es anterior a la fecha de inicio.

Puede escoger los productos que quiera para la promoción, pero tenga en cuenta que contiene una validación por si un producto contiene varias promociones 
a la vez, por lo que si la fecha de inicio o de cierre de su nueva promoción choca con promociones creadas anteriormente y esta va a estar activa 
entonces el módulo no le permitirá crearla o modificarla.

Puede alternar entre la vista tree/list y kanban y puede exportar las promociones como un pdf en la vista tree/list.

En el apartado de órdenes de venta (Sale order), puede crear órdenes de venta con los productos en promoción. El módulo automáticamente aplica el descuento si 
la promoción está activa y si se encuentra entre la fecha de inicio y cierre.

Respuestas de las preguntas teóricas:

1. Conceptos básicos de Odoo
- ¿Cuáles son los componentes principales de un módulo en Odoo?
- R: Los modelos, las vistas, archivos de datos, de seguridad y los controladores.

- Explica la diferencia entre fields.Char y fields.Text
- R: fields.Char se utiliza en textos más cortos y fields.Text se utiliza en textos más largos.

- ¿Para qué sirve el archivo __manifest__.py?
- R: El archivo manifest.py contiene diferentes metadatos importantes para el módulo en cuestión, como el directorio de las vistas, archivos de datos, y las 
dependencias hacia otros módulos. Sin ese archivo, directamente no se puede instalar el módulo en ningún entorno de Odoo.

2. Conocimientos Retail
- ¿Cómo manejarías el control de inventario en Odoo para una tienda retail?
- R: Se debe realizar la recepción de mercancía nueva, ya sea hacia la tienda o algún almacén extra que tenga, especificando la localización de la misma,
además de la ubicación, el control del estado de la mercancía, si ya fue vendida, si aún queda stock, si en algún punto se realizó una devolución, etc.

- ¿Qué módulos de Odoo consideras esenciales para una tienda retail?
- R: Esto puede variar dependiendo de la tienda o el comercio, pero considero que los más importantes son los de inventario, compras, ventas, punto de venta, 
facturacion y contabilidad.

3. Seguridad y Accesos
- ¿Cómo defines grupos de usuarios y permisos en Odoo?
- R: Hay varias formas. Puede hacerse a través de la interfaz de Odoo o creando archivos de datos donde se especifiquen los roles específicos y los 
permisos que va a tener.

- ¿Cuál es la diferencia entre una regla de registro (record rule) y una lista de control de acceso (ACL)?
- R: La lista de control de acceso controla qué persona puede ingresar o no al módulo y la regla de registro permite determinar qué puede o no hacer 
dentro de ese mismo módulo.

