
flowchart TD

A[Inicio] --> B[Abrir Brave]
B --> C[Ir a WhatsApp Web]
C --> D{¿Sesión Activa?}

D -- No --> E[Esperar Login]
E --> D

D -- Sí --> F[Obtener Chats]

F --> G{¿Chat Tiene Mensaje Nuevo?}

G -- Sí --> H[Abrir Chat]
H --> I[Escribir Hola Como Estas]
I --> J[Enviar Mensaje]
J --> F

G -- No --> F
```