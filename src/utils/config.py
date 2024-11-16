import os
from dotenv import load_dotenv

# Cargar variables de entorno
load_dotenv()

def get_database_uri() -> str:
    """Obtener URI de conexión a la base de datos desde variables de entorno."""
    return (f"mysql+pymysql://{os.getenv('MYSQL_USER')}:{os.getenv('MYSQL_PASSWORD')}@"
            f"{os.getenv('MYSQL_HOST')}:{os.getenv('MYSQL_PORT')}/usuarios_cibersecurity")

def get_openai_api_key() -> str:
    """Obtener API key de OpenAI desde variables de entorno."""
    return os.getenv("OPENAI_API_KEY")

# Otras configuraciones
MODEL_NAME = "gpt-4o-mini"
TEMPERATURE = 0