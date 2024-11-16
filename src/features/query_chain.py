from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough

from src.model.database import Database
from src.utils.config import get_openai_api_key, MODEL_NAME, TEMPERATURE
from src.utils.logger import setup_logger

logger = setup_logger(__name__)


class DatabaseQueryChain:
    """Clase para manejar consultas a la base de datos usando LangChain."""

    def __init__(self):
        """Inicializar la cadena de consulta."""
        self.db = Database()
        self.llm = ChatOpenAI(
            model=MODEL_NAME,
            temperature=TEMPERATURE,
            api_key=get_openai_api_key()
        )
        self._setup_chains()

    def _setup_chains(self):
        """Configurar las cadenas de procesamiento."""
        self.sql_prompt = PromptTemplate.from_template(
            """Given the database schema below, write a clear, efficient SQL query to answer the user's question.
            Return ONLY the SQL query without any markdown, comments, or explanations.

            Schema:
            {table_info}

            Question: {question}
            SQL Query: """
        )

        self.answer_prompt = PromptTemplate.from_template(
            """Based on the following information, provide a clear and concise answer in Spanish:

            Question: {question}
            SQL Query: {query}
            SQL Result: {result}

            Answer in a user-friendly way, providing context when useful.
            Answer: """
        )

        self._setup_processing_chain()

    def _setup_processing_chain(self):
        """Configurar la cadena de procesamiento principal."""
        self.chain = (
                RunnablePassthrough.assign(
                    query=self._generate_sql_query
                ).assign(
                    result=self._execute_sql_query
                )
                | self.answer_prompt
                | self.llm
                | StrOutputParser()
        )

    def _clean_sql_query(self, query: str) -> str:
        """Limpiar y formatear la consulta SQL."""
        query = query.replace("```sql", "").replace("```", "").strip()
        return " ".join(query.split())

    def _generate_sql_query(self, inputs: dict) -> str:
        """Generar la consulta SQL a partir de la pregunta."""
        try:
            prompt_value = self.sql_prompt.format_prompt(
                question=inputs["question"],
                table_info=self.db.get_table_info()
            )
            query = self.llm.predict(prompt_value.to_string())
            clean_query = self._clean_sql_query(query)
            logger.info(f"Consulta SQL generada: {clean_query}")
            return clean_query
        except Exception as e:
            logger.error(f"Error generando consulta SQL: {e}")
            raise

    def _execute_sql_query(self, inputs: dict) -> str:
        """Ejecutar la consulta SQL."""
        try:
            result = self.db.run_query(inputs["query"])
            logger.info(f"Resultado de la consulta: {result}")
            return result
        except Exception as e:
            logger.error(f"Error ejecutando consulta SQL: {e}")
            raise

    def process_question(self, question: str) -> str:
        """Procesar una pregunta y obtener una respuesta."""
        try:
            logger.info(f"Procesando pregunta: {question}")
            response = self.chain.invoke({"question": question})
            logger.info("Respuesta generada exitosamente")
            return response
        except Exception as e:
            logger.error(f"Error procesando pregunta: {e}")
            return f"Lo siento, hubo un error al procesar tu pregunta: {str(e)}"