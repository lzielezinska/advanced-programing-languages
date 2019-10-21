# -*- coding: utf-8 -*-
class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)


class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def check_if_item_should_be_updated(self):
        for item in self.items:
            item.sell_in -=1 
            self.update_quality(item)
    
    def update_quality(self, item):
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

    def update_quality_of_backstage_passes(self, item):
        if item.quality >=50:
            pass
        elif item.sell_in > 9:
            item.quality+=1
        elif item.sell_in in range(5,9):
            item.quality+=2
        elif item.sell_in in range(1,5):
            item.quality+=3
        elif item.sell_in <= 0:
            item.quality=0

    def update_quality_of_aged_bree(self, item):
        if item.quality >=50:
            pass
        else:
            item.quality +=1
    
    def update_quality_of_conjured_item(self, item):
        if item.quality < 2:
            pass
        else:
            item.quality -=2

    def update_quality_of_sulfurus(self, item):
        pass

    def update_quality_of_normal_item(self, item):
        if item.quality < 1:
            pass
        elif item.sell_in > 0:
            item.quality -= 1
        else:
            item.quality-=2

