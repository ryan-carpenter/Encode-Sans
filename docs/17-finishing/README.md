# Finishing & PRing to Google Fonts

It's been a long time (more than a year) since this variable font upgrade was started. In that time, Google Fonts has grown a lot in the processes around variable fonts, and the support for them on the front end of fonts.google.com. I have learned a lot myself! So, now it's time to finish this and PR it.

Goals:
- PR as a single variable font, removing the script setup to split fonts by widths in preprocessing (this can just be done with the FontTools Instancer)
- Simplify build. E.g. probably implment designspace fixes directly to primary Glyphs source, and remove that step from build.
- Pass as many FontBakery checks as possible
- Set `name` table as well as possible 
- Set up a proper STAT table with statmake
- Smallcaps separated into a separate family & PR
- Static fonts autohinted and put into `static` subfolder for PR
- fix `notdef` – currently this is not building into the proper `.notdef` glyph


Dz ǅ ǲ Dz


### Smallcap fixes

Problems to fix
- [x] **Add missing .sc glyphs to source** subsetting the `SC` font doesn't work fully, because there are a few component glyphs that don't yet have `.sc` versions, and therefore, the lowercase bases of these end up hanging around in the subset `SC` font. For example, ẗ (uni1E97) is in the font but there is no `.sc` version, so `t` remains in the `SC` font.
  - [x] uni1E97.sc (ẗ)
  - [x] napostrophe.sc (ŉ)
  - [x] uni01F2.sc (ǲ)
  - [x] uni01C5.sc (ǅ)
  - [x] uni01C8.sc (ǈ)
  - [x] uni01CB.sc (ǋ)
  - [x] kgreenlandic.sc (just the normal `k.sc`, but needs a unicode to work)
- [x] **Add arg to SC subsetter script that removes specified glyphs** there are some ligatures like `f_j` and `fi` that should be subset, but aren't currently, because they don't have (and don't need) smallcap versions.
  - [x] `f_i f_j f_l fi fl`


Glyph recipes for missing smallcaps:

```
t.sc+dieresiscomb=uni1E97.sc
n.sc+apostrophemod=napostrophe.sc
D+z.sc=uni01F2.sc
D+zcaron.sc=uni01C5.sc
L+j.sc=uni01C8.sc 
N+j.sc=uni01CB.sc 
k.sc=kgreenlandic.sc
```