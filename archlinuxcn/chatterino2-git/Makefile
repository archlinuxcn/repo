.PHONY: all

all: clean rebuild srcinfo chroot-rebuild

rebuild:
	makepkg -s


chroot-rebuild:
	@ [ -n "${CHROOT}" ] && \
		echo "Creating chroot in ${CHROOT}" && \
		[ -d "${CHROOT}/root" ] || mkarchroot "${CHROOT}/root" base-devel && \
		arch-nspawn "${CHROOT}/root" pacman -Syu && \
		makechrootpkg -c -r "${CHROOT}" || \
		echo "export the CHROOT environment variable if you want to use chroot-rebuild"

srcinfo:
	makepkg --printsrcinfo > .SRCINFO

clean:
	rm -rf \
		pkg \
		src \
		chatterino2 \
		chatterino2-*.pkg.tar.xz \
		chatterino2-*.pkg.tar.zst \
		chatterino2-*.log \
		libcommuni \
		humanize \
		crash-handler \
		settings \
		signals \
		serialize \
		rapidjson \
		qtkeychain \
		sanitizers-cmake \
		websocketpp \
		magic_enum \
		miniaudio
