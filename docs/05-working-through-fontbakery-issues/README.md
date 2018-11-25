# Working through FontBakery Issues

Some of the FontBakery `FAIL`s and `WARN`s are pretty self-explanatory, so I'll just fix them (e.g. "WARN: Name table strings must not contain the string 'Reserved Font Name'."). Others will take a bit more doing, so I'll document the process here.

## Reserved Font Name

I was at first confused why this continued to warn me, after changing it in the GlyphsApp source. Turns out, the "Reserved Font Name" line was coming from `scripts/NAMEpatch.xml`.

🎉 PASS

## Caret positions for ligatures

> ⚠️ WARN: Are there caret positions declared for every ligature?

Using [my simple glyphs script](https://github.com/thundernixon/glyphs_scripts/blob/master/add-caret-anchors.py) to make this a bit faster and more fun.

🎉 PASS

## Kerning non-ligated sequences

> ⚠️ WARN: Is there kerning info for non-ligated sequences?
> com.google.fonts/check/065
> 
> ⚠️ WARN GPOS table lacks kerning info for the following non-ligated sequences:
> 
> f + i
> i + j
> j + l
> [code: lacks-kern-info]

Do they all need kerning? It helps to look at what the ligatures *are* in the design. The `f_j` and `f_i` ligatures have an `f` which has a shorter top "hook," to avoid a clash between the `f` and the `i`/`j` dot. So, the `/f/i` combination understandably uses positive kerning to also prevent a clash. I matched the `/f/j` combination to it.

![](assets/2018-11-23-12-51-27.png)

I'm confused why FontBakery is advising me to check `j + l` ... I can't find that ligature anywhere in this typeface, and it isn't a very logical ligature for these shapes, anyway. There *is* an `l_j` ligature (for some reason...), but this seems to be somehow getting reverse by FontBakery.

🎉 (I've fixed what is worth fixing.)


## OTS Sanitize

> * 🔥 FAIL: ots-sanitize returned an error code (1). Output follows:
> 
> ERROR: GDEF: bad caret value format: 3
> ERROR: GDEF: Invalid ligature caret list
> ERROR: GDEF: Failed to parse table
> Failed to sanitize file!

- [x] find where the caret value is coming from ... maybe there's an accidental duplication of a `caret_1` in a ligature? Start by looking at the GDEF table.

On line 170 of [ots/src/gdef.cc](https://github.com/khaledhosny/ots/blob/63f8d7e47cf9ab75a25b2b63bb359349fef050fa/src/gdef.cc), there is the following comment:

>       // TODO(bashi): We only support caret value format 1 and 2 for now
>       // because there are no fonts which contain caret value format 3
>       // as far as we investigated.

However, in the TTX of my variable font, I have `<CaretValue index="0" Format="3">` for each caret description in the `<LigCaretList>` table. 

On [MS Docs for the GDEF table](https://docs.microsoft.com/en-us/typography/opentype/otspec140/gdef#ligature-caret-list-table), it says:

> One format represents values in design units only, another fine-tunes a value based on a designated contour point, and the third uses a Device table to adjust values at specific font sizes.

I am simply using the built in GlyphsApp recommendation for inserting caret positions, as described on page 27 of the [Glyphs Handbook](https://glyphsapp.com/downloads/handbook/Glyphs-Handbook-2.3.pdf). So, I'm guessing that if my exported variable font is getting `format 3` either from GlyphsApp or from FontMake's VF exporting.

I have filed this issue at https://github.com/khaledhosny/ots/issues/178 with a few more details.

## Family Naming

> ⚠️ WARN: Combined length of family and style must not exceed 20 characters.

Currently, the longest instance name I can find is:

```
>>> len("Encode Sans ExtraLight SemiCondensed")
36
```

...so, this (and other instances) will definitely require attention in the static instance export.

However, as described in [FontBakery Issue 2179](https://github.com/googlefonts/fontbakery/issues/2179), it is `nameID 4` and `nameID 6` that need to be short enough to avoid issues. For this variable font, `nameID 4`, `Encode Sans Thin Condensed`, clocks in at 26 characters. Because the limits I've been able to find documentation of are between 29 and 32, this variable font is (almost definitely) fine.

On [a posting in the GlyphsApp forum](https://forum.glyphsapp.com/t/overly-strict-font-name-max-length-recommendation-in-naming-tutorial/10164), @mekkablue says that he has "had errors triggered with combined lengths of names that were just above 20" on Windows, though the screenshot provided has a font name with a length of 47 characters ("ImpossibleFamilynameFont-WithAVeryLongStyleName"). I can't help but wondering whether his experience with install failure have had other issues, besides font name length.

I'll test install this on Windows to see whether 26 characters causes any issue.

- [ ] Test with virtual machine, windows, and Mac Office
- [ ] Be sure to keep exported static instance names below 29 characters

## Keeping static instance exports below 29 characters

It's possible to add `preferredSubfamilyName` custom parameters to a GlyphsApp source. To avoid future potential installation errors, I'll make a script to add in params that shorten names.

- [x] first, export static instances with FontMake to check whether this is taken care of already
- [ ] if FontMake doesn't do it, make a script to add your own

A static instance export of Encode doesn't abbreviate naming. For instance, Condensed ExtraLight exports with:

```
<namerecord nameID="4" platformID="3" platEncID="1" langID="0x409">
      Encode Sans Condensed ExtraLight
</namerecord>
```

### Making a script to shorten names for static instances

`nameID4` must keep below 27–29 characters. There are a couple of ways this might be done:

- Writing a script to add "Preferred Subfamily Names" custom parameter to instances in the GlyphsApp source
- Writing a build script to TTX built fonts, update the names, and then TTX again

I'll start with a test of the Glyphs script, because it has fewer open questions. Also, while it does change the source file, it's still "non-destructive" in the sense that it doesn't alter the source in a way that is hard to reverse.

**Test 1: seeing whether "Preferred Subfamily Names" custom parameters in a GlyphsApp source are picked up by FontMake.**

I've changed the custom parameters manually:

![](assets/2018-11-24-17-15-59.png)

Then exported the specific instance:

```
fontmake -g sources/Encode-Sans.glyphs --output ttf --interpolate "Encode Sans SemiCond XBold" --autohint
```

...But actually, this doesn't seem to export to the designspace or eventual font generated by FontMake, when checked with TTX. It seems that it might be necessary to fix this in post, after all. This will allow me to target the specific XML elements I want to change (nameIDs 4 and 6), and change only those – leaving in-tact the names that won't cause trouble later.


**Test 2: using xmlStarlet to update name IDs 4 & 6, swapping out key words for abbreviations**

| Width         | Abbreviation |
| ------------- | ------------ |
| Condensed     | Cond         |
| SemiCondensed | SemiCond     |
| Expanded      | Expd         |
| SemiExpanded  | SemiExpd     |

| Weight      | Abbreviation |
| ----------- | ------------ |
| ExtraLight  | ExLght       |
| Light       | Lght         |
| Regular (?) | Reg          |
| Medium      | Med          |
| SemiBold    | SemiBld      |
| Bold        | Bold         |
| ExtraBold   | ExBold       |
| Black (?)   | Blck         |


```Python
>>> len("Encode Sans SemiExpd SemiBld")
28
```

Script Logic
- make a dictionary for abbreviations
- for file of directory
    - ttx file
    - make variables: use xmlStarlet to find inner text of `nameID="4"` and `nameID="6"`
    - If words in the inner text are keys of the dict, update variables to associated values
    - use xmlStarlet to update those values


Print value of nameID 4
`xml sel -t -v "//*/namerecord[@nameID='4']" autohinted/instance_ttf/EncodeSansCondensed-ExtraLight.ttx`

and nameID 6...
`xml sel -t -v "//*/namerecord[@nameID='6']" autohinted/instance_ttf/EncodeSansCondensed-ExtraLight.ttx`

EncodeSansCond-ExLght
`xml ed -u "//*/namerecord[@nameID='6']" -v EncodeSansCond-ExLght autohinted/instance_ttf/EncodeSansCondensed-ExtraLight.ttx`


Edit value with this format:
`xml ed -u "/xml/table/rec[@id=1]/numField" -v 0 FILE/PATH/HERE`

To keep line breaks, you can actually just use them in the command:
```
xml ed -u "//*/namerecord[@nameID='6']" -v "
      ${updatedNameID6}
    " autohinted/instance_ttf/EncodeSansCondensed-ExtraLight.ttx > autohinted/instance_ttf/update.ttx
```