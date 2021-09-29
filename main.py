# inflacja na kazdy miesiac
Styczen = 1.592824484
Luty = -0.453509101
Marzec = 2.324671717
Kwiecien = 1.261254407
Maj = 1.782526286
Czerwiec = 2.329384541
Lipiec = 1.502229842
Sierpnien = 1.782526286
Wrzesien = 2.328848994
Pazdziernik = 0.616921348
Listopad = 2.352295886
Grudzien = 0.337779545
Styczen_2 = 1.577035247
Luty_2 = -0.292781443
Marzec_2 = 2.48619659
Kwiecien_2 = 0.267110318
Maj2 = 1.417952672
Czerwiec_2 = 1.054243267
Lipiec_2 = 1.480520104
Sierpnien_2 = 1.577035247
Wrzesien_2 = -0.07742069
Pazdziernik_2 = 1.165733399
Listopad_2 = -0.404186718
Grudzien_2 = 1.499708521

# = (1 + ((B4+3) / 1200) * C3 - 200
tekst = "Twoja pozostala kwota kredytu to: {}, to o {} mniej niz w poprzednim miesiacu"
kwota_kredytu = float(input("Podaj kwote kredytu: "))
wysokosc_oprocentowania = float(input("Podaj wysokosc oprocentowania: "))
wysokosc_raty = float(input("Podaj wysokosc raty"))
inflacja = Styczen
pozostala_kwota_kredytu = (1 + (inflacja + wysokosc_oprocentowania) / 1200) * kwota_kredytu - wysokosc_raty

print(tekst.format(pozostala_kwota_kredytu, kwota_kredytu - pozostala_kwota_kredytu))

kwota_kredytu = pozostala_kwota_kredytu
