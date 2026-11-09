# Proyecto Docker: aplicación web y base de datos

Entrega 1 de Integración Continua. El proyecto levanta dos contenedores comunicados entre sí:

- **web:** aplicación Flask que registra cada visita.
- **db:** PostgreSQL 16 (Alpine) que guarda el registro en la tabla `visitas`.

El código está en la carpeta `Entrega 1/proyecto/`.

## Requisitos

- Docker
- Docker Compose

## Ejecución

Todos los comandos de Docker Compose se ejecutan desde la carpeta `Entrega 1/proyecto/`:

```bash
cd "Entrega 1/proyecto"
docker compose up --build -d
curl http://localhost:5000/
```

Cada petición a `/` incrementa el contador guardado en PostgreSQL.

## Verificación

Desde la carpeta `Entrega 1/proyecto/`:

```bash
docker compose ps
docker compose exec web getent hosts db
docker compose exec db psql -U usuario -d visitas -c "SELECT * FROM visitas;"
```

## Detener el proyecto

Desde la carpeta `Entrega 1/proyecto/`:

```bash
docker compose down
```

Para borrar también los datos de la base de datos, usa `docker compose down -v`.

Las credenciales de `docker-compose.yml` son solo para desarrollo local.
