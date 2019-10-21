# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose

class GildedRoseTest(unittest.TestCase):
    def test_foo(self):
        items = [Item("foo", 0, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.check_if_item_should_be_updated()
        self.assertEquals("foo", items[0].name)
 
    def test_if_bree_is_updated_properly(self):
        items = [Item("Aged Brie", 20, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.check_if_item_should_be_updated()
        self.assertEquals(21, items[0].quality)
    
    def test_if_bree_is_updated_properly_when_quality_is_50(self):
        items = [Item("Aged Brie", 20, 50)]
        gilded_rose = GildedRose(items)
        gilded_rose.check_if_item_should_be_updated()
        self.assertEquals(50, items[0].quality)
 
    def test_if_bree_is_updated_properly(self):
        items = [Item("Aged Brie", 20, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.check_if_item_should_be_updated()
        self.assertEquals(21, items[0].quality)
    
    def test_if_bree_is_backstage_passes_are_ok_when_sell_in_is_more_than_10(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 11, 30)]
        gilded_rose = GildedRose(items)
        gilded_rose.check_if_item_should_be_updated()
        self.assertEquals(31, items[0].quality)

    def test_if_bree_is_backstage_passes_are_ok_when_sell_in_is_more_than_5(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 8, 30)]
        gilded_rose = GildedRose(items)
        gilded_rose.check_if_item_should_be_updated()
        self.assertEquals(32, items[0].quality)
    
    def test_if_bree_is_backstage_passes_are_ok_when_sell_in_is_less_than_5(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 2, 30)]
        gilded_rose = GildedRose(items)
        gilded_rose.check_if_item_should_be_updated()
        self.assertEquals(33, items[0].quality)
    
    def test_if_bree_is_backstage_passes_are_ok_when_sell_in_is_equal_0(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 0, 30)]
        gilded_rose = GildedRose(items)
        gilded_rose.check_if_item_should_be_updated()
        self.assertEquals(0, items[0].quality)

if __name__ == '__main__':
    unittest.main()
