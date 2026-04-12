from seleniumbase import SB

BRAVE_PATH = r"C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe"
REAL_PROFILE = r"C:\Users\alejo\AppData\Local\BraveSoftware\Brave-Browser\User Data"

UNREAD_SELECTORS = [
    'span[aria-label*="mensajes no leídos"]',
    'span[aria-label*="mensaje no leído"]',
    'span[aria-label*="no leídos"]',
    'div._ahlk',
    'div[aria-hidden="true"] span[aria-label*="no leídos"]',
]


def obtener_nombre_chat(chat):
    try:
        return chat.find_element(
            "css selector",
            'span[title]'
        ).get_attribute("title")
    except:
        return "Nombre no encontrado"


def detectar_mensajes_nuevos(chat):
    selectores_exitosos = []

    for selector in UNREAD_SELECTORS:
        encontrados = chat.find_elements("css selector", selector)

        if encontrados:
            selectores_exitosos.append(selector)

    return selectores_exitosos


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

        for i, chat in enumerate(chats, start=1):

            nombre = obtener_nombre_chat(chat)

            selectores_ok = detectar_mensajes_nuevos(chat)

            print(f"\nCHAT #{i}: {nombre}")

            if selectores_ok:
                print("ESTADO: TIENE MENSAJES NUEVOS")

                print("SELECTORES QUE FUNCIONARON:")
                for sel in selectores_ok:
                    print(f"   [✓] {sel}")

            else:
                print("ESTADO: SIN MENSAJES NUEVOS")

        sb.sleep(5)