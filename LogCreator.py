import datetime # kui tahame kasutada aeg

def createLog():
    name = input("Sinu nimi: ")
    action = input("Tegevus: ")
    time = datetime.datetime.now()
    text = f"Date: {time} Nimi: {name}, Oli salline tegevu: {action}/n"
    file = open("logs.txt", "a", encoding="utf-8")
    file.write(text)
    file.close()
    print("Logid oli salvestatud edukalt")