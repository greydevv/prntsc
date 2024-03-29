# prntsc

`prntsc` is a Python web-scraper that downloads images from `prnt.sc`.

This script will generate a specified amount of URLs and download the screenshot from that URL. URLs are generated by concatenating two random letters and four random numbers to the base URL (`https://prnt.sc/`).

### Usage

This repository is no longer actively maintained. The most recent supported Python is `Python 3.8`.


From terminal, run `python3.8 main.py`, followed by the number of images to be generated.

To generate five images:
```
python main.py 5
```

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

### Disclaimer

Neither I nor this script are affiliated with `prnt.sc` in any way, shape, or form. With that being said, this script will not decide if an image is appropriate or not for some users. Keeping this in mind, ***viewer/user discretion advised***. I am **not** responsible for how this script is used.
