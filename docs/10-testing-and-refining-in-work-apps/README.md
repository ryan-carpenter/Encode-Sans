# Testing in software and refining fonts

In MS Word and Apple Pages Font instances were arranging first by weight, then by width. This was a very unhelpful arrangement. So, I'm seeing whether changing the NAME table patch might correct this. I'm switching names from a format of `ExtraLight SemiCondensed` to `SemiCondensed ExtraLight`. This might also make sense to change in the GlyphsApp source. 

Changing just the font's NAME table does help organize things better in Apple Pages, but doesn't work how I'd like in MS Word.

Encode Sans VF in Apple Pages:

![](assets/2018-11-28-17-16-17.png)

Encode Sans VF in Microsoft Word:

![](assets/2018-11-28-17-19-38.png)

## Making names better

Based on a TTX of Bahnschrift, an open-source font packaged with Windows, the nameID 4 and 6 doesn't need to include the default weight name. Bahnschrift is simplye `Bahnschrift` for both IDs, which may help it to show up in font menus in a more-straightforward way.