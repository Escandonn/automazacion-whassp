from seleniumbase import SB

BRAVE_PATH = r"C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe"
REAL_PROFILE = r"C:\Users\alejo\AppData\Local\BraveSoftware\Brave-Browser\User Data"

UNREAD_SELECTOR = 'span[aria-label*="no leídos"]'


def obtener_nombre_chat(chat):
    try:
        return chat.find_element(
            "css selector",
            'span[title]'
        ).get_attribute("title")
    except:
        return "Nombre no encontrado"


def tiene_mensajes_nuevos(chat):
    return bool(
        chat.find_elements(
            "css selector",
            UNREAD_SELECTOR
        )
    )


with SB(
    browser="chrome",
    binary_location=BRAVE_PATH,
    user_data_dir=REAL_PROFILE,
    maximize=True
) as sb:

    sb.open("https://web.whatsapp.com/")
    sb.wait_for_element('div[role="grid"]', timeout=60)

    while True:

        chats = sb.find_elements('div[role="row"]')

        print("\n" + "=" * 60)
        print(f"CHATS VISIBLES DETECTADOS: {len(chats)}")
        print("=" * 60)

        chats_con_unread = []

        for i, chat in enumerate(chats, start=1):

            nombre = obtener_nombre_chat(chat)

            if tiene_mensajes_nuevos(chat):
                estado = "TIENE MENSAJES NUEVOS"
                chats_con_unread.append(nombre)
            else:
                estado = "SIN MENSAJES NUEVOS"

            print(f"CHAT #{i}: {nombre} -> {estado}")

        print("\nRESUMEN:")
        print(f"Chats con mensajes nuevos: {len(chats_con_unread)}")

        for nombre in chats_con_unread:
            print(f"   • {nombre}")

        sb.sleep(5)