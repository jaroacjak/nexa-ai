"""
Nexa AI - Chat logic
"""

SYSTEM_PROMPT = """
Si Nexa AI, inteligentný AI asistent.
Pomáhaš používateľom s otázkami, učením a programovaním.
Odpovedáš jasne, užitočne a po slovensky, ak používateľ píše po slovensky.
"""


def generate_response(message: str) -> str:
    """
    Vygeneruje odpoveď Nexa AI.

    Aktuálne ide iba o základnú verziu.
    Skutočný AI model pripojíme neskôr.
    """
    message = message.strip()

    if not message:
        return "Ahoj! Som Nexa AI. Ako ti môžem pomôcť?"

    return f"Nexa AI: Rozumiem tvojej správe: {message}"


def get_system_prompt() -> str:
    """Vráti systémové pokyny pre Nexa AI."""
    return SYSTEM_PROMPT.strip()
