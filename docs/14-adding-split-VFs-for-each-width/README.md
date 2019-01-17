# Adding a "split" Variable Font for each width family

Initially, Google Fonts will launch variable fonts (VFs) with just the weight axis enabled. This means that for a type family like Encode Sans, in which there are 2 axes of weight and width, the first VFs will be continue to be separated into primary width-based families, but they can each have variable weight axis.

Initially, I was asked to simply make a weight-axis VF for Encode Sans normal, in addition to the full, 2-axis VF. However, it makes sense to extend my work just a bit further and make a VF for Condensed, SemiCondensed, SemiExpanded, and Expanded. It will increase the number of VFs Google can launch the feature with, and it will be simpler for users to understand that any Encode Sans font is at least partially variable. 

## Process

I was using a Python script to split the normal-width instances into a new GlyphsApp source file, then exporting from there. 

So, I extended this script slightly, in order to separate the primary GlyphsApp source into *five* width-separated sources. 

Next, I will extend my split VF build script to process all five sources, rather than just one.

## Getting it right

The splitting update didn't immediately work ([as of Jan 16](https://github.com/thundernixon/Encode-Sans/blob/3d0bfd3639ebc04be6aee8a9cbedaaf993bba5e6/sources/scripts/helpers/split-encode-vf-glyphs_script.py)). It was splitting the single source into five, as intended, but messed up a few pieces of metadata, which Marc helped to point out. 

Instances:
- Kept their "Width" setting, so Condensed styles were still called "Condensed" when they need to be "Medium (Normal)." This put an unintended width axis makes it into the output fonts.
- Hung onto their Custom Parameter of "familyName." This is not needed, because the script updates the main Family Name of the generated GlyphsApp font.

Masters:
- (In the Condensed and Expanded sources) retained their original master names of Light Condensed, Bold Condensed, Light Expanded, and Bold Expanded. They need to be simply `Light` and `Bold`.

The font should also have only "Weight" in its Custom Param "Axes."

Finally, the "Expanded" masters weren't being smart enough in their trimming, so I had to improve that.

Result: split VFs are now generating well, as far as I can tell.

[Current splitter script, as of Jan 17 ](https://github.com/thundernixon/Encode-Sans/blob/281128d1e74013799e4b08676f5dd8b64fd6595e/sources/scripts/helpers/split-encode-vf-glyphs_script.py)

