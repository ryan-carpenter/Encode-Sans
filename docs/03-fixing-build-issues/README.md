# Fixing Build Issues

Problems:

- Width values aren't being scaled to 70–130, but are rather outputting as 0–1000
- "normalized" weights are getting out of sorts – the ExtraBold is getting a value of `234` while the Black gets a value of `232`
  - the "untouched" source file appears to have been edited to have a rectangular designspace.
  - because the `fix-designspace.py` file relied on correctly-set min and max `wght` value variables, it was morphing values that were already morphed.

```
# Bold Extended and Bold Condensed original values
# TODO: make these read from the file rather than relying on user entry
wghtWideMax = 232.0
wghtCondMax = 193.0
```

Steps

- [x] pull in the previous / original Encode Sans file
- [ ] re-evaluated math being done to instance weight in the `fix-designspace.py` script. This shouldn't cause problems if it gets a GlyphsApp source with correct values ... but it is.
- [ ] Make `fix-designspace.py` detect min and max instance weight values, rather than relying on variables to be manually set
