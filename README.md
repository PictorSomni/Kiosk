Everything's works
A fully operationnal kiosk to select photos after a photoshoot.
You can set options in the CONSTANT.py like sizes and prices.
Everything is generated based on what you put in it.

You open a FOLDER (not a specific file !) and it will load images and generate cells accordingly.

You select a print size on the left then, on each cell, you can add or subtract the number of prints you want the purchase.

The price at the top (next to the logo) will change based on the prices you've set in the CONSTANT.py.

When you validate your order, a text file will be added to the folder conbtaining your photos, listing the selection ordered by size. The price is calculated at the bottom.

This text file is in append mode so you can make several orders in the same folder.
You can copy the photo selection by uncomment lines 350 to 352 but in my case the customers selects their photos before i photoshop them so i prefer not to copy anything.

The UI in optimized for touchscreens. ;)
