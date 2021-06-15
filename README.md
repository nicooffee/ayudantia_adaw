# Instalación PostgreSQL

Descargar el servidor en este [link](https://www.postgresql.org/download/).

Instalar pgAdmin 4 junto al servidor, con las opciones predeterminadas.

Añadir una contraseña para poder realizar las conexiones al servidor desde pgAdmin/aplicación.

## Iniciar y parar el servidor

Para iniciar o parar el servidor se utilizan los siguientes comandos en la consola PowerShell:

- `pg_ctl start -D [path a los datos]`
- `pg_ctl stop -D [path a los datos]`

Para revisar el PATH al servidor se utiliza el siguiente comando en una ventana *query tool* en pgAdmin 4:

- `show data_directory;`

Ejemplo:
- Iniciar: `pg_ctl start -D 'C:/Program Files/PostgreSQL/13/data'`
- Finalizar: `pg_ctl stop -D 'C:/Program Files/PostgreSQL/13/data'`

## Problemas
### Inicio de Windows
Si se desea que el servidor no inicie automáticamente al iniciar Windows, cambiar el servicio **postgres** de automático a manual. Presionar `Alt + R` e ingresar `services.msc`. Luego buscar el servicio postgres y cambiar la opción. 

Si pgAdmin no puede entrar al servidor probablemente es porque el servidor está apagado.
### `pg_ctl` no encontrado

Para agregar el comando `pg_ctl` a Windows ir a: 
1. PC
2. Propiedades 
3. Propiedades avanzadas del sistema
4. Variables de entorno.

Editar la variable `path` y agregar la siguiente linea:

- `;C:\Program Files\PostgreSQL\13\bin;C:\Program Files\PostgreSQL\13\lib`

Cambiar la ruta dependiendo de la versión y nombre las carpetas.

---
Links de utilidad: 
- [Cambiar servicio postgres a manual](https://serverfault.com/questions/311565/stop-postgresql-from-starting-on-windows)
- [Opciones del comando pg_ctl](https://www.postgresql.org/docs/10/app-pg-ctl.html)
- [Solución a problema pg_ctl/psql 1](https://www.computerhope.com/issues/ch000549.htm)
- [Solución a problema pg_ctl/psql 2](https://stackoverflow.com/questions/30401460/postgres-psql-not-recognized-as-an-internal-or-external-command)