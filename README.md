# Zaawansowane Języki Programowania
| Travis CI Status | Codacy |
|:----:|:----:|
|[![Build Status](https://travis-ci.com/lzielezinska/advanced-programing-languages.svg?branch=master)](https://travis-ci.org/lzielezinska/advanced-programing-languages) | [![Codacy Badge](https://api.codacy.com/project/badge/Grade/362593fea2904e0383bdf71efbd44e3d)](https://www.codacy.com/manual/lzielezinska/advanced-programing-languages?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=lzielezinska/advanced-programing-languages&amp;utm_campaign=Badge_Grade)|

## Przebieg pracy
### Testy
Napisanie testów:
1. Sprawdzających czy wartość produktu zmienia się w prawidłowy sposób.
2. Sprawdzająych czy metoda update nie nadaje przedmiotom wartości z poza zakresu od 0 do 50.

Do pisania testów użyłam pythonowej biblioteki do testów jednodtkowych  `unitest`

Wywołanie testów:
Testy należy wywołać z katalogu "GildedRose-Refactoring-Kata" za pomocą komendy
```
python3 test_gilded_rose -v
```
### Refaktoryzacja metody update_quality()

Metoda `update_quality()` iteruje po tablicy, której elementami są obiekty klasy Item.
Jeżeli `item.quality` jest mniejsza od 0 lub większa od 50 metoda zgłasza wyjątek, jeżeli wartość `item.quality` quality jest prawidłowa zostaje wywołana metoda `update_quality_of_specialized_item`.
```python
def update_quality(self):
    for item in self.items:
        if item.quality < 0 or item.quality > 50:
            raise ValueError(item.name + str(item.quality) + "Item quality must be in a range beetween 0 and 50!")

        item.sell_in -= 1 
        self.update_quality_of_specialized_item(item)
```
Zadaniem metody `update_quality_of_specialized_item` jest rozpoznanie przedmiotu oraz wywołanie dedykowanej dla niego metody poprawijącej wartość konkretnego przedmiotu.
```python
    def update_quality_of_specialized_item(self, item):
        if item.name == "Backstage passes to a TAFKAL80ETC concert":
            self.update_quality_of_backstage_passes(item)
        elif item.name == "Aged Brie":
            self.update_quality_of_aged_bree(item)
        elif item.name == "Sulfuras, Hand of Ragnaros":
            self.update_quality_of_sulfurus(item)
        elif item.name == "Conjured Mana Cake":
            self.update_quality_of_conjured_item(item)
        else:
            self.update_quality_of_normal_item(item)
```
Dla każedego rodzaju przedmiotu stworzyłam odrębną funckję (nawet w przypadku gdy wykonywana jest dokładnie taka sama operacja).
Zapewnia to łatwość wprowadzania zamian oraz dodawania nowych obiektów o specjalnych właściwościach. To rozwiązanie umożliwia również dalszą refactoryzację polegającą na stworzeniu odrębnej klasy i przeniesieniu do niej metody update.
Przykład metody obsugującej "Conjured Mana Cake":

```python
def update_quality_of_conjured_item(self, item):
    if item.quality <= 2:
        item.quality == 0
    else:
        item.quality -= 2
```

Jak widać na powyższym przykładzie w każdej metodzie przed dokonaniem aktualizacji sprawdzam czy nie spowoduje ona nadaniu item.quality nieodpowiedniej wartości.

### Podsumowanie refactoryzacji

