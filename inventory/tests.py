from django.test import TestCase
from inventory.models import Item

# Create your tests here.
def calculate_quantity_level(item):
    thresholds = [ 0.1, 0.25, 1.0 ]
    percent    = item.quantity / item.max_quantity

    for t in range(len(thresholds)):
        if percent < thresholds[t]: return t

class InventoryTests(TestCase):
    def test_item_quantity_levels(self):
        item = Item( name         = "CUSTOM_ITEM",
                     max_quantity = 50 )

        test_values = [
                    ( 0.01, 0 ), ( 0.09, 0 ),
                    ( 0.11, 1 ), ( 0.24, 1 ),
                    ( 0.26, 2 ), ( 0.99, 2 ),
                ]

        for test in test_values:
            item.quantity = item.max_quantity * test[0]
            qty_level     = calculate_quantity_level(item)
            self.assertEqual(qty_level, test[1])
