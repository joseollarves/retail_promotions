Prueba Tecnica Odoo - Retail Promotions

Instrucciones de Instalacion

1. Ya el repositorio contiene el nombre del modulo, si se descarga como un zip en teoria el nombre deberia ser 'retail_promotions-master', 
puede descargarlo de esa forma o con git dentro de una carpeta en los addons de Odoo, la version utilizada para la prueba es la version 18.

2. Una vez descargado en una carpeta debe guardarla en la carpeta de addons extras de odoo, esa carpeta (la de adddons extras) debe 
estar especificada en el archivo de configuracion de odoo para que pueda detectarla.

3. Tras haber especificado la carpeta de addons extras puede instalar el modulo dentro del apartado de Apps de Odoo (actualzando la lista 
de aplicaciones), el modulo depende del modulo de ventas base de odoo (sale), la prueba se realizo en un entorno donde unicamente se instalo 
ese modulo oficial, no obstante, cuando se instalo a su vez se instalaron otros modulos base de Odoo, pero el modulo de la prueba 
solo necesita el modulo sale.

Para ver los cambios que trae el modulo puede ingresar en el apartado de ventas (Sales), ahi saldra una opcion llamada Promociones donde se
veran reflejadas las promociones que se encuentren activas o inactivas, al ser la primera vez que ingresa no vera ninguna, si pulsa el boton 
de new (Nuevo), podra crear una promocion con los campos especificados en la prueba, cuenta con validaciones para verificar si 
el porcentaje de descuento se encuentra entre 0 y 100 y si la fecha de cierre ingresada es anterior a la fecha de inicio.

Puede escoger los productos que quiera para la promocion, pero tenga en cuenta que contiene una validacion por si un producto contiene
varias promociones a la vez, por lo que si la fecha de inicio o de cierre de su nueva promocion choca con promociones creadas anteriormente
y esta va a estar activa entonces el modulo no le permitira crearla o modificarla.

Puede alternar entre la vista tree/list y kanban y puede exportar las promociones como un pdf en la vista tree/list.

En el apartado de ordenes de venta (Sale order), puede crear ordenes de venta con los productos en promocion, el modulo automaticamente
aplica el descuento si la promocion esta activa y si se encuentra entre la fecha de inicio y cierre.


Respuestas de las preguntas teoricas:

1. Conceptos basicos de Odoo
- ¿Cuáles son los componentes principales de un módulo en Odoo?
- R: Los modelos, las vistas, archivos de datos, de seguridad y los controladores.

- Explica la diferencia entre fields.Char y fields.Text
R: fields.Char se utiliza en textos mas cortos y fields.Text se utiliza en textos mas largos.

- ¿Para qué sirve el archivo __manifest__.py?
- R: El archivo  __manifest__.py contiene diferentes metadatos importantes para el modulo en cuestion como el directorio de las vistas, archivos de datos, 
    y las dependencias hacia otros modulos. Sin ese archivo directamente no se puede instalar el modulo en ningun entorno de Odoo.

2. Conocimientos Retail
- ¿Cómo manejarías el control de inventario en Odoo para una tienda retail?
- R: Se debe realizar la recepcion de mercancia nueva, ya sea hacia a la tienda o algun almacen extra que tenga, especificando la localizacion de la misma,
  ademas de la ubicacion el control del estado de la mercancia, si ya fue vendida, si aun queda stock, si en algun punto se realizo una devolucion, etc.

- ¿Qué módulos de Odoo consideras esenciales para una tienda retail?
- R: Esto puede variar dependiendo de la tienda o el comercio pero considero que los mas importantes son los de inventario, compras, ventas, punto de venta,
  facturacion y contabilidad.

3. Seguridad y Accesos
- ¿Cómo defines grupos de usuarios y permisos en Odoo?
- R: Hay varias formas, puede hacerse a traves de la interfaz de Odoo o creando archivos de datos donde se especifiquen los roles especificos y los permisos
  que va a tener.

- ¿Cuál es la diferencia entre una regla de registro (record rule) y una lista de control de acceso (ACL)?
- R: La lista de control de acceso controla que persona puede ingresar o no al modulo y la regla de registro permite determinar que puede o no hacer dentro de 
ese mismo modulo.

