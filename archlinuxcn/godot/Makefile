.PHONY: get-checksum
get-checksum:
	updpkgsums

.PHONY: update
update: get-checksum
	makepkg --printsrcinfo > .SRCINFO

# you may want to do a setup previous to use this target
# follow https://wiki.archlinux.org/index.php/DeveloperWiki:Building_in_a_clean_chroot#Classic_way
.PHONY: build
build:
	@echo "updating ${CHROOT}/root chroot environment..."
	@arch-nspawn ${CHROOT}/root pacman -Syu
	@echo "building package in isolation"
	makechrootpkg -c -r ${CHROOT}
