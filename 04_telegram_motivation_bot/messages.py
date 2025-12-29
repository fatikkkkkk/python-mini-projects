import random

messages = [
    "Bugün harika bir gün olacak 💪",
    "Asla vazgeçme, başarı yakında 🚀",
    "Küçük adımlar büyük sonuçlar getirir 🌱",
    "Kendine inan, yapabilirsin ✨",
    "Disiplin motivasyondan üstündür 🔥"
]

def get_random_message():
    return random.choice(messages)
