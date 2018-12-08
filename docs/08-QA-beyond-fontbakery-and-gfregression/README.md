# Checking outlines for quality

Approaches:
- Use FontLab6's "FontAudit," which checks for issues in glyph paths
- Use the GlyphsApp plugin *Red Arrows* to check for issues in glyph paths


## Red Arrows

### Inserting inflection points

![](assets/2018-11-30-14-20-53.png)

Even when I do fix it, it has a small version of the issue:

![](assets/2018-11-29-16-27-15.png)


# /oslash issue

Strangely, the `/oslash` component is "reversing" improperly when rendered by Apple Pages or Drawbot (despite other component overlaps being fine, like `/lslash`, `/Hbar`, and even uppercase and smallcap `/Oslash`). The problem is solved if I remove some of the points in the "slash" component.

![](assets/2018-12-07-16-07-39.png)

![](assets/2018-12-07-16-08-56.png)

It is fine in Adobe Illustrator and Acrobat.

It's also fine in MS Word.

![](assets/2018-12-07-16-19-05.png)

It happens to cap `/Oslash`, too, if it has a complex slash, and to `/oslash` even if its slash it in a few pieces:
![](assets/2018-12-07-16-54-38.png)

And if it's simplified:

![](assets/2018-12-07-16-56-06.png)

![](assets/2018-12-07-16-56-52.png)

Apple Pages:
![](assets/2018-12-07-17-12-58.png)

GlyphsApp:
![](assets/2018-12-07-17-13-26.png)

Apple Pages:
![](assets/2018-12-07-17-42-51.png)

GlyphsApp:
![](assets/2018-12-07-17-44-58.png)

Apple Pages:
![](assets/2018-12-07-17-52-21.png)

GlyphsApp:
![](assets/2018-12-07-17-52-39.png)

### Oslash is okay with 5 or fewer nodes on the inside of the slash component

Somehow, 6 or more nodes must confuse the renderer to "think" there is a counter space inside those overlap areas.

Apple Pages:
![](assets/2018-12-07-17-56-59.png)

GlyphsApp:
![](assets/2018-12-07-17-57-21.png)

**Conclusion: decompose part or all of the /oslash, as a hack to make the design work.**