.PHONY: all

all: clean rebuild srcinfo

rebuild:
	makepkg -s

srcinfo:
	makepkg --printsrcinfo > .SRCINFO

clean:
	rm -rf pkg src chatterino2/ chatterino2-*.pkg.tar.xz \
		libcommuni \
		humanize \
		qBreakpad \
		WinToast \
		settings \
		signals \
		serialize \
		rapidjson \
		qtkeychain \
		websocketpp
