# Hinting for Variable (and static) Fonts

## Questions for Micah Stupak-Hahn, Nov 27, 2018

(Most of these were answered and are in a Google Docs document, and I need to port this to an open area).

### What hinting process do you currently recommend for a VF? Do you expect this to change soon?

(From Marc) TTFAutohint

### I assume I can ignore FontBakery tests `062` (GASP) & `072` (PREP) in a VF. Is this correct?

[🔥 FAIL: Is 'gasp' table set to optimize rendering?](https://github.com/googlefonts/fontbakery/search?q=com.google.fonts/check/062)

[🔥 FAIL: Font enables smart dropout control in "prep" table instructions?](https://github.com/googlefonts/fontbakery/search?q=com.google.fonts/check/072)


Micah: “prep table is important; gasp less so. gasp is important for small text faces, I think, but less so with the decrease in multiple renderers out there.”

(Observation from Stephen: if the PREP table is missing, autohint probably didn’t work)


### Should I run `gftools fix-nonhinting` script, or skip this? I've heard it's only for display fonts...

### Is it better to export static fonts from GlyphsApp, or via FontMake w/ the `--autohint` flag?

Autohint

### How might I check whether I've done autohinting properly?