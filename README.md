# Sistema de Consulta de Base de Datos en Lenguaje Natural

## Descripción
Sistema que permite realizar consultas a una base de datos MySQL utilizando lenguaje natural. El sistema utiliza LangChain y GPT-4 para traducir preguntas en español a consultas SQL y presentar los resultados de manera comprensible para el usuario.

## Características Principales
- 🗣️ Consultas en lenguaje natural en español
- 🔄 Traducción automática a SQL
- 📊 Integración con MySQL
- 🤖 Utiliza GPT-4 para procesamiento de lenguaje natural
- 📝 Respuestas formatadas y contextualizadas
- 🔍 Logging detallado para debugging
- 🛡️ Manejo robusto de errores

## Estructura del Proyecto
proyecto/
├── pyproject.toml          # Configuración de Poetry y dependencias
├── README.md              # Documentación del proyecto
├── main.py               # Punto de entrada principal
└── src/                  # Código fuente
├── models/           # Modelos y conexiones a base de datos
├── utils/            # Utilidades (configuración, logging)
└── features/         # Funcionalidades principales


## Tecnologías Utilizadas
-
- Python 3.9 - 3.13
- LangChain
- OpenAI GPT-4
- MySQL
- Poetry para gestión de dependencias

## Requisitos Previos
- Python 3.9 o superior
- Poetry instalado
- MySQL Server
- API Key de OpenAI
- Variables de entorno configuradas

## Instalación

1. Clonar el repositorio:
```bash
git clone https://github.com/infantesromeroadrian/SQL-Queries-RAG-LangChain.git
cd tu-proyecto

Instalar dependencias con Poetry:

bash

Configurar variables de entorno (crear archivo .env):

envCopyMYSQL_HOST=tu_host
MYSQL_PORT=tu_puerto
MYSQL_USER=tu_usuario
MYSQL_PASSWORD=tu_contraseña
OPENAI_API_KEY=tu_api_key_de_openai
Uso

Activar el entorno virtual:

bash

Ejecutar el script principal:

bashCopypython main.py
Ejemplos de Uso
pythonCopyfrom src.features.query_chain import DatabaseQueryChain

# Crear instancia del sistema
query_chain = DatabaseQueryChain()

# Realizar consultas
question = "¿Cuáles son los últimos 5 usuarios registrados?"
response = query_chain.process_question(question)
print(response)
Estructura de la Base de Datos
Tabla: usuarios
CampoTipoDescripciónid_usuarioINTEGERID único del usuario (PK)nombreVARCHAR(100)Nombre completonivel_estudiosVARCHAR(50)Nivel de estudiosespecialidadVARCHAR(100)Área de especializaciónexperiencia_añosINTEGERAños de experienciaemailVARCHAR(100)Correo electrónicotelefonoVARCHAR(15)Número de teléfonociudadVARCHAR(50)Ciudad de residenciafecha_registroDATEFecha de registrocomentariosTEXTComentarios adicionales
Características Detalladas
Procesamiento de Consultas

Traducción de lenguaje natural a SQL
Limpieza y validación de consultas
Ejecución segura de queries
Formateo de respuestas

Sistema de Logging

Registro detallado de operaciones
Trazabilidad de errores
Monitoreo de consultas

Manejo de Errores

Validación de inputs
Manejo de excepciones específicas
Mensajes de error informativos

Contribuir

Fork el repositorio
Crear una rama para tu feature (git checkout -b feature/AmazingFeature)
Commit tus cambios (git commit -m 'Add some AmazingFeature')
Push a la rama (git push origin feature/AmazingFeature)
Abrir un Pull Request

Licencia
Este proyecto está bajo la Licencia MIT - ver el archivo LICENSE.md para detalles
Autores

[Tu Nombre] - Trabajo Inicial - TuUsuario

Agradecimientos

LangChain por el framework
OpenAI por el modelo GPT-4
Todos los contribuidores que participan en este proyecto

Estado del Proyecto
🚧 En desarrollo activo
Contacto
Tu Nombre - @tutwitter - email@ejemplo.com
Link del Proyecto: https://github.com/tu-usuario/tu-proyecto
Copy
Este README.md proporciona:
1. Una descripción clara del proyecto
2. Instrucciones de instalación y uso
3. Detalles técnicos importantes
4. Estructura del proyecto
5. Ejemplos de uso
6. Información sobre contribuciones
7. Contacto y licencia

Puedes personalizar esta descripción según tus necesidades específicas, añadiendo o modificando secciones según sea necesario. ¿Hay alguna sección específica que te gustaría expandir o modificar? CopyRetryClaude does not have internet access. Links provided may not be accurate or up to date.