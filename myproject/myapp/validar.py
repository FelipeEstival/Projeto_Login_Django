import re

def validar_senha(senha):

    if len(senha) < 12:
        return "A senha deve conter no mínimo 12 caracteres"
    if not re.search(r"[A-Z]", senha):
        return "A senha deve conter pelo menos uma letra maiúscula"
    if not re.search(r"[a-z]", senha):
        return "A senha deve conter pelo menos uma letra minúscula" 
    if not re.search(r"\d", senha):
        return"A senha deve conter pelo menos um número"
    if not re.search(r"[!@#$%^&*()_+\-=\[\]{};':\"\\|,.<>/?]", senha):
        return "A senha deve conter pelo menos um caractere especial"

    return "sucesso"