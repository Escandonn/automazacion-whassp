from dataclasses import dataclass
from typing import Optional

@dataclass
class Chat:
    nombre: str
    tiene_no_leidos: bool = False
    cantidad_no_leidos: int = 0
    ultimo_mensaje: Optional[str] = None
    
    def __str__(self):
        estado = "NUEVOS MENSAJES" if self.tiene_no_leidos else "SIN MENSAJES"
        return f"{self.nombre} -> {estado}"
