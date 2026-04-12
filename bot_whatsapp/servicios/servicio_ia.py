class ServicioIA:
    """Placeholder para integración de un modelo de IA."""
    
    def __init__(self):
        self.modo_activado = False

    def generar_respuesta(self, contexto_usuario, mensaje_base=""):
        """
        Simula la respuesta de una IA.
        Aquí podrías conectar una API key de OpenAI u otro LLM.
        """
        prompt_enviado = f"{mensaje_base}\n(Generado automáticamente por IA para {contexto_usuario})"
        return prompt_enviado
