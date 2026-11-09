# Proyecto Docker: aplicación web y base de datos

Entrega 1 de Integración Continua. El proyecto levanta dos contenedores comunicados entre sí:

- **web:** aplicación Flask que registra cada visita.
- **db:** PostgreSQL 16 (Alpine) que guarda el registro en la tabla `visitas`.

## Requisitos

- Docker
- Docker Compose

## Ejecución

```bash
docker compose up --build -d
curl http://localhost:5000/
```

Cada petición a `/` incrementa el contador guardado en PostgreSQL.

## Verificación

```bash
docker compose ps
docker compose exec web getent hosts db
docker compose exec db psql -U usuario -d visitas -c "SELECT * FROM visitas;"
```

## Detener el proyecto

```bash
docker compose down
```

Para borrar también los datos de la base de datos, usa `docker compose down -v`.

Las credenciales de `docker-compose.yml` son solo para desarrollo local.
