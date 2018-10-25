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

1. Installing the latest osx release from https://github.com/HinTak/Font-Validator/releases, then unzip
2. Change the unzipped binary's permissions, `chmod 755 FontValidator`
3. Moving the downloaded file into the same directory I use for my Python environment (for me, that's just `~/Environments/gfonts/bin`).

~~Find `general.py` in the FontBakery code, then find lines 160–166. Change:

1. Change `FontValidator.exe` to `FontValidator`
2. Change `+` to `-no-raster-tests`

When done, the code this will look like this:

```
  try:
    import subprocess
    fval_cmd = [
       "FontValidator", "-file", font, "-all-tables",
       "-report-in-font-dir", "-no-raster-tests"
    ]
    subprocess.check_output(fval_cmd, stderr=subprocess.STDOUT)
```
~~