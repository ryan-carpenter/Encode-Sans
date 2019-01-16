# Adding a "split" Variable Font for each width family

Initially, Google Fonts will launch variable fonts (VFs) with just the weight axis enabled. This means that for a type family like Encode Sans, in which there are 2 axes of weight and width, the first VFs will be continue to be separated into primary width-based families, but they can each have variable weight axis.

Initially, I was asked to simply make a weight-axis VF for Encode Sans normal, in addition to the full, 2-axis VF. However, it makes sense to extend my work just a bit further and make a VF for Condensed, SemiCondensed, SemiExpanded, and Expanded. It will increase the number of VFs Google can launch the feature with, and it will be simpler for users to understand that any Encode Sans font is at least partially variable. 

## Process

I was using a Python script to split the normal-width instances into a new GlyphsApp source file, then exporting from there. 

So, I extended this script slightly, in order to separate the primary GlyphsApp source into *five* width-separated sources. 

Next, I will extend my split VF build script to process all five sources, rather than just one.