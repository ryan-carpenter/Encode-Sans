# Making a pull request to the google/fonts master repo


## To Dos

- [x] clean `master` branch of [Encode Sans repo](https://github.com/thundernixon/Encode-Sans) to match general format of [Dosis VF](https://github.com/eliheuer/dosis-vf)
    - [x] move working state into `wip` branch
    - [x] move static & latest dist fonts into `fonts/` folder
    - [x] move `scripts` and `requirements` into `sources/` folder


- [x] Make PR
    - [x] update fork of google/fonts repo and make `encode-sans` branch
    - [x] add encode sans files, sorted
    - [x] mark PR as "WIP"
    - [x] show latest fontbakery report
    - [x] give known remaining to-do items (search through these docs for `- [ ]`, for starters)
    - [x] PR!

## Known remaining to-do items (include in PR)
- [ ] Check that filenames and folder sorting is as expected (Ask)
- [x] update `FONTLOG.txt`
  - [x] added with `sources/scripts/helpers/add-fontlog.py`
- [x] update `METADATA.pb` for variable font
- [ ] Apply autohinting to VFs
- [ ] Test hinting in new statics
- [x] Check that font naming/sorting is how others expect in desktop apps
- [x] Methodical Red Arrows check. 
    - [x] Ask: are *any* inflected curves okay (e.g. in accent marks like `/tilde`?)
- [ ] Extra proof kerning for refined glyphs (`/Germandbls`es, `/Oslash`es)
- [ ] Show clear regression/diffing results
- [x] Do I need to fix mark-to-mark positioning? See docs/diffing-against-old-statics
- [x] Upgrade build scripts
    - [x] Make build scripts direct new fonts into `fonts/` directory
    - [x] Add fontbakery checking to static font builds
    - [x] (maybe) streamline split-VF build



## Steps to PR, in more detail

1. Fork repo google/fonts
2. Clone
3. Make a branch for font, e.g. `git checkout -b encode-sans`
4. Be sure to pull in lastest google/fonts `master` branch
    1. `git fetch https://github.com/google/fonts.git` to get
    2. `git reset --hard FETCH_HEAD` to hard reset to fetched head


## FontBakery Checks & Explanations, Full VF

**FAIL: METADATA.pb: check if fonts field only contains unique style:weight pairs.**
- The weights repeat because they exist in different widths
- Presumably, `width` values will be added as GFonts gains support for new axes

**FAIL: Checking file is named canonically.**
- This filename needs some kind of indication that it's a variable font, rather than a static instance "regular".

**FAIL: Font has old ttfautohint applied?**
- I'm using a version of TTFautohint that supports VFs. If there is a newer version of this, I'll add it my my build process!

**FAIL: Checking with ots-sanitize.**
- There's an open issue for this at OTS. It doesn't yet support the latest caret format.

**WARN: Check if each glyph has the recommended amount of contours.**
- It's a variable font, so many glyphs have overlapping contours

**WARN: Name table strings must not contain the string 'Reserved Font Name'.**
- Encode Sans had this from before. Dave said to keep it.

**WARN: Is there kerning info for non-ligated sequences?**
- Kerning exists on other non-ligated sequences, but is not needed on f + i, i + j, j + l

**FAIL: METADATA.pb font.full_name value matches fullname declared on the name table?**
- **FAIL Unmatched fullname in font: TTF has "Encode Sans" while METADATA.pb has "Encode Sans Condensed Thin". [code: mismatch]**
**FAIL: METADATA.pb font.full_name and font.post_script_name fields have equivalent values ?**
**FAIL: METADATA.pb font.filename and font.post_script_name fields have equivalent values?**
- **FAIL METADATA.pb font filename="EncodeSans-VF.ttf" does not match post_script_name="EncodeSans".**
**FAIL: METADATA.pb font.name and font.full_name fields match the values declared on the name table?**
- **FAIL METADATA.pb: Fullname ("Encode Sans Condensed Thin") does not match name table entry "Encode Sans" ! [code: fullname-mismatch]**
**FAIL: Checking OS/2 usWeightClass matches weight specified at METADATA.pb.**
- **FAIL OS/2 usWeightClass (400:"Regular") does not match weight specified at METADATA.pb (100:"Thin").**
**FAIL: METADATA.pb weight matches postScriptName.**
- **FAIL METADATA.pb: Mismatch between postScriptName ("EncodeSans") and weight value (100). The name must be ended with "Thin" or "ThinItalic".**
- That is just the first named instance of the variable font, not the full name of the entire font.

**SKIPS**

**SKIP: Does DESCRIPTION file contain broken links?**
- This must be in the wrong level of the repo, compared to the font...



**SKIP: Font has ttfautohint params?**
- It use TTFautohint VF, which must not be including this

**SKIP: Version number has increased since previous release on Google Fonts?**
**SKIP: Check font has same encoded glyphs as version hosted on fonts.google.com**
- Maybe it can't match the name?

**OS/2, Metadata checks, post.italicAngle, head.macStyle, NAME table entries**
- Skips  because of lack of `Unfulfilled Conditions: style`

**SKIP: FontForge validation outputs error messages?**
- Unfulfilled Conditions: fontforge_check_results

**SKIP: CFF table FontName must match name table ID 6 (PostScript name).**
- not CFF

**SKIP: Monospace font has hhea.advanceWidthMax equal to each glyph's advanceWidth?**
- not monospace

**Skips for slnt, ital, and opsz axes**
- does not have these axes

Look into:
- [ ] Ask Marc: Should I add a prep table (maybe with `fix-autohinting` script?) if TTFautohint VF doesn't add it?
- [ ] FontForge checks (is FF installed correctly?)