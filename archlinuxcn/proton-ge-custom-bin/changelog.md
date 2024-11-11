## GE-Proton9-20

Hotfix:
- Revert DRI_PRIME auto-setting (broke too many non-standard setups)
- DXVK updated with dxvk.hideIntegratedGraphics = True for Diablo IV (doitsujin/dxvk@125f0ac) to resolve the grey screen issue on systems with AMD iGPU + dGPU.


## GE-Proton9-19

- bump wine to latest bleeding edge
- bump dxvk to latest git
- bump vkd3d-proton to latest git (contains additional MH Wilds fix)
- bump dxvk-nvapi to latest git
- import upstream lsteamclient changes
- import upstream vrclient changes
- add xdefiant patch (thanks tperalta82)
- auto-apply DRI_PRIME=1 when more than one gpu is detected. This allows Diablo IV to get passed the grey screen on igpu+dgpu systems.
- add protonfixes for silent hill 3 video playback
- add protonfixes for Horizon Zero Dawn Remastered internet connection (thanks UsernamesAreNotMyThing)

## GE-Proton9-18

Hotfix:
- Add missing proton script python uuid import (which broke prefix creation)


## GE-Prooton-17

Proton:
- wine updated to latest bleeding edge
- dxvk updated to latest git
- vkd3d-proton updated to latest git
- dxvk-nvapi updated to latest git
- ICU building + linking imported from upstream
- misc proton script fixes imported from upstream

Protonfixes:
- Audio fix for Mini Ninjas (thanks UsernamesAreNotMyThing)
- Fix typo'd mod support for ES: Oblivion (thanks MaxBosse)
- Disable esync/fsync in Disgaea 4 to prevent crash (thanks UsernamesAreNotMyThing)

Nothing major here, just a refresh of various parts that need updates from git, mostly to add new video playback fixes from upstream proton.

## GE-Proton9-16

Proton:

- import upstream makefile changes
- import upstream proton changes
- import upstream steam_helper changes
- import upstream vkd3d-shader changes
- update wine to latest bleeding edge
- updated dxvk to latest git
- update vkd3d-proton to latest git
- update dxvk-nvapi to e4bad70

Protonfixes:

- fixed issue with game_titles not being pulled correctly for UMU
- game_titles are now looked up as part of included umu-database csv instead of trying to send online website api call
- games run with UMU will now have /mnt,/run/media,/media/, and the user's home folder added as drives u:,v:,w:,x: respectively inside the prefix if they are not empty. This is to allow users to install or import games outside of the prefix more conveniently. A typical scenario for this would be if you have your games pre-installed on a different mounted drive, or somewhere else in your home folder outside of the prefix and you want to add them without reinstalling the game, OR if you want to install the game to one of those mounts instead of the C:\ drive inside the wine prefix. With steam, users don't really have to worry about this because steam handles the drive mounts and the install locations, however we found that outside of steam users were trying to use the Z: drive (which is symlinked to root (/)) -- which is of course containerized and read only, and therefore also unable to provide a proper drive size, resulting in users being told they don't have enough space. With the new drives added into the prefix it should fix this, allowing users to access their mount locations or existing game folders for installation or importing via the new drives instead of Z:.
- Mod support for various bethesda games has been added (Thanks Root-Core). If a mod executable is found for bethesda games it will launch the mod executable instead of the original:
 mapping = {
 '22380': ('FalloutNV.exe', 'nvse_loader.exe'), # Fallout New Vegas
 '22370': ('FalloutLauncher.exe', 'fose_loader.exe'), # Fallout 3
 '377160': ('Fallout4Launcher.exe', 'f4se_loader.exe'), # Fallout 4
 '22330': ('OblivionLauncher.exe', 'obse_loader.exe'), # Oblivion
 '72850': ('SkyrimLauncher.exe', 'skse_loader.exe'), # Skyrim
 '489830': ('SkyrimSELauncher.exe', 'skse64_loader.exe'), # Skyrim SE
 '1716740': ('Starfield.exe', 'sfse_loader.exe') # Starfield
 }.get(game_id, ('', ''))
- protonfix added for metal gear solid 2 (thanks FranjeGueje)
- protonfix for Kindom Hearts HD Remix added for steam version (already existed for egs version) (thanks Internetbestfriend)
- protonfix added for Gothic Playable Teaser (thanks Root-Core)
- Star Citizen protonfix updated (no longer requires EAC workaround)


## GE-Proton9-15

Hotfix build:

Proton:

- Updated wine to latest bleeding edge -- fixes regression in video playback from 9-14
- Updated dxvk to latest git -- fixes regression which causes black textures and stuttering on NVIDIA cards.
- Updated vkd3d-proton to latest git
- import upstream changes for lsteamclient
- update xalia to 0.4.4

Protonfixes:

- Remove deprecated workaround for Total War Rome 2


## GE-Proton9-14

Proton:

- Update wine to latest bleeding edge
- Update dxvk to latest git
- Update vkd3d-proton to latest git
- Update dxvk-nvapi to latest git
- Import upstream proton changes
- Update mono to 9.3.0
- Rebase wine-staging

Protonfixes:

- Added god of war ragnarok SteamDeck=1 workaround (thanks UserNamesAreNotMyThing)
- Added Star Citizen libcuda nvidia fix (thanks ProjectSynchro)
- Added fix for Plain Site (thanks iodream)
- Added fix for Worms: Blast (thanks iodream)
- Remove deprecated Sleeping Dogs: DE fix
- winetricks now built from source
- Elden Ring fix updated (thanks UserNamesAreNotMyThing)

## GE-Proton9-13

Hotfix:

- Update vkd3d-proton to latest git to include World of Warcraft MSAA fix

proton:

- wine updated to latest bleeding edge
- dxvk updated to latest git
- proton upstream fixes added

Additional:

- protonfixes updated to latest git

## GE-Proton9-12

- added latest upstream proton changes
- added latest upstream steamclient changes
- updated wine to latest bleeding edge
- updated dxvk to latest git
- updated vkd3d to latest git

protonfixes:

- libmspack, xrandr, cabextract are now built as part of the proton-ge build process instead of being included as prebuilt binaries (thanks R1kaB3rN)
- winetricks updated to latest git
- star citizen protonfix updated (thanks marcan)
- fix added for Full Metal Daemon Muramasa (thanks R1kaB3rN)
- fix install location of xlive.dll for xliveless (thanks ProjectSynchro)
- add fix for Bully: Scholarship edition (thanks Root-Core)
- add fix for Dirt 2 (thanks ProjectSynchro)
- add fix for CYGNI: All Guns Blazing (thanks Root-Core)

## GE-Proton9-11

- Update wine to latest bleeding edge
- Update dxvk to latest git
- Update vkd3d-proton to latest git
- Import upstream proton changes
- Rebase staging
- Add xinput patch for Dragon Age: Inquisition ( thanks cammoore1 )

Protonfixes:

- Add protonfix and steamgameid envvar to trigger Dragon Age: Inquisition xinput patch (allows to work with EA version in umu)
- Add protonfix for Flowers - Le Volume series (thanks R1kaB3rN)
- Add protonfix for The Last Blade (thanks ranplayer)
- Add protonfix for GOG Beyond Good and Evil (thanks ImLinguin)
- Add protonfix for WRC4 (thanks ToRRen1812)

## GE-Proton9-10

- Updated wine to latest bleeding edge
- Updated wine-mono to 9.2.0
- Updated dxvk to latest git (which includes d8vk now)
- Removed d8vk build options as it's part of dxvk now
- Updated proton script so that d8vk is enabled by default as part of dxvk's files
- Updated vkd3d-proton to latest git
- protonfixes: added EAC fix to allow elden ring to run even if dlc not owned

## GE-Proton9-9

Hotfix:
- When I updated winetricks in 9-8 I forgot to make it executable. This fixes it so winetricks is executable again.


## GE-Proton9-8

- wine updated to latest bleeding edge
- dxvk updated to latest git
- vkd3ed-proton updated to latest git
- dxvk-nvapi updated to latest git
- steam client changes pulled in from upstream
- vrclient changes pulled in from upstream
- various game quirk fixes pulled in from upstream (Farlight 84, MultiVersus, Bad Mojo Redux, (Arcanum: Of Steamworks and Magick Obscura)
- umu clients can now run winetricks verbs (Thanks R1kaB3rN)
- added pending patch for DXGI_FORMAT_R8G8B8A8_UNORM on d2d_wic_render_target_init needed for Alt:V -- GTA V custom client (Thanks S0P4)
- staging patches rebased (minor)
- fsr patch rebased (minor)
- protonfixes: winetricks updated to current git
- protonfixes: winetricks vcrun2022 sha256 hashes updated for vcrun2022 (Winetricks/winetricks#2235)
- protonfixes: fix added for Contractors VR (thanks ToRRent1812)
- protonfixes: fix added for gog: resident evil (thanks ImLinguin and keenanweaver)

## GE-Proton9-7

HOTFIXES:
- update FSR patchset, to fix colour issue on HD Graphics 630 (thanks loathingKernel)
- proton: Fix typo for calling winetricks gui with protontricks (thanks R1kaB3rN)
- steam_helper: import upstream changes
- build: import upstream changes
- dxvk: update dxvk
- wine: update bleeding edge -- Adds FULLSCREEN_PRESERVE_WINDOW_SIZE option to enable fullscreen workaround for preserving window size.


## GE-Proton9-6

Nothing too crazy with this release, mostly just importing upstream changes from Valve this time around.

- Persona 4 Golden video fixes have been re-added.
- wine updated to latest bleeding edge
- dxvk updated to latest git
- vkd3d-proton updated to latest git
- upstream proton changes added
- upstream steamclient changes added
- upstream wineopenxr changes added


## GE-Proton9-5

- added TCP_KEEP patches needed for Star Citizen 2.0 launcher
- updated wine to latest bleeding edge (fixes Apex Legends)
- updated dxvk to latest git
- updated vkd3d-proton to latest git
- updated dxvk-nvapi to match upstream
- updated various build files to match upstream
- updated steam client to match upstream
- added upstream cpu topology fixes
- protonfixes: Add fix for The Witcher 2: Assassins of Kings Enhanced Edition (thanks R1kaB3rN)
- protonfixes: Add fix for COJ Gunslinger (thanks Tiagoquix)
- protonfixes: Add fix for Total War: Shogun 2 (thanks Crumb5)
- protonfixes: Update Oddworld: Munch's Oddysee fix (thanks doZenn)
- protonfixes: Add fix for Oddworld: Abe's Oddysee (thanks doZenn)
- protonfixes: Add fix for Overlord II (thanks doZenn)
- protonfixes: Add fix for Stranger's Wrath HD (thanks doZenn)
- protonfixes: Add fix for Ducati World Championship (thanks doZenn)
- protonfixes: Add fix for Add fix for Café Stella and the Reaper's Butterflies (thanks R1kaB3rN)
- protonfixes: Add fix for Add fix for Sabbat of the Witch (thanks R1kaB3rN)
- protonfixes: Add fix for Add fix for Riddle Joker (thanks R1kaB3rN)
- protonfixes: Add fix for Add fix for Senren * Banka (thanks R1kaB3rN)
- protonfixes: Add fix for (Newest) Many WMP9 Video Playback fixes for Yuzusoft VN's (thanks R1kaB3rN)

## GE-Proton9-4

- hotfix: fix issue with protonfixes not getting applied (R1kaB3rN)
- vkd3d-proton: update to work around halo infinite bug HansKristian-Work/vkd3d-proton@1d73fdc

## GE-Proton9-3

    COPYPREFIX=1 option added. What this does:

By default steam stores the wine prefixes in the steam library where the game is installed under SteamLibrary/steamapps/compatdata/ as well as shader cache files in shadercache/. When 'Steam Deck' session aka gamescope session is used, the -steamdeck option is appended to steam. This causes the default path for prefix compatdata and shadercache to change to the default steam install location ~/.steam/steam/steamapps/compatdata (or shadercache). This can be problematic if you are say for example switching from normal desktop steam to steamdeck. Or for example if you have a portable hard drive or SD card you keep your games on to use between the two. If you did something like say install mods for a game or played a game that doesnt work with cloud saves on the desktop, the prefix would not get used when you move the drive over from the desktop to steamdeck. Instead steamdeck would try to make a new one. The same goes in reverse for if you play games on the steam deck and try to move the game drive or sd card to a desktop.

What COPYPREFIX=1 DOES is if -steamdeck is applied it will check if a prefix exists on the game partition/drive. If it does, it will then WIPE the steamdeck prefix, and replace it with the one from the game partition/drive. . It does this with shader cache as well. This way steam will pick up your mods/saves that you had on your desktop or other PC you used the drive on before.

Alternatively, if -steamdeck is NOT applied -- it works in reverse. It will try to wipe the prefix on the game partition, and replace it with the one in steamdeck's default location. It does this with shader cache as well. A good use case for the reverse of the desktop -- say you've put in a ton of hours on a game with saves that don't work with steam cloud saving -- or have a bunch of mods you've applied on a game on your steam deck -- then you want to migrate to your desktop. In this case, put steam in desktop mode. Close steam then re-open it from the terminal using the steam command so that -steamdeck is NOT applied, then you can use COPYPREFIX to copy the steamdeck prefix to your game's partition/drive.

Again to clarify usage scenarios:

Steam launched in deck mode (-steamdeck applied) or from terminal with -steamdeck = copy FROM game partition prefix TO steamdeck prefix

OR

Steam launched from desktop shortcut or terminal without -steamdeck -- copy FROM steamdeck prefix TO game partition prefix.

How to use:

Put COPYPREFIX=1 %command% in the game launch options. When you run the game it will copy the prefix. You can remove the option afterwards.

Please be careful when using this, it wipes the destination prefix contents before copying.

Other updates:
-wine updated to latest bleeding edge
-dxvk updated to latest git
-vkd3d-proton updated to latest git
-imported upstream proton changes
-imported upstream steamclient changes

Protonfixes:

    Add XAudio 2.9 verb for Space Engineers
    Update Cease to Breathe fix
    fix audio for in-game videos YOU and ME and HER: A Love Story
    Game fix for Fallout 76 -- this one needs a double check. It adds faudio to the prefix, but faudio is already built into proton's wine. Not sure if this is still needed.

UMU:

    add a way to run winetricks within proton on the fly
    Many refactors in protofixes by R1kaB3rN and Root-Core


## GE-Proton9-2

- wine updated to latest bleeding edge
- dxvk updated to latest git
- vkd3d-proton updated to latest git
- dxvk-nvapi updated to latest git
- upstream proton changes added
- upstream steamclient changes added
- ULWGL-protonfixes renamed to umu-protonfixes per upstream project
- previous noted wmv playback regression appears to be fixed now -- working with ultimate marvel vs capcom 3 again.


## GE-Proton9-1

Proton:

    Pulled in upstream changes from proton 9 bleeding edge
    wine updated to Proton 9 bleeding edge
    dxvk updated to latest git
    vkd3d updated to latest git

Wine:

    All previous proton-ge patches rebased to proton 9 (thanks for the FSR rebase loathingKernel)
    Star Citizen EAC patch removed, no longer needed, instead currently uses protonfix with EOS_USE_ANTICHEATCLIENTNULL=1
    Wine-staging rebased on top of proton 9 bleeding edge wine

Protonfixes:

    core count fix added for farcry primal (allows game to run)
    added ulwgl entry for egs version of farcry primal
    core count fix added for farcry 2
    added ulwgl entry for uplay and egs versions of farcry 2
    core count fix added for far cry blood dragon
    added ulwgl entries for uplay and egs versions of far cry blood dragon
    added ulwgl entries for uplay and egs version of farcry 3
    added ulwgl entries for uplay and egs versions of farcry 4
    added ulwgl entry for egs version of uncharted legacy of thieves collection
    added fixes for Trails in the Sky 1-3 and ulwgl entries for the gog versions (thanks keenanweaver)
    added core count fix for New World
    added zoom games platform for ulwlgl
    added fix for duke nukem manhatten project zoom edition
    added fixes and ulwgl entries for the gog version of Soldier of Fortune II (thanks keenanweaver)
    added fix for Street Racing Syndicate (thanks doZennn)
    added fix and ulwgl entry for zoom version of hardwar (thanks keenanweaver)
    added fix for They Are Billions and ulwgl entry for gog version (thanks zocker-160)
    added fix for black screen in Grim Dawn and add ulwgl entry for gog version (thanks Aqa-Ib)
    added fix for Dirt 3 complete edition
    added fix for Postal III (thanks doZennn)
    added fixes for Incoming trilogy (thanks doZennn)
    fixed assetto corsa dotnet not installing (game runs again)
    added fix and ulwgl entry for GOG version of Silent Hill 4 (thanks keenanweaver)
    added fix and ulwgl entry for GOG version of Wheel of Time (thanks keenanweaver)
    added fix for Gabriel Knight 3 (thanks marianoag)
    added fix for Gobliiins 5 (thanks marianoag)
    added fix for Ceville (thanks marianoag)
    added fix for Nine Witches: Family Disruption (thanks marianoag)
    xrandr added to protonfixes for screen resolution detection -- this is needed for some games like gothic/gothic 2 (fixes for those those games are still a work in progress)
    added fix which wil skip running winetricks in protonfixes if no internet connection is available. A winetricks check is performed on every run. If a winetrick is found to be missing it tries to install it. During that time it will check if there is an internet connection available. If there is not one, the winetrick is skipped until the next time the game is run and subsequently the winetrick.)

Known Issue:

    wmv video playback regression in some games (one example being Ultimate Marvel vs Capcom 3). This is a known regression in upstream proton and they are aware/working on it.


## GE-Proton8-32

HOTFIX:

- fix wine subcommands not working using ulwgl (winecfg, console, etc)

Protonfixes:

- Add video playback fixes for all Agarest games (Generations of War/Zero/2/Mariage)

## GE-Proton8-31

Proton:

- updated wine to latest bleeding edge, allows helldivers to run
- updated vkd3d-proton to latest git
- updated dxvk to latest git

ULWGL:

- added fix for older games to properly set CWD (current working directory) if executable is not inside the wine prefix

GStreamer:

- fixed this annoying ass unclosable wayland window from popping up when a game uses gstreamer:
![image](https://github.com/GloriousEggroll/proton-ge-custom/assets/11287837/0b3174c0-6f55-479b-a28a-d92b8a82b449)

Original upstream bugs + fix:
- https://gitlab.freedesktop.org/gstreamer/gstreamer/-/issues/2997
- https://gitlab.freedesktop.org/gstreamer/gstreamer/-/merge_requests/5511
- https://gitlab.freedesktop.org/gstreamer/gstreamer/-/merge_requests/5509

Protonfixes:

- added fixes for Dark and Darker (thanks nmlynch94)
- updated BDO fixes to work with standalone
- updated yakuza 5 cutscenes fixes to work on non-steam versions

General:

- cleaned up various no longer required patches (either upstreamed or already fixed)

## GE-Proton8-30

Hotfix:

- fixed EAC not getting loaded. During my ULWGL changes I accidentally made it so steam games werent running using steam.exe inside the prefix... which of course broke EAC games. The code snippet involved is needed so that non-steam games don't try to run using steam.exe and thus dont create the Steam_API error. woops. fixed now.

## GE-Proton8-29

- hotfix: updated proton bleeding edge to include tekken 8 online match disconnect fix
- updated vkd3d-proton
- fix issue with drive_c symlink during prefix creation when using ulwgl (it's now possible to run scripted game installations using ulwgl and proton-ge)

Files will attach when build action finishes: https://github.com/GloriousEggroll/proton-ge-custom/actions

## GE-Proton8-28

- fixed `[S_API FAIL] SteamAPI_Init() failed; no appID found.` from being reported when running non-steam games
- non-steam games will now run using wine inside proton rather than calling steam.exe with wine then the game inside steam -- this goes alongside the API failure fix
- controller axis patch added from 8-27 has been removed as it is now properly upstreamed
- added ULWGL support for non-steam games (https://github.com/Open-Wine-Components/ULWGL)
- beamng VR patch removed per request by developers, they have stated they will fix the issue in 0.32 (https://www.beamng.com/threads/experimental-virtual-reality.94206/page-27#post-1674152)
- black desert online now works

Protonfixes:

- now using ULWGL-protonfixes
- can now call the winetricks gui using util.protontricks('gui')
- winetricks now performs an internet check before attempting any downloads
- fixed long standing issue with protontricks not being able to install dotnet4* using anything newer than proton 5. works now and no longer requires proton 5.
- fixed dll overwrites in winetricks, no longer need to maintain a massive list of specific overwriteable dlls in proton
- protonfixes added for Catherine Classic -- videos now fully working
- protonfixes added for Ys Origin -- videos now fully working
- protonfixes for Age of Wonders -- videos now fully working
- protonfixes added for Model 2 emulator
- protonfixes added for Alien Breed: Impact
- protonfixes added for Alien Breed 2: Assault
- protonfixes added for Alien Breed 3: Descent
- protonfixes added for Black Desert Online NOSTEAM=1 option. Launch game like `NOSTEAM=1 %command%` to launch non-steam standalone version.

Files will auto-attach to release when finished building in Actions: https://github.com/GloriousEggroll/proton-ge-custom/actions

## GE-Proton8-27

- Disabled Nvidia Latency Reflex patches. After discussion with dxvk devs they are currently deemed problematic and need more work, and are known to currently cause stutters in games even when the feature is disabled. We will re-enable the patches when they are ready.
- Fixed Farlight 84 patch that was missing a lock causing problems in SDL games
- Backported a fix for HID devices with more than 8 axis https://bugs.winehq.org/show_bug.cgi?id=55660

## GE-Proton8-26

- updated wine to bleeding edge
- updated dxvk to git
- updated vkd3d-proton to git
- updated dxvk-nvapi to latest upstream proton
- pulled in latest upstream proton bleeding edge changes
- added farlight 84 patch update
- VR fix for Beam.NG.Drive added ([#106](https://github.com/GloriousEggroll/proton-ge-custom/pull/106) thanks gamingdoom)
- NVIDIA Reflex implemented ([#104](https://github.com/GloriousEggroll/proton-ge-custom/pull/104) thanks loathingKernel)

protonfixes:

- unified fix for cpu topology workaround ([GloriousEggroll/protonfixes#167](https://github.com/GloriousEggroll/protonfixes/pull/167) thanks Root-Core)
- unified fix for protonaudioconv workaround ([GloriousEggroll/protonfixes#168](https://github.com/GloriousEggroll/protonfixes/pull/168) thanks R1kaB3rN)
- unified fix for xliveless xlive workaround added ([GloriousEggroll/protonfixes#170](https://github.com/GloriousEggroll/protonfixes/pull/170) thanks Root-Core)
- unified fix for esync/fsync enable/disable added ([GloriousEggroll/protonfixes#169](https://github.com/GloriousEggroll/protonfixes/pull/169) thanks R1kaB3rN)
- cutscene audio in BlazBlue Centralfiction workaround added (thanks spifferoo)
- game fix added for Renegade Ops (thanks Root-Core)
- cleanup of deprecated LAA, dxvk-async, and win32 helper functions (thanks R1kaB3rN)
- cutscene audio fix for The Great Ace Attorney Chronicles workaround added (thanks eagleflo)
- game fix added for The Forest (thanks Root-Core)
- updated fix for Super Naughty Maid 2 (thanks R1kaB3rN)

## GE-Proton8-25

HOTFIX:

- Remove Baldur's Gate 3 launcher workaround (no longer needed)
- Add mpegvideo codec to ffmpeg, should complete Crimson Skies, Azumanga Fighter and possibly a lot of other early 2000s games. (thanks loathingKernel)

FYI: github Actions builds the release files now. If they are not attatched wait an hour or so and github Actions will attach them when finished building:

https://github.com/GloriousEggroll/proton-ge-custom/actions/runs/6950027102

## GE-Proton8-24

- Added protonfix for Fable III
- Added yakuza 5 cutscenes fix (thanks NishiyamaPedro) https://gitlab.winehq.org/wine/wine/-/merge_requests/4244
- updated Farlight 84 fix (thanks OOOOOF123) https://gitlab.winehq.org/wine/wine/-/merge_requests/4428
- Added D8VK to proton for DirectX 8 games. Disabled by default, need to use PROTON_ENABLE_D8VK=1 to use it. (thanks loathingKernel)
- Enabled vc1image,mpeg1video,mp2 decoders in ffmpeg for Crimson Skies (thanks loathingKernel)
- Enabled indeo5, adpcm_ms decoders in ffmpeg for Mafia (thanks loathingKernel)
- Fixed github actions (thanks loathingKernel)
- imported upstream VR changes
- imported upstream steamclient changes
- imported upstream Resident Evil 2,3,7,8, Hogwarts Legacy nvapi overrides
- imported upstream Hogwarts Legacy amd ags override
- updated dxvk to master
- updated vkd3d-proton to master
- updated wine to bleeding edge

## GE-Proton8-23

- added reverts for vrclient to allow VRChat to work again (pending proper fix from valve: [ValveSoftware#1199 (comment)](https://github.com/ValveSoftware/Proton/issues/1199#issuecomment-1800923686))
- the gstreamer plugin build options have been re-worked. Rather than enabling everything under the sun, we've now manually enabled each option that was reported as enabled in previous builds, and disabled the rest. This was done to more align with what Valve is doing and to allow a clearer picture of what may be missing from Valve's proton rather than taking wild guesses. Doing this may allow Valve a better idea of additional codecs/filters that might be missing in case they need and/or can be enabled. (thanks loathingKernel for taking the time to do this)
- dxvk updated to latest git
- vkd3d-proton updated to latest git
- wine updated to latest bleeding edge

## GE-Proton8-22

- Alan Wake 2 HDR fixup added from upstream: [ValveSoftware/wine@1182ef7](https://github.com/ValveSoftware/wine/commit/1182ef740346c62b76992f425593fa72e23203a7)
- FAudio WMA3 support added from upstream: [ValveSoftware/wine@8855b75](https://github.com/ValveSoftware/wine/commit/8855b754068988adab22c50aa8c3a84075c2cd4f)
- protonfix: Add fix for NUKITASHI (thanks R1kaB3rN)
- dxvk updated to latest git
- vkd3d-proton updated to latest git
- wine updated to latest bleeding edge

## GE-Proton8-21

- fixed washed out colors on some games with FSR disabled and incorrect screen resolution applied (such as Deep Rock Galactic) -- thanks loathingKernel
- fixed crash in DOOM Eternal on clean prefix due to incorrect screen resolution detection when FSR disabled -- thanks loathingKernel
- Rebased and re-added more accurate screen resolution detection for FSR -- thanks loathingKernel
- imported upstream patch needed for libreVR Revive https://bugs.winehq.org/show_bug.cgi?id=54687
- updated wine bleeding edge
- updated vkd3d-proton

## GE-Proton8-20

HOTFIX:

- updated world of warships workaround patch with proper fix, no longer requires environment variable (thanks OOOOOF123)

## GE-Proton8-19

HOTFIX:

Added workaround that fixes World of Warships login hang introduced in upstream proton since GE-Proton8-5:
[ValveSoftware#333 (comment)](https://github.com/ValveSoftware/Proton/issues/333#issuecomment-1763560466)

## GE-Proton8-18

HOTFIX:

For some reason the Alan Wake protonfix was missing from the last release even though it was noted in the release notes. This is a small hotfix to actually add it this time.

## GE-Proton8-17

- added protonfix for Alan Wake (thanks FozziHi)
- added protonfix for Batman Arkham Asylum (thanks FozziHi)
- added protonfix for Tokyo Necro (thanks R1kaB3rN)
- added protonfix for The Song of Saya (thanks R1kaB3rN)
- added protonfix for YOU and ME and HER: A Love Story (thanks R1kaB3rN)
- added upstream patch to allow R6 Siege to launch again (https://gitlab.winehq.org/wine/wine/-/merge_requests/3777) (multiplayer still does not work due to anticheat)
- added fixup for resolution calculation when WINE_FULLSCREEN_FSR is used (thanks Ph42oN and loathingKernel)
- import upstream proton build changes
- import upstream VR changes
- update vkd3d-proton
- update dxvk
- update wine to bleeding-edge

## GE-Proton8-16

- imported build changes from upstream proton
- update wine to latest bleeding edge
- updated dxvk to latest git
- updated vkd3d-proton to latest git
- added patch to fix genshin impact crash on opening long urls (thanks iglu47 and Awekening on discord)
- protonfixes: removed various no longer needed video playback fixes for resident evil games (thanks Bitwolfies)

## GE-Proton8-15

- Upstream proton symstore fixes added
- dxvk updated to git
- vkd3d-proton updated to git
- proton-wine updated to bleeding edge
- protonfixes: added update to remove no longer needed mafia DE launcher workaround, fix physx install on mafia DE (thanks Bitwolfies)

## GE-Proton8-14

- removed previously added ealink patch (turned out to be a Legendary launcher bug, not a wine bug. Pending on Legendary side: derrod/legendary#595)
- vkd3d-proton updated to latest git
- vkd3d updated to upstream proton version
- dxvk updated to latest git
- gstreamer updated to 1.22.5
- dav1d updated to 1.2.1
- imported upstream lsteamclient changes
- imported upstream media converter changes
- winemono updated to 8.0.1
- upstream proton overrides imported:
[c954b31](https://github.com/GloriousEggroll/proton-ge-custom/commit/c954b311fb9f7260bbb478c897f3a08237da3613)
[98ee282](https://github.com/GloriousEggroll/proton-ge-custom/commit/98ee282c2e9013188d8ebae2299043accabc5d2a)
[979d582](https://github.com/GloriousEggroll/proton-ge-custom/commit/979d582e84eb1d4f82d578549270b213cdcf6cbb)
[92be0cd](https://github.com/GloriousEggroll/proton-ge-custom/commit/92be0cd79288f90d690c6bc7c440ed0687f262a2)
- protonfixes: Remove several deprecated workarounds: Monster Hunter Rise, Horizon Zero Dawn, Mass Effect: LE, Madia Definitive Edition (thanks Bitwolfies)
- protonfixes: Fix for Star Trek Online black/empty launcher window (thanks dunconio)
- protonfixes: Restore audio in cutscenes in Atelier Ryza trilogy (thanks salixor)
- protonfixes: use older winetricks version for Proton 5.0 (thanks skryvel)

## GE-Proton8-13

-HOTFIX-

steam helper MR ValveSoftware#6555 re-added and updated.
Allows -northstar to work with Titanfall 2 while not breaking other games that use bash script launchers.
This also allows other launch options to be used alongside -northstar option, regardless of arguement ordering (ie -northstar -novid, or -novid -northstar).
This MR also allows launch options to be used with EA games (link2ea commands).

Updated Titanfall 2 protonfix to restore original Titanfall2.exe if NorthstarLauncher.exe symlink was previously used.
(the -northstar option does not use/need NorthstarLauncher.exe, it works instead via wsock32 override)

## GE-Proton8-12

- FSR is no longer enabled by default as it was found to limit in-game resolutions in some games. To enable/use it you will need WINE_FULLSCREEN_FSR=1 alongside the usual options.
- Added patch to allow Farlight 84 to not crash at the main menu
- Reverted ValveSoftware#6555 which caused several games since GE-Proton8-4 which used batch scripts to not work properly, including Guilty Gear Xrd,Escape from Monkey Island,Memento Mori
- Added protonfix to allow Titanfall 2 '-northstar' launch option to work without patching steam helper.
- Protonfix added for DCS World steam edition (thanks skryvel)
- Protonfix added for Assetto Corsa (thanks skryvel)
- Protonfix added for Persona 5 Strikers audio (thanks marianoag)
- Protonfix added for Shin Megami Tensei III Nocturne HD Remaster audio (thanks marianoag)
- Protonfix added for Memento Mori logo hang and broken videos (thanks marianoag)
- Protonfix added for Tex Murphy: Overseer (thanks marianoag):
Digital Sound Initialization Error (Intel RSX 3D drivers are not installed)
LAV Filters for video and DgVoodoo for textures
edit registry to avoid ffdshow compatibility manager popup
- Protonfix added for Alternativa logo hang and broken videos (thanks marianoag)
- Protonfix added for The Big Secret of a Small Town no cursor or double cursor selecting custom cursor in options (thanks marianoag)
- Protonfix added for Escape From Monkey Island force anti-aliasing and allow higher resolution (thanks marianoag)
- Removed no longer needed Kovaaks protonfix
- Import upstream proton fixes
- Updated wine bleeding edge
- Updated dxvk git
- Updated vkd3d-proton git

## GE-Proton8-11

- HOTFIX: Somehow the addon patches for GE-Proton8-10 did not get applied.. whoops :|. They are applied now in this release. DXVK and wine also updated.

## GE-Proton8-10

- wine updated to latest bleeding edge (fixes Ubisoft Connect, adds patch needed for some UE4 games)
- steam runtime update pulled from upstream
- patch required for EALink from upstream wine added (https://gitlab.winehq.org/wine/wine/-/merge_requests/2740)
- dxvk updated to latest git
- protonfix added for kovaaks (thanks xaizone)

## GE-Proton8-9

-Hotfix: Apparently yesterdays build was missing the normal proton packaged Gecko and Mono (the file size was significantly smaller than usual). This build fixes that.

## GE-Proton8-8

- This is a minor hotfix release that just syncs proton-wine and dxvk with upstream versions from today. A user complained they were seeing some odd CPU+GPU usage in 8-7 but was fine in today's proton-experimental. After testing with this build based on today's experimental they confirmed it was working here too.

## GE-Proton8-7

- FSR IS BACK!!!

Huge shoutout/thank you to Ph42oN for completely rebasing, updating and combining all of the old FSR patches to make them compatible with Proton 8.

- Additionally a bug was fixed by Ph42oN with fullscreen not working properly when fsr is disabled which was present in proton 7
- protonfix for Oceanhorn removed as it's no longer needed (thanks Iglu47)
- protonfixes added for Neptunia Re;Birth 1 & 2 (thanks NishiyamaPedro)
- proton-wine updated to latest git
- dxvk updated to latest git
- vkd3d-proton updated to latest git
- dxvk-nvapi updated to latest git
- upstream build changes pulled in

## GE-Proton8-6

HOTFIX:

- fixed FFXIV Hydaelyn new player intro video not playing (again)

## GE-Proton8-5

- Gears 5 now works with EAC without any workarounds needed. If you previously used proton-ge to play, go into the game folder and remove these folders:

/GearGame/Binaries/Steam/EasyAntiCheat-backup
/Engine/Binaries/ThirdParty/GFSDK_Aftermath

Then verify the integrity of the game files so that it re-downloads the originals.

- protonfix added for Two Worlds audio (thanks marciocr)
- protonfix added for APB Reloaded (thanks telqor)
- dxvk updated to latest git
- vkd3d-proton updated to latest git
- wine updated to latest bleeding edge
- staging patches rebased
- steam_helper updates imported from upstream
- imported kaldi, openfst, vosk-api modules from upstream

## GE-Proton8-4

* protonfixes: fix for Moero Chronicle (Thanks Kaedras and Snaggly)
* protonfixes: fix for Shadows on the Vatican games (Thanks marianoag)
* protonfixes: fix for The Blind Prophet (Thanks marianoag)
* protonfixes: fix for Alter Ego (Thanks marianoag)
* protonfixes: remove no longer needed fall guys easyanticheat_x64.so workaround (Thanks Corben)
* added fix for northstar launch arguement not working (Thanks Jan ValveSoftware#6555)
* added upstream proton script changes
* added upstream font changes
* added upstream openxr changes
* added upstream steam helper fixes
* added upstream user_settings changes
* updated wine to latest bleeding edge
* updated dxvk to latest git
* updated vkd3d-proton to latest git
* updated dxvk-nvapi to latest release

Notes: On Fall Guys when the Epic Online Services installer is running on a clean prefix, you must hit cancel on step 2/2, otherwise Fall Guys will tell you the game is missing files and force you to exit.

## GE-Proton8-3

* wine updated to latest bleeding edge -- fixes video playback regression introduced in 8-2
* fixed issue with some applications swapping to windowed mode when alt+tabbing or focus lost
* dxvk updated to latest git
* vkd3d-proton updated to latest git

## GE-Proton8-2

* wine updated to bleeding edge
* dxvk updated to latest git
* vkd3d-proton updated to latest git
* dxvk-nvapi updated to latest git
* flicker issue fixed in MH Rise
* Shatterline working again
* missing stub backported from wine 8.5 to fix chromium, gameglass
* fixup for daedalic games protonfixes (they were in the wrong folder, thanks marianoag)
* protonfix added for Conception PLUS
* instructions added for steam snap installation in readme (thanks baa14453)
* flatpak url updated in readme (thanks benaryorg)
* dxvk-nvapi game-specific enablements updated from upstream proton
* steam client update from upstream proton

## GE-Proton8-1

* All build components rebased to Proton 8 experimental/upstream
* proton-wine updated to latest experimental
* wine-staging rebased on top of proton-wine 8
* proton-ge game patches and pending wine upstream patches rebased on top of proton-wine 8
* dxvk updated to latest git
* vkd3d-proton updated to latest git
* protonfix: No cutscene audio in Daedalic Games (Memoria, The Night of the Rabbit, A New Beginning - Final Cut) - (thanks marianoag)
* protonfix: Megadimension Neptunia VII - (thanks snaggly)

NOTES:

    FSR is currently disabled again. It needs a massive rebase and same as before I don't know if it's currently possible to rebase/port it over to the new proton 8 build.

    Having the nvapi hack configuration enabled in dxvk.conf seems to crash battlenet. Recommend removing it from the config for existing Lutris battle.net installations and related games.

    Overwatch losing focus after death seems to be fixed

## GE-Proton7-55

This is a hotfix for EAC. In 7-53 the star citizen hotfix broke EAC compatibility for other games, this has been fixed now.

* wine updated to latest bleeding edge
* dxvk updated to git
* vkd3d-proton updated to git
* nvapi enabled for final fantasy stranger of paradise
* legacy xactengine winetricks protonfix removed as it's finally no longer needed

Note: If you are using the 0.5.13-beta1 of Lutris, a patch is needed to prevent SteamGameId being overridden:
[lutris/lutris@6d78eeb](https://github.com/lutris/lutris/commit/6d78eeb9fb18680905572d2e35f2d4666106119c)

## GE-Proton7-54

* update wine bleeding edge: brings is fall guys eac fix from upstream
* update vkd3d-proton: brings in some fixes for the last of us, uncharted, and a few more
* update dxvk
* protonfixes: Remove deprecated Saints Row 2 fix (thanks Bitwolfies)
* protonfixes: add fix for Carnage cross (thanks ranplayer)
* protonfixes: correct Outlaws fix script (thanks Sterophonick)

## GE-Proton7-53

This is a hotfix that brings the Star Citizen specific EAC patch to upstream. It allows Star Citizen to run without needing to change the /etc/hosts file and does not interfere with EAC for other games.

Note:

Before running Star Citizen
(1) You must set SteamGameId=starcitizen environment variable to trigger the EAC workaround
(2) this script should be run to remove existing EAC files:

```
#!/bin/sh
if [ -d \"$WINEPREFIX/drive_c/users/$USER/AppData/Roaming/EasyAntiCheat\" ]; then rm -rf \"$WINEPREFIX/drive_c/users/$USER/AppData/Roaming/EasyAntiCheat\"; fi
```

## GE-Proton7-52

* Diablo IV proper fix from proton upstream added
* Halo Infinite fix/patches from proton upstream added/updated
* protonfix for Outlaws + A Handful of Missions (thanks Stereophonick)
* protonfix for Underdog Detective (thanks Neodamode)
* dxvk updated to git
* vkd3d-protonupdated to git
* wine updated to bleeding edge

## GE-Proton7-51

* added fix for halo infinite (thanks TheMaister):
* HansKristian-Work/vkd3d-proton#1465
* added fix for Anno 1800 multiplayer (thanks Knogle):
* ValveSoftware/wine#181
* added protonfix for Tokyo Necro (thanks R1kaB3rN)
* fixed typo in Witcher 2 protonfix (thanks Bitwolfies)
* updated wine to bleeding edge
* updated dxvk to git
* update vkd3d-proton to git
* removed deprecated RE:0 protonfix (thanks Bitwolfies)
* removed deprecated Jedi Fallen order protonfix (thanks Bitwolfies)
* removed deprecated Pentiment protonfix (thanks tgurr)

## GE-Proton7-50

* update dxvk to latest git
* update vkd3d-proton to latest git
* update wine to latest bleeding edge
* rebase wine-staging patches
* import upstream vkd3d updates
* import upstream font updates
* import upstream vrclient/openvr updates
* import upstream steamclient updates
* import upstream proton updates
* protonfixes: remove no longer needed persona 4 golden fixes (thanks tgurr)
* protonfixes: remove no longer needed Battle Fantasia FPS lock (merged in dxvk, thanks ranplayer)
* protonfixes: Metal Slug -- fix black window (thanks ranplayer)

## GE-Proton7-49

This is mainly just a hotfix release that adds the upstream Ubisoft Uplay fix
* Updated proton-wine bleeding edge
* Updated vkd3d-proton
* Updated dxvk
* Updated proton steamclient

## GE-Proton7-48

* Updated proton-wine bleeding edge
* Updated vkd3d-proton
* Updated dxvk
* Update dxvk-nvapi

Latest upstream changes should include the most recent Dead Space fixes.

Additionally, in the previous proton-ge build I noted a problem with Monster Hunter: Rise. This issue turned out to be specific to the 7900 XT/X cards. The fix is currently pending on mesa/radv:

https://gitlab.freedesktop.org/mesa/mesa/-/issues/8153
https://gitlab.freedesktop.org/mesa/mesa/-/merge_requests/20941

## GE-Proton7-47

Hotfix release:

I received a ping from the dxvk author today for the following hotfix:

> @GloriousEggroll sorry for ping but you might want to update dxvk in your proton builds asap,
> since we've been writing invalid state cache files that can lead to all sorts of trouble.
>
> relevant commits to fix stuff:
>
> [doitsujin/dxvk@`0af5ece...master`](https://github.com/doitsujin/dxvk/compare/0af5ececa6ba250b529c9eb988791cf4c0a347e5...master)

Per the commit it will invalidate old caches automatically, you do not need to do anything yourself.

Phew, what a wild week of hotfixing :/

## GE-Proton7-46

This is a hotfix release for vkd3d that fixes several DX12 games not launching and/or crashing on launch, including:

* Warhammer 40,000: Darktide
* Death Stranding
* The Division 2

MH:Rise is still broken unfortunately (stuck on flickering compiling shaders screen)

## GE-Proton7-45

Removed deprecated broken dxvk-async patch:

Upstream DXVK has implemented the GraphicsPipelineLibrary (GPL) back in August, which takes over dxvk-async's job:

https://www.khronos.org/blog/reducing-draw-time-hitching-with-vk-ext-graphics-pipeline-library

doitsujin/dxvk#2798

Driver support for Nvidia was added in version 515.49.10:
https://developer.nvidia.com/vulkan-driver

Driver support for AMD/RADV was added in August 2022 and is an ongoing WIP:
https://gitlab.freedesktop.org/mesa/mesa/-/merge_requests/17542

Per the above, it can be exposed/enabled for testing on AMD/RADV via:
RADV_PERFTEST=gpl

dxvk-async now causes problems with the dxvk-cache, which is not something new users may know how to clear:
Sporif/dxvk-async#55

In light of the above, in addition to the current rebase still not working properly, I am removing the dxvk-async patch from Proton-GE.

RIP dxvk-async 2018-2023

## GE-Proton7-44

- wine: updated to latest bleeding edge (includes alt+tab fix)
- wine-staging: rebased for latest proton-wine bleeding edge
- dxvk: updated to latest git (includes HDR patches)
- vkd3d-proton: updated to latest git (includes HDR patches)
- proton: import upstream changes (includes prefix sync revert/fix)
- protonfixes: add workaround for pentiment launch failure (thanks tgurr)
- protonfixes: add multiplayer fix for stronghold hd/stronghold crusader hd/ stronghold crusader extreme hd (thanks jopejoe1)
- protonfixes: add framerate fix for Battle Fantia Revised Edition (thanks ranplayer)
- protonfixes: add launcher workaround for Assassin's Creed Brotherhood (thanks ranplayer)


## GE-Proton7-43

- import upstream proton changes
- immortals: fenyx rising now playable (from my testing I did not have any cutscene audio skips or garbled output)
- added launcher skip (again) for baldur's gate 3 -- runs vulkan version by default
- added fix for gears 5 hang after hitting enter on logo screen
- added fix for game drive option not being applied properly to elder scrolls online (fixes installation -- still need to hit space at black window)
- added fix for witcher 3 -- no longer crashes on hairworks
- updated protonfix for fall guys (does not need exe workaround -- thanks rokam)
- update dxvk git
- update vkd3d git
- update wine to bleeding edge

## GE-Proton7-42

- Pull in upstream build changes from proton experimental
- update dxvk-nvapi
- update dxvk
- update vkd3d
- update media converter
- update wine to latest proton experimental bleeding edge
- rebase wine staging
- dxvk: add launcher fix for secret world:legends
- protonfixes: add d3d9_43 and 11_43 winetricks for secret world: legends (thanks zerodogg)
- protonfixes: remove no longer needed fps cap for king of fighters (applied in dxvk directly instead, thanks Bitwolfies)
- protonfixes: remove no longer needed EAC workaround for SQUAD (thanks mikk150)
- protonfixes: add protonfix for Skeleton Boomerang (thanks xperia64)
- protonfixes: add protonfix for Re-Volt (thanks mthsk)

## GE-Proton7-41

HOTFIX:

- fixed issue with EasyAntiCheat folder not being renamed correctly for the Gears 5 EAC workaround -- should now work on the Steam Deck for single player campaign. I've been told coop also works but not confirmed.

## GE-Proton7-40

HOTFIX:

- fixes regression in vkd3d-proton which allows Gears 5 to run again. Still uses EAC workaround, still single-player only. (thanks Rhedox/K0bin!)

## GE-Proton7-39

- proton-wine updated to latest bleeding edge
- dxvk updated to git
- vkd3d-proton updated to git
- overwatch 2 freeze fix added (may help other games)
- pulled in upstream proton nvapi fixes
- enabled gamedrive option for ESO by default
- mono updated to 7.4.0
- no-longer-required protonfixes removed for Sonic Adventures 2, Farcry 5 EAC, Origin (thanks Bitwolfies)

## GE-Proton7-38

- Added protonfix to allow Uncharted: Legacy of Thieves collection to launch on systems with more than 16 cpu cores
- Added tll.exe amd_ags_x64 override to allow Uncharted: Legacy of Thieves - The Lost Legacy to run
- Added save file fix for Persona 5 Royal (https://gitlab.winehq.org/wine/wine/-/merge_requests/1145)
- Added overwatch 2 shader compilation patch (https://gitlab.winehq.org/wine/wine/-/merge_requests/1152) -- please note this is only added as it may help other games. proton-ge is not meant for non-steam games, for non-steam games use wine-ge: github.com/gloriouseggroll/wine-ge-custom
- Removed no longer needed shatterline protonfix
- Upstream NVAPI/DLSS list of enabled games updated (https://github.com/GloriousEggroll/proton-ge-custom/blob/df646c0db71a0548b1a8dd501dbd9821cde8ab88/proton#L1232)
- DXVK updated to latest git
- VKD3D updated to latest git
- wine updated to latest bleeding edge
- wine-staging rebased

## GE-Proton7-37

HOTFIX: The return of FSR

-Huge thanks to Discord community member OOOOOF123 for rebasing the FSR patch, FSR is back in business!

That's the only change in this build. Since it's a pretty important one I felt it should be released right away,i

## GE-Proton7-36

Updates:

- import nvapi enablement list from proton upstream (ValveSoftware@9a708e0)
- import media-converter changes from proton upstream (ValveSoftware@5339633)
- update dxvk
- update vkd3d-proton
- update wine-bleeding edge
- add protonfix for Shatterline (thanks orowith2os)
- add protonfix for Halo Reach mod tools (thanks orowith2os)
- add protonfix for Ougon Musoukyoku (thanks namaenonaimumei)

FSR Removed/Disabled indefinitely:

Due to this commit in upstream proton -- ValveSoftware/wine@7c5306e

The FSR patches had to be disabled.

The commit is important because it fixes some problems that were happening with winevulkan, but unfortunately it also patches in a lot of components that were already part of the FSR patch.
The problem is that the commit has much of the same contents as the FSR patch, but the FSR patch has the FSR bits all mixed in and its not within my know how to rebase.
The original author of the FSR patches has already stated since the functionality was moved to gamescope (he was the one who moved it to gamescope) the wine patches will not be updated.
With that being said the FSR patches have been increasingly problematic to maintain over time due to the lack of the original author willing to rebase the wine version in favor of instead of using the gamescope version.
Moving forward if you need to use FSR, you will need to either use gamescope, or rely on the game itself having FSR as a built-in feature.

## GE-Proton-7-35

- The Phantasy Star Online 2 update wasn't working properly. I've updated it and it's now working as expected (double checked on steam deck) -- Thanks Goldreaver

## GE-Proton-7-34

- Phantasy Star Online 2 fixed (again)
- Persona 4 Golden fixed (again) -- Thanks tgurr
- GTA IV custom radio protonfix added -- Thanks xperia64
- upstream WINE_HEAP_DELAY_FREE fix for CoD BO3 Multiplayer + zombies added
- upstream LAA disable for Sword and Fairy 4 added
- wine updated to latest bleeding edge
- DXVK updated to latest git
- vkd3d updated to latest git

## GE-Proton-7-33

- wine updated to latest bleeding edge, pulls in more fixes for gta v, rdr2, verified bioshock remastered 1/2 + infinite work with 2k launcher
- dxvk updated to latest git
- vkd3d updated to latest git
- pulled in latest proton script changes from upstream
- fixed issue with fall guys protonfix trying to replace incorrect command name (Thanks Corben78)
- removed Divinity Original Sin 2 launcher protonfix as it's no longer needed

## GE-Proton-7-32

- Version deprecated by upstream

## GE-Proton-7-31 Released

- FXIV Launcher fixed (thanks Valve)
- GTA V fixes added (thanks Valve)
- NOSTEAM=1 envvar option available for Guild Wars 2. Use it the same way you do for ffxiv non-steam accounts:
- NOSTEAM=1 %command%
- dxvk updated to git
- vkd3d-proton updated to git
- wine updated to latest bleeding edge
- patches added for Visual Novel Doukyuusei

## GE-Proton-7-30 Released

- protonfix for Flatout Ultimate Carnage (single player only) added -- thanks Ranplayer
- amazon games patch added (this is mainly for possible future compatibility, please use wine-ge for non-steam games)
- wine-staging ddraw-Device_Caps and ddraw-version-check patchsets disabled in favor of new proton ddraw changes.
- dxvk updated to latest git
- vkd3d-proton updated to latest git
- wine updated to latest bleeding-edge
- upstream openxr patches applied

## GE-Proton-7-29 Released

- Halo Infinite patches pulled in from Proton experimental. Game should be playable now with videos. Mouse pointer issue is also fixed.
- Upside down videos fixed in Endless Space 2 and some players in VRChat:

## GE-Proton-7-28 Released

- Halo infinite wine video playback patches disabled -- they break too many games. You can still play it without videos like before. This should fix most issues with various games crashing in 7-27. Currently pending an update from Valve to fix the issue.
- dxvk updated to latest git
- vkd3d-proton updated to latest git
- protonfix added for Super naughty maid 2 (thanks Marc-Pierre-Barbier!)

## GE-Proton-7-27 Released

- DXVK:

- dxvk updated to latest git (fixes some issues that were in 1.10* branch)
- halo infinite required dxvk patches merged (for dxgi which is used by vkd3d) -- thanks Guy1524! (Derek Lesho)
- dxvk-async patch updated for latest git -- thanks Sporif!

- VKD3D:

- vkd3d-proton updated to latest git
- halo infinite required vkd3d patches merged -- thanks Guy1524! (Derek Lesho)

- WINE:

- wine updated to latest bleeding edge
- halo infinite patches required for wine merged (campaign now playable, videos work) -- thanks Guy1524! (Derek Lesho)

- PROTONFIXES:

- protonfix added for Halo CE mod tools (confirmed working) -- thanks Oro!
- protonfix added for Halo 2 mod tools (still has issues) -- thanks Oro!
- protonfix added for Halo 3 mod tools (confirmed working) -- thanks Oro!
- protonfix added for Halo 3: ODST mod tools (confirmed working) -- thanks Oro!
- Fall Guys protonfix updated to fix hang after EOS install on clean prefix setup.
- Witcher 2 protonfix added to fix failure to launch on systems with large core counts
- Farcry 3 protonfix added to fix failure to launch on systems with large core counts
- Battlefield Bad Company 2 protonfix removed, no longer needed and was causing DXVK not to load for the game
- Endless Space 2 protonfix removed, was causing game to crash. Game now works but videos are upside down (known proton issue)
- Gwent: Rogue Mage protonfix added
- SQUAD protonfix EAC blob updated to last-known working version

## GE-Proton-7-26 Released

- Fix WINE_FULLSCREEN_FSR_MODE= not working after previous aspect ratio update.

## GE-Proton-7-25 Released

- FFXIV hydaelyn intro video after datacenter select fixed (again). May also fix WMV playback in some other games.
- Trion/Glyph launcher and its games are now fixed (Trove, Rift)
- revert proton commit 96b8220 to re-enable gallium nine patching compatibility
- wine updated to bleeding edge, brings in numerous fixes
- dxvk updated to 1.10.2 (git currently has conflicts with dxvk-async)
- vkd3d-proton updated to git
- MODS=1 option added for allowing choosing between launching skyrim with SKSE or the normal launcher
- FSR will now auto-calculate resolutions based on screen aspect ratio rather than adding pre-defined entries based on width.

## GE-Proton-7-24 Released

- Hotfix: Death Stranding crash fixed
- FSR Updates

## GE-Proton-7-23 Released

- Hotfix: fix Path of Exile not launching
- FSR:

I've attempted to make the FSR issue a bit easier for people by implementing a new option

## GE-Proton-7-22 Released

- Hotfix:

- Fixes crashes with 3440x1440 screen resolution
- FSR resolutions removed from in-game resolution list. Please use WINE_FULLSCREEN_FAKE_CURRENT_RES to set scale-from resolution

## GE-Proton-7-21 Released

- Wine:

- Paladins crash fixed. I found the fix and reported it upstream and they were able to get it fixed. As long as they allow EAC to keep working the game should now be playable (again)
- Black Ops II: Zombies is now fixed! (pulled from proton)
- Black Ops II: Multiplayer is now fixed! (pulled from proton)
- Elden Ring missing fullscreen resolutions fixed
- Apex Legends crashing on fullscreen 1080p mode for some systems fixed
- Wine updated to bleeding edge from 6/23 (6/24 has broken mfplat commits)
- dxvk updated to latest git
- vkd3d-proton updated to latest git

- Protonfixes:

- Fall Guys: disabled esync and fsync to prevent random crashes
- Warhammer 40,000: Space Marine crash fixed on systems with high core counts
- Lara Croft and the Guardian of Light fixed on systems with high core counts
- Ys Origin demo protonfix added (thanks Neodamode!)
- SQUAD protonfix added -- should work OOTB now (thanks rokam!)
- Total War Rome II protonfix added (thanks patmann03!)
- Gwent protonfix added (thanks games647!)
- Bionic Commander Rearmed protonfix added (thanks ruineka!)
- Sonic Adventure 2 protonfix added (thanks ruineka!)'
- klite codec protonfix updated for persona 4 golden (thanks tgurr!)
- FarCry 4 crash fixed on systems with high core counts (it still has a crashing problem with dxvk + amd. works with dxvk+nvidia and wined3d+amd):

## GE-Proton-7-20 Released

- Fix FSR missing
- Fix some WMV videos broken after previous release (UMVC3, Atelier, RE5)
- Note: Audio is still broken on some of these (audio was broken before e.g. UMVC3)
- Fix nvcuda missing

## GE-Proton-7-19 Released

- V Rising fixes imported from upstream proton
- More FFXIV fixes imported from upstream proton
- FFXIV A Realm Reborn intro video missing audio fixed
- Star Citizen fixes imported from upstream wine (PLEASE NOTE THIS IS NOT FOR RUNNING STAR CITIZEN. THIS WAS ADDED ONLY FOR OTHER GAMES THAT NEED THE SAME PATCHES.)
- video fix for Outward added
- video fix for El Hijo added from upstream proton
- video fix for We Were Here Forever added from upstream proton
- video fix for The Room 4 added from upstream proton
- video fix for EZ2ON REBOOT added from upstream proton
- Added fix for Fall Guys to for Proton EAC runtime to install if not already present (Thanks Rokam!)
- Removed Serious Sam 4 DX12 workaround (no longer needed). It will now only set OpenAL audio (still needed)
- wine updated to latest bleeding edge
- dxvk updated to latest bleeding edge
- vkd3d-proton updated to latest bleeding edge

## GE-Proton7-18 Released

- proton bleeding edge updates, contains patches to fix official FFXIV Launcher (finally)
Additional notes:
- As before, you can still also use NOSTEAM=1 %command% to log in with a standalone non-steam account.
- The login and download progress bar both render at the bottom of the launcher, you'll need to scroll down.
- dxvk updated
- vkd3d-proton updated

## GE-Proton7-17 Released

- This is just a minor update/hotfix release.
- sapi-iteration-tokens staging patchset updated. Fixes Bless Unleashed launcher crash and fixes performance hit when patch set is not applied. Game is now playable.
- wine updated to latest bleeding edge

## GE-Proton7-16 Released

- added patch to fix crash in Elden Ring with fsync enabled after an extended period of time (thanks Paul Gofman!)
- pull in video playback updates from upstream proton
- pull in steam client updates from upstream proton
- dxvk updated to latest git
- vkd3d-proton updated to latest git

## GE-Proton7-15 Released

- vp9 support enabled in gst-plugins-good for ghostwire tokyo videos (they work now)
- protonfix added for State of Decay 2 crashes (thanks ThisNekoGuy!)
- protonfix added for Fall Guys EAC (works now, thanks rokam!)
- WINE_DO_NOT_CREATE_DXGI_DEVICE_MANAGER video fix enabled for Car Mechanic Simulator 2021
- WINE_DO_NOT_CREATE_DXGI_DEVICE_MANAGER video fix enabled for Harspace: Shipbreaker
- WINE_DO_NOT_CREATE_DXGI_DEVICE_MANAGER video fix enabled for Solasta
- WINE_DO_NOT_CREATE_DXGI_DEVICE_MANAGER video fix enabled for Monster Train
- WINE_DO_NOT_CREATE_DXGI_DEVICE_MANAGER video fix enabled for The Complex
- WINE_DO_NOT_CREATE_DXGI_DEVICE_MANAGER video fix enabled for Cook-Out
- WINE_DO_NOT_CREATE_DXGI_DEVICE_MANAGER video fix enabled for DJMAX Respect V
- WINE_DO_NOT_CREATE_DXGI_DEVICE_MANAGER video fix enabled for Gloomhaven
- steam runtime and sdk updated (contains vp9 libraries required)
- various build commits pulled from upstream proton
- vkd3d-proton updated to git HansKristian-Work/vkd3d-proton@4a05360 prior to 4/21 (latest UAT updates on 4/21 caused gpu hang during testing)
- vkd3d-proton upstream ghostwire tokyo commit HansKristian-Work/vkd3d-proton@119e00e cherry-picked and applied
- dxvk updated to latest git
- dxvk-nvapi updated to latest git
- wine updated to latest bleeding edge

## GE-Proton7-14 Released

- Hotfix: Received more complaints than praise surrounding the gamemode change so I've reverted the changes. Gamemode is removed from the build and will not be used by default.

## GE-Proton7-13 Released

Woops another hotfix -- forgot to patch dxvk with async.

## GE-Proton7-12 Released

This is a hotfix that adds a workaround to launch New World since it's launcher hangs. They added the EAC .so library and it appears to work. Hopefully it stays that way.

## GE-Proton7-11 Released

- Feral Interactive's 'gamemode' has been added to the build and will now be automatically used when games are launched (you no longer need to run 'gamemode %command%')  (Thanks manueliglesiasgarcia!)
- proton experimental bleeding edge wine build has been updated (fixes a prefix creation bug)
- several build-specific updates have been pulled from upstream proton
- dxvk updated to git
- vkd3d-proton updated to git
- dxvk-nvapi updated to git

## GE-Proton7-10 Released

Updated wine to latest bleeding edge
Updated dxvk to latest git
Updated vkd3d-proton to latest git
Corrected VKD3D_FEATURE_LEVEL being in the wrong python script block so it actually loads now.

Thanks to upstream proton devs Rémi Bernon (rbernon), Derek Lesho (Guy1524), Philip Rebohle (doitsujin):

Nioh 2 videos now work
Persona 5 Strikers videos now work

## GE-Proton7-9 Released

Added loader-KeyboardLayouts from staging. This fixes a big performance issue in Overwatch but may also help other games.
Set VKD3D_FEATURE_LEVEL=12_0 by default. This allows some older AMD GPUs to get past the "white screen" bug in Elden Ring
protonfix to set L.A. Noire to use DX11 (it tries DX9 by default) -- Thanks VoodaGod

## GE-Proton7-8 Released

Hotfix:

disable ntdll-CriticalSection from staging, it breaks ffxiv and deep rock galactic
EDIT: 3/5/22 -- I uploaded an incorrect build previously. I have now uploaded the correct build. Please note that the sha512sum has -changed-.

Sorry for the hiccup.

## GE-Proton7-7 Released

HOTFIX:

disabled server-Signal_Thread staging patchset that breaks steamclient in new prefixes for some games (notably Dragonball Fighter Z)
fixed path check for 32 bit smite EAC protonfix
fixed video rendering in RUST

Sigh. One of these days I'll get a release right the first time. That day is not today.

## GE-Proton7-6 Released

Wine-Staging is back! I rebased all of the patch sets from staging that did not cleanly apply and applied them on top of proton-experimental.

A detailed list surrounding staging patches can be found in /patches/protonprep-valve-staging.sh. If it's in the -W list then reasoning is provided. If it's not in the -W list that means it applied cleanly without issues. Note that some patch sets in the -W list are applied manually because they do apply, just not without fuzz.

wine-staging rebased and applied on top of proton-experimental (yes, all of it!)
wine updated to latest proton-experimental
dxvk updated to git
vkd3d-proton updated to git
protonfix added for SMITE to fix incorrect EAC library location (works now, yay)

## GE-Proton7-5 Released

### WINE:
Added NVCUDA patches from staging (required to allow physx to work again -- yay)
Added missing mouse rawinput patch from staging that allows true rawinput values rather than transformed values (this restores the same rawinput functionality of the previous proton-ge staging builds)
Added upstream powrprof patches for FFVII and SpecialK
Removed no longer needed customized mfplat reverts/patches -- upstream proton's work for CoD Blops III now

### Protonfixes:

Add protonfix for Project MIKHAIL: A Muv-Luv War Story
Add protonfix for MotorGP
Add protonfix for Exo One
Remove no longer needed protonfix for Apex Legends

### FFmpeg:

Added missing h264 and AAC decoders (fixes video decoding when shadercache is disabled in some games, such as BL3 Markus intro) (Thanks mmbossoni)

### DXVK:

updated dxvk to git

### VKD3D:

updated vkd3d-proton to git

## GE-Proton7-4 Released
Another hotfix build:

Added HideWineExports patch from wine-staging. Fixes games that need it, notably those using EAC disable workarounds such as:

Jump Force
Dragonball Fighter Z
Naruto to Boruto: Shinobi Striker

Added EAC disable workaround for single player in Naruto to Boruto: Shinobi Striker
Added upstream ldap patch so that build does not fail when using newer ldap library (this is mostly needed for compiling outside of proton build environment)
Fixed build environment submodule symlink issue

## GE-Proton7-3 Released

Another hotfix build.

--Finally-- got the build corruption issue fixed. There was a mixup with the pefixup script and transition from proton 7 stable to proton 7 experimental builds.
Took me a while but I got it sorted and Warframe and the Batman games as well as vcrun are all working properly again.
I quadruple checked on my side this time. What a long day.

## GE-Proton7-1 Released

Why the new naming scheme?

As discussed here:

https://www.patreon.com/posts/63101415

The base for WINE was changed from wine upstream to Proton experimental, and staging currently is not used in this new build. There are several reasons this was done, which are explained in detail in the post above.

I needed a way to express that the base is all Proton7 and to reset the minor versions. Additionally, from previous discussions I've had with some other devs on official proton, they requested that I modify the name so that the GE versions were easier to differentiate, which is why the GE prefix has been moved to the front of the name.

### What exactly has changed?

WINE upstream repo has been changed to Proton experimental bleeding edge.
Wine-staging is no longer used, but we keep it within the repository in case it is discovered that patches are needed from it later on.

### What has remained the same from previous Proton-GE builds?

mfplat implementation and continued work
gstreamer and ffmpeg implementation
protonfixes implementation and continued work
Various game patches which are not included in either upstream wine or proton and continuation to add such patches
dxvk-git and adding new patches or pending PRs as they become available
dxvk is still patched with async
vkd3d-proton-git and adding new patches or pending PRs as they become available

### What's actually fixed in this release compared to the last one?

Elden Ring EAC now works
The crash in various Unity games is resolved
Since we are now using proton's bleeding-edge experimental, we now have -all- of the controller and gamescope related patches. So if something is broken there -- it's an upstream proton bug.
Fixed doubled size issue caused by both dist folder and dist tarball being included. The dist tarball is not necessary and has been removed, returning the build to its original size instead of double.

## Proton-7.3-GE-1 Released

### WINE:

imported rebased fullscreen hack from proton 7.0
imported SDL patches from proton 7.0
imported gamepad patches from proton 7.0
imported racing wheel/ffb patches from proton 7.0
imported several misc. game fixes/patches from proton 7.0
imported gamescope patches from proton 7.0
imported updated mfplat patches from proton 7.0
imported rebased audio patches from proton 7.0
imported rebased mouse focus patches from proton 7.0
imported keyboard translation patches from proton 7.0
imported rebased font patches from proton 7.0
imported EAC patches from proton 7.0
imported network connectivity patches from proton 7.0
Cities XXL fix added (Thanks Alistair Leslie-Hughes)
updated wine + staging to git

### PROTON:

imported build system changes from proton 7.0
updated gstreamer to 1.18.6
updated dxvk to git
updated vkd3d-proton to git
updated dxvk-nvapi to git
removed FAudio from build (it's part of WINE now and works with WMA decoding)
removed jxrlib from build (it's part of WINE now)

### PROTONFIXES:

Added EAC disable workaround to allow Gears5 single-player to work (Thanks ga2mer)
Added EAC disable workaround to allow Jump Force single-player to work (Thanks Nej on discord)
Added EAC disable workaround to allow Dragonball Fighter Z single-player to work (Thanks Nej on discord)
Added EAC disable workaround to allow Elden Ring single-player to work
Added fix for Civ IV: Colonization (Thanks jo-oe)
Added fix for Heavy Rain (Thanks Sterophonick)
Added fix for Putt Putt PBS (Thanks Sterophonick)
Removed Baldur's Gate 3 Launcher disable -- it works now. (Thanks Mershi)
Removed video disable for Black Ops III -- they work now

Some mfplat related test results:

### Working:

borderlands 3
bloodstained ritual of the night
seven: days gone
mortal kombat 11
monster hunter rise
ffxiv
soul calibur vi
Astroneer
American Fugutive
Aven Colony
Scrap Mechanic
nier replicant
power rangers battle for the grid
haven
tokyo xanadu xe+
Resident Evil 3 remake
call of duty: black ops III
biomutant
industry of titan
mutant year zero

### Broken:

spyro - in-game videos play audio in wrong language
Catherine Classic
darksiders warmastered edition
Devil may cry Collection
Battlestar Galactica - Cinematic upside down.
the good life

## Proton-7.2-GE-2 Released

    Hotfix: fix wine mono checksum failure
    fshack: Add faking current resolution ability. Details here: #52 (thanks Dragomir-Ivanov)

## Proton-7.2-GE-1 Released

wine: updated Forza Horizon 5 wine pulseaudio crash on splash screen fix -- properly fixed now rather than reverting. (thanks Paul Goffman)
wine: updated MK11 patch with pending upstream patch for proper TIB handler fix (thanks Paul Goffman)
wine: updated to 7.2
wine-staging: updated to 7.2
wine-staging: winepulse patches updated and re-enabled (wine-staging/wine-staging@c437a01)
dxvk-nvapi: dxvk-nvapi has been updated to latest git -- allows physx to work in games that use it when physx is installed
dxvk: updated to latest git
vkd3d-proton: updated to latest git
FAudio: updated to latest git
protonfixes: protonfix added to allow Batman Arkham Knight to use physx (thanks SveSop)
protonfixes: protonfix added to fix Watch Dogs xaudio2_7 crash (thanks Sterophonick)
protonfixes: winetricks updated

## Proton-7.1-GE-2 Released

-This is a hotfix to restore WMA audio support.

The FAudio author removed GStreamer support -- which is needed for WMA playback.

The reason he did it is because WINE is in the process of upstreaming WMA decode support, but the problem is that decode support is not in WINE yet, and since it was removed from FAudio, no WMA audio is working.

This update restores FAudio GStreamer support so that WMA audio is working again.

## Proton-7.1-GE-1 Released

Wine:

    Add missing patch to fix Forza Horizon 5 login window not accepting mouse focus
    Fixed Forza Horizon 5 crashing after splash screen

Protonfixes:

    protonfix added for Progressbar95 (thanks Benibla124)
    protonfix Resident Evil 5 videos disabled as workaround to allow game to be playable (thanks manueliglesiasgarcia)
    protonfixes klite verb updated version (used for persona 4 golden)
    protonfix added to enable game drive option for Elder Scrolls Online installer. (Note -- the installer works but you have to press space at the black screen, updater and game works perfectly fine after that)

DXVK:

    add pending Resident Evil games patch doitsujin/dxvk#2466

-wine and wine-staging updated to 7.1
-vkd3d-proton updated to git
-dxvk updated to git
-FAudio updated to git

## Proton-7.0rc6-GE-1 Released

Protonfixes:

    Update Oceanhorn protonfix (thanks Iglu47 GloriousEggroll/protonfixes#50)
    Add wmp11 protonfix for most of the Resident Evil series (thanks manueliglesiasgarcia GloriousEggroll/protonfixes#49)
    Remove unnecessary dotnet 4.x protonfix in most titles (thanks manueliglesiasgarcia GloriousEggroll/protonfixes#48)
    Add protonfix for Super Meat Boy (thanks Sterophonick GloriousEggroll/protonfixes#47)
    Add protonfix for Lord of the Rings: War in the North (thanks chelobaka GloriousEggroll/protonfixes#52)

Proton:

    Remove d3d10/d3d10_1 dxvk overrides (ValveSoftware@0ca077d)

Wine:

    Add Monster Hunter Rise patch from upstream proton (ValveSoftware/wine@40f9cba)
    update wine to latest 7.0rc6
    update wine-staging to latest 7.0rc6
    Remove proton pulseaudio patches and reverts. Upstream wine has fixed the crackling audio in Cyberpunk 2077 and various other games so the reverts are no longer needed (https://bugs.winehq.org/show_bug.cgi?id=52225)
    Add Sea of Thieves voice patches from upstream proton

DXVK:

    update dxvk to latest git

vkd3d-proton:

    update vkd3d-proton to latest git

FAudio:

    update faudio to latest git

## Proton-7.0rc3-GE-1 Released

-fixed issue with rockstar launcher stuck on connecting
-fixed Path of Exile crash on launch
-fixed DayZ crash on launch
-fixed Elder Scrolls Online crash on launch
-fixed STEEP crash
-added protonfix for LEGO Batman 2: DC Super Heroes (thanks daddeltrotter)
-removed deprecated styx:master of shadows protonfix (thanks manueliglesiasgarcia)
-updated winetricks to allow removal of no longer needed proton_5 workaround for wmp11 (thanks manueliglesiasgarcia)
-dxvk updated to latest git
-faudio updated to latest git

## Proton-7.0rc2-GE-1 Released

-Biomutant video playback fix imported from proton
-FFXIV Old launcher "Log In" button crash fix imported from proton (transgaming patch +hidewineexports no longer needed)
-FFXIV New player cutscene playback fix imported from proton (game fully works without skipping it now yay)
-Mass Effect Legendary Edition audio fix imported from proton (no longer needs protonfixes workaround)
-Oceanhorn protonfix added - thanks Iglu47!
-Arcania protonfix added - thanks manueliglesiasgarcia!
-Gothic 4 protonfix added - thanks manueliglesiasgarcia!
-The Bureau: XCOM Declassified esync + fsync disabled via protonfix per ValveSoftware#797 (comment) - thanks manueliglesiasgarcia!
-Pending patch added for https://bugs.winehq.org/show_bug.cgi?id=52222 - thanks Bill and rbernon!
-wine and wine-staging updated to 7.0rc2
-DXVK updated to git
-vkd3d-proton updated to git
-faudio updated to git

## Proton-6.21-GE-2 Released

This is a hotfix to apply the following important revert from Valve:

ValveSoftware/Proton@7ce8140

Additionally, the release files for Proton-6.21-GE-1 have been removed to aide in further preventing people from accidentally launching Destiny 2 and getting themselves banned, per the above hotfix.

## Proton-6.21-GE-1 Released

-Proton BattlEye patches added
-Proton CEG patches added
-Proton Forza Horizon 5 patches added
-Proton Guardians of the Galaxy patches added
-Proton Fallout76 patches added
-Proton Baldur's Gate 3 patches added
-Proton Age of Empires IV driver nag fix patch added
-Proton fsync patches updated to futex_waitv version
-Fix for error when using file browser to pick a file location added (this occurred usually in applications when you tried to specify an existing file location)
-Fix for broken mouse input in Borderlands and R6S added (was not present in 6.20, issue appeared in 6.21)
-Fix for the beamng mouse issue updated so that it does not affect non-steam games
-Bcrypt patches updated (steep works again, thanks openglfreak!)
-vulkan childwindow patches updated
-vkd3d Forza Horizon 5 patches added
-vkd3d Guardians of the Galaxy patches added
-vkd3d updated to latest git
-dxvk updated to latest git
-protonfixes uplay overlay disable function has been fixed to apply correctly when used.
-wine mono version updated
-protonfix added for ship graveyard simulator (and prologue, Thanks Alistair Leslie-Hughes!)

Notes:
-Fsync has been disabled on all Uplay titles -- it causes Uplay to hang on "Looking for patches" when initiationg a new prefix. Esync works fine.
-Various Uplay titles that have a vulkan native mode (Rainbow 6 siege) need the overlay disabled in order not to crash. DX11 mode works fine.
-For games that have a protonfix that uses the uplay overlay disable -- if creating a new prefix you will need to relaunch the game a second time. Uplay completely removes any pre-existing configurations on first launch, so any appending to the file gets removed. Upon re-launch the option will be re-appended and uplay will then see it.
-uplay likes to hang out after the game has closed -- make sure you close it in the task manager.

BattlEye games tested and working:

Ark: Survival Evolved

BattlEye games tested and not working:

Mount & Blade: Bannerlord -- hitting this issue: ValveSoftware#3706 (comment)

CEG games tested and working:

Bioshock Infinite
Just Cause 2
Black Ops II Campaign
Sid Meier's Civilization V
Mafia II (Classic)

CEG games tested and not working:

Black Ops II Zombies Mode -- exemption occurs a few seconds after getting to main menu
Black Ops II Multiplayer -- same issue as zombies mode
Warhammer: Space Marine -- bugsplats
Lara Croft and the Guardian of Light -- just hangs in the background infinitely until force killed

## Proton-6.20-GE-1 Released

-wine: Added fix for broken right click camera control in BeamNG.drive
-wine: Revert some upstream commits to re-allow mfplat patches (it was disabled in wine-staging 6.20 due to patches needing a rebase)
-wine: Add patch to fix Eve online launcher (thanks Tr4sk!)
-wine: Add patch to workaround The Good Life video playback (thanks popsUlfr!)
-wine: Add patch to fix Castlevania Advance Collection and a few other Konami "collection" games (thanks Raptor85!)
-wine: rebased proton patches for 6.20
-wine: updated to 6.20
-protonfixes: Added vcrun2019 to Injustice 2 -- fixes multiplayer desync
-protonfixes: Removed no-longer needed .NET installation from Batman Arkham Asylum protonfix (allows it to work again)
-protonfixes: Added xaudio3_7 protonfix for Resident Evil 4 (fixes crash on loading from save)
-protonfixes: Removed no-longer needed xlive override for Fallout 3 (thanks manueliglesiasgarcia!)
-protonfixes: Added workaround that uses Proton 5.0 to install .NET into the prefix for Space Engineers (.NET installation is broken on wine 6.0+, thanks manueliglesiasgarcia! )
-protonfixes: Added vcrun2019 to Madden NFL 21 -- fixes multiplayer desync (thanks Alexithymia2014!)
-protonfixes: Gothic2: account for varying casing in game paths (thanks codicodi!)
-protonfixes: Uplay overlay disabled for Assassin's Creed: Odyssey (thanks PolisanTheEasyNick!)
-protonfixes: mfc42 override added for GT Legends (thanks otokawa-mon!)
-proton-valve: Imported fixes for paradox launcher from proton upstream
-proton-valve: Imported fixes for Nickelodeon All-Star brawl from proton upstream
-proton-valve: Imported fixes for WRC8/9/10 from proton upstream
-proton-valve: Imported fixes for Satisfactory multiplayer from proton upstream
-proton-valve: Imported fixes for Fallout 76 crash from proton upstream
-vkd3d-proton: Update to git
-vkd3d-proton: DXR 1.1 is now experimentally exposed. It can be enabled with VKD3D_CONFIG=dxr11.
-vkd3d-proton: Resizable bar now enabled automatically if available. NOTE: You may need to disable this in eGPU setups to avoid performance issues: VKD3D_CONFIG=no_upload_hvv
-vkd3d-proton: Marvel's Avengers now playable (again)
-dxvk: Update to git
-faudio: Update to git

## Proton-6.19-GE-2 released

-Added protonfix that allows Apex Legends to run (It needed winetricks xact in order to not crash at black screen. This allows it to at least get to the character screen. Still does not allow to join match due to EAC)
-Added protonfix that allows BeamNG.drive to run
-Added patch that allows RaceRoom Racing Experience to run (Thanks Alistair Leslie-Hughes!)

## Proton-6.19-GE-1 released

-Added protonfix for Syberia black screen (runs in a window, you will want to use gamescope to upscale)
-Added protonfix for Japanese version of Tree of Savior (we already had one for the English version, thanks Alistair Leslie-Hughes!)
-Added patches that allow EA Desktop beta client to work (Thanks Esdras Tarsis!)
-Removed deprecated mouse focus patches (no longer used in upstream proton) -- fixes mouse focus issues in some various games.
-Added uuid-dev package to build environment to fix antlr build dependency (thanks Optimus22Prime!)
-Imported proton experimental build environment updates
-Imported proton DLSS patches/updates
-Updated dxvk-nvapi to proton experimental version (for DLSS)
-Updated wine and wine-staging to 6.19
-Updated vkd3d-proton to latest git
-Updated dxvk to latest git
-Updated FAudio to latest git

## Proton-6.18-GE-2 released

-This is a hotfix, I forgot to update the mono version in the proton build environment (whoopsie). Fixes mono install request popup.

## Proton-6.18-GE-1 released

-hotfix added for hitman 2 and death stranding hangs (thanks Paul Goffman!)
-patches added from proton upstream to allow deathloop to run (thanks Paul Goffman!)
-protonfix added to allow crysis remastered to run
-protonfix added for Sonic CD (thanks Chloe Stars!)
-protonfix added for Bejeweled 3 (thanks Chloe Stars!)
-steamhelper patch added so it no longer requires a large revert patch in wine (thanks openglfreak!)
-wine + staging updated to 6.18
-dxvk updated to git
-vkd3d updated to git
-faudio updated to git

Notes:

(1) A large amount of changes have been added in this WINE release for HID gamepad support, as noted:

HID joystick enabled by default.

Two additional pending upstream patches have been added on top of this for better functionality. Currently proton's SDL gamepad patches have been disabled in favor of WINE upstream's HID implementation. I did my usual test with Guilty Gear Strive and everything seems to appear OK. The test is done in the dojo, with one xbox controller and one ps5 controller -- both controllers showed up fully functional for player 1 and 2, and proper button mappings and button images showed and worked.

Another note regarding GG Strive in particular with the testing:
note you have to take some funky steps for 2 player to work in training mode (not linux specific): https://playgame.tips/how-to-play-with-a-friend-in-training

I have not tested any force feedback games and am not sure if patches for that have been added. Unfortunately re-enabling the SDL patches will require a -massive- list of reverts, so for the time being as mentioned, the default HID joystick impementation is being used and proton's SDL patches disabled, at least until proton upstream rebases.

(2) Deathloop seems to very much dislike alt+tabbing out. For me it would freeze the game. Other than that it appeared to be playable.

## Proton-6.16-GE-1 released

Nothing too crazy in this release, mainly just updating to 6.16 and other relevant submodules to latest git

    FSR default sharpness changed from 5 to 2 per AMD recommendations (page 25): https://github.com/GPUOpen-Effects/FidelityFX-FSR/blob/master/docs/FidelityFX-FSR-Overview-Integration.pdf
    protonfixes added to fix black screen in Gothic 1 and 2 -- thanks manueliglesiasgarcia!
    protonfixes added to enable dxvk async for Final Fantaxy XIII and Tomb Raider 2013 -- thanks iWeaker4you!
    Wine + Wine-staging updated to 6.16
    FAudio updated to git
    DXVK updated to git
    VKD3D updated to git

## Proton-6.15-GE-2 released

-Fixed regression that broke TemTem
-Fixed regression(s) that broke Tokyo Xanadu eX+
-Added workaround that skips CoD Black Ops III videos (allows game to be playable).

## Proton-6.15-GE-1 released

NOTE: Due to the symlink updates for steam cloud saves, you will want to remove your old game prefixes so that they are properly regenerated with new symlinks. Your games may not launch otherwise:

Proton Game and Prefix Launch troubleshooting:
https://www.youtube.com/watch?v=uxWJ1xvowMk

Changes:

    Import proper steam cloud save fixes from upstream proton

    Import Project Cars III window focus fixes from upstream proton

    Import Tokyo Xanadu Xe+ ASF fixes from upstream proton

    Import Guilty Gear Strive cloud save path fixes from upstream proton

    Import multiple font fixes from upstream proton

    Fixed crash with Hitman 2

    Added workaround for FFXIV broken login button
    Details:
    There are two executables shipped with FFXIV for the launcher -- ffxivboot.exe and ffxivboot64.exe.
    Each one has a 'new' launcher mode and an 'old' launcher mode. The 'old' launcher mode is what we use to login on linux,
    however it uses mshtml and jscript by default, which break the 'Log In' button.
    The normal way to usually get around this is to just press enter after you input your password,
    but that can be annoying when you accidentally hit the button.

    Added FFXIV frame timing configuration for DXVK to resolve some stuttering, noted here: doitsujin/dxvk#2210

    Re-added missing mfplat stub that was accidentally removed from staging's mfplat patches. This re-fixes some unity games that had broken mfplat in 6.14 (Notably Power Rangers: Battle for the Grid)

    Added pending upstream wine patches for Riftbreaker

    Added pending upstream winelib patch (fixes https://bugs.winehq.org/show_bug.cgi?id=51596)

    vkd3d patch added for Diablo II Resurrected (Note: This was added in case it fixes other games. Running non-steam games with proton is -not- supported).

    Wine + Wine-staging updated to 6.15

    DXVK updated to latest git (fixes Endless Legend and Borderlands 2 crashing)

    vkd3d updated to latest git

    Faudio updated to latest git

    Rebased proton sdl joystick patchset. Removed: winebus: Make it more explicit how we are checking for duplicate devices

## Proton-6.14-GE-2 released

This is just a hotfix. The previous release was missing the protonfixes listed for Metro 2033 and L.A. Noire. I've updated the version as I received complaints over releasing hotfixes without changing the version.

## Proton-6.14-GE-1 released

-Issue with uplay services not connecting fixed from upstream wine
-FFXIV launcher certificate popup box spam fixed from upstream wine
-EVE Online launcher issue fixed from upstream wine
-Added d3dx11_42 protonfix for Metro 2033 (thanks lukashoracek!)
-Added d3dcompiler protonfix for L.A.Noire (thanks manueliglesiasgarcia!)
-Added d3dcompiler protonfix for HighFleet (thanks Alistair Leslie-Hughes!)
-Fixed shutil missing from protonfixes which broke set_ini_options (thanks djazz!)
-Added Microsoft Flight Simulator 2020 fixes from proton
-Re-added revert for 97afac469fbe012e22acc1f1045c88b1004a241f which breaks controllers in some unity games (https://bugs.winehq.org/show_bug.cgi?id=51277)
-dxvk updated
-vkd3d updated
-wine and wine-staging updated to 6.14

## Proton-6.13-GE-1 released

-Added NOSTEAM=1 envvar for FFXIV and FFXIV trial. This allows you to run either the steam OR the standalone version in steam through proton. See the video below for in-depth details: https://youtu.be/SihRNczHn_4
-FFXIV launcher workaround updated (previously used BrowserType, needed Browser instead)
-Rebased proton SDL gamepad patches on top of staging. Fixes various controller mapping issues and force feedback issues
-Steam input profiles now work again due to SDL patch update
-Warframe 5 minute no-controller crash is properly fixed now, steamclient patch is no longer needed finally
-Guilty Gear Strive 2 player mode works with two controllers now
-Grand Theft Auto V save on exit is fixed
-Swords of Legends launcher is fixed
-Resident Evil 8 crash fixed (it was crashing after they updated the game with FSR)
-vkd3d/dx12 resizable bar patches added. Can be enabled with VKD3D_CONFIG=upload_hvv
-AMD FidelityFX Super Resolution (FSR) has been patched in as the fullscreen hack's upscaling backend. Works on most games (not all, there are some caveats). For basic usage in most case only WINE_FULLSCREEN_FSR=1 is needed. The default sharpening of 5 is enough without needing modification, but can be changed with WINE_FULLSCREEN_FSR_STRENGTH=# (0-5) if wanted.
-1080p, 4k, and ultrawide input quality resolutions have been added to the FSR patch. See: https://gpuopen.com/fidelityfx-superresolution/#quality
-Various cloud save location symlink fixes have been added:
    My Documents -> Documents
    Application Data -> AppData/Roaming
    Local Settings/Application Data -> AppData/Local
-Font fixes imported from proton upstream
-DXVK updated
-vkd3d updated
-FAudio updated
-Wine-mono updated to 6.2.2

-A note on controller changes: hotplugging is still a bit wonky. If you unplug a controller then replug it, you may need to restart the game.

## Proton-6.12-GE-1 Released

-Necromunda "glowing" fixed
-Cyberpunk 2077 inventory crash fixed
-Guilty Gear Strive video playback fixed
-Forza Horizon 4 appears playable on Nvidia now (so far from my testing it seems to run now without issue)
-Battlefield 4 multiplayer ping issue fixed -- new ping patch from upstream added https://source.winehq.org/patches/data/207990
-Civilization VI now playable
-RDR2 working again (turns out it worked before, it just needed -fullscreen option otherwise it refused to launch. added in protonfixes now)
-fixed issue where directx and/or other prefix preinstall steps would hang/fail
-added fixes for star wars galactic battlegrounds saga
-dxvk updated to git
-vkd3d updated to git and pending 2.4 pull requests added
-faudio updated

## Proton-6.10-GE-1 Released

-Added UE4 preinstall workaround for Necrumunda
-Added UE4 preinstall workaround for Deliver us the Moon
-Added fix for Guilty Gear XX Accent Core R 2 hang
-Added Horizon Zero Dawn animations patch
-Added FarCry regression hotfix
-Origin seems to be much more stable/reliable now in regards to installation and launching
-Added staging bcrypt patches rebased on top of proton rdr2 patches (allows Steep online mode to work again)
-Added proton nvapi updates
-Added proton QPC performance patches (should help with fps regression)
-Added proton LFH performance patches (should help with frame times)
-dxvk updated with proton latency fixes
-vkd3d updated with proton latency fixes
-faudio updated
-steamclient updated with splitgate fix

## Proton-6.9-GE-2 Released

This build is a hotfix for Resident Evil Village (8)

## Proton-6.9-GE-1 Released

-Removed patch that was causing a lot of the RE8 crashes. Stability should be a lot better now. You may still occasionally get crashes when first opening the game, or during loading, or while changing screen resolution. Apart from that I was able to get through all of the intro cutscenes up to the playable 'van' area (trying not to spoil the game here) at the beginning on both AMD and Nvidia . Nvidia still takes a while to load the game, but it should at least be playable now.
-vcrun2019_ge checksum has been disabled. It's downloaded from Microsoft and changes too often, resulting in regular breakage. Removing the checksum allows it to download and install regardless of if the sha sum has changed. If people are worried about it they can check the sha sum themselves in ~/.cache/winetricks/vcrun2019_ge
-Days Gone is playable now (it takes a while to load, just a warning)
-Marvel's Avengers is playable now
-Mortal Kombat X story mode audio fixed/playable now
-Halo:MCC should no longer force windowed mode (issue it was required for has since been fixed)
-DXVK updated to latest git
-FAudio updated to latest git
-vkd3d updated to latest git
-wine/staging updated to 6.9

## Proton-6.8-GE-2 Released

-Mass Effect Legendary Edition Launcher and ME1 fixes added. All 3 games should be playable.
-DOOM Eternal should no longer hang and resolution change should work again
-Forza Horizon 4 frequency patch added, however this does not seem to improve the crashing :/
-RE8 REENGINE Logo audio is fixed and no longer plays static (game is still crashy)
-RE8 Display menu fixes ported from proton experimental
-Nioh 2 hang fixed (videos still don't play)
-Fallout: New Vegas audio looping fixed
-2k Launcher fixes ported from proton experimental (fixes mafia, mafia II, and others)
-Yakuza 0 - fsync disabled (thanks tgurr!)
-Yakuza Kiwami - fsync disabled (thanks tgurr!)
-LEGO The Lord of the Rings d3dx9_41 override added (thanks alkazar and FigoFrago!)


## Proton-6.8-GE-1 Released

HOTFIX 2:
-Resident Evil Village (8) now works. RE Engine intro logo audio plays static, everything else works fine.
HOTFIX:
-Fixed video distortion issue in RE2 videos (was being caused by the nier replicant patch forcing wrong video format type on all videos)

Changelog:
-Forza Horizon 4 now works
-Nier Replicant now works (Video Playback included)
-Fixed various issues surrounding start.exe Such as ShellExecuteEx failures (causing games not to launch).
-Fixed issue with Borderlands 2 not launching
-Fixed issue with Borderlands 3 hanging on claptrap loading screen
-Fixed audio loop issue in Fallout New Vegas
-Fixed issue with Yu-Gi-Oh Duel Links needing vcrun2019
-Fixed issue with uplay, origin, and other game clients not installing on new prefixes
-Fixed issue with Persona 4 Golden not relaunching after first time.
-Fixed issue with keyboard input not working if a controller is connected.


## Proton-6.5-GE-2 Released

HOTFIX:
-Added wine-mirror/wine@fcb37c9 to resolve start.exe issue
-Added sha512sum file to releases for external update tools

Attached build has been updated.

General Proton fixes:
-Added mouse stutter fix from proton experimental
-Fullscreen hack is back! Works with MK11 finally!
-DXVK updated
-vkd3d updated
-FAudio updated

Game fixes:
-Fixed RDR2 Online mode, works now
-Fixed GTA V forcing players into solo online sessions and making them unable
to join events
-Fixed Sea of Thieves crash on loading after creating a new lobby
-Fixed issue with games exiting and leaving steam in 'running' mode
-Added launcher workaround for Evil Genius 2

MFPlat fixes:
-Fixed MK11 random mid-game/mid-cutscene mfplat crashes (hopefully)

Known issues:
-MK11 will crash in story mode on chapter select if you do not select a level
before one of the video clip animations completes
-Catherine Classic still doesn't work
-Darksiders Warmastered Edition still doesn't work
-Grandia/Grandia II HD Remaster still crash on opening.

## Proton-6.5-GE-1 Released

@GloriousEggroll GloriousEggroll released this 9 hours ago

This release is mainly a big cleanup of the mfplat stuff that was broken and should get most of the things working which were working before in addition to a few new fixes:
MFPlat/Video playback fixes:

-Trials of Mana video playback fixed
-Devil May Cry 5's "History of DMC" video playback fixed
-Power Rangers Battle for the Grid video playback fixed
-Seven: Days Long Gone video playback fixed
-Borderlands 3 Marcus intro video playback fixed
-Resident Evil 2/3 video playback fixed
Other Game fixes:

-Red Dead Redemption 2 single player story mode finally works
-Dragon Star Varnir opening crash fixed -- game is now playable
Component updates:

-DXVK updated
-VKD3D updated
-OpenXR patches updated
-Wine and Wine-Staging updated to 6.5
Still Broken:

-Red Dead Redemption 2 online mode does not work (disconnects)
-GTA V puts users in solo session
-Catherine Classic still hangs at new game loading screen
-Darksiders Warmastered Edition hangs at thq nordiq intro logo
-Grandia/Grandia II HD Remaster still crash on opening.

## Proton-6.4-GE-1

Thanks everyone for being patient with this one. There's still some media foundation related bugs and pending fixes that Derek (mfplat patchset author) is working on, but this release should be good enough to get some new games working that weren't previously (notably MK11, Injustice 2, Need for Speed), At the end of the week wine 6.5 releases so if the media foundation patches are fully resolved by then there will likely be another release. Here are the details on this release for now:
Media Foundation changes/currently known issues:

Working:
-MK11 cutscenes fully working, video+audio in cutscenes works, has slight audio desync. Crypt also works.
-Injustice 2 cutscenes fully working, video+audio in cutscenes works, has slight audio desync

Broken:
-DmC 5's "History of DMC" video is broken again
-Power Rangers Battle for the Grid Story videos broken
-Seven: Days Long Gone Humble Bundle logo video will hang if intros are not skipped
-Borderlands 3 Marcus intro on new game hangs (again)
-RE2/RE3 WMV playback currently broken
Notes:
-As this is a new implementation of the mfplat patches, WMV support and MPEG4 Section 2 support are both missing/not added yet. It is a work in progress, and you may see bugs that were previously fixed. Please be patient as this is a work in progress.
Wine:
-Updated wine + wine-staging to 6.4-git
-Need For Speed atiadlxx fix ported from proton (Need For Speed now runs)
-Crown Trick + Home Behind 2 fix ported from proton
-Hades controller input fix ported from proton
-DualSense/PS5 controller mapping ported from proton
-Additional OpenXR patches ported from proton

-FAudio updated to git
-Wine and Wine-staging updated to git
-vkd3d updated to git
-dxvk updated to git and FarCry 5 texture issue worked around
-Dead or Alive 5 protonfix added (thanks iglu47)
-watchdogs 2 and farcry5 uplay overlay disable protonfixes added (thanks iglu47)
-corefonts fixed in protonfixes (thanks iglu47)
-vcrun2019_ge download url updated in protonfixes
-winetricks updated in protonfixes
-msiexec re-enabled in wine build (thanks fastrizwaan)

All in all, I would say the summary of this build is if you want to play MK11 or Injustice 2, this build is for you, but if you have any games that heavily relied on Media Foundation (mfplat) prior to this, chances are they may be broken in this build. Once Derek gets WMV and MP4S2 implemented along with some cleanups the next build should work nicely regarding mfplat.

## Proton-6.1-GE-2

HOTFIX: 2/7/2021
-removed futex2 patches, they cause warframe's launcher to freeze.
Download link updated
Release notes:

-removed previous steam common redistributables fix for winetricks -- it was causing crashes on arch systems, and winetricks fixed the download urls upstream anyway. This should also fix some issues with games launching once then not launching again.
-updated winetricks in protonfixes
-added tree of savior d3dcompiler_47 override
-fixed crash issue in RE2 and Visage on vega APUs due to dxvk being compiled with gcc9 (resolved with gcc10)
-cyberpunk heap allocation/shared memory patches added, should improve performance
-additional spatial audio patches added from experimental
-futex2 patches added from experimental

## Proton-6.1-GE-1

Hotfix #3: 2/1/2021

Since Microsoft decided to remove the download URLs for DirectX:

https://techcommunity.microsoft.com/t5/windows-it-pro-blog/sha-1-windows-content-to-be-retired-august-3-2020/ba-p/1544373
https://www.reddit.com/r/pcgaming/comments/l79r4x/psa_microsoft_has_removed_directx_download_from/
https://www.reddit.com/r/linux_gaming/comments/l7sax5/microsoft_removed_older_offline_directdownloads/

It broke some of the usual protonfixes/winetricks overrides -- such as d3dx11_43, d3dcompiler_43, xaudio, xactengine, vcrun2015/17/19 and a few others. Luckily for us, Valve ships most of these and it's auto-downloaded on most systems that run Windows or Proton games, under the 'Steamworks Common Redistributables' tool.

With that being said, I've added functionality to proton to detect this folder, and install the overrides from this folder, instead of having to download them from Microsoft. This should save both bandwidth and disk space.

Again, if you have issues with protontricks not being applied to the prefix, make sure you have 'Steamworks Common Redistributables' installed under the 'TOOLS' section of your library in steam.

Download updated.
Hotfix #2: 1/31/2021

-Persona 4 Golden sound actually fixed this time with xactengine3_7 override
-Persona 4 Golden protonfixes k-lite install fixed to use locally written config for unattended install instead of github download
(If this was an issue for you before, please try again with a clean prefix)
-Microsoft Flight Simulator crash on new flight loading fixed (needed missing wmphoto patches)

Download updated.

Hotfix: 1/31/2021

-Small hotfix which adds rebased patch for doitsujin/dxvk#1582. Allows it to be applied to upstream dxvk without reverting doitsujin/dxvk@2d670ec and doitsujin/dxvk@c107345. Not a major change, but not reverting them fixes some validation errors per the commit comment. Download updated.
Updates:

-Persona 4 Golden in-game audio fixed, game should now be fully playable
-Cyberpunk 2077 issue resolved where FPS would be half of that experienced in regular proton (Thanks TKG for finding the dxgi override which resolved it)
-fsync issue causing conhost to pin 1 cpu at 100% resolved (thanks openglfreak Frogging-Family/wine-tkg-git@ddd28ce)
-controller hotplugging fixes imported from proton experimental for Subnautica and DOOM 2016
-Yakuza like a dragon controller detection fix imported from proton experimental
-Warframe controller workaround functionality updated
-dxvk updated
-vkd3d updated
-faudio updated
-wine + wine-staging updated
A note about Warframe controller functionality:

The issue with Warframe via Steam Play/Proton as many people know is that if you do not have a controller plugged in, the game would crash after 5 minutes on the dot. The workaround for this was to run xboxdrv to create a fake controller. About a year ago I created a patch for steamclient that worked around this issue by checking the names of joystick devices (js0,1,2 etc) in /dev/input/. This -sort of- worked. The reason I say sort of, is because some non-gamepad devices such as corsair mice and keyboards register themselves as joysticks.

So the trick was to check the name for anything that didn't have 'keyboard' or 'mouse' in the name. This however, did not work, as other devices such as steering wheels and flight controllers also got passed as 'gamepads'. Since steering wheels and flight controllers are not used in Warframe.. this again led to the crash.

I've now edited the patch again, this time steamclient's controller interface (which causes the crash), will not load in Warframe unless the device name contains 'controller' or 'pad'. I tested this with xbox, ps4, switch, and logitech controllers, as well as off-brand controllers, both wired, bluetooth, and ms xbox wireless, all were recognized ok, and the interface did not load with my steering wheel or hotas flight stick.

The purpose of this patch is to allow Warframe to run -with out- needing xboxdrv, so that it will not crash. If you experience warframe crashing after 5 minutes on the dot, please let me know, as I'd like to know more about your joystick devices in /dev/input and possibly add an exception if needed.

Please keep in mind this detection system only affects Warframe. Outside of Warframe controllers and other devices will act as they would normally in Valve's proton.
A note about Skyrim SE Script Extender (skse64):

The patch for SKSE has been removed, per:

https://bugs.winehq.org/show_bug.cgi?id=44893#c17

The author of SKSE admitted a bug in skse and and fixed it upstream in skse:

--- quote ---
I reached out to the SKSE team about this and Ian Patterson confirmed that there
had been a bug with calculating the minimum safe address and corrected it in
F4SE, but somehow it was not corrected for SKSE.
--- quote ---

This has since been fixed here:

ianpatt/skse64@4a1e121

However a new version of SKSE has not been released yet so the fix is not in it. The fix was added Dec 28 but the current SKSE build available at https://skse.silverlock.org/ is from August.

I've recompiled it and supplied it here (with sources) until the Author releases a new version:

https://drive.google.com/file/d/1I6tgvZDaSs2JPXkHdWJwuZVwzF0OSpzz/view?usp=sharing

Seems to work for me. Game launches and my mods work. If a specific mod doesn't work but others do it's likely an issue with that mod specifically more so than SKSE. Please note I'm providing this to get mods working for the majority of people without needing patching, and -not- responsible if any specific single mod does not work. The latest version of SkyUI seems to work here for me.
Known issues:

-The build uses proton's new runtime, which runs within a container, therefore all of the current Proton 5.13 issues also apply here.

ValveSoftware#4289

-MK11 Story mode and Cinematics do not work
-Injustice 2 Cinematics do not work
-Catherine Classic is not working
-Darksiders Warmastered Edition intro + cutscenes do not work
-Black Ops III does not work
-Grandia and Grandia II do not work

## Proton-6.0-GE-1

Game Fixes:

Persona 4 Golden now playable but with issue -- in-game audio is broken. Cutscenes and cutscene audio are working.
Fixed issue that prevented Death Stranding from running in 5.21
Fixed issue with video playback in DmC 5 (again)
Fixed issue preventing controllers from being detected in some games on certain distros
Controller Hot Plugging now working
Controller patches completely rebased from 5.13
Mangohud now working
Vulkan device select layer now working
Wine updated to Wine-Staging 6.0
gstreamer libraries updated to 1.18.3
vkd3d updated to 2.1-037efbd to contain Dirt 5 fix
dxil-spirv submodule in vkd3d updated to contain latest Horizon Zero Dawn fixes.
DXVK updated, contains F1 game fixes
DXVK pending pull requests 1582,1673,1759,1805 added:

doitsujin/dxvk#1582
doitsujin/dxvk#1673
doitsujin/dxvk#1759
doitsujin/dxvk#1805

Should contain most of the fixes from Proton-5.13 from Valve, if something is missing let me know in discord.

Proton Fixes:

added klite verb with ini for custom silent install for Persona 4 Golden
updated Persona 4 Golden protonfixes script

Known Issues:

-The build uses proton's new runtime, which runs within a container, therefore all of the current Proton 5.13 issues also apply here.

ValveSoftware#4289

-Red Dead Redemption 2 still does not work. Unfortunately the syscall patches in current proton do not work with upstream wine.
-Fullscreen hack is still currently disabled.
Known mfplat+quartz issues:

-Catherine Classic is not working
-Black Ops III is not working
-Injustice 2 cutscenes broken currently
-Darksiders Warmastered Edition intro+cutscenes broken currently


## Proton-5.11-GE-3-MF

Fixes:
-Re-enable rawinput (seems staging had it disabled in the previous build)
-Re-enable FakeDLLs and SECCOMP (seems staging had it disabled in the previous build) - needed for Doom Eternal,Detroit:BH, Origin
-Re-enable HideWineExports (seems staging had it disabled in the previous build) - needed for FFXIV
-Fix issue with not being able to regain focus after alt+tab in various games
-Fix issue with GTA V keyboard input not working
-Fix issue with rawinput not working properly within a virtual desktop
-Fix issue with Warframe and SWTOR not rendering correctly in dxvk on nvidia
-Added patch that allows Indiana Jones and the Emperor's Tomb to run
-Added patch that allows MGS: Ground Zeroes to run (keyboard+mouse input is currently broken, needs more work. Works with controller)
-Added workaround for Warframe launcher rendering all black in wined3d mode (game still crashes in wined3d) - Thanks Iglu47
-README has been overhauled. Thank you TheEvilSkeleton!

## Proton-5.11-GE-2-MF

GloriousEggroll released this Jun 29, 2020

This is a minor hotfix/stability release:

-Fixed issue with steam overlay causing mouse lag after 30+ minutes (issue present since 5.9, was missing from rawinput patches)
-Fixed issue with mouse hitting 'invisible walls' (issue present since 5.9, was missing from rawinput patches)
-Fixed issue with prefixes not generating properly causing some games not to be able to save due to the recent user name changes
-Ashes of the Singularity now works, vulkan renderer does not. Need to use DX11/12
-Jurassic World: Evolution now works

NOTE: If you want to allow your save games to work when using proton within lutris, you need to set WINEUSERNAME environment variable
NOTE: If you want proton's media foundation to work in lutris, you need to set GST_PLUGIN_SYSTEM_PATH_1_0 and WINE_GST_REGISTRY_DIR environment variables.


## Proton-5.11-GE-1-MF

GloriousEggroll released this Jun 26, 2020

Game fixes:
-Origin 5.11 hang fixed
-Origin fixes ported from Proton 5.0.9
-Path of Exile Vulkan Renderer in-game swap fixed (for radv you will need mesa-git for upstream graphical glitch fixes)
-StarCitizen hang fixed
-Divinity Original Sin 2 hang fixed
-Mount and Blade: Bannerlord launcher fix added
-Persona 4 protonfixes fixed (thanks Pobega)
-Warframe launcher download hang fixed (broke in 5.10, still does not show progress bar)
-Sea of Thieves proper websockets implementation patches added (no longer needs win7)
-Partial fix for Catherine -- game now opens and can reach menus. Hangs on new game, waiting on EVR implementation in wine
-Deep Rock Galactic (and other games) libffi dependency fixed that was causing various crashes -- note, please do not use steam-native if you are on arch, steam-runtime should always be used.
-Protonfixes added for Assetto Corsa, should now work OOTB

Build additions:
-'wmp9_x86_64' winetricks verb imported to protonfixes from upstream winetricks that allows wmp9 to be installed in 64 bit prefixes
-hotfix added to use normal username instead of 'steamuser' when run with non-steam games. This also seems to fix issues with origin and other platforms not being able to save game (such as running Jedi Fallen Order origin version in lutris with proton)
-vkd3d updated
-dxvk updated
-FAudio updated

Build removals:
-Temporary removal of fshack, currently breaks MK11
-Temporary removal of esync, 5.10+ did a large rework of ntdll which broke compatibility with esync. The patchset needs to be rebased. It is currently disabled in staging.
-Temporary removal of fsync - fsync relies on esync. No esync = no fsync.

Known issues but playable:
-MK11 - no audio in custscenes -- needs SAR fixes, online matches broken
-Injustice 2 - no audio in custscenes -- needs SAR fixes
-Broken sound in Borderlands 3 Marcus new game intro -- can be skipped.
-Age of Empires II WMV videos don't play
-Street Fighter V intro videos don't play

Still broken:
-Seven (hangs on new game)
-Catherine (hangs on new game)
-Soul Calibur VI (hangs at main menu, needs SAR fixes)
-Nioh videos don't play, gameplay untested

Marking this as release as it has a lot of regression fixes and should be quite stable, despite the ongoing media foundation work and esync/fsync being disabled.


## Proton-5.9-GE-2-MF

GloriousEggroll released this Jun 06, 2020

--HOTFIX--
6/10/2020 7:17 PM MST:
After reviewing the issue tracker again for Sea of Thieves I found via ga2mer's comments that it becomes working/playable after login if the prefix is set to Win7. I tested this and it did indeed allow me to login and get past the previous journal issue/became playable. I've added a hotfix in protonfixes that should do this automagically. Updated Proton-5.9-GE-2-MF.tar.gz again.
--HOTFIX--
6/10/2020 10:15 AM MST:
I accidentally applied part 1 of a 2 part patch for RE3 twice instead of both 1st and 2nd parts, so I just corrected that and recompiled + reattached Proton-5.9-GE-2-MF.tar.gz. RE3 credits should work now

Hi all, I'm marking this as another pre-release as we still have some audio issues with media foundation, and a few other pending issues, however we also have quite a few fixes:

-Fullscreen hack is disabled still for compatibility with MK11.
-Rawinput re-enabled
-Nier/sekiro winex11 patch re-enabled
-winevulkan patches re-enabled
-The weird Skyrim mouse reverse input issue was fixed in 5.10, so I've backported it.
-There is some heavy work being done on wined3d and dxgi, which causes some additional issues, so TOXIKK and Killer Instinct require wined3d to currently run properly. Protonfixes have been added to do that automatically, so those games both work with wined3d currently.
-There is also some heavy work being done on ntdll in 5.10+, which cause esync and fsync patchsets to not be compatible. Due to this, I'm currently working with 5.9 and backporting specific changes necessary to retain esync and fsync compatibility.
-A dxgi native override was also added in protonfixes so that Metal Gear Solid V: Phantom Pain now works
-A fix has been added for the RE3 credits crash - thanks vitorhnn!
-A fix has been added for the MK11 and Injustice 2 video color issue - thanks vitorhnn!
-A partial fix for websockets has been added for Sea of Thieves so that login now works, however it is currently crashing after login on 'Opening the Journal' - thanks ga2mer!
-5.10 media foundation patches have been backported
-Remi Bernon's free range memory allocation patches have been backported which increases performance in We Happy Few and some other games.
-Proton 5.0.8 changes backported
-DXVK updated
-vkd3d updated
-FAudio updated

Known issues:
-Fullscreen hack still disabled for the time being to retain compatiblity with MK11
-Path of Exile cannot switch to vulkan renderer when using RADV, but works with AMDVLK. This is something else tied to fullscreen hack, as patching in fullscreen hack allows it to switch. RADV currently has a lot of graphical glitches with PoE anyway, so for the time being AMDVLK is the better option to use.
-Soul Calibur VI still hangs at intro due to incomplete SAR work in media foundation
-Injustice 2 and MK11 cut scene audio is missing due to incomplete SAR work in media foundation
-Borderlands 3 Marcus intro on new game audio is distorted due to incomplete SAR work in media foundation, but is skippable.
-Seven still only plays intro audio, no video, and crashes after starting new game due to incomplete SAR work in media foundation.
-libffi6 is still needed for some rolling release distros such as arch
-As mentioned, due to work being done with wined3d, dxgi is in an odd state. If a game works in proton, but does not work in proton-ge, try adding WINEDLLOVERRIDES=dxgi=n %command% to the options. If it works, let me know and I can add a protonfixes override for it.

Currently I would say this should be ok to use for most games except Soul Calibur VI and Seven


## Proton-5.9-GE-1-NR

GloriousEggroll released this on May 28, 2020

-Fullscreen hack was found to be the cause of Mortal Kombat 11 not working. This also requires a few other patches to be disabled such as some additional vulkan patches and raw input, as well as the Sekiro patch. Fullscreen hack used to work with this game, so this is just a temporary disable until I can figure out what in the patchset is causing MK11 to not work.
-Spyro audio is fully working now
-BL3 Markus intro has audio issues still but is skippable
-Soul Calibur VI freezes at the intro screen currently due to an issue with SAR audio.
-Seven actually launches now. Audio for intro movie plays but shows black screen. New game results in crash, again due to SAR audio.
-PC Building Simulator no longer freezes when running 3dmark on low settings. It just skips the video.


## Proton-5.8-GE-2-MF

GloriousEggroll released this on May 13, 2020

This is an update to 5.8-GE-1 in regards to media foundation work:

Completed:
-RE3: Bathroom scene fixed
-Dangonronpa v3 fixed
-Power Rangers Battle for the grid chipmunk voices fixed
-Monster Hunter World tutorial movies fixed
-Super Lucky's Tale -- Fixed an issue with bink videos not playing in GE builds which work in proton

WIP (work in progress):
Borderlands 3 Marcus intro video
Darksiders Warmastered Edition opening videos play now play, but New Game movie crashes
Street Fighter V intro videos don't play
Seven intro videos don't play

Todo:
-Age of Empires II WMV videos don't play - check if MF or quartz
-Catherine Classic does not play, opens small black box for game window - check if MF or quartz
-Nioh videos don't play - check if MF or quartz


## Proton-5.8-GE-1-MF

GloriousEggroll released this May 10, 2020

Overall fixes:
-Fix for ValveSoftware#2929 added, fixes crash in Dark Souls 3, Sekiro, Nier: Automata
-GTA IV should be fully playable now, patches imported from upstream proton
-Street Fighter V should be fully playable now, patches imported from upstream proton
-HideWineExports=Y registration added for FFXIV, fixes license issue
-Homeworld Remastered Collection should be playable without custom launcher necessary
-Updated steep patch for wine 5.8
-fixed proton controller patch issues -- should now have full proton controller patchset and functionality to match upstream proton
-patch added that fixes overwatch breakage in 5.7
-patch added that fixes star citizen breakage in 5.7
-patch added that fixes Path of Exile flicker in 5.7
-FFXV patch is now working again, game should be playable
-Monster Hunter World patches added which enable DX12 mode with vkd3d
MF (Media Foundation) specific fixes:
-Resident Evil 2 videos fixed, should now be fully playable, also works in DX12/vkd3d
-Spyro Reignited Trilogy videos fixed, should now be fully playable
-Remnant: From the Ashes videos fixed, should now be fully playable
-Soul Calibur VI videos fixed, should now be fully playable
-Street Fighter V videos fixed, should now be fully playable
-Deep Rock Galactic videos fixed, should now be fully playable
-BlazBlue Centralfiction videos fixed, should now be fully playable
-Bloodstained: Ritual of the night intro videos fixed, should now be fully playable
-Crazy Machines 3 videos fixed, should now be fully playable


## Proton-5.6-GE-2

GloriousEggroll released this Apr 14, 2020

-This is a hotfix that reverts the fullscreen hack changes, as they introduced a regression with mouse stutter on movement after a period of time. What this means:
-Fullscreen hack is still enabled, it's just using proton's version, not customized for staging
-Staging's winex11.drv-mouse-coorrds and rawinput patchsets have been disabled
-Proton's rawinput patchset has been re-enabled.

Normally I'd wait to release smaller changes like this, but the regression made some games basically unplayable. This should allow games to be played at least without the mouse stutter.


## Proton-5.6-GE-1

GloriousEggroll released this Apr 13, 2020

This is a pre-release continuation of the mfplat work done by Guy1524 (Derek) along with some additional fixes.

Wine + Wine-staging:
-Update to 5.6 release

mfplat:
-Add partial WMV playback support (Should allow RE2 and RE3 movies to play)
-Add gst-plugins-ugly and wmv playback patch to build

protonfixes:
-Add dxgi=n override for Darksiders Warmastered Edition, game seems to crash with wine's dxgi when using dxvk
-Add Divinity Original Sin 2 symlink fix update - fixes black screen on first launch
-Add SECCOMP override for RE3, needed by Denuvo
-Add SECCOMP override for DOOM Eternal, needed by Denuvo

proton:
-Add Proton 5.0.6 alpha patches
-Add Proton 5.0.6 alpha DOOM Eternal Audio patches
-fixed build system to include dist folder directly instead of tarball. This fixes the issue with sometimes having to hit the play button twice, or some issues people have on their system where the dist tarball never extracts.
-fullscreen hack patches modified to work with staging's winex11.drv-mouse-coorrds and rawinput patch sets

Notes:
-Spyro is still broken
-MHW Tutorials are still broken
-BL3 usually wants to set Direct12, which crashes. This generally leads to a popup asking you to restore default settings (confirm/hit yes). You will then need to relaunch the game and go in the games settings and change it to DirectX11 manually. After that DirectX11 should stick as the default mode.
-RE2 Crashes in DX12 with vkd3d at main menu, you'll need to set DirectX11 in re2_config.ini for DX11 with DXVK
-RE3 Seems to work with DX12 and vkd3d with minor interface graphical glitches. Can set DirectX11 in re3_config.ini for DX11 with DXVK
-FFXV seems to be working again

Again, I must note that 'pre-release' builds are basically alpha-testing builds. While they may contain a lot of fixes, some things may also be broken that normally are not.

Specifically in this regard - proton normally disables 'mfplay' which allows media foundation movies in many games (WMV and MP4) to just be skipped automatically. Since we enable this without full functionality, some games, such as Spyro or MHW, may hang when a movie tries to play.

If you wish to re-disable media foundation to use this version with your other games, you can use WINEDLLOVERRIDES=mfplay=n %command% in the game's launch options.


## Proton-5.5-GE-1

GloriousEggroll released this Apr 5, 2020

So I'd like to preface that this is a pre-release that has a massive amount of media foundation/mfplat wine patches. A huge thank you goes to Derek Lesho (Guy1524: https://github.com/Guy1524/wine) as well as Nikolay Sivov and Sergio Gómez Del Real all from CodeWeavers for getting this stuff working and taking the time to help me get it working with the correct dependencies in proton.

What this does is allows mp4 playback in MANY titles, including UE4 -and- Unity engine games. This fixes a lot (not all, but a lot) of issues surrounding media foundation/mfplat without the need for the 'mf-install' workaround that has legal issues and limitations, and is much safer for us to ship.

Tested fixes:
-Fixed borderlands 3 lilith in-head videos and 'watch the monitor' video bug
-Fixes Remnant: From the Ashes intro videos, intro menu, character menu
-Fixes intro video on Bloodstained: Ritual of the Night
-Fixes mp4 playback issues related to Crazy Machines 3

Still broken:
-Borderlands 3 intro narrative with Marcus's voice on new game does not play
-Spyro is still broken
-Probably some other mp4 related titles

Additional updates:
-A small patch has been added that should fix sunset overdrive from crashing on launch: https://source.winehq.org/patches/data/182631
-Two warframe launcher regressions have been fixed
-Mouse input fix patches which were added to wine-staging for Mount & Blade II: Bannerlord: https://bugs.winehq.org/show_bug.cgi?id=36873
-Lots of gstreamer plugin related work has been done/added in order to get media foundation stuff working. This was also cleared with aeikum and kisak from Valve personally, and deemed -ok- to include in my repository. This means it is safe to continue to link in Valve's issue trackers, unlike the 'mf-install' workaround. HURRAY!

Additional notes:
-Not -all- mp4s are fixed. There are still some that have problematic formats that are being worked on.
-Also coming down the pipe soon will be WMV playback fixes. This is to be handled after the mp4 issues are sorted.

Enjoy!


## Proton-5.4-GE-3

GloriousEggroll released this Mar 25, 2020

-wine 5.4 updated to latest git which includes some fixes/updates winevulkan to 1.2.134. DOOM Eternal seems to work fine with it when not blocked by Denuvo.
-Added ValveSoftware/wine#86 for more winevulkan compatibility
-Added https://source.winehq.org/patches/data/181826 for more winevulkan compatibility
-FAudio reverted to 20.03 stable release as some audio issues were reported
-Warframe controller patch updated to strictly only take effect when warframe is running, since the issue doesn't seem to affect other games.
-proton controller patches have been disabled (again) in favor of standard wine+wine-staging's, after reports of 'ghost' input and/or periodic input loss. SDL patches are still in applied.


## Proton-5.4-GE-2

GloriousEggroll released this Mar 22, 2020

This is more of a clean-up release although some new stuff/fixes have been added, mainly for DOOM Eternal

-Updated wine + staging to 5.4-git/upstream for DOOM Eternal
-Added ValveSoftware/wine#85 VK_KHR_get_surface_capabilities2 and fake support for VK_EXT_full_screen_exclusive for DOOM Eternal
-Added ValveSoftware/wine#83 which fixes some crashes in DARK SOULS III (374320), Nier: Automata (524220), Sekiro: Shadows Die Twice (814380)
-Added some missing registry entries that prevented Batman: Arkham Knight from starting on a clean prefix
-Cleaned up/removed unused mf_install verb in protonfixes in preparation for newer mfplat alpha patches (coming soon)
-Removed '-wolcen lords of mayhem 'blob head' fix' as the game devs fixed it internally per update 1.0.10.0
-Removed 'plasma systray fix' as it didn't really benefit anything, and actually interfered with some games.
-Removed Detroit:Become Human patch as it's already been upstreamed
-Cleaned up some duplicate patches and updated our current patches to work with latest wine-git+staging/git
-Updated vkd3d
-Updated dxvk
-Updated FAudio

Notes on DOOM Eternal:

    DOOM Eternal currently requires vulkan-loader/vulkan-icd-loader 1.2.135
    For AMD also requires mesa-git .
    ACO did not work for me with DOOM Eternal when I tried it, but llvm worked fine.
    To get rid of pre-launch GPU notices such as (HDR not supported), open DOOMEternal/launcherData/launcher.cfg and change all of these to 0:

rgl_showAMDStartupWarning 0
rgl_showIntelStartupWarning 0
rgl_showNvidiaStartupWarning 0


## Proton-5.4-GE-1

GloriousEggroll released this Mar 16, 2020

-controller fix for warframe - allows controller profiles to be loaded only if a controller is plugged in. fixes crash if no controller plugged in after 5 min.
-vkd3d updated, allows WoW to be played using proton via lutris (disable dxvk in lutris)
-more metro exodus vkd3d fixes
-wolcen lords of mayhem 'blob head' fix
-detroit: become human patch added
-need for speed world launcher patch added
-wine+ wine-staging updated to 5.4
-dxvk updated to latest git
-faudio updated to latest git
-fixes from Proton 5.0.4 imported

Known issues:

-MHW broken since last patch.
-MK11 broken since wine 5.0
-Injustice 2 broken since wine 5.0 (did not work here, but have had it reported working in 4.21)
-Borderlands 3 does not work with vkd3d yet


## Proton-5.2-GE-2

GloriousEggroll released this Feb 23, 2020

This is a pre-release to fix Fallout New Vegas from crashing on main menu.
-fixes a missing portion of the fullscreen hack
-dxvk updated
-more metro exodus vkd3d fixes
-wine 5.2 updated to latest git


## Proton-5.2-GE-1

GloriousEggroll released this Feb 19, 2020

This is a pre-release to fix the Warframe Launcher bug introduced in 2/18's update.


## Proton-5.1-GE-2

GloriousEggroll released this Feb 17, 2020

This is mainly a hotfix + feature release build.

Hotfix:
-Fixed warframe requiring a controller to be plugged in. That's right, you no longer need xboxdrv! I spent the weekend debugging it and was finally able to come up with a bit of a hacky workaround, but it works for now until valve addresses the issue (it has to do with the way lsteamclient handles controllers)

Feature:
-vkd3d branch is latest from codeweavers + DXIL changes by Hans Kristian (who has been doing a lot of vkd3d submissions) + metro exodus commits that both Hans and Doitsujin (creator of dxvk) have been working on together. The previous release had Hans's DXIL changes, this just adds the Metro changes on top of it. With that being said, expect some minor graphical glitches in vkd3d with Metro Exodus

Additions:
-This commit: ValveSoftware#3518 has been merged. This was a previous open PR from Guy1542, but it had a bug that would cause clustertruck and a few others not to launch. The new PR is by joshie (d9vk dev) and works now

-dxvk update to latest git
-faudio updated to latest git

Known issues:
-Just Cause 3 not able to save
-Batman Arkham Knight grappling hook not working
-MK11 hanging at launch (again)


## Proton-5.1-GE-1

GloriousEggroll released this Feb 10, 2020

-added fullscreen hack rebase from proton 5
-added updated steamclient rebase from proton 5 so that jc3 and batman AK denuvo problems work
-added updated monster hunter world patch that limits the changes to monster hunter world
-added proton patch that sets prefixes to win10 by default
-added dsound surround sound patches from proton 5
-proton dxvk wine integration patches added so that vkd3d works ootb without PROTON_USE_WINED3D
-reenabled proton's gamepad changes in favor over staging's (for now. let me know in discord if issues occur)
-updated to include proton's gstreamer and glib integration work
-added plasma systray patch
-fixed proton compatibility for staging patchset winex11.drv-mouse-coorrds
-disabled winex11-_NET_ACTIVE_WINDOW temporarily (not working correctly)
-disabled winex11-WM_WINDOWPOSCHANGING temporarily (depends on winex11-_NET_ACTIVE_WINDOW)
-updated dxvk to 1.5.4 official
-updated FAudio
-updated vkd3d

Known issues:
-Just Cause 3 not able to save
-Please note, vkd3d is very new and still does not work for DirectX 12 on all games.


## Proton-5.0-GE-1

GloriousEggroll released this Jan 30, 2020

-fixed issue with uplay games not recognizing they were being launched from steam
-fixed issue with farcry 5 hanging at launch
-fixed issue with stuttering in various games introduced by staging's ntdll-ForceBottomUpAlloc patches (darksiders 3, farcry 5)
-raw input patches finally fixed and enabled
-fixed issue with the MK11/skyrim skyui patch trying to allocate 119t virtual memory
-added patches that allow For Honor and steep to launch and work in single-player mode
-added patch that fixes battlenet beta crashing with win10 set in winecfg
-added patch that fixes fullscreen mode in steep
-added patch that fixes performance regression in Monster Hunter World caused by Iceborn DLC release.
-fixed proton compatibility for staging patchset winex11-MWM_Decorations (fixes https://bugs.winehq.org/show_bug.cgi?id=42117 which affects battlenet)
-fixed proton compatibility for staging patchset winex11-_NET_ACTIVE_WINDOW (fixes https://bugs.winehq.org/show_bug.cgi?id=2155 which affects some older games and apps)
-added proton's internal wined3d dxvk integration changes
-updated dxvk
-updated faudio
-changed vkd3d repository to one regularly worked on.

Edit:
-added fix for loading hang for endless legend
-added black ops 2 launch crash fix
-added winex11-WM_WINDOWPOSCHANGING patch from staging
-fixed an issue with proton not using d3d9 override (whoopsie)

Disabled the following for now, has an issue that causes windows to open and immediately close:
-proton compatibility for staging patchset winex11.drv-mouse-coorrds (fixes https://bugs.winehq.org/show_bug.cgi?id=46309 which affects origin)
