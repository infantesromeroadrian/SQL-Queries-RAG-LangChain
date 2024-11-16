from src.features.query_chain import DatabaseQueryChain
from src.utils.logger import setup_logger

logger = setup_logger(__name__)


def main():
    """Función principal para demostración."""
    try:
        # Crear instancia de la cadena
        query_chain = DatabaseQueryChain()

        # Ejemplos de preguntas
        questions = [
            "¿Cuáles son los últimos 5 usuarios registrados?",
            "¿Cuántos usuarios hay en total?",
            "¿Cuál es el promedio de años de experiencia?"
        ]

        # Procesar cada pregunta
        for question in questions:
            print("\n" + "=" * 50)
            print(f"Pregunta: {question}")
            print("-" * 50)
            response = query_chain.process_question(question)
            print(f"Respuesta: {response}")

    except Exception as e:
        logger.error(f"Error en la ejecución principal: {e}")


if __name__ == "__main__":
    main()