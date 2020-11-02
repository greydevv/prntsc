# prntsc

`prntsc` is a Python web-scraper that downloads images from `prnt.sc`.

This script will generate a variable amount of URLs and download the screenshot from that URL. URLs are generated by concatenating two random letters and four random numbers to the base URL (`https://prnt.sc/`).
 
### Example

If five URLs are to be generated:
```
https://prnt.sc/ci8242
https://prnt.sc/jg6886
https://prnt.sc/ky4487
https://prnt.sc/pc5572
https://prnt.sc/si9988
```
The image on each of these URLs will then be opened and saved.