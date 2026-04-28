# Mapa planeado del repositorio

## Objetivo

El repositorio se organizará como una aplicación web full stack orientada a integrar, consultar y visualizar información macroeconómica, financiera y regulatoria de fuentes públicas peruanas como BCRP, SBS y SMV.

La estructura se creará progresivamente para evitar carpetas vacías o módulos innecesarios durante las primeras etapas del desarrollo.

## Estructura planeada

```text
radar-financiero-peru/
│
├── backend/
│   └── API, lógica del servidor, validaciones, servicios y conexión a base de datos.
│
├── frontend/
│   └── Interfaz web, componentes, páginas, gráficos y consumo de la API.
│
├── data/
│   ├── raw/
│   │   └── Datos originales descargados o extraídos desde fuentes públicas.
│   │
│   ├── interim/
│   │   └── Datos parcialmente transformados.
│   │
│   ├── processed/
│   │   └── Datos limpios y listos para carga o análisis.
│   │
│   └── samples/
│       └── Muestras pequeñas para pruebas y documentación.
│
├── database/
│   ├── schema/
│   │   └── Definiciones conceptuales del modelo de datos.
│   │
│   ├── migrations/
│   │   └── Cambios progresivos de estructura de base de datos.
│   │
│   ├── seeds/
│   │   └── Datos iniciales de prueba.
│   │
│   └── queries/
│       └── Consultas SQL útiles para análisis y validación.
│
├── docs/
│   └── Documentación técnica del proyecto.
│
├── scripts/
│   └── Scripts auxiliares de ingesta, limpieza, carga y mantenimiento.
│
├── tests/
│   └── Pruebas automatizadas del backend, datos y lógica de negocio.
│
├── .gitignore
├── LICENSE
└── README.md

