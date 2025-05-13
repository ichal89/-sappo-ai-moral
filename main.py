from sappo_core import respond

print("🌟 Selamat datang di Sappo AI 🌟")
print("Silakan berbicara denganku... (ketik 'keluar' untuk berhenti)")

while True:
    user_input = input("Anda: ")
    if user_input.lower() in ["keluar", "exit"]:
        print("Sappo: Terima kasih. Semoga harimu diberkahi.")
        break
    print("Sappo:", respond(user_input))
