# QA methods outside of FontBakery and GFRegression

Approaches:
- Use FontLab6's "FontAudit," which checks for issues in glyph paths
- Use the GlyphsApp plugin *Red Arrows* to check for issues in glyph paths

## FontLab?

I've been asked to look into additional QA testing in FontLab, so I've done a bit of digging.

So far as I can tell, the only built-in QA testing in FontLab is "FontAudit," a tool somewhat similar to the Red Arrows plugins from GlyphsApp and RoboFont.

[I asked on the FontLab forum](https://forum.fontlab.com/fontlab-vi/are-there-qa-checks-besides-fontaudit/) whether there are additional QA-testing tools. It sounds like [FontQA](http://www.fontqa.com/) is a tool that can be useful, though according to Luc(as) de Groot, this works in FontLab5.

