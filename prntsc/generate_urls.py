from string import ascii_lowercase
from random import choice

def generate_urls(n):
	"""
	Generates a list of URLs by concatenating two random letters followed by four random numbers to the end of the URL prefix.
	"""
	prefix = "https://prnt.sc/"
	urls = []
	i = 0
	while i < n:
		chars = [choice(ascii_lowercase) for _ in range(2)]
		nums = [str(choice(range(10))) for _ in range(4)]
		img = "".join(chars+nums)
		url = f"{prefix}{img}"
		if url not in urls:
			urls.append(url)
			i += 1
	return urls