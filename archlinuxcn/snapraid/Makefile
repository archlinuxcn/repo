srcfile:
	makepkg --printsrcinfo > .SRCINFO

checksums:
	updpkgsums

build:
	makepkg -C -f --noconfirm

clean:
	rm -rf pkg src snapraid*
