# Freya

> Tadeusz Wachowski | November 16th, 2021

This is a list of tools collected or written by me to help the CTF community with different challenges.

---

# Table of contents

1. [Cryptography](#cryptography)
2. [Forensics](#forensics)


## Cryptography

* [CyberChef](https://gchq.github.io/CyberChef/)

	Work with Base64, XOR, Hex etc.

* [factordb](http://factordb.com)
	
	Find `p` and `q` knowing `n`.

* [crackstation](https://crackstation.net/)

	Recover password from hash.

* [dcode.fr](https://www.dcode.fr/en)

	Encrypt and decrypt pretty much every cipher there is.

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
