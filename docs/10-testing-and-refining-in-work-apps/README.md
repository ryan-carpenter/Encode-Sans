# Testing in software and refining fonts

In MS Word and Apple Pages Font instances were arranging first by weight, then by width. This was a very unhelpful arrangement. So, I'm seeing whether changing the NAME table patch might correct this. I'm switching names from a format of `ExtraLight SemiCondensed` to `SemiCondensed ExtraLight`. This might also make sense to change in the GlyphsApp source. 

Changing just the font's NAME table does help organize things better in Apple Pages, but doesn't work how I'd like in MS Word.

Encode Sans VF in Apple Pages:

![](assets/2018-11-28-17-16-17.png)

Encode Sans VF in Microsoft Word:

![](assets/2018-11-28-17-19-38.png)

## Making names better

Based on a TTX of Bahnschrift, an open-source font packaged with Windows, the nameID 4 and 6 doesn't need to include the default weight name. Bahnschrift is simple `Bahnschrift` for both IDs. Additionally, unlike the NAME patch I was using, the `platform="1"` elements in the `<name>` table don't have every style name declared (though they are for `platform="3"`/Mac). These changes may help it to show up in font menus in a more-straightforward way.

.....aaaand they actually do make a difference! The fonts are now showing up in MS Word with the ordering I want, as well as all the styles I expect. 

![](assets/2018-11-28-17-52-19.png)

## Style Linking

One strange thing about Encode Sans in MS Word is that the Regular–Bold style linking works ... but the line height jumps substantially when the Bold style is used.

![](assets/ms-word-regular_bold.gif)

This doesn't happen in Bahnschrift:

![](assets/ms-word-bahnschrift-regular_bold.gif)


- [ ] TODO: check [Saira](https://github.com/m4rc1e/Saira-1/tree/master/SairaGF/sources) as a possible good weight + width VF reference.


## Name table improvements

I'm using Bahnschrift and the MS Typography docs to upgrade my `NAMEpatch.xml` file slightly.
- I've changed `nameID 2` to "Regular," as this is subbed in for `nameID 17`: "Preferred Subfamily. No name string present, since it is the same as name ID 2 (Font Subfamily name)". This should hopefully make the Regular named instance be used as the default in some apps, rather than the Condensed Thin style.
- I'm changing `nameID 2` from `2.000;GOOG;EncodeSans-ThinCondensed` to `2.000;GOOG;EncodeSans`
- I've changed `nameID`s 4 & 6 to simply `Encode Sans`, from `Encode Sans Condensed Thin`, so it avoids name-length issues and hopefully shows up more simply in font menus
- I've also added specific sample text to `nameID` 19, for display in font-viewing apps.




- [ ] TODO: Check if name patches need to exist for weight-split / linked variable fonts

## Sorting on Mac

Currently, the named instance "Regular" is the default style in macOS pages (good) ... but it's also the first to show up in macOS Pages font menu, when I would expect "Condensed Thin" to be the first to appear, and "Thin" itself doesn't show up until the last place of the menu (bad).

![](assets/2018-11-29-16-20-17.png)