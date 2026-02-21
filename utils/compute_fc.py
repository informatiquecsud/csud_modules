import micropip
await micropip.install("https://raw.githubusercontent.com/informatiquecsud/csud_modules/refs/heads/main/dist/csud-0.1.0-py3-none-any.whl")

from csud.crypto import *

from prepared_fr_texts import *
from prepared_de_texts import *

print("Français")
print("--------")
print("Misérables I:", friedman_characteristic(miserables_tome_1))
print("Misérables III:", friedman_characteristic(miserables_tome_3))
print("Misérables V:", friedman_characteristic(miserables_tome_5))
print("Trois Mousquetaires:", friedman_characteristic(trois_mousquetaires))

print()
print("Allemand")
print("--------")
print("Faust de Goethe: ", friedman_characteristic(faust_1))
print("Also sprach Zaratustra: ", friedman_characteristic(also_sprach_zarathustra))
