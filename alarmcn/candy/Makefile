default:
	updpkgsums
	makepkg --printsrcinfo > .SRCINFO
	makepkg -si

clean:
	rm -rf *.pkg.tar.zst *.tar.gz pkg src
