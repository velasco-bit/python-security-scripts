# password_checker.py
# Script básico para validar la fortaleza de una contraseña

def check_password(password):
    if len(password) < 8:
        return "❌ La contraseña debe tener al menos 8 caracteres"

    if not any(char.isdigit() for char in password):
        return "❌ La contraseña debe contener al menos un número"

    if not any(char.isupper() for char in password):
        return "❌ La contraseña debe contener al menos una letra mayúscula"

    if not any(char.islower() for char in password):
        return "❌ La contraseña debe contener al menos una letra minúscula"

    return "✅ Contraseña segura"


if __name__ == "__main__":
    user_password = input("Ingresa una contraseña: ")
    result = check_password(user_password)
    print(result)
