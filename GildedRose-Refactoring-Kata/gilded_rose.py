class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            if item.quality < 0 or item.quality > 50:
                raise ValueError(item.name + str(item.quality) + "Item quality must be in a range beetween 0 and 50!")

            item.sell_in -= 1 
            GildedRose.update_quality_of_specialized_item(item)

    @classmethod
    def update_quality_of_specialized_item(cls, item):
        if item.name == "Backstage passes to a TAFKAL80ETC concert":
            GildedRose.update_quality_of_backstage_passes(item)
        elif item.name == "Aged Brie":
            GildedRose.update_quality_of_aged_bree(item)
        elif item.name == "Sulfuras, Hand of Ragnaros":
            GildedRose.update_quality_of_sulfurus(item)
        elif item.name == "Conjured Mana Cake":
            GildedRose.update_quality_of_conjured_item(item)
        else:
            GildedRose.update_quality_of_normal_item(item)

    @classmethod
    def update_quality_of_backstage_passes(cls, item):
        print(item.sell_in)
        if item.quality > 50:
            pass
        elif (item.sell_in > 9) or (item.sell_in in range(5,10) and item.quality == 49 ):
            item.quality += 1
        elif (item.sell_in in range(5,10) and item.quality < 49) or (item.sell_in in range(1,5) and item.quality == 48):
            item.quality += 2
        elif ((item.sell_in in range(1,5)) and (item.quality < 48)):
            item.quality += 3
        elif item.sell_in <= 0:
            item.quality = 0

    @classmethod
    def update_quality_of_aged_bree(cls, item):
        if item.quality >= 50:
            pass
        else:
            item.quality += 1

    @classmethod
    def update_quality_of_conjured_item(cls, item):
        if item.quality <= 2:
            item.quality == 0
        else:
            item.quality -= 2

    @classmethod
    def update_quality_of_sulfurus(cls, item):
        pass

    @classmethod
    def update_quality_of_normal_item(cls, item):
        if item.quality < 1:
            pass
        elif item.sell_in > 0:
            item.quality -= 1
        else:
            item.quality -= 2
