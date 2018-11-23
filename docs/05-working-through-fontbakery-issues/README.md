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

- [ ] first, export static instances with FontMake to check whether this is taken care of already
- [ ] if FontMake doesn't do it, make a script to add your own