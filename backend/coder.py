"""
Nexa AI - AI Programmer
"""

CODER_SYSTEM_PROMPT = """
Si Nexa AI Coder, AI programátor.
Pomáhaš používateľom písať, opravovať a vysvetľovať kód.

Pravidlá:
- Píš čistý a čitateľný kód.
- Vysvetľuj riešenia jednoducho.
- Zachovávaj programovací jazyk, ktorý používateľ požaduje.
- Ak používateľ neposkytne dostatok informácií, povedz, čo chýba.
"""


def generate_code(request: str) -> str:
    """
    Vygeneruje kód podľa požiadavky používateľa.

    Zatiaľ používa iba základnú odpoveď.
    Skutočný AI model pripojíme neskôr.
    """
    request = request.strip()

    if not request:
        return "Napíš, čo chceš naprogramovať."

    return (
        "Nexa AI Coder rozumie tvojej požiadavke:\n\n"
        f"{request}\n\n"
        "Skutočný AI programátor bude pripojený v ďalšej verzii."
    )


def explain_code(code: str) -> str:
    """
    Pripraví požiadavku na vysvetlenie kódu.
    """
    code = code.strip()

    if not code:
        return "Pošli mi kód, ktorý chceš vysvetliť."

    return (
        "Nexa AI Coder by mal vysvetliť tento kód:\n\n"
        f"{code}"
    )


def fix_code(code: str) -> str:
    """
    Pripraví požiadavku na opravu kódu.
    """
    code = code.strip()

    if not code:
        return "Pošli mi kód, ktorý chceš opraviť."

    return (
        "Nexa AI Coder by mal opraviť tento kód:\n\n"
        f"{code}"
    )


def get_coder_system_prompt() -> str:
    """Vráti systémové pokyny pre AI programátora."""
    return CODER_SYSTEM_PROMPT.strip()
