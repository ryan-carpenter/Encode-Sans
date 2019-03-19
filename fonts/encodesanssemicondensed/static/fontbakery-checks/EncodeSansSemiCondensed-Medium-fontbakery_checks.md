## Fontbakery report

Fontbakery version: 0.6.11

<details>
<summary><b>[26] Family checks</b></summary>
<details>
<summary>:broken_heart: <b>ERROR:</b> Do we have the latest version of FontBakery installed?</summary>

* [com.google.fonts/check/fontbakery_version](https://github.com/googlefonts/fontbakery/search?q=com.google.fonts/check/fontbakery_version)
* :broken_heart: **ERROR** Running 'pip search fontbakery' returned an error code. Output follows :

Retrying (Retry(total=4, connect=None, read=None, redirect=None, status=None)) after connection broken by 'NewConnectionError('<pip._vendor.urllib3.connection.VerifiedHTTPSConnection object at 0x10bbd7cf8>: Failed to establish a new connection: [Errno 8] nodename nor servname provided, or not known')': /pypi
Retrying (Retry(total=3, connect=None, read=None, redirect=None, status=None)) after connection broken by 'NewConnectionError('<pip._vendor.urllib3.connection.VerifiedHTTPSConnection object at 0x10bbd7ac8>: Failed to establish a new connection: [Errno 8] nodename nor servname provided, or not known')': /pypi
Retrying (Retry(total=2, connect=None, read=None, redirect=None, status=None)) after connection broken by 'NewConnectionError('<pip._vendor.urllib3.connection.VerifiedHTTPSConnection object at 0x10a9717b8>: Failed to establish a new connection: [Errno 8] nodename nor servname provided, or not known')': /pypi
Retrying (Retry(total=1, connect=None, read=None, redirect=None, status=None)) after connection broken by 'NewConnectionError('<pip._vendor.urllib3.connection.VerifiedHTTPSConnection object at 0x10bbc9fd0>: Failed to establish a new connection: [Errno 8] nodename nor servname provided, or not known')': /pypi
Retrying (Retry(total=0, connect=None, read=None, redirect=None, status=None)) after connection broken by 'NewConnectionError('<pip._vendor.urllib3.connection.VerifiedHTTPSConnection object at 0x10bbb87f0>: Failed to establish a new connection: [Errno 8] nodename nor servname provided, or not known')': /pypi
Exception:
Traceback (most recent call last):
  File "/Users/stephennixon/type-repos/google-font-repos/Encode-Sans/venv/lib/python3.7/site-packages/pip/_vendor/urllib3/connection.py", line 159, in _new_conn
    (self._dns_host, self.port), self.timeout, **extra_kw)
  File "/Users/stephennixon/type-repos/google-font-repos/Encode-Sans/venv/lib/python3.7/site-packages/pip/_vendor/urllib3/util/connection.py", line 57, in create_connection
    for res in socket.getaddrinfo(host, port, family, socket.SOCK_STREAM):
  File "/usr/local/Cellar/python/3.7.2_1/Frameworks/Python.framework/Versions/3.7/lib/python3.7/socket.py", line 748, in getaddrinfo
    for res in _socket.getaddrinfo(host, port, family, type, proto, flags):
socket.gaierror: [Errno 8] nodename nor servname provided, or not known

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/Users/stephennixon/type-repos/google-font-repos/Encode-Sans/venv/lib/python3.7/site-packages/pip/_vendor/urllib3/connectionpool.py", line 600, in urlopen
    chunked=chunked)
  File "/Users/stephennixon/type-repos/google-font-repos/Encode-Sans/venv/lib/python3.7/site-packages/pip/_vendor/urllib3/connectionpool.py", line 343, in _make_request
    self._validate_conn(conn)
  File "/Users/stephennixon/type-repos/google-font-repos/Encode-Sans/venv/lib/python3.7/site-packages/pip/_vendor/urllib3/connectionpool.py", line 839, in _validate_conn
    conn.connect()
  File "/Users/stephennixon/type-repos/google-font-repos/Encode-Sans/venv/lib/python3.7/site-packages/pip/_vendor/urllib3/connection.py", line 301, in connect
    conn = self._new_conn()
  File "/Users/stephennixon/type-repos/google-font-repos/Encode-Sans/venv/lib/python3.7/site-packages/pip/_vendor/urllib3/connection.py", line 168, in _new_conn
    self, "Failed to establish a new connection: %s" % e)
pip._vendor.urllib3.exceptions.NewConnectionError: <pip._vendor.urllib3.connection.VerifiedHTTPSConnection object at 0x10bbb87b8>: Failed to establish a new connection: [Errno 8] nodename nor servname provided, or not known

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/Users/stephennixon/type-repos/google-font-repos/Encode-Sans/venv/lib/python3.7/site-packages/pip/_vendor/requests/adapters.py", line 449, in send
    timeout=timeout
  File "/Users/stephennixon/type-repos/google-font-repos/Encode-Sans/venv/lib/python3.7/site-packages/pip/_vendor/urllib3/connectionpool.py", line 667, in urlopen
    **response_kw)
  File "/Users/stephennixon/type-repos/google-font-repos/Encode-Sans/venv/lib/python3.7/site-packages/pip/_vendor/urllib3/connectionpool.py", line 667, in urlopen
    **response_kw)
  File "/Users/stephennixon/type-repos/google-font-repos/Encode-Sans/venv/lib/python3.7/site-packages/pip/_vendor/urllib3/connectionpool.py", line 667, in urlopen
    **response_kw)
  [Previous line repeated 2 more times]
  File "/Users/stephennixon/type-repos/google-font-repos/Encode-Sans/venv/lib/python3.7/site-packages/pip/_vendor/urllib3/connectionpool.py", line 638, in urlopen
    _stacktrace=sys.exc_info()[2])
  File "/Users/stephennixon/type-repos/google-font-repos/Encode-Sans/venv/lib/python3.7/site-packages/pip/_vendor/urllib3/util/retry.py", line 398, in increment
    raise MaxRetryError(_pool, url, error or ResponseError(cause))
pip._vendor.urllib3.exceptions.MaxRetryError: HTTPSConnectionPool(host='pypi.org', port=443): Max retries exceeded with url: /pypi (Caused by NewConnectionError('<pip._vendor.urllib3.connection.VerifiedHTTPSConnection object at 0x10bbb87b8>: Failed to establish a new connection: [Errno 8] nodename nor servname provided, or not known'))

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/Users/stephennixon/type-repos/google-font-repos/Encode-Sans/venv/lib/python3.7/site-packages/pip/_internal/cli/base_command.py", line 176, in main
    status = self.run(options, args)
  File "/Users/stephennixon/type-repos/google-font-repos/Encode-Sans/venv/lib/python3.7/site-packages/pip/_internal/commands/search.py", line 48, in run
    pypi_hits = self.search(query, options)
  File "/Users/stephennixon/type-repos/google-font-repos/Encode-Sans/venv/lib/python3.7/site-packages/pip/_internal/commands/search.py", line 65, in search
    hits = pypi.search({'name': query, 'summary': query}, 'or')
  File "/usr/local/Cellar/python/3.7.2_1/Frameworks/Python.framework/Versions/3.7/lib/python3.7/xmlrpc/client.py", line 1112, in __call__
    return self.__send(self.__name, args)
  File "/usr/local/Cellar/python/3.7.2_1/Frameworks/Python.framework/Versions/3.7/lib/python3.7/xmlrpc/client.py", line 1452, in __request
    verbose=self.__verbose
  File "/Users/stephennixon/type-repos/google-font-repos/Encode-Sans/venv/lib/python3.7/site-packages/pip/_internal/download.py", line 823, in request
    headers=headers, stream=True)
  File "/Users/stephennixon/type-repos/google-font-repos/Encode-Sans/venv/lib/python3.7/site-packages/pip/_vendor/requests/sessions.py", line 581, in post
    return self.request('POST', url, data=data, json=json, **kwargs)
  File "/Users/stephennixon/type-repos/google-font-repos/Encode-Sans/venv/lib/python3.7/site-packages/pip/_internal/download.py", line 403, in request
    return super(PipSession, self).request(method, url, *args, **kwargs)
  File "/Users/stephennixon/type-repos/google-font-repos/Encode-Sans/venv/lib/python3.7/site-packages/pip/_vendor/requests/sessions.py", line 533, in request
    resp = self.send(prep, **send_kwargs)
  File "/Users/stephennixon/type-repos/google-font-repos/Encode-Sans/venv/lib/python3.7/site-packages/pip/_vendor/requests/sessions.py", line 646, in send
    r = adapter.send(request, **kwargs)
  File "/Users/stephennixon/type-repos/google-font-repos/Encode-Sans/venv/lib/python3.7/site-packages/pip/_vendor/cachecontrol/adapter.py", line 53, in send
    resp = super(CacheControlAdapter, self).send(request, **kw)
  File "/Users/stephennixon/type-repos/google-font-repos/Encode-Sans/venv/lib/python3.7/site-packages/pip/_vendor/requests/adapters.py", line 516, in send
    raise ConnectionError(e, request=request)
pip._vendor.requests.exceptions.ConnectionError: HTTPSConnectionPool(host='pypi.org', port=443): Max retries exceeded with url: /pypi (Caused by NewConnectionError('<pip._vendor.urllib3.connection.VerifiedHTTPSConnection object at 0x10bbb87b8>: Failed to establish a new connection: [Errno 8] nodename nor servname provided, or not known'))


* :bread: **PASS** Font Bakery is up-to-date

</details>
<details>
<summary>:fire: <b>FAIL:</b> Does DESCRIPTION file contain broken links?</summary>

* [com.google.fonts/check/003](https://github.com/googlefonts/fontbakery/search?q=com.google.fonts/check/003)
* :fire: **FAIL** The following links are broken in the DESCRIPTION file: 'https://fonts.google.com/?query=encode+sans', 'https://github.com/thundernixon/Encode-Sans'

</details>
<details>
<summary>:bread: <b>PASS:</b> Is this a proper HTML snippet?</summary>

* [com.google.fonts/check/004](https://github.com/googlefonts/fontbakery/search?q=com.google.fonts/check/004)
* :bread: **PASS** fonts/encodesanssemicondensed/DESCRIPTION.en_us.html is a propper HTML file.

</details>
<details>
<summary>:bread: <b>PASS:</b> DESCRIPTION.en_us.html must have more than 200 bytes.</summary>

* [com.google.fonts/check/005](https://github.com/googlefonts/fontbakery/search?q=com.google.fonts/check/005)
* :bread: **PASS** DESCRIPTION.en_us.html is larger than 200 bytes.

</details>
<details>
<summary>:bread: <b>PASS:</b> DESCRIPTION.en_us.html must have less than 1000 bytes.</summary>

* [com.google.fonts/check/006](https://github.com/googlefonts/fontbakery/search?q=com.google.fonts/check/006)
* :bread: **PASS** DESCRIPTION.en_us.html is smaller than 1000 bytes.

</details>
<details>
<summary>:bread: <b>PASS:</b> Check font has a license.</summary>

* [com.google.fonts/check/028](https://github.com/googlefonts/fontbakery/search?q=com.google.fonts/check/028)
* :bread: **PASS** Found license at '/Users/stephennixon/type-repos/google-font-repos/Encode-Sans/OFL.txt'

</details>
<details>
<summary>:bread: <b>PASS:</b> All tabular figures must have the same width across the RIBBI-family.</summary>

* [com.google.fonts/check/tnum_horizontal_metrics](https://github.com/googlefonts/fontbakery/search?q=com.google.fonts/check/tnum_horizontal_metrics)
* :bread: **PASS** OK

</details>
<details>
<summary>:bread: <b>PASS:</b> Checking all files are in the same directory.</summary>

* [com.google.fonts/check/002](https://github.com/googlefonts/fontbakery/search?q=com.google.fonts/check/002)
* :bread: **PASS** All files are in the same directory.

</details>
<details>
<summary>:bread: <b>PASS:</b> Is the command `ftxvalidator` (Apple Font Tool Suite) available?</summary>

* [com.google.fonts/check/ftxvalidator_is_available](https://github.com/googlefonts/fontbakery/search?q=com.google.fonts/check/ftxvalidator_is_available)
* :bread: **PASS** ftxvalidator is available.

</details>
<details>
<summary>:bread: <b>PASS:</b> Fonts have equal unicode encodings?</summary>

* [com.google.fonts/check/013](https://github.com/googlefonts/fontbakery/search?q=com.google.fonts/check/013)
* :bread: **PASS** Fonts have equal unicode encodings.

</details>
<details>
<summary>:bread: <b>PASS:</b> Make sure all font files have the same version value.</summary>

* [com.google.fonts/check/014](https://github.com/googlefonts/fontbakery/search?q=com.google.fonts/check/014)
* :bread: **PASS** All font files have the same version.

</details>
<details>
<summary>:bread: <b>PASS:</b> Fonts have consistent PANOSE proportion?</summary>

* [com.google.fonts/check/009](https://github.com/googlefonts/fontbakery/search?q=com.google.fonts/check/009)
* :bread: **PASS** Fonts have consistent PANOSE proportion.

</details>
<details>
<summary>:bread: <b>PASS:</b> Fonts have consistent PANOSE family type?</summary>

* [com.google.fonts/check/010](https://github.com/googlefonts/fontbakery/search?q=com.google.fonts/check/010)
* :bread: **PASS** Fonts have consistent PANOSE family type.

</details>
<details>
<summary>:bread: <b>PASS:</b> Fonts have consistent underline thickness?</summary>

* [com.google.fonts/check/008](https://github.com/googlefonts/fontbakery/search?q=com.google.fonts/check/008)
* :bread: **PASS** Fonts have consistent underline thickness.

</details>
<details>
<summary>:zzz: <b>SKIP:</b> Check METADATA.pb parse correctly. </summary>

* [com.google.fonts/check/metadata/parses](https://github.com/googlefonts/fontbakery/search?q=com.google.fonts/check/metadata/parses)
* :zzz: **SKIP** Font family at 'fonts/encodesanssemicondensed' lacks a METADATA.pb file.

</details>
<details>
<summary>:zzz: <b>SKIP:</b> Font designer field in METADATA.pb must not be 'unknown'.</summary>

* [com.google.fonts/check/007](https://github.com/googlefonts/fontbakery/search?q=com.google.fonts/check/007)
* :zzz: **SKIP** Unfulfilled Conditions: family_metadata

</details>
<details>
<summary>:zzz: <b>SKIP:</b> METADATA.pb: Fontfamily is listed on Google Fonts API?</summary>

* [com.google.fonts/check/081](https://github.com/googlefonts/fontbakery/search?q=com.google.fonts/check/081)
* :zzz: **SKIP** Unfulfilled Conditions: family_metadata

</details>
<details>
<summary>:zzz: <b>SKIP:</b> METADATA.pb: check if fonts field only has unique "full_name" values.</summary>

* [com.google.fonts/check/083](https://github.com/googlefonts/fontbakery/search?q=com.google.fonts/check/083)
* :zzz: **SKIP** Unfulfilled Conditions: family_metadata

</details>
<details>
<summary>:zzz: <b>SKIP:</b> METADATA.pb: check if fonts field only contains unique style:weight pairs.</summary>

* [com.google.fonts/check/084](https://github.com/googlefonts/fontbakery/search?q=com.google.fonts/check/084)
* :zzz: **SKIP** Unfulfilled Conditions: family_metadata

</details>
<details>
<summary>:zzz: <b>SKIP:</b> METADATA.pb license is "APACHE2", "UFL" or "OFL"?</summary>

* [com.google.fonts/check/085](https://github.com/googlefonts/fontbakery/search?q=com.google.fonts/check/085)
* :zzz: **SKIP** Unfulfilled Conditions: family_metadata

</details>
<details>
<summary>:zzz: <b>SKIP:</b> METADATA.pb should contain at least "menu" and "latin" subsets.</summary>

* [com.google.fonts/check/086](https://github.com/googlefonts/fontbakery/search?q=com.google.fonts/check/086)
* :zzz: **SKIP** Unfulfilled Conditions: family_metadata

</details>
<details>
<summary>:zzz: <b>SKIP:</b> METADATA.pb subsets should be alphabetically ordered.</summary>

* [com.google.fonts/check/087](https://github.com/googlefonts/fontbakery/search?q=com.google.fonts/check/087)
* :zzz: **SKIP** Unfulfilled Conditions: family_metadata

</details>
<details>
<summary>:zzz: <b>SKIP:</b> METADATA.pb: Copyright notice is the same in all fonts?</summary>

* [com.google.fonts/check/088](https://github.com/googlefonts/fontbakery/search?q=com.google.fonts/check/088)
* :zzz: **SKIP** Unfulfilled Conditions: family_metadata

</details>
<details>
<summary>:zzz: <b>SKIP:</b> Check that METADATA.pb family values are all the same.</summary>

* [com.google.fonts/check/089](https://github.com/googlefonts/fontbakery/search?q=com.google.fonts/check/089)
* :zzz: **SKIP** Unfulfilled Conditions: family_metadata

</details>
<details>
<summary>:zzz: <b>SKIP:</b> METADATA.pb: According Google Fonts standards, families should have a Regular style.</summary>

* [com.google.fonts/check/090](https://github.com/googlefonts/fontbakery/search?q=com.google.fonts/check/090)
* :zzz: **SKIP** Unfulfilled Conditions: family_metadata

</details>
<details>
<summary>:zzz: <b>SKIP:</b> METADATA.pb: Regular should be 400.</summary>

* [com.google.fonts/check/091](https://github.com/googlefonts/fontbakery/search?q=com.google.fonts/check/091)
* :zzz: **SKIP** Unfulfilled Conditions: family_metadata, has_regular_style

</details>
<br>
</details>
<details>
<summary><b>[117] EncodeSansSemiCondensed-Medium.ttf</b></summary>
<details>
<summary>:broken_heart: <b>ERROR:</b> Familyname must be unique according to namecheck.fontdata.com </summary>

* [com.google.fonts/check/165](https://github.com/googlefonts/fontbakery/search?q=com.google.fonts/check/165)
* :broken_heart: **ERROR** Failed to access: 'http://namecheck.fontdata.com/?q=EncodeSansSemiCondensed'.
Please report this issue at:
https://github.com/googlefonts/fontbakery/issues

</details>
<details>
<summary>:fire: <b>FAIL:</b> Check name table: FONT_FAMILY_NAME entries. </summary>

* [com.google.fonts/check/157](https://github.com/googlefonts/fontbakery/search?q=com.google.fonts/check/157)
* :fire: **FAIL** Entry [FONT_FAMILY_NAME(1):WINDOWS(3)] on the 'name' table: Expected 'Encode Sans Semi Condensed Medium' but got 'Encode Sans SemiCondensed Medium'.

</details>
<details>
<summary>:fire: <b>FAIL:</b> Check name table: FULL_FONT_NAME entries. </summary>

* [com.google.fonts/check/159](https://github.com/googlefonts/fontbakery/search?q=com.google.fonts/check/159)
* :fire: **FAIL** Entry [FULL_FONT_NAME(4):WINDOWS(3)] on the 'name' table: Expected 'Encode Sans Semi Condensed Medium' but got 'Encode Sans SemiCond Med'.

</details>
<details>
<summary>:fire: <b>FAIL:</b> Check name table: POSTSCRIPT_NAME entries. </summary>

* [com.google.fonts/check/160](https://github.com/googlefonts/fontbakery/search?q=com.google.fonts/check/160)
* :fire: **FAIL** Entry [POSTSCRIPT_NAME(6):WINDOWS(3)] on the 'name' table: Expected 'EncodeSansSemiCondensed-Medium' but got 'EncodeSansSemiCond-Med'.

</details>
<details>
<summary>:fire: <b>FAIL:</b> Check name table: TYPOGRAPHIC_FAMILY_NAME entries. </summary>

* [com.google.fonts/check/161](https://github.com/googlefonts/fontbakery/search?q=com.google.fonts/check/161)
* :fire: **FAIL** Entry [TYPOGRAPHIC_FAMILY_NAME(16):WINDOWS(3)] on the 'name' table: Expected 'Encode Sans Semi Condensed' but got 'Encode Sans SemiCondensed'. [code: non-ribbi-bad-value]

</details>
<details>
<summary>:fire: <b>FAIL:</b> Does full font name begin with the font family name?</summary>

* [com.google.fonts/check/068](https://github.com/googlefonts/fontbakery/search?q=com.google.fonts/check/068)
* :fire: **FAIL**  On the 'name' table, the full font name (NameID 4 - FULL_FONT_NAME: 'Encode Sans SemiCondensed Medium') does not begin with font family name (NameID 1 - FONT_FAMILY_NAME: 'Encode Sans SemiCond Med') [code: does-not]

</details>
<details>
<summary>:warning: <b>WARN:</b> Check if each glyph has the recommended amount of contours.</summary>

* [com.google.fonts/check/153](https://github.com/googlefonts/fontbakery/search?q=com.google.fonts/check/153)
* :warning: **WARN** This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are infered from the typical ammounts of contours observed in a large collection of reference font families. The divergences listed below may simply indicate a significantly different design on some of your glyphs. On the other hand, some of these may flag actual bugs in the font such as glyphs mapped to an incorrect codepoint. Please consider reviewing the design and codepoint assignment of these to make sure they are correct.

The following glyphs do not have the recommended number of contours:

Glyph name: Eth	Contours detected: 3	Expected: 2
Glyph name: Dcroat	Contours detected: 3	Expected: 2
Glyph name: dcroat	Contours detected: 3	Expected: 2
Glyph name: hbar	Contours detected: 2	Expected: 1
Glyph name: Lslash	Contours detected: 2	Expected: 1
Glyph name: lslash	Contours detected: 2	Expected: 1
Glyph name: Tbar	Contours detected: 2	Expected: 1
Glyph name: tbar	Contours detected: 2	Expected: 1
Glyph name: uni1E08	Contours detected: 3	Expected: 2
Glyph name: uni1E09	Contours detected: 3	Expected: 2
Glyph name: uni1E1C	Contours detected: 3	Expected: 2
Glyph name: uni1E1D	Contours detected: 4	Expected: 3

</details>
<details>
<summary>:warning: <b>WARN:</b> Name table strings must not contain the string 'Reserved Font Name'.</summary>

* [com.google.fonts/check/152](https://github.com/googlefonts/fontbakery/search?q=com.google.fonts/check/152)
* :warning: **WARN** Name table entry ("Copyright 2018 The Encode Project Authors (https://github.com/thundernixon/Encode-Sans), with Reserved Font Name 'Encode Sans'.") contains "Reserved Font Name". This is an error except in a few specific rare cases.

</details>
<details>
<summary>:warning: <b>WARN:</b> Combined length of family and style must not exceed 20 characters.</summary>

* [com.google.fonts/check/163](https://github.com/googlefonts/fontbakery/search?q=com.google.fonts/check/163)
* :warning: **WARN** The combined length of family and style exceeds 20 chars in the following 'WINDOWS' entries: FONT_FAMILY_NAME = 'Encode Sans SemiCondensed Medium' / SUBFAMILY_NAME = 'Regular'

</details>
<details>
<summary>:warning: <b>WARN:</b> Monospace font has hhea.advanceWidthMax equal to each glyph's advanceWidth?</summary>

* [com.google.fonts/check/079](https://github.com/googlefonts/fontbakery/search?q=com.google.fonts/check/079)
* :warning: **WARN** This seems to be a monospaced font, so advanceWidth value should be the same across all glyphs, but 99.67% of them have a different value: A, Aacute, Abreve, uni1EAE, uni1EB6, uni1EB0, uni1EB2, uni1EB4, Acircumflex, uni1EA4, uni1EAC, uni1EA6, uni1EA8, uni1EAA, uni0200, Adieresis, uni1EA0, Agrave, uni1EA2, uni0202, Amacron, Aogonek, Aring, Aringacute, Atilde, AE, AEacute, B, C, Cacute, Ccaron, Ccedilla, uni1E08, Ccircumflex, Cdotaccent, D, uni01F1, uni01C4, Eth, Dcaron, Dcroat, uni1E0C, uni1E0E, uni01F2, uni01C5, E, Eacute, Ebreve, Ecaron, uni1E1C, Ecircumflex, uni1EBE, uni1EC6, uni1EC0, uni1EC2, uni1EC4, uni0204, Edieresis, Edotaccent, uni1EB8, Egrave, uni1EBA, uni0206, Emacron, uni1E16, uni1E14, Eogonek, uni1EBC, F, G, uni01F4, Gbreve, Gcaron, Gcircumflex, uni0122, Gdotaccent, uni1E20, H, Hbar, uni1E2A, Hcircumflex, uni1E24, I, Iacute, Ibreve, Icircumflex, uni0208, Idieresis, uni1E2E, Idotaccent, uni1ECA, Igrave, uni1EC8, uni020A, Imacron, Iogonek, Itilde, J, Jcircumflex, K, uni0136, L, uni01C7, Lacute, Lcaron, uni013B, Ldot, uni1E36, uni01C8, uni1E3A, Lslash, M, uni1E42, N, uni01CA, Nacute, Ncaron, uni0145, uni1E44, uni1E46, Eng, uni01CB, uni1E48, Ntilde, O, Oacute, Obreve, Ocircumflex, uni1ED0, uni1ED8, uni1ED2, uni1ED4, uni1ED6, uni020C, Odieresis, uni022A, uni0230, uni1ECC, Ograve, uni1ECE, Ohorn, uni1EDA, uni1EE2, uni1EDC, uni1EDE, uni1EE0, Ohungarumlaut, uni020E, Omacron, uni1E52, uni1E50, uni01EA, Oslash, Oslashacute, Otilde, uni1E4C, uni1E4E, uni022C, OE, P, Thorn, Q, R, Racute, Rcaron, uni0156, uni0210, uni1E5A, uni0212, uni1E5E, S, Sacute, uni1E64, Scaron, uni1E66, Scedilla, Scircumflex, uni0218, uni1E60, uni1E62, uni1E68, uni1E9E, uni018F, T, Tbar, Tcaron, uni0162, uni021A, uni1E6C, uni1E6E, U, Uacute, Ubreve, Ucircumflex, uni0214, Udieresis, uni1EE4, Ugrave, uni1EE6, Uhorn, uni1EE8, uni1EF0, uni1EEA, uni1EEC, uni1EEE, Uhungarumlaut, uni0216, Umacron, uni1E7A, Uogonek, Uring, Utilde, uni1E78, V, W, Wacute, Wcircumflex, Wdieresis, Wgrave, X, Y, Yacute, Ycircumflex, Ydieresis, uni1E8E, uni1EF4, Ygrave, uni1EF6, uni0232, uni1EF8, Z, Zacute, Zcaron, Zdotaccent, uni1E92, Iacute_J.loclNLD, a, aacute, abreve, uni1EAF, uni1EB7, uni1EB1, uni1EB3, uni1EB5, acircumflex, uni1EA5, uni1EAD, uni1EA7, uni1EA9, uni1EAB, uni0201, adieresis, uni1EA1, agrave, uni1EA3, uni0203, amacron, aogonek, aring, aringacute, atilde, ae, aeacute, b, c, cacute, ccaron, ccedilla, uni1E09, ccircumflex, cdotaccent, d, eth, dcaron, dcroat, uni1E0D, uni1E0F, uni01F3, uni01C6, e, eacute, ebreve, ecaron, uni1E1D, ecircumflex, uni1EBF, uni1EC7, uni1EC1, uni1EC3, uni1EC5, uni0205, edieresis, edotaccent, uni1EB9, egrave, uni1EBB, uni0207, emacron, uni1E17, uni1E15, eogonek, uni1EBD, uni0259, f, g, uni01F5, gbreve, gcaron, gcircumflex, uni0123, gdotaccent, uni1E21, h, hbar, uni1E2B, hcircumflex, uni1E25, i, dotlessi, iacute, ibreve, icircumflex, uni0209, idieresis, uni1E2F, i.loclTRK, uni1ECB, igrave, uni1EC9, uni020B, imacron, iogonek, itilde, j, uni0237, jcircumflex, k, uni0137, kgreenlandic, l, lacute, lcaron, uni013C, ldot, uni1E37, uni01C9, uni1E3B, lslash, m, uni1E43, n, nacute, napostrophe, ncaron, uni0146, uni1E45, uni1E47, eng, uni01CC, uni1E49, ntilde, o, oacute, obreve, ocircumflex, uni1ED1, uni1ED9, uni1ED3, uni1ED5, uni1ED7, uni020D, odieresis, uni022B, uni0231, uni1ECD, ograve, uni1ECF, ohorn, uni1EDB, uni1EE3, uni1EDD, uni1EDF, uni1EE1, ohungarumlaut, uni020F, omacron, uni1E53, uni1E51, uni01EB, oslash, oslashacute, otilde, uni1E4D, uni1E4F, uni022D, oe, p, thorn, q, r, racute, rcaron, uni0157, uni0211, uni1E5B, uni0213, uni1E5F, s, sacute, uni1E65, scaron, uni1E67, scedilla, scircumflex, uni0219, uni1E61, uni1E63, uni1E69, germandbls, t, tbar, tcaron, uni0163, uni021B, uni1E97, uni1E6D, uni1E6F, u, uacute, ubreve, ucircumflex, uni0215, udieresis, uni1EE5, ugrave, uni1EE7, uhorn, uni1EE9, uni1EF1, uni1EEB, uni1EED, uni1EEF, uhungarumlaut, uni0217, umacron, uni1E7B, uogonek, uring, utilde, uni1E79, v, w, wacute, wcircumflex, wdieresis, wgrave, x, y, yacute, ycircumflex, ydieresis, uni1E8F, uni1EF5, ygrave, uni1EF7, uni0233, uni1EF9, z, zacute, zcaron, zdotaccent, uni1E93, iacute_j.loclNLD, f.short, f_i, f_j, f_l, fi, fl, I_J.loclNLD, i_j.loclNLD, a.sc, aacute.sc, abreve.sc, uni1EAF.sc, uni1EB7.sc, uni1EB1.sc, uni1EB3.sc, uni1EB5.sc, acircumflex.sc, uni1EA5.sc, uni1EAD.sc, uni1EA7.sc, uni1EA9.sc, uni1EAB.sc, uni0201.sc, adieresis.sc, uni1EA1.sc, agrave.sc, uni1EA3.sc, uni0203.sc, amacron.sc, aogonek.sc, aring.sc, aringacute.sc, atilde.sc, ae.sc, aeacute.sc, b.sc, c.sc, cacute.sc, ccaron.sc, ccedilla.sc, uni1E09.sc, ccircumflex.sc, cdotaccent.sc, d.sc, eth.sc, dcaron.sc, dcroat.sc, uni1E0D.sc, uni1E0F.sc, uni01F3.sc, uni01C6.sc, e.sc, eacute.sc, ebreve.sc, ecaron.sc, uni1E1D.sc, ecircumflex.sc, uni1EBF.sc, uni1EC7.sc, uni1EC1.sc, uni1EC3.sc, uni1EC5.sc, uni0205.sc, edieresis.sc, edotaccent.sc, uni1EB9.sc, egrave.sc, uni1EBB.sc, uni0207.sc, emacron.sc, uni1E17.sc, uni1E15.sc, eogonek.sc, uni1EBD.sc, uni0259.sc, f.sc, g.sc, uni01F5.sc, gbreve.sc, gcaron.sc, gcircumflex.sc, uni0123.sc, gdotaccent.sc, uni1E21.sc, h.sc, hbar.sc, uni1E2B.sc, hcircumflex.sc, uni1E25.sc, i.sc, iacute.sc, iacute_j.loclNLD.sc, ibreve.sc, icircumflex.sc, uni0209.sc, idieresis.sc, uni1E2F.sc, i.loclTRK.sc, uni1ECB.sc, igrave.sc, uni1EC9.sc, uni020B.sc, imacron.sc, iogonek.sc, itilde.sc, j.sc, jcircumflex.sc, k.sc, uni0137.sc, l.sc, lacute.sc, lcaron.sc, uni013C.sc, ldot.sc, uni1E37.sc, uni01C9.sc, uni1E3B.sc, i_j.loclNLD.sc, lslash.sc, m.sc, uni1E43.sc, n.sc, nacute.sc, ncaron.sc, uni0146.sc, uni1E45.sc, uni1E47.sc, eng.sc, uni01CC.sc, uni1E49.sc, ntilde.sc, o.sc, oacute.sc, obreve.sc, ocircumflex.sc, uni1ED1.sc, uni1ED9.sc, uni1ED3.sc, uni1ED5.sc, uni1ED7.sc, uni020D.sc, odieresis.sc, uni022B.sc, uni0231.sc, uni1ECD.sc, ograve.sc, uni1ECF.sc, ohorn.sc, uni1EDB.sc, uni1EE3.sc, uni1EDD.sc, uni1EDF.sc, uni1EE1.sc, ohungarumlaut.sc, uni020F.sc, omacron.sc, uni1E53.sc, uni1E51.sc, uni01EB.sc, oslash.sc, oslashacute.sc, otilde.sc, uni1E4D.sc, uni1E4F.sc, uni022D.sc, oe.sc, p.sc, thorn.sc, q.sc, r.sc, racute.sc, rcaron.sc, uni0157.sc, uni0211.sc, uni1E5B.sc, uni0213.sc, uni1E5F.sc, s.sc, sacute.sc, uni1E65.sc, scaron.sc, uni1E67.sc, scedilla.sc, scircumflex.sc, uni0219.sc, uni1E61.sc, uni1E63.sc, uni1E69.sc, germandbls.sc, t.sc, tbar.sc, tcaron.sc, uni0163.sc, uni021B.sc, uni1E6D.sc, uni1E6F.sc, u.sc, uacute.sc, ubreve.sc, ucircumflex.sc, uni0215.sc, udieresis.sc, uni1EE5.sc, ugrave.sc, uni1EE7.sc, uhorn.sc, uni1EE9.sc, uni1EF1.sc, uni1EEB.sc, uni1EED.sc, uni1EEF.sc, uhungarumlaut.sc, uni0217.sc, umacron.sc, uni1E7B.sc, uogonek.sc, uring.sc, utilde.sc, uni1E79.sc, v.sc, w.sc, wacute.sc, wcircumflex.sc, wdieresis.sc, wgrave.sc, x.sc, y.sc, yacute.sc, ycircumflex.sc, ydieresis.sc, uni1E8F.sc, uni1EF5.sc, ygrave.sc, uni1EF7.sc, uni0233.sc, uni1EF9.sc, z.sc, zacute.sc, zcaron.sc, zdotaccent.sc, uni1E93.sc, ordfeminine, ordmasculine, uni0394, uni03A9, uni0394.tf, uni03A9.tf, uni03BC, pi, uni03BC.tf, pi.tf, zero, one, two, three, four, five, six, seven, eight, nine, zero.osf, one.osf, two.osf, three.osf, four.osf, five.osf, six.osf, seven.osf, eight.osf, nine.osf, zero.tf, one.tf, two.tf, three.tf, four.tf, five.tf, six.tf, seven.tf, eight.tf, nine.tf, zero.tosf, one.tosf, two.tosf, three.tosf, four.tosf, five.tosf, six.tosf, seven.tosf, eight.tosf, nine.tosf, uni2080, uni2081, uni2082, uni2083, uni2084, uni2085, uni2086, uni2087, uni2088, uni2089, zero.dnom, one.dnom, two.dnom, three.dnom, four.dnom, five.dnom, six.dnom, seven.dnom, eight.dnom, nine.dnom, zero.numr, one.numr, two.numr, three.numr, four.numr, five.numr, six.numr, seven.numr, eight.numr, nine.numr, uni2070, uni00B9, uni00B2, uni00B3, uni2074, uni2075, uni2076, uni2077, uni2078, uni2079, fraction, onehalf, uni2153, uni2154, onequarter, threequarters, oneeighth, threeeighths, fiveeighths, seveneighths, period, comma, colon, semicolon, ellipsis, exclam, exclamdown, question, questiondown, periodcentered, bullet, asterisk, numbersign, slash, backslash, periodcentered.CAT, periodcentered.loclCAT.case, period.tf, comma.tf, colon.tf, semicolon.tf, periodcentered.tf, numbersign.tf, slash.tf, parenleft, parenright, braceleft, braceright, bracketleft, bracketright, hyphen, uni00AD, endash, emdash, figuredash, uni2015, uni2010, underscore, underscore.tf, quotesinglbase, quotedblbase, quotedblleft, quotedblright, quoteleft, quoteright, guillemotleft, guillemotright, guilsinglleft, guilsinglright, quotedbl, quotesingle, quotedbl.tf, quotesingle.tf, parenleft.sc, parenright.sc, braceleft.sc, braceright.sc, bracketleft.sc, bracketright.sc, uni2007, uni200A, uni2008, space, uni00A0, uni2009, uni200B, CR, uni20B5, cent, colonmonetary, currency, dollar, dong, Euro, florin, franc, uni20B2, uni20AD, lira, uni20BA, uni20BC, uni20A6, peseta, uni20B1, uni20BD, uni20B9, sterling, uni20BF, uni20A9, yen, uni20BF.tf, uni20B5.tf, cent.tf, colonmonetary.tf, currency.tf, dollar.tf, dong.tf, Euro.tf, florin.tf, franc.tf, uni20B2.tf, uni20AD.tf, lira.tf, uni20BA.tf, uni20BC.tf, uni20A6.tf, peseta.tf, uni20B1.tf, uni20BD.tf, uni20B9.tf, sterling.tf, uni20A9.tf, yen.tf, uni2219, uni2215, plus, minus, multiply, divide, equal, notequal, greater, less, greaterequal, lessequal, plusminus, approxequal, asciitilde, logicalnot, asciicircum, infinity, integral, uni2126, uni2206, product, summation, radical, uni00B5, partialdiff, percent, uni2219.osf, plus.osf, minus.osf, multiply.osf, divide.osf, equal.osf, notequal.osf, greater.osf, less.osf, greaterequal.osf, lessequal.osf, plusminus.osf, approxequal.osf, asciitilde.osf, logicalnot.osf, asciicircum.osf, infinity.osf, uni2219.tf, uni2215.tf, plus.tf, minus.tf, multiply.tf, divide.tf, equal.tf, notequal.tf, greater.tf, less.tf, greaterequal.tf, lessequal.tf, plusminus.tf, approxequal.tf, asciitilde.tf, logicalnot.tf, asciicircum.tf, infinity.tf, integral.tf, uni2126.tf, uni2206.tf, product.tf, summation.tf, radical.tf, uni00B5.tf, partialdiff.tf, percent.tf, perthousand.tf, uni2219.tosf, uni2215.tosf, plus.tosf, minus.tosf, multiply.tosf, divide.tosf, equal.tosf, notequal.tosf, greater.tosf, less.tosf, greaterequal.tosf, lessequal.tosf, plusminus.tosf, approxequal.tosf, asciitilde.tosf, logicalnot.tosf, asciicircum.tosf, infinity.tosf, arrowup, arrowright, arrowdown, arrowleft, lozenge, lozenge.osf, lozenge.tf, lozenge.tosf, at, ampersand, paragraph, section, copyright, registered, trademark, degree, minute, second, bar, brokenbar, dagger, uni2113, daggerdbl, uni2116, estimated, uni2120, degree.tf, bar.tf, brokenbar.tf, ampersand.sc, uni02BC, uni02BB, uni02C9, uni02CB, uni02BF, uni02BE, uni02CA, uni02CC, uni02C8, uni0308, uni03080301, uni03080304, uni0307, uni03070304, gravecomb, acutecomb, uni03010307, uni030B, uni030C.alt, uni0302, uni030C, uni030C0307, uni0306, uni030A, uni030A0301, tildecomb, uni03030308, tildecomb_acutecomb, uni03030304, uni0304, uni03040308, uni03040300, uni03040301, hookabovecomb, uni030F, uni0311, uni0312, uni031B, dotbelowcomb, uni0324, uni0326, uni0327, uni0328, uni032E, uni0331, acute, breve, caron, cedilla, circumflex, dieresis, dotaccent, grave, hungarumlaut, macron, ogonek, ring, tilde, uni0326.alt, caron.alt, uni0308.case, uni03080301.case, uni03080304.case, uni0307.case, uni03070304.case, gravecomb.case, acutecomb.case, uni03010307.case, uni030B.case, uni030C.alt.case, uni0302.case, uni030C.case, uni030C0307.case, uni0306.case, uni030A.case, uni030A0301.case, tildecomb.case, uni03030308.case, tildecomb_acutecomb.case, uni03030304.case, uni0304.case, uni03040308.case, uni03040300.case, uni03040301.case, hookabovecomb.case, uni030F.case, uni0311.case, uni0312.case, dotbelowcomb.case, uni0324.case, uni0326.case, uni0327.case, uni0328.case, uni032E.case, uni0331.case, uni0308.sc, uni03080301.sc, uni03080304.sc, uni0307.sc, uni03070304.sc, gravecomb.sc, acutecomb.sc, uni03010307.sc, uni030B.sc, uni030C.alt.sc, uni0302.sc, uni030C.sc, uni030C0307.sc, uni0306.sc, uni030A.sc, tildecomb.sc, uni03030308.sc, tildecomb_acutecomb.sc, uni03030304.sc, uni0304.sc, uni03040308.sc, uni03040300.sc, uni03040301.sc, hookabovecomb.sc, uni030F.sc, uni0311.sc, uni0312.sc, dotbelowcomb.sc, uni0324.sc, uni0326.sc, uni0327.sc, uni0328.sc, uni032E.sc, uni0331.sc, uni0335.sc, uni0337.sc, uni030A0301.case.sc, uni0337, uni0335.D, uni0335.case, uni0336.case, uni0337.case, uni0335.d, uni0335.dsc, uni0335.h, uni0336.hsc, uni0335.t, uni03060301, uni03060300, uni03060309, uni03060303, uni03020301, uni03020300, uni03020309, uni03020303, uni03060301.case, uni03060300.case, uni03060309.case, uni03060303.case, uni03020301.case, uni03020300.case, uni03020309.case, uni03020303.case, uni03060301.sc, uni03060300.sc, uni03060309.sc, uni03060303.sc, uni03020301.sc, uni03020300.sc, uni03020309.sc, uni03020303.sc, slashcomb.case, slashcomb.sc, notdef [code: should-be-monospaced]
* :warning: **WARN** Double-width and/or zero-width glyphs were detected. These glyphs should be set to the same width as all others and then add GPOS single pos lookups that zeros/doubles the widths as needed: uni200B, uni0308, uni03080301, uni0307, gravecomb, acutecomb, uni03010307, uni030B, uni030C.alt, uni0302, uni030C, uni0306, uni030A, uni030A0301, tildecomb, uni03030308, tildecomb_acutecomb, uni03030304, uni0304, uni03040300, uni03040301, hookabovecomb, uni030F, uni0311, uni0312, uni031B, dotbelowcomb, uni0324, uni0326, uni0327, uni0328, uni032E, uni0331, uni0326.alt, uni0308.case, uni03080301.case, uni0307.case, gravecomb.case, acutecomb.case, uni03010307.case, uni030B.case, uni030C.alt.case, uni0302.case, uni030C.case, uni0306.case, uni030A.case, uni030A0301.case, tildecomb.case, uni03030308.case, tildecomb_acutecomb.case, uni03030304.case, uni0304.case, uni03040300.case, uni03040301.case, hookabovecomb.case, uni030F.case, uni0311.case, uni0312.case, dotbelowcomb.case, uni0324.case, uni0326.case, uni0327.case, uni0328.case, uni032E.case, uni0331.case, uni0308.sc, uni03080301.sc, uni0307.sc, gravecomb.sc, acutecomb.sc, uni03010307.sc, uni030B.sc, uni030C.alt.sc, uni0302.sc, uni030C.sc, uni0306.sc, uni030A.sc, tildecomb.sc, uni03030308.sc, tildecomb_acutecomb.sc, uni03030304.sc, uni0304.sc, uni03040300.sc, uni03040301.sc, hookabovecomb.sc, uni030F.sc, uni0311.sc, uni0312.sc, dotbelowcomb.sc, uni0324.sc, uni0326.sc, uni0327.sc, uni0328.sc, uni032E.sc, uni0331.sc, uni0335.sc, uni0337.sc, uni030A0301.case.sc, uni0337, uni0335.D, uni0335.case, uni0336.case, uni0337.case, uni0335.d, uni0335.dsc, uni0335.h, uni0336.hsc, uni0335.t, uni03060301, uni03060300, uni03060309, uni03060303, uni03020301, uni03020300, uni03020309, uni03020303, uni03060301.case, uni03060300.case, uni03060309.case, uni03060303.case, uni03020301.case, uni03020300.case, uni03020309.case, uni03020303.case, uni03060301.sc, uni03060300.sc, uni03060309.sc, uni03060303.sc, uni03020301.sc, uni03020300.sc, uni03020309.sc, uni03020303.sc [code: variable-monospaced]

</details>
<details>
<summary>:warning: <b>WARN:</b> Is there kerning info for non-ligated sequences?</summary>

* [com.google.fonts/check/065](https://github.com/googlefonts/fontbakery/search?q=com.google.fonts/check/065)
* :warning: **WARN** GPOS table lacks kerning info for the following non-ligated sequences:
	- f + i
	- i + j
	- j + l

   [code: lacks-kern-info]

</details>
<details>
<summary>:zzz: <b>SKIP:</b> Checks METADATA.pb font.name field matches family name declared on the name table.</summary>

* [com.google.fonts/check/092](https://github.com/googlefonts/fontbakery/search?q=com.google.fonts/check/092)
* :zzz: **SKIP** Unfulfilled Conditions: font_metadata

</details>
<details>
<summary>:zzz: <b>SKIP:</b> Checks METADATA.pb font.post_script_name matches postscript name declared on the name table.</summary>

* [com.google.fonts/check/093](https://github.com/googlefonts/fontbakery/search?q=com.google.fonts/check/093)
* :zzz: **SKIP** Unfulfilled Conditions: font_metadata

</details>
<details>
<summary>:zzz: <b>SKIP:</b> METADATA.pb font.full_name value matches fullname declared on the name table?</summary>

* [com.google.fonts/check/094](https://github.com/googlefonts/fontbakery/search?q=com.google.fonts/check/094)
* :zzz: **SKIP** Unfulfilled Conditions: font_metadata

</details>
<details>
<summary>:zzz: <b>SKIP:</b> METADATA.pb font.name value should be same as the family name declared on the name table.</summary>

* [com.google.fonts/check/095](https://github.com/googlefonts/fontbakery/search?q=com.google.fonts/check/095)
* :zzz: **SKIP** Unfulfilled Conditions: font_metadata

</details>
<details>
<summary>:zzz: <b>SKIP:</b> METADATA.pb font.full_name and font.post_script_name fields have equivalent values ?</summary>

* [com.google.fonts/check/096](https://github.com/googlefonts/fontbakery/search?q=com.google.fonts/check/096)
* :zzz: **SKIP** Unfulfilled Conditions: font_metadata

</details>
<details>
<summary>:zzz: <b>SKIP:</b> METADATA.pb font.filename and font.post_script_name fields have equivalent values?</summary>

* [com.google.fonts/check/097](https://github.com/googlefonts/fontbakery/search?q=com.google.fonts/check/097)
* :zzz: **SKIP** Unfulfilled Conditions: font_metadata

</details>
<details>
<summary>:zzz: <b>SKIP:</b> METADATA.pb font.name field contains font name in right format?</summary>

* [com.google.fonts/check/098](https://github.com/googlefonts/fontbakery/search?q=com.google.fonts/check/098)
* :zzz: **SKIP** Unfulfilled Conditions: font_metadata

</details>
<details>
<summary>:zzz: <b>SKIP:</b> METADATA.pb font.full_name field contains font name in right format?</summary>

* [com.google.fonts/check/099](https://github.com/googlefonts/fontbakery/search?q=com.google.fonts/check/099)
* :zzz: **SKIP** Unfulfilled Conditions: font_metadata

</details>
<details>
<summary>:zzz: <b>SKIP:</b> METADATA.pb font.filename field contains font name in right format?</summary>

* [com.google.fonts/check/100](https://github.com/googlefonts/fontbakery/search?q=com.google.fonts/check/100)
* :zzz: **SKIP** Unfulfilled Conditions: family_metadata

</details>
<details>
<summary>:zzz: <b>SKIP:</b> METADATA.pb font.post_script_name field contains font name in right format?</summary>

* [com.google.fonts/check/101](https://github.com/googlefonts/fontbakery/search?q=com.google.fonts/check/101)
* :zzz: **SKIP** Unfulfilled Conditions: font_metadata

</details>
<details>
<summary>:zzz: <b>SKIP:</b> Copyright notices match canonical pattern?</summary>

* [com.google.fonts/check/102](https://github.com/googlefonts/fontbakery/search?q=com.google.fonts/check/102)
* :zzz: **SKIP** Unfulfilled Conditions: font_metadata

</details>
<details>
<summary>:zzz: <b>SKIP:</b> Copyright notice on METADATA.pb should not contain 'Reserved Font Name'.</summary>

* [com.google.fonts/check/103](https://github.com/googlefonts/fontbakery/search?q=com.google.fonts/check/103)
* :zzz: **SKIP** Unfulfilled Conditions: font_metadata

</details>
<details>
<summary>:zzz: <b>SKIP:</b> METADATA.pb: Copyright notice shouldn't exceed 500 chars.</summary>

* [com.google.fonts/check/104](https://github.com/googlefonts/fontbakery/search?q=com.google.fonts/check/104)
* :zzz: **SKIP** Unfulfilled Conditions: font_metadata

</details>
<details>
<summary>:zzz: <b>SKIP:</b> METADATA.pb: Filename is set canonically?</summary>

* [com.google.fonts/check/105](https://github.com/googlefonts/fontbakery/search?q=com.google.fonts/check/105)
* :zzz: **SKIP** Unfulfilled Conditions: font_metadata, canonical_filename

</details>
<details>
<summary>:zzz: <b>SKIP:</b> METADATA.pb font.style "italic" matches font internals?</summary>

* [com.google.fonts/check/106](https://github.com/googlefonts/fontbakery/search?q=com.google.fonts/check/106)
* :zzz: **SKIP** Unfulfilled Conditions: font_metadata

</details>
<details>
<summary>:zzz: <b>SKIP:</b> METADATA.pb font.style "normal" matches font internals?</summary>

* [com.google.fonts/check/107](https://github.com/googlefonts/fontbakery/search?q=com.google.fonts/check/107)
* :zzz: **SKIP** Unfulfilled Conditions: font_metadata

</details>
<details>
<summary>:zzz: <b>SKIP:</b> METADATA.pb font.name and font.full_name fields match the values declared on the name table?</summary>

* [com.google.fonts/check/108](https://github.com/googlefonts/fontbakery/search?q=com.google.fonts/check/108)
* :zzz: **SKIP** Unfulfilled Conditions: font_metadata

</details>
<details>
<summary>:zzz: <b>SKIP:</b> METADATA.pb: Check if fontname is not camel cased.</summary>

* [com.google.fonts/check/109](https://github.com/googlefonts/fontbakery/search?q=com.google.fonts/check/109)
* :zzz: **SKIP** Unfulfilled Conditions: font_metadata

</details>
<details>
<summary>:zzz: <b>SKIP:</b> METADATA.pb: Check font name is the same as family name.</summary>

* [com.google.fonts/check/110](https://github.com/googlefonts/fontbakery/search?q=com.google.fonts/check/110)
* :zzz: **SKIP** Unfulfilled Conditions: family_metadata, font_metadata

</details>
<details>
<summary>:zzz: <b>SKIP:</b> METADATA.pb: Check that font weight has a canonical value.</summary>

* [com.google.fonts/check/111](https://github.com/googlefonts/fontbakery/search?q=com.google.fonts/check/111)
* :zzz: **SKIP** Unfulfilled Conditions: font_metadata

</details>
<details>
<summary>:zzz: <b>SKIP:</b> Checking OS/2 usWeightClass matches weight specified at METADATA.pb.</summary>

* [com.google.fonts/check/112](https://github.com/googlefonts/fontbakery/search?q=com.google.fonts/check/112)
* :zzz: **SKIP** Unfulfilled Conditions: font_metadata

</details>
<details>
<summary>:zzz: <b>SKIP:</b> METADATA.pb weight matches postScriptName.</summary>

* [com.google.fonts/check/113](https://github.com/googlefonts/fontbakery/search?q=com.google.fonts/check/113)
* :zzz: **SKIP** Unfulfilled Conditions: font_metadata

</details>
<details>
<summary>:zzz: <b>SKIP:</b> METADATA.pb: Font styles are named canonically?</summary>

* [com.google.fonts/check/115](https://github.com/googlefonts/fontbakery/search?q=com.google.fonts/check/115)
* :zzz: **SKIP** Unfulfilled Conditions: font_metadata

</details>
<details>
<summary>:zzz: <b>SKIP:</b> Version number has increased since previous release on Google Fonts?</summary>

* [com.google.fonts/check/117](https://github.com/googlefonts/fontbakery/search?q=com.google.fonts/check/117)
* :zzz: **SKIP** Unfulfilled Conditions: api_gfonts_ttFont

</details>
<details>
<summary>:zzz: <b>SKIP:</b> Glyphs are similiar to Google Fonts version?</summary>

* [com.google.fonts/check/118](https://github.com/googlefonts/fontbakery/search?q=com.google.fonts/check/118)
* :zzz: **SKIP** Unfulfilled Conditions: api_gfonts_ttFont

</details>
<details>
<summary>:zzz: <b>SKIP:</b> Check font has same encoded glyphs as version hosted on fonts.google.com</summary>

* [com.google.fonts/check/154](https://github.com/googlefonts/fontbakery/search?q=com.google.fonts/check/154)
* :zzz: **SKIP** Unfulfilled Conditions: api_gfonts_ttFont

</details>
<details>
<summary>:zzz: <b>SKIP:</b> Copyright field for this font on METADATA.pb matches all copyright notice entries on the name table ?</summary>

* [com.google.fonts/check/155](https://github.com/googlefonts/fontbakery/search?q=com.google.fonts/check/155)
* :zzz: **SKIP** Unfulfilled Conditions: font_metadata

</details>
<details>
<summary>:zzz: <b>SKIP:</b> Check a static ttf can be generated from a variable font. </summary>

* [com.google.fonts/check/174](https://github.com/googlefonts/fontbakery/search?q=com.google.fonts/check/174)
* :zzz: **SKIP** Unfulfilled Conditions: is_variable_font

</details>
<details>
<summary>:zzz: <b>SKIP:</b> Check that variable fonts have an HVAR table. </summary>

* [com.google.fonts/check/varfont/has_HVAR](https://github.com/googlefonts/fontbakery/search?q=com.google.fonts/check/varfont/has_HVAR)
* :zzz: **SKIP** Unfulfilled Conditions: is_variable_font

</details>
<details>
<summary>:zzz: <b>SKIP:</b> All name entries referenced by fvar instances exist on the name table?</summary>

* [com.google.fonts/check/fvar_name_entries](https://github.com/googlefonts/fontbakery/search?q=com.google.fonts/check/fvar_name_entries)
* :zzz: **SKIP** Unfulfilled Conditions: is_variable_font

</details>
<details>
<summary>:zzz: <b>SKIP:</b> A variable font must have named instances.</summary>

* [com.google.fonts/check/varfont_has_instances](https://github.com/googlefonts/fontbakery/search?q=com.google.fonts/check/varfont_has_instances)
* :zzz: **SKIP** Unfulfilled Conditions: is_variable_font

</details>
<details>
<summary>:zzz: <b>SKIP:</b> Variable font weight coordinates must be multiples of 100.</summary>

* [com.google.fonts/check/varfont_weight_instances](https://github.com/googlefonts/fontbakery/search?q=com.google.fonts/check/varfont_weight_instances)
* :zzz: **SKIP** Unfulfilled Conditions: is_variable_font

</details>
<details>
<summary>:zzz: <b>SKIP:</b> FontForge validation outputs error messages?</summary>

* [com.google.fonts/check/038](https://github.com/googlefonts/fontbakery/search?q=com.google.fonts/check/038)
* :zzz: **SKIP** Unfulfilled Conditions: fontforge_check_results

</details>
<details>
<summary>:zzz: <b>SKIP:</b> FontForge checks.</summary>

* [com.google.fonts/check/039](https://github.com/googlefonts/fontbakery/search?q=com.google.fonts/check/039)
* :zzz: **SKIP** Unfulfilled Conditions: fontforge_check_results

</details>
<details>
<summary>:zzz: <b>SKIP:</b> CFF table FontName must match name table ID 6 (PostScript name).</summary>

* [com.adobe.fonts/check/postscript_name_cff_vs_name](https://github.com/googlefonts/fontbakery/search?q=com.adobe.fonts/check/postscript_name_cff_vs_name)
* :zzz: **SKIP** Unfulfilled Conditions: is_cff

</details>
<details>
<summary>:zzz: <b>SKIP:</b> The variable font 'wght' (Weight) axis coordinate must be 400 on the 'Regular' instance.</summary>

* [com.google.fonts/check/167](https://github.com/googlefonts/fontbakery/search?q=com.google.fonts/check/167)
* :zzz: **SKIP** Unfulfilled Conditions: is_variable_font, regular_wght_coord

</details>
<details>
<summary>:zzz: <b>SKIP:</b> The variable font 'wdth' (Width) axis coordinate must be 100 on the 'Regular' instance.</summary>

* [com.google.fonts/check/168](https://github.com/googlefonts/fontbakery/search?q=com.google.fonts/check/168)
* :zzz: **SKIP** Unfulfilled Conditions: is_variable_font, regular_wdth_coord

</details>
<details>
<summary>:zzz: <b>SKIP:</b> The variable font 'slnt' (Slant) axis coordinate must be zero on the 'Regular' instance.</summary>

* [com.google.fonts/check/169](https://github.com/googlefonts/fontbakery/search?q=com.google.fonts/check/169)
* :zzz: **SKIP** Unfulfilled Conditions: is_variable_font, regular_slnt_coord

</details>
<details>
<summary>:zzz: <b>SKIP:</b> The variable font 'ital' (Italic) axis coordinate must be zero on the 'Regular' instance.</summary>

* [com.google.fonts/check/170](https://github.com/googlefonts/fontbakery/search?q=com.google.fonts/check/170)
* :zzz: **SKIP** Unfulfilled Conditions: is_variable_font, regular_ital_coord

</details>
<details>
<summary>:zzz: <b>SKIP:</b> The variable font 'opsz' (Optical Size) axis coordinate should be between 9 and 13 on the 'Regular' instance.</summary>

* [com.google.fonts/check/171](https://github.com/googlefonts/fontbakery/search?q=com.google.fonts/check/171)
* :zzz: **SKIP** Unfulfilled Conditions: is_variable_font, regular_opsz_coord

</details>
<details>
<summary>:zzz: <b>SKIP:</b> The variable font 'wght' (Weight) axis coordinate must be 700 on the 'Bold' instance.</summary>

* [com.google.fonts/check/172](https://github.com/googlefonts/fontbakery/search?q=com.google.fonts/check/172)
* :zzz: **SKIP** Unfulfilled Conditions: is_variable_font, bold_wght_coord

</details>
<details>
<summary>:zzz: <b>SKIP:</b> The variable font 'wght' (Weight) axis coordinate must be within spec range of 1 to 1000 on all instances.</summary>

* [com.google.fonts/check/wght_valid_range](https://github.com/googlefonts/fontbakery/search?q=com.google.fonts/check/wght_valid_range)
* :zzz: **SKIP** Unfulfilled Conditions: is_variable_font

</details>
<details>
<summary>:information_source: <b>INFO:</b> Show hinting filesize impact.</summary>

* [com.google.fonts/check/054](https://github.com/googlefonts/fontbakery/search?q=com.google.fonts/check/054)
* :information_source: **INFO** Hinting filesize impact:

|  | fonts/encodesanssemicondensed/EncodeSansSemiCondensed-Medium.ttf |
|:--- | ---:|
| Dehinted Size | 118.5kb |
| Hinted Size | 155.0kb |
| Increase | 36.6kb |
| Change   | 30.9 % |


</details>
<details>
<summary>:information_source: <b>INFO:</b> EPAR table present in font?</summary>

* [com.google.fonts/check/061](https://github.com/googlefonts/fontbakery/search?q=com.google.fonts/check/061)
* :information_source: **INFO** EPAR table not present in font. To learn more see https://github.com/googlefonts/fontbakery/issues/818

</details>
<details>
<summary>:information_source: <b>INFO:</b> Is 'gasp' table set to optimize rendering?</summary>

* [com.google.fonts/check/062](https://github.com/googlefonts/fontbakery/search?q=com.google.fonts/check/062)
* :information_source: **INFO** These are the ppm ranges declared on the gasp table:

PPM <= 65535:
	flag = 0x0F
	- Use gridfitting
	- Use grayscale rendering
	- Use gridfitting with ClearType symmetric smoothing
	- Use smoothing along multiple axes with ClearType®

* :bread: **PASS** 'gasp' table is correctly set, with one gaspRange:value of 0xFFFF:0x0F.

</details>
<details>
<summary>:information_source: <b>INFO:</b> Check for font-v versioning </summary>

* [com.google.fonts/check/166](https://github.com/googlefonts/fontbakery/search?q=com.google.fonts/check/166)
* :information_source: **INFO** Version string is: "Version 3.000; ttfautohint (v1.8.2) -l 8 -r 50 -G 200 -x 14 -D latn -f none -a nnn -X """
The version string must ideally include a git commit hash and either a 'dev' or a 'release' suffix such as in the example below:
"Version 1.3; git-0d08353-release"

</details>
<details>
<summary>:information_source: <b>INFO:</b> Font contains all required tables?</summary>

* [com.google.fonts/check/052](https://github.com/googlefonts/fontbakery/search?q=com.google.fonts/check/052)
* :information_source: **INFO** This font contains the following optional tables [prep, cvt , GSUB, loca, GPOS, fpgm, DSIG, gasp]
* :bread: **PASS** Font contains all required tables.

</details>
<details>
<summary>:information_source: <b>INFO:</b> Font follows the family naming recommendations?</summary>

* [com.google.fonts/check/071](https://github.com/googlefonts/fontbakery/search?q=com.google.fonts/check/071)
* :information_source: **INFO** Font does not follow some family naming recommendations:

| Field | Value | Recommendation |
|:----- |:----- |:-------------- |
| Family Name | Encode Sans SemiCondensed Medium | exceeds max length (31) |


</details>
<details>
<summary>:bread: <b>PASS:</b> Checking file is named canonically.</summary>

* [com.google.fonts/check/001](https://github.com/googlefonts/fontbakery/search?q=com.google.fonts/check/001)
* :bread: **PASS** fonts/encodesanssemicondensed/EncodeSansSemiCondensed-Medium.ttf is named canonically.

</details>
<details>
<summary>:bread: <b>PASS:</b> Fonts have equal numbers of glyphs?</summary>

* [com.google.fonts/check/011](https://github.com/googlefonts/fontbakery/search?q=com.google.fonts/check/011)
* :bread: **PASS** All font files in this family have an equal total ammount of glyphs.

</details>
<details>
<summary>:bread: <b>PASS:</b> Fonts have equal glyph names?</summary>

* [com.google.fonts/check/012](https://github.com/googlefonts/fontbakery/search?q=com.google.fonts/check/012)
* :bread: **PASS** All font files have identical glyph names.

</details>
<details>
<summary>:bread: <b>PASS:</b> Checking OS/2 fsType.</summary>

* [com.google.fonts/check/016](https://github.com/googlefonts/fontbakery/search?q=com.google.fonts/check/016)
* :bread: **PASS** OS/2 fsType is properly set to zero.

</details>
<details>
<summary>:bread: <b>PASS:</b> Checking OS/2 achVendID.</summary>

* [com.google.fonts/check/018](https://github.com/googlefonts/fontbakery/search?q=com.google.fonts/check/018)
* :bread: **PASS** OS/2 VendorID 'GOOG' looks good!

</details>
<details>
<summary>:bread: <b>PASS:</b> Substitute copyright, registered and trademark symbols in name table entries.</summary>

* [com.google.fonts/check/019](https://github.com/googlefonts/fontbakery/search?q=com.google.fonts/check/019)
* :bread: **PASS** No need to substitute copyright, registered and trademark symbols in name table entries of this font.

</details>
<details>
<summary>:bread: <b>PASS:</b> Checking OS/2 usWeightClass.</summary>

* [com.google.fonts/check/020](https://github.com/googlefonts/fontbakery/search?q=com.google.fonts/check/020)
* :bread: **PASS** OS/2 usWeightClass value looks good!

</details>
<details>
<summary>:bread: <b>PASS:</b> Check copyright namerecords match license file.</summary>

* [com.google.fonts/check/029](https://github.com/googlefonts/fontbakery/search?q=com.google.fonts/check/029)
* :bread: **PASS** Licensing entry on name table is correctly set.

</details>
<details>
<summary>:bread: <b>PASS:</b> "License URL matches License text on name table?</summary>

* [com.google.fonts/check/030](https://github.com/googlefonts/fontbakery/search?q=com.google.fonts/check/030)
* :bread: **PASS** Font has a valid license URL in NAME table.

</details>
<details>
<summary>:bread: <b>PASS:</b> Description strings in the name table must not exceed 200 characters.</summary>

* [com.google.fonts/check/032](https://github.com/googlefonts/fontbakery/search?q=com.google.fonts/check/032)
* :bread: **PASS** All description name records have reasonably small lengths.

</details>
<details>
<summary>:bread: <b>PASS:</b> Version format is correct in 'name' table?</summary>

* [com.google.fonts/check/055](https://github.com/googlefonts/fontbakery/search?q=com.google.fonts/check/055)
* :bread: **PASS** Version format in NAME table entries is correct.

</details>
<details>
<summary>:bread: <b>PASS:</b> Font has ttfautohint params? </summary>

* [com.google.fonts/check/has_ttfautohint_params](https://github.com/googlefonts/fontbakery/search?q=com.google.fonts/check/has_ttfautohint_params)
* :bread: **PASS** Font has ttfautohint params (-l 8 -r 50 -G 200 -x 14 -D latn -f none -a nnn -X "")

</details>
<details>
<summary>:bread: <b>PASS:</b> Font has old ttfautohint applied?</summary>

* [com.google.fonts/check/056](https://github.com/googlefonts/fontbakery/search?q=com.google.fonts/check/056)
* :bread: **PASS** ttfautohint available in the system (1.8.2) is older than the one used in the font (1.8.2).

</details>
<details>
<summary>:bread: <b>PASS:</b> Make sure family name does not begin with a digit.</summary>

* [com.google.fonts/check/067](https://github.com/googlefonts/fontbakery/search?q=com.google.fonts/check/067)
* :bread: **PASS** Font family name first character is not a digit.

</details>
<details>
<summary>:bread: <b>PASS:</b> Font has all expected currency sign characters?</summary>

* [com.google.fonts/check/070](https://github.com/googlefonts/fontbakery/search?q=com.google.fonts/check/070)
* :bread: **PASS** Font has all expected currency sign characters.

</details>
<details>
<summary>:bread: <b>PASS:</b> Are there non-ASCII characters in ASCII-only NAME table entries?</summary>

* [com.google.fonts/check/074](https://github.com/googlefonts/fontbakery/search?q=com.google.fonts/check/074)
* :bread: **PASS** None of the ASCII-only NAME table entries contain non-ASCII characteres.

</details>
<details>
<summary>:bread: <b>PASS:</b> Stricter unitsPerEm criteria for Google Fonts. </summary>

* [com.google.fonts/check/116](https://github.com/googlefonts/fontbakery/search?q=com.google.fonts/check/116)
* :bread: **PASS** Font em size is good (unitsPerEm = 2000).

</details>
<details>
<summary>:bread: <b>PASS:</b> Checking OS/2 fsSelection value.</summary>

* [com.google.fonts/check/129](https://github.com/googlefonts/fontbakery/search?q=com.google.fonts/check/129)
* :bread: **PASS** OS/2 fsSelection REGULAR bit is properly set.
* :bread: **PASS** OS/2 fsSelection ITALIC bit is properly set.
* :bread: **PASS** OS/2 fsSelection BOLD bit is properly set.

</details>
<details>
<summary>:bread: <b>PASS:</b> Checking post.italicAngle value.</summary>

* [com.google.fonts/check/130](https://github.com/googlefonts/fontbakery/search?q=com.google.fonts/check/130)
* :bread: **PASS** Value of post.italicAngle is 0.0 with style='Medium'.

</details>
<details>
<summary>:bread: <b>PASS:</b> Checking head.macStyle value.</summary>

* [com.google.fonts/check/131](https://github.com/googlefonts/fontbakery/search?q=com.google.fonts/check/131)
* :bread: **PASS** head macStyle ITALIC bit is properly set.
* :bread: **PASS** head macStyle BOLD bit is properly set.

</details>
<details>
<summary>:bread: <b>PASS:</b> Font has all mandatory 'name' table entries ?</summary>

* [com.google.fonts/check/156](https://github.com/googlefonts/fontbakery/search?q=com.google.fonts/check/156)
* :bread: **PASS** Font contains values for all mandatory name table entries.

</details>
<details>
<summary>:bread: <b>PASS:</b> Check name table: FONT_SUBFAMILY_NAME entries. </summary>

* [com.google.fonts/check/158](https://github.com/googlefonts/fontbakery/search?q=com.google.fonts/check/158)
* :bread: **PASS** FONT_SUBFAMILY_NAME entries are all good.

</details>
<details>
<summary>:bread: <b>PASS:</b> Check name table: TYPOGRAPHIC_SUBFAMILY_NAME entries. </summary>

* [com.google.fonts/check/162](https://github.com/googlefonts/fontbakery/search?q=com.google.fonts/check/162)
* :bread: **PASS** TYPOGRAPHIC_SUBFAMILY_NAME entries are all good.

</details>
<details>
<summary>:bread: <b>PASS:</b> Length of copyright notice must not exceed 500 characters. </summary>

* [com.google.fonts/check/164](https://github.com/googlefonts/fontbakery/search?q=com.google.fonts/check/164)
* :bread: **PASS** All copyright notice name entries on the 'name' table are shorter than 500 characters.

</details>
<details>
<summary>:bread: <b>PASS:</b> Checking OS/2 usWinAscent & usWinDescent.</summary>

* [com.google.fonts/check/040](https://github.com/googlefonts/fontbakery/search?q=com.google.fonts/check/040)
* :bread: **PASS** OS/2 usWinAscent & usWinDescent values look good!

</details>
<details>
<summary>:bread: <b>PASS:</b> Checking OS/2 Metrics match hhea Metrics.</summary>

* [com.google.fonts/check/042](https://github.com/googlefonts/fontbakery/search?q=com.google.fonts/check/042)
* :bread: **PASS** OS/2.sTypoAscender/Descender values match hhea.ascent/descent.

</details>
<details>
<summary>:bread: <b>PASS:</b> Font enables smart dropout control in "prep" table instructions?</summary>

* [com.google.fonts/check/072](https://github.com/googlefonts/fontbakery/search?q=com.google.fonts/check/072)
* :bread: **PASS** 'prep' table contains instructions enabling smart dropout control.

</details>
<details>
<summary>:bread: <b>PASS:</b> There must not be VTT Talk sources in the font.</summary>

* [com.google.fonts/check/vttclean](https://github.com/googlefonts/fontbakery/search?q=com.google.fonts/check/vttclean)
* :bread: **PASS** There are no tables with VTT Talk sources embedded in the font.

</details>
<details>
<summary>:bread: <b>PASS:</b> Are there unwanted Apple tables?</summary>

* [com.google.fonts/check/aat](https://github.com/googlefonts/fontbakery/search?q=com.google.fonts/check/aat)
* :bread: **PASS** There are no unwanted AAT tables.

</details>
<details>
<summary>:bread: <b>PASS:</b> PPEM must be an integer on hinted fonts.</summary>

* [com.google.fonts/check/integer_ppem_if_hinted](https://github.com/googlefonts/fontbakery/search?q=com.google.fonts/check/integer_ppem_if_hinted)
* :bread: **PASS** OK

</details>
<details>
<summary>:bread: <b>PASS:</b> Checking with ftxvalidator.</summary>

* [com.google.fonts/check/035](https://github.com/googlefonts/fontbakery/search?q=com.google.fonts/check/035)
* :bread: **PASS** ftxvalidator passed this file

</details>
<details>
<summary>:bread: <b>PASS:</b> Checking with ots-sanitize.</summary>

* [com.google.fonts/check/036](https://github.com/googlefonts/fontbakery/search?q=com.google.fonts/check/036)
* :bread: **PASS** ots-sanitize passed this file

</details>
<details>
<summary>:bread: <b>PASS:</b> Font contains .notdef as first glyph?</summary>

* [com.google.fonts/check/046](https://github.com/googlefonts/fontbakery/search?q=com.google.fonts/check/046)
* :bread: **PASS** Font contains the .notdef glyph as the first glyph, it does not have a Unicode value assigned and contains a drawing.

</details>
<details>
<summary>:bread: <b>PASS:</b> Font contains glyphs for whitespace characters?</summary>

* [com.google.fonts/check/047](https://github.com/googlefonts/fontbakery/search?q=com.google.fonts/check/047)
* :bread: **PASS** Font contains glyphs for whitespace characters.

</details>
<details>
<summary>:bread: <b>PASS:</b> Font has **proper** whitespace glyph names?</summary>

* [com.google.fonts/check/048](https://github.com/googlefonts/fontbakery/search?q=com.google.fonts/check/048)
* :bread: **PASS** Font has **proper** whitespace glyph names.

</details>
<details>
<summary>:bread: <b>PASS:</b> Whitespace glyphs have ink?</summary>

* [com.google.fonts/check/049](https://github.com/googlefonts/fontbakery/search?q=com.google.fonts/check/049)
* :bread: **PASS** There is no whitespace glyph with ink.

</details>
<details>
<summary>:bread: <b>PASS:</b> Are there unwanted tables?</summary>

* [com.google.fonts/check/053](https://github.com/googlefonts/fontbakery/search?q=com.google.fonts/check/053)
* :bread: **PASS** There are no unwanted tables.

</details>
<details>
<summary>:bread: <b>PASS:</b> Glyph names are all valid?</summary>

* [com.google.fonts/check/058](https://github.com/googlefonts/fontbakery/search?q=com.google.fonts/check/058)
* :bread: **PASS** Glyph names are all valid.

</details>
<details>
<summary>:bread: <b>PASS:</b> Font contains unique glyph names?</summary>

* [com.google.fonts/check/059](https://github.com/googlefonts/fontbakery/search?q=com.google.fonts/check/059)
* :bread: **PASS** Font contains unique glyph names.

</details>
<details>
<summary>:bread: <b>PASS:</b> Checking with fontTools.ttx</summary>

* [com.google.fonts/check/ttx-roundtrip](https://github.com/googlefonts/fontbakery/search?q=com.google.fonts/check/ttx-roundtrip)
* :bread: **PASS** Hey! It all looks good!

</details>
<details>
<summary>:bread: <b>PASS:</b> Check all glyphs have codepoints assigned.</summary>

* [com.google.fonts/check/077](https://github.com/googlefonts/fontbakery/search?q=com.google.fonts/check/077)
* :bread: **PASS** All glyphs have a codepoint value assigned.

</details>
<details>
<summary>:bread: <b>PASS:</b> Checking unitsPerEm value is reasonable.</summary>

* [com.google.fonts/check/043](https://github.com/googlefonts/fontbakery/search?q=com.google.fonts/check/043)
* :bread: **PASS** unitsPerEm value (2000) on the 'head' table is reasonable.

</details>
<details>
<summary>:bread: <b>PASS:</b> Checking font version fields (head and name table).</summary>

* [com.google.fonts/check/044](https://github.com/googlefonts/fontbakery/search?q=com.google.fonts/check/044)
* :bread: **PASS** All font version fields match.

</details>
<details>
<summary>:bread: <b>PASS:</b> Check if OS/2 xAvgCharWidth is correct.</summary>

* [com.google.fonts/check/034](https://github.com/googlefonts/fontbakery/search?q=com.google.fonts/check/034)
* :bread: **PASS** OS/2 xAvgCharWidth value is correct.

</details>
<details>
<summary>:bread: <b>PASS:</b> Font has correct post table version (2 for TTF, 3 for OTF)?</summary>

* [com.google.fonts/check/015](https://github.com/googlefonts/fontbakery/search?q=com.google.fonts/check/015)
* :bread: **PASS** Font has post table version 2.

</details>
<details>
<summary>:bread: <b>PASS:</b> Description strings in the name table must not contain copyright info.</summary>

* [com.google.fonts/check/031](https://github.com/googlefonts/fontbakery/search?q=com.google.fonts/check/031)
* :bread: **PASS** Description strings in the name table do not contain any copyright string.

</details>
<details>
<summary>:bread: <b>PASS:</b> Checking correctness of monospaced metadata.</summary>

* [com.google.fonts/check/033](https://github.com/googlefonts/fontbakery/search?q=com.google.fonts/check/033)
* :bread: **PASS** Font is not monospaced and all related metadata look good. [code: good]

</details>
<details>
<summary>:bread: <b>PASS:</b> Name table entries should not contain line-breaks.</summary>

* [com.google.fonts/check/057](https://github.com/googlefonts/fontbakery/search?q=com.google.fonts/check/057)
* :bread: **PASS** Name table entries are all single-line (no line-breaks found).

</details>
<details>
<summary>:bread: <b>PASS:</b> Checking Vertical Metric Linegaps.</summary>

* [com.google.fonts/check/041](https://github.com/googlefonts/fontbakery/search?q=com.google.fonts/check/041)
* :bread: **PASS** OS/2 sTypoLineGap and hhea lineGap are both 0.

</details>
<details>
<summary>:bread: <b>PASS:</b> MaxAdvanceWidth is consistent with values in the Hmtx and Hhea tables?</summary>

* [com.google.fonts/check/073](https://github.com/googlefonts/fontbakery/search?q=com.google.fonts/check/073)
* :bread: **PASS** MaxAdvanceWidth is consistent with values in the Hmtx and Hhea tables.

</details>
<details>
<summary>:bread: <b>PASS:</b> Does the font have a DSIG table?</summary>

* [com.google.fonts/check/045](https://github.com/googlefonts/fontbakery/search?q=com.google.fonts/check/045)
* :bread: **PASS** Digital Signature (DSIG) exists.

</details>
<details>
<summary>:bread: <b>PASS:</b> Whitespace and non-breaking space have the same width?</summary>

* [com.google.fonts/check/050](https://github.com/googlefonts/fontbakery/search?q=com.google.fonts/check/050)
* :bread: **PASS** Whitespace and non-breaking space have the same width.

</details>
<details>
<summary>:bread: <b>PASS:</b> Does GPOS table have kerning information?</summary>

* [com.google.fonts/check/063](https://github.com/googlefonts/fontbakery/search?q=com.google.fonts/check/063)
* :bread: **PASS** GPOS table has got kerning information.

</details>
<details>
<summary>:bread: <b>PASS:</b> Are there caret positions declared for every ligature?</summary>

* [com.google.fonts/check/064](https://github.com/googlefonts/fontbakery/search?q=com.google.fonts/check/064)
* :bread: **PASS** Looks good!

</details>
<details>
<summary>:bread: <b>PASS:</b> Is there a "kern" table declared in the font?</summary>

* [com.google.fonts/check/066](https://github.com/googlefonts/fontbakery/search?q=com.google.fonts/check/066)
* :bread: **PASS** Font does not declare an optional "kern" table.

</details>
<details>
<summary>:bread: <b>PASS:</b> Is there any unused data at the end of the glyf table?</summary>

* [com.google.fonts/check/069](https://github.com/googlefonts/fontbakery/search?q=com.google.fonts/check/069)
* :bread: **PASS** There is no unused data at the end of the glyf table.

</details>
<details>
<summary>:bread: <b>PASS:</b> Check for points out of bounds.</summary>

* [com.google.fonts/check/075](https://github.com/googlefonts/fontbakery/search?q=com.google.fonts/check/075)
* :bread: **PASS** All glyph paths have coordinates within bounds!

</details>
<details>
<summary>:bread: <b>PASS:</b> Does the number of glyphs in the loca table match the maxp table?</summary>

* [com.google.fonts/check/180](https://github.com/googlefonts/fontbakery/search?q=com.google.fonts/check/180)
* :bread: **PASS** 'loca' table matches numGlyphs in 'maxp' table.

</details>
<br>
</details>

### Summary

| :broken_heart: ERROR | :fire: FAIL | :warning: WARN | :zzz: SKIP | :information_source: INFO | :bread: PASS |
|:-----:|:----:|:----:|:----:|:----:|:----:|
| 2 | 6 | 5 | 54 | 6 | 70 |
| 1% | 4% | 3% | 38% | 4% | 49% |
