# Breaking up VF into width-separated families

Google Fonts will start supporting the variable font "Weight" axis before any others (e.g. Width). So, the total deliverable of Encode Sans will need to be:

- Static fonts, broken into width-based families (matching existing font styles, but with new refinements and slight adjustments from the remapped designspace)
    - Encode Sans Condensed (8 weights)
    - Encode Sans SemiCondensed (8 weights)
    - Encode Sans  (8 weights)
    - Encode Sans Expanded (8 weights)
    - Encode Sans SemiExpanded (8 weights)

- Weight-only variable fonts, broken into width-based families
    - Encode Sans Condensed (Light–Black)
    - Encode Sans SemiCondensed (Light–Black)
    - Encode Sans (Light–Black)
    - Encode Sans Expanded (Light–Black)
    - Encode Sans SemiExpanded (Light–Black)

- 2-axis variable font, with Weight & Width axes
    - Encode Sans  (Light–Black, Condensed–Expanded)

## Process

The good news is, FontMake works with existing GlyphsApp sources to export static fonts as weight-separated families, using the GlyphsApp custom parameter, `familyName`.

FontMake does seem to support breaking a file into separate families during variable font building. So, the most likely process I'll need is to create a temporary GlyphsApp file for each width, then separately export from there.

