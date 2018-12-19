unix:!macx {
	isEmpty(PREFIX) {
		PREFIX = /usr
	}

	target.path = $${PREFIX}/bin

	icon.path = $${PREFIX}/share/pixmaps
	icon.files = pictures/vokoscreen.png

	desktop.path = $${PREFIX}/share/applications
	desktop.files = applications/vokoscreen.desktop

	INSTALLS += target icon desktop
}
