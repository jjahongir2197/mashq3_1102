class Savol:
    def __init__(self, matn, javob):
        self.matn = matn
        self.javob = javob

def test_boshlash(savollar):
    togri = 0

    for s in savollar:
        javob = input(s.matn + " ")
        if javob.lower() == s.javob.lower():
            togri += 1

    print(f"\nTo'g'ri javoblar: {togri}/{len(savollar)}")


savollar = [
    Savol("Python'da funksiya qanday boshlanadi?", "def"),
    Savol("Class kalit so'zi?", "class"),
    Savol("Ro'yxat qaysi qavsda yoziladi? [] yoki {} ?", "[]"),
]

test_boshlash(savollar)
