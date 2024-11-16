from langchain_community.utilities import SQLDatabase
from src.utils.config import get_database_uri
from src.utils.logger import setup_logger

logger = setup_logger(__name__)


class Database:
    """Clase para manejar la conexión y operaciones con la base de datos."""

    def __init__(self):
        """Inicializar la conexión a la base de datos."""
        try:
            self.db = SQLDatabase.from_uri(get_database_uri())
            logger.info("Conexión a la base de datos establecida")
        except Exception as e:
            logger.error(f"Error conectando a la base de datos: {e}")
            raise

    def get_table_info(self) -> str:
        """Obtener información de las tablas de la base de datos."""
        return self.db.get_table_info()

    def run_query(self, query: str) -> str:
        """Ejecutar una consulta SQL."""
        try:
            result = self.db.run(query)
            logger.info("Consulta ejecutada exitosamente")
            return result
        except Exception as e:
            logger.error(f"Error ejecutando consulta SQL: {e}")
            raise