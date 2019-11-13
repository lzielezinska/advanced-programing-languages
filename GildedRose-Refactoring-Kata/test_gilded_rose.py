# -*- coding: utf-8 -*-
import unittest

from gilded_rose import GildedRose
from item import Item

class GildedRoseTest(unittest.TestCase):
 
    def test_if_bree_is_updated_properly(self):
        items = [Item("Aged Brie", 20, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(21, items[0].quality)
    
    def test_if_bree_is_updated_properly_when_quality_is_50(self):
        items = [Item("Aged Brie", 20, 50)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(50, items[0].quality)
    
    def test_if_bree_is_backstage_passes_are_ok_when_sell_in_is_more_than_10(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 11, 30)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(31, items[0].quality)

    def test_if_bree_is_backstage_passes_are_ok_when_sell_in_is_more_than_5(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 8, 30)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(32, items[0].quality)
    
    def test_if_bree_is_backstage_passes_are_ok_when_sell_in_is_less_than_5(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 2, 30)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(33, items[0].quality)
    
    def test_if_bree_is_backstage_passes_are_ok_when_sell_in_is_equal_0(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 0, 30)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(0, items[0].quality)

    def test_if_conjured_item_is_updated_properly(self):
        items = [Item("Conjured Mana Cake", 2, 30)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(28, items[0].quality)

    def test_if_conjured_item_is_updated_properly_when_quality_equas_1(self):
        items = [Item("Conjured Mana Cake", 2, 1)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(1, items[0].quality)
    
    def test_if_normal_item_is_updated_properly(self):
        items = [Item("Elixir of the Mongoose", 10, 30)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(29, items[0].quality)

    def test_if_normal_item_is_updated_properly_when_sell_in_less_than_0(self):
        items = [Item("Elixir of the Mongoose", 0, 30)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(28, items[0].quality)

if __name__ == '__main__':
    unittest.main()
