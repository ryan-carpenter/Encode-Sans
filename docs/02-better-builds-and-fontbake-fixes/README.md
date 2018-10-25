# Font Baking Encode Sans

After getting past the "weight cliff" issue (see previous doc), I've had more work to do in getting past errors and failures flagged by FontBakery.

## Font-mastering techniques I've found useful

### Using a build script

I have had quite a bit of success in correcting issues by using [a build script](https://github.com/thundernixon/Encode-Sans/blob/2e5e25f462172b3f2e8b7cc03738a8a4888dc5a4/scripts/build.sh) based on a shell script inherited from [@mjlagattuta](https://github.com/mjlagattuta) (NOTE: currently only works in my Python3 environment). This script strings together useful functionality:

- the GlyphsApp source is temporarily duplicated and get its designspace morphed (to fix the weight cliff issue)
- the FontMake variable font build is triggered
- the generated designspace is be either kept or discarded
- gftools is be run to fix various metadata errors
- ttx is used to generate an XML version of the VF so that
  - the STAT table is replaced with a hand-edited STATpatch.xml
  - the NAME table is replaced with a hand-edited NAMEpatch.xml
- ttx is used again to compile back to TTF
- the built fonts is moved into a timestamped folder
- FontBakery is run

I have kept a log of FontBakery runs as [a GitHub issue](https://github.com/thundernixon/Encode-Sans/issues/1).

### Setting common weight values across widths

```
FAIL: The variable font 'wght' (Weight) axis coordinate must be 400 on the 'Regular' instance.
```

```
FAIL: The variable font 'wght' (Weight) axis coordinate must be 700 on the 'Bold' instance.
```

To fix: Set the instances to a common weight value in [the script which morphs the designspace to be rectangular](https://github.com/thundernixon/Encode-Sans/blob/2e5e25f462172b3f2e8b7cc03738a8a4888dc5a4/scripts/fix-designspace.py). Before, the instances were slightly off. This meant that something with a weight of 85 would map to 700, but something with a weight of 86 (as was the case in the SemiCondensed regular instance) would map to 403.7037.

### Installing fontvalidator and changing how FontBakery handles it

```
💔 ERROR: Checking with Microsoft Font Validator.
- com.google.fonts/check/037
- 💔 ERROR Mono runtime and/or Microsoft Font Validator are not available!
- 💔 ERROR Failed with FileNotFoundError: [Errno 2] No such file or directory: 'FontValidator.exe': 'FontValidator.exe'
```

This probably doesn't have a final solution, because fontvalidator seems to be undergoing some changes. However, I've gotten past this error and received QA from Font Validator by:

1. Installing the latest osX release from https://github.com/HinTak/Font-Validator/releases, then unzip
2. Change the unzipped binary's permissions, `chmod 755 FontValidator`
3. Moving the downloaded file into the same directory I use for my Python environment (for me, that's just `~/Environments/gfonts/bin`).

~~Find `general.py` in the FontBakery code, then find lines 160–166. Change:~~

~~1. Change `FontValidator.exe` to `FontValidator`~~
~~2. Change `+` to `-no-raster-tests`~~

Update: the latest FontBakery just has this working, so now I've simply run `pip3 install --upgrade fontbakery`.

And now, I'm getting a bunch of FontValidator errors reporting! I'll next need to understand which to fix, and which to accept (assuming some might be fine).



### FontVal errors

MS FontVal duplicates errors a lot, because it reports them for every glyph checked. I literally have 11,000+ lines of errors from it, but they boil down to these:

- :fire: **FAIL** MS-FonVal: The version number is neither 0x00010000 nor 0x0001002 DETAILS: 0x00010003

**A ton of these:**

- :fire: **FAIL** MS-FonVal: The device table's DeltaFormat value is invalid DETAILS: LookupList, Lookup[0], SubTable[0](PairPos, fmt 1), PairSet[0], PairValueRecord[0], Value1, XAdvDeviceTable, DeltaFormat = 32768- 
* :fire: **FAIL** MS-FonVal: Intersecting contours DETAILS: Glyph index 1

* :fire: **FAIL** MS-FonVal: The Mac PostScript string does not match the Microsoft PostScript string DETAILS: mac postscript = EncodeSans-ThinCondensed, MS postscript = EncodeSans-Regular
* :information_source: **INFO** Microsoft Font Validator returned an error code. Output follows :

- :information_source: **INFO** MS-FonVal: The MarkSetCount of the GDEF table DETAILS: MarkGlyphSetsDef: MarkSetCount=3

- :information_source: **INFO** MS-FonVal: Not an OpenType table, contents not validated

-  :information_source: **INFO** MS-FonVal: Not an OpenType table, contents not validated DETAILS: This table type is defined in the Apple TrueType spec.

**A bunch of these:**

* :information_source: **INFO** MS-FonVal: Unable to perform test due to previously detected errors DETAILS: Glyph index 1 Test: ValidateSimpContMisor 

**Plus:**

- :information_source: **INFO** MS-FonVal: Loca references a zero-length entry in the glyf table DETAILS: Number of glyphs that are empty = 9

- :information_source: **INFO** MS-FonVal: maxSizeOfInstructions via method #1 DETAILS: maxSizeOfInstructions=0, computed from the glyf table

- :information_source: **INFO** MS-FonVal: No string for Typographic Family name (Name ID 16)

- :information_source: **INFO** MS-FonVal: No string for Typographic Subfamily name (Name ID 17)

- :information_source: **INFO** MS-FonVal: The post name has an unexpected value DETAILS: glyph = 1120, char = U+FFFF, name = uni0337

- :information_source: **INFO** MS-FonVal: The post name isn't in uniXXXX or uXXXXX format and there is no Adobe Glyph List entry DETAILS: glyph = 1217, char = U+000D, name = CR

- :information_source: **INFO** MS-FonVal: The post name isn't in uniXXXX or uXXXXX format and there is no Adobe Glyph List entry DETAILS: glyph = 1218, char = U+0000, name = NULL

* :information_source: **INFO** MS-FonVal: Rasterization not selected for validation

