# Hinting for Variable (and static) Fonts

## Questions for Micah Stupak-Hahn, Nov 27, 2018

### What hinting process do you currently recommend for a VF? Do you expect this to change soon?

### I assume I can ignore FontBakery tests `062` (GASP) & `072` (PREP) in a VF. Is this correct?

[🔥 FAIL: Is 'gasp' table set to optimize rendering?](https://github.com/googlefonts/fontbakery/search?q=com.google.fonts/check/062)

[🔥 FAIL: Font enables smart dropout control in "prep" table instructions?](https://github.com/googlefonts/fontbakery/search?q=com.google.fonts/check/072)

### Should I run `gftools fix-nonhinting` script, or skip this? I've heard it's only for display fonts...

### Is it better to export static fonts from GlyphsApp, or via FontMake w/ the `--autohint` flag?

### How might I check whether I've done autohinting properly?