# Making a pull request to the google/fonts master repo


## To Dos

- [x] clean `master` branch of [Encode Sans repo](https://github.com/thundernixon/Encode-Sans) to match general format of [Dosis VF](https://github.com/eliheuer/dosis-vf)
    - [x] move working state into `wip` branch
    - [x] move static & latest dist fonts into `fonts/` folder
    - [x] move `scripts` and `requirements` into `sources/` folder


- [x] Make PR
    - [x] update fork of google/fonts repo and make `encode-sans` branch
    - [x] add encode sans files, sorted
    - [x] mark PR as "WIP"
    - [x] show latest fontbakery report
    - [x] give known remaining to-do items (search through these docs for `- [ ]`, for starters)
    - [ ] PR!

## Known remaining to-do items (include in PR)
- [ ] Check that filenames and folder sorting is as expected (Ask)
- [ ] update `FONTLOG.txt`
- [ ] update `METADATA.pb` for variable font
- [ ] Apply autohinting to VFs
- [ ] Test hinting in new statics
- [ ] Check that font naming/sorting is how others expect in desktop apps
- [ ] Methodical Red Arrows check. 
    - [ ] Ask: are *any* inflected curves okay (e.g. in accent marks like `/tilde`?)
- [ ] Extra proof kerning for refined glyphs (`/Germandbls`es, `/Oslash`es)
- [ ] Show clear regression/diffing results
- [ ] Do I need to fix mark-to-mark positioning? See docs/diffing-against-old-statics
- [ ] Upgrade build scripts
    - [ ] Make build scripts direct new fonts into `fonts/` directory
    - [ ] Add fontbakery checking to static font builds
    - [ ] (maybe) streamline split-VF build



## Steps to PR, in more detail

1. Fork repo google/fonts
2. Clone
3. Make a branch for font, e.g. `git checkout -b encode-sans`
4. Be sure to pull in lastest google/fonts `master` branch
    1. `git fetch https://github.com/google/fonts.git` to get
    2. `git reset --hard FETCH_HEAD` to hard reset to fetched head

