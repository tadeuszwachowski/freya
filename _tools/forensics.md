---
layout: writeup
title: "forensics"
---

## Forensics

* [stegoveritas](https://github.com/bannsec/stegoVeritas)

	Find all kinds of hidden data in files.

	Install with:
	```
	$ pip3 install stegoveritas
	$ stegoveritas_install_deps
	```
	
	Usage:

	`stegoveritas [file]`

* [zsteg](https://github.com/zed-0xff/zsteg)

	Analyze the image in various ways to find the embedded flag. Solves most of the easy challenges.

	Install with:
	```
	gem install zsteg
	``` 

	Useful commands:

	`zsteg -a [file]` - try all methods on the given file

	`zsteg -E [options] [file]` - extract data from the file

* [foremost](https://github.com/korczis/foremost)

	Extract embedded images.

	Install with:
	```
	apt install foremost
	```

	Useful commands:

	`foremost -i [file]` - extracts all files hidden within the file

* [binwalk](https://github.com/ReFirmLabs/binwalk)

	Analyze and extract data from images.

	Install with:
	```
	apt install binwalk
	```

	Useful commands:

	`binwalk [file]` - only display the data
	`binwalk -e [file]` - display and extract the data

* [stegsolve](https://github.com/zardus/ctf-tools/blob/master/stegsolve/install)

	Analyze the image color planes, invert colors and many more.

* [steghide](https://github.com/StefanoDeVuono/steghide)

	Hide or extract data from `JPEG, BMP and WAV` files.
	Useful commands:
	`steghide info [file]` - checks if the file contains hidden data
	`steghide extract -sf [file]` - extract hidden data

* [file headers](https://github.com/corkami/pics)

	Recover file header, CRC and more!
