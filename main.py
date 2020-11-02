from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
import lxml
import os
from prntsc.generate_urls import generate_urls


def main():
	check_dir()
	urls = generate_urls(10)
	for url in urls:
		load_url(url)

def check_dir():
	"""
	If /imgs/ directory doesn't exist, one will be created in the current directory.
	"""
	cwd = os.getcwd()
	savedir = cwd + "/imgs"
	if not os.path.exists(savedir):
		print("Image save directory does not exist, making folder: 'imgs'\n")
		os.makedirs(savedir)

def load_url(url):
	"""
	Scrapes the image URL from the webpage and sends the url to save_img() to be saved.
	"""
	path = os.getcwd() + "/imgs/"
	file_ext = ".png"
	req = Request(url, headers={"User-Agent":"Mozilla/5.0"})
	webpage = urlopen(req).read()
	soup = BeautifulSoup(webpage, "lxml")
	img = soup.find("img", {"class":"no-click screenshot-image"}).get("src")
	if not img.startswith("https://image.prntscr.com/image/"):
		newurl = generate_urls(1)[0]
		return load_url(newurl)

	save_img(img, f"{url[-6:]}{file_ext}", path)

def save_img(img, filename, path):
	"""
	Opens the image URL and saves the image.
	"""
	print(f"Loading <{filename}>...")
	req = Request(img, headers={"User-Agent":"Mozilla/5.0"})
	webpage = urlopen(req).read()
	with open(path+filename, "wb") as f:
		f.write(webpage)
	print(f"Success.\n")


if __name__ == "__main__":
	print("\n")
	main()
	print("\n")