📅 Sistema de Reservas Genérico

Backend desarrollado con FastAPI para la gestión de reservas en negocios basados en agendamiento (barberías, centros estéticos, clínicas, entrenadores personales, etc.).

El sistema permite administrar:

Negocios

Staff (empleados/profesionales)

Servicios

Clientes

Reservas con validación de disponibilidad

Control de concurrencia y consistencia de datos

🚀 Tecnologías Utilizadas

FastAPI

PostgreSQL

SQLAlchemy 2.0

Alembic

JWT Authentication

Docker (opcional en fase de despliegue)

🎯 Objetivo del Proyecto

Construir un backend profesional que:

Garantice consistencia en reservas

Maneje concurrencia correctamente

Separe responsabilidades (API, Services, Repositories)

Siga buenas prácticas de arquitectura

Sea escalable a múltiples tipos de negocio

🧱 Arquitectura del Proyecto
app/
 ├── main.py
 ├── core/           # Configuración y utilidades
 ├── db/             # Conexión y sesión de base de datos
 ├── models/         # Modelos SQLAlchemy
 ├── schemas/        # Esquemas Pydantic
 ├── repositories/   # Acceso a datos
 ├── services/       # Lógica de negocio
 ├── api/            # Rutas (endpoints)

Principios aplicados

Separación de responsabilidades

Lógica de negocio fuera de los endpoints

Validación doble (service + base de datos)

Uso de transacciones para operaciones críticas

📦 Modelos Principales

Negocio

Usuario

Staff

Servicio

Reserva

Las reservas validan:

Que el staff pertenece al negocio

Que el servicio pertenece al negocio

Que el horario esté disponible

Que no existan conflictos de concurrencia

🔐 Control de Concurrencia

La consistencia se garantiza mediante:

Validación en capa de servicio

Restricciones en base de datos

Manejo de IntegrityError

Uso de transacciones

Esto evita reservas duplicadas en escenarios de múltiples solicitudes simultáneas.