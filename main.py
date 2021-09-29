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
Maj_2 = 1.417952672
Czerwiec_2 = 1.054243267
Lipiec_2 = 1.480520104
Sierpnien_2 = 1.577035247
Wrzesien_2 = -0.07742069
Pazdziernik_2 = 1.165733399
Listopad_2 = -0.404186718
Grudzien_2 = 1.499708521

# = (1 + ((B4+3) / 1200) * C3 - 200
tekst = "\nTwoja pozostala kwota kredytu to: {}, to o {} mniej niz w poprzednim miesiacu"
kwota_kredytu = float(input("Podaj kwote kredytu: "))
wysokosc_oprocentowania = float(input("Podaj wysokosc oprocentowania: "))
wysokosc_raty = float(input("Podaj wysokosc raty: "))

# Styczen
inflacja = Styczen
pozostala_kwota_kredytu = (1 + (inflacja + wysokosc_oprocentowania) / 1200) * kwota_kredytu - wysokosc_raty

print(tekst.format(round(pozostala_kwota_kredytu, 2), round(kwota_kredytu - pozostala_kwota_kredytu,2)), end='')

kwota_kredytu = pozostala_kwota_kredytu

# Luty

inflacja = Luty
pozostala_kwota_kredytu = (1 + (inflacja + wysokosc_oprocentowania) / 1200) * kwota_kredytu - wysokosc_raty

print(tekst.format(round(pozostala_kwota_kredytu, 2), round(kwota_kredytu - pozostala_kwota_kredytu,2)), end='')

kwota_kredytu = pozostala_kwota_kredytu

# Marzec

inflacja = Marzec
pozostala_kwota_kredytu = (1 + (inflacja + wysokosc_oprocentowania) / 1200) * kwota_kredytu - wysokosc_raty

print(tekst.format(round(pozostala_kwota_kredytu, 2), round(kwota_kredytu - pozostala_kwota_kredytu,2)), end='')

kwota_kredytu = pozostala_kwota_kredytu

# Kwiecien
inflacja = Kwiecien
pozostala_kwota_kredytu = (1 + (inflacja + wysokosc_oprocentowania) / 1200) * kwota_kredytu - wysokosc_raty

print(tekst.format(round(pozostala_kwota_kredytu, 2), round(kwota_kredytu - pozostala_kwota_kredytu,2)), end='')

kwota_kredytu = pozostala_kwota_kredytu

# Maj
inflacja = Maj
pozostala_kwota_kredytu = (1 + (inflacja + wysokosc_oprocentowania) / 1200) * kwota_kredytu - wysokosc_raty

print(tekst.format(round(pozostala_kwota_kredytu, 2), round(kwota_kredytu - pozostala_kwota_kredytu,2)), end='')

kwota_kredytu = pozostala_kwota_kredytu

# Czerwiec
inflacja = Czerwiec
pozostala_kwota_kredytu = (1 + (inflacja + wysokosc_oprocentowania) / 1200) * kwota_kredytu - wysokosc_raty

print(tekst.format(round(pozostala_kwota_kredytu, 2), round(kwota_kredytu - pozostala_kwota_kredytu,2)), end='')

kwota_kredytu = pozostala_kwota_kredytu

# Lipiec
inflacja = Lipiec
pozostala_kwota_kredytu = (1 + (inflacja + wysokosc_oprocentowania) / 1200) * kwota_kredytu - wysokosc_raty

print(tekst.format(round(pozostala_kwota_kredytu, 2), round(kwota_kredytu - pozostala_kwota_kredytu,2)), end='')

kwota_kredytu = pozostala_kwota_kredytu

#Sierpien
inflacja = Sierpnien
pozostala_kwota_kredytu = (1 + (inflacja + wysokosc_oprocentowania) / 1200) * kwota_kredytu - wysokosc_raty

print(tekst.format(round(pozostala_kwota_kredytu, 2), round(kwota_kredytu - pozostala_kwota_kredytu,2)), end='')

kwota_kredytu = pozostala_kwota_kredytu

#Wrzesien
inflacja = Wrzesien
pozostala_kwota_kredytu = (1 + (inflacja + wysokosc_oprocentowania) / 1200) * kwota_kredytu - wysokosc_raty

print(tekst.format(round(pozostala_kwota_kredytu, 2), round(kwota_kredytu - pozostala_kwota_kredytu,2)), end='')

kwota_kredytu = pozostala_kwota_kredytu

# Pazdziernik
inflacja = Pazdziernik
pozostala_kwota_kredytu = (1 + (inflacja + wysokosc_oprocentowania) / 1200) * kwota_kredytu - wysokosc_raty

print(tekst.format(round(pozostala_kwota_kredytu, 2), round(kwota_kredytu - pozostala_kwota_kredytu,2)), end='')

kwota_kredytu = pozostala_kwota_kredytu

#Listopad
inflacja = Listopad
pozostala_kwota_kredytu = (1 + (inflacja + wysokosc_oprocentowania) / 1200) * kwota_kredytu - wysokosc_raty

print(tekst.format(round(pozostala_kwota_kredytu, 2), round(kwota_kredytu - pozostala_kwota_kredytu,2)), end='')

kwota_kredytu = pozostala_kwota_kredytu

# Grudzien
inflacja = Grudzien
pozostala_kwota_kredytu = (1 + (inflacja + wysokosc_oprocentowania) / 1200) * kwota_kredytu - wysokosc_raty

print(tekst.format(round(pozostala_kwota_kredytu, 2), round(kwota_kredytu - pozostala_kwota_kredytu,2)), end='')

kwota_kredytu = pozostala_kwota_kredytu

# Styczen 2
inflacja = Styczen_2
pozostala_kwota_kredytu = (1 + (inflacja + wysokosc_oprocentowania) / 1200) * kwota_kredytu - wysokosc_raty

print(tekst.format(round(pozostala_kwota_kredytu, 2), round(kwota_kredytu - pozostala_kwota_kredytu,2)), end='')

kwota_kredytu = pozostala_kwota_kredytu

# Luty 2
inflacja = Luty_2
pozostala_kwota_kredytu = (1 + (inflacja + wysokosc_oprocentowania) / 1200) * kwota_kredytu - wysokosc_raty

print(tekst.format(round(pozostala_kwota_kredytu, 2), round(kwota_kredytu - pozostala_kwota_kredytu,2)), end='')

kwota_kredytu = pozostala_kwota_kredytu

# Marzec 2
inflacja = Marzec_2
pozostala_kwota_kredytu = (1 + (inflacja + wysokosc_oprocentowania) / 1200) * kwota_kredytu - wysokosc_raty

print(tekst.format(round(pozostala_kwota_kredytu, 2), round(kwota_kredytu - pozostala_kwota_kredytu,2)), end='')

kwota_kredytu = pozostala_kwota_kredytu

# Kwiecien 2
inflacja = Kwiecien_2
pozostala_kwota_kredytu = (1 + (inflacja + wysokosc_oprocentowania) / 1200) * kwota_kredytu - wysokosc_raty

print(tekst.format(round(pozostala_kwota_kredytu, 2), round(kwota_kredytu - pozostala_kwota_kredytu,2)), end='')

kwota_kredytu = pozostala_kwota_kredytu

# Maj 2
inflacja = Maj_2
pozostala_kwota_kredytu = (1 + (inflacja + wysokosc_oprocentowania) / 1200) * kwota_kredytu - wysokosc_raty

print(tekst.format(round(pozostala_kwota_kredytu, 2), round(kwota_kredytu - pozostala_kwota_kredytu,2)), end='')

kwota_kredytu = pozostala_kwota_kredytu

# Czerwiec 2
inflacja = Czerwiec_2
pozostala_kwota_kredytu = (1 + (inflacja + wysokosc_oprocentowania) / 1200) * kwota_kredytu - wysokosc_raty

print(tekst.format(round(pozostala_kwota_kredytu, 2), round(kwota_kredytu - pozostala_kwota_kredytu,2)), end='')

kwota_kredytu = pozostala_kwota_kredytu

# Lipiec 2
inflacja = Lipiec_2
pozostala_kwota_kredytu = (1 + (inflacja + wysokosc_oprocentowania) / 1200) * kwota_kredytu - wysokosc_raty

print(tekst.format(round(pozostala_kwota_kredytu, 2), round(kwota_kredytu - pozostala_kwota_kredytu,2)), end='')

kwota_kredytu = pozostala_kwota_kredytu

# Sierpien 2
inflacja = Sierpnien_2
pozostala_kwota_kredytu = (1 + (inflacja + wysokosc_oprocentowania) / 1200) * kwota_kredytu - wysokosc_raty

print(tekst.format(round(pozostala_kwota_kredytu, 2), round(kwota_kredytu - pozostala_kwota_kredytu,2)), end='')

kwota_kredytu = pozostala_kwota_kredytu

# Wrzesien 2
inflacja = Wrzesien_2
pozostala_kwota_kredytu = (1 + (inflacja + wysokosc_oprocentowania) / 1200) * kwota_kredytu - wysokosc_raty

print(tekst.format(round(pozostala_kwota_kredytu, 2), round(kwota_kredytu - pozostala_kwota_kredytu,2)), end='')

kwota_kredytu = pozostala_kwota_kredytu

# Pazdziernik 2
inflacja = Pazdziernik_2
pozostala_kwota_kredytu = (1 + (inflacja + wysokosc_oprocentowania) / 1200) * kwota_kredytu - wysokosc_raty

print(tekst.format(round(pozostala_kwota_kredytu, 2), round(kwota_kredytu - pozostala_kwota_kredytu,2)), end='')

kwota_kredytu = pozostala_kwota_kredytu

# Listopad 2
inflacja = Listopad_2
pozostala_kwota_kredytu = (1 + (inflacja + wysokosc_oprocentowania) / 1200) * kwota_kredytu - wysokosc_raty

print(tekst.format(round(pozostala_kwota_kredytu, 2), round(kwota_kredytu - pozostala_kwota_kredytu,2)), end='')

kwota_kredytu = pozostala_kwota_kredytu

# Grudzien 2
inflacja = Grudzien_2
pozostala_kwota_kredytu = (1 + (inflacja + wysokosc_oprocentowania) / 1200) * kwota_kredytu - wysokosc_raty

print(tekst.format(round(pozostala_kwota_kredytu, 2), round(kwota_kredytu - pozostala_kwota_kredytu,2)))

kwota_kredytu = pozostala_kwota_kredytu