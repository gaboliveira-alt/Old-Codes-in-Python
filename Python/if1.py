note1 = int(input("Nota 1: "))
note2 = int(input("Nota 2: "))

if note1 <= 0 or note1 >= 10:
    print("Apenas zero e dez")
if note2 <= 0 or note2 >= 10:
    print("Apenas zero e dez")


media_notes = (note1 + note2) / 2

if media_notes >= 7.0:
    print("Parabens voce esta aprovado:", media_notes)
elif media_notes >= 5.0 and media_notes < 7.0:
    print("Exame final")
else:
 print("Reprovado")
 