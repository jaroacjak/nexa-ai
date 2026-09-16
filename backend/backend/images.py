"""
Nexa AI - Image Generation
"""

IMAGE_SYSTEM_PROMPT = """
Si Nexa AI Image Generator.
Pomáhaš vytvárať kvalitné obrazové prompty podľa požiadaviek používateľa.
"""


def create_image_prompt(description: str) -> str:
    """
    Vytvorí prompt pre generovanie obrázka.
    """
    description = description.strip()

    if not description:
        return "Napíš, aký obrázok chceš vytvoriť."

    return (
        f"Nexa AI Image Prompt:\n\n"
        f"{description}\n\n"
        "Vytvor kvalitný obrázok podľa tejto požiadavky."
    )


def get_image_system_prompt() -> str:
    """Vráti systémové pokyny pre generovanie obrázkov."""
    return IMAGE_SYSTEM_PROMPT.strip()
