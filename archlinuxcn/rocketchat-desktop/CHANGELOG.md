## [3.7.3](https://github.com/RocketChat/Rocket.Chat.Electron/compare/3.7.2...3.7.3) (2021-12-27)


### Bug Fixes

* Object has destroyed message ([#2273](https://github.com/RocketChat/Rocket.Chat.Electron/issues/2273)) ([3560b93](https://github.com/RocketChat/Rocket.Chat.Electron/commit/3560b93a541d5ae0b00cb886228942e4525f7246))



## [3.7.1](https://github.com/RocketChat/Rocket.Chat.Electron/compare/3.7.0...3.7.1) (2021-12-20)


### Bug Fixes

* add Windows zip to releases and fix Windows architecture switching on release ([#2258](https://github.com/RocketChat/Rocket.Chat.Electron/issues/2258)) ([a67818e](https://github.com/RocketChat/Rocket.Chat.Electron/commit/a67818e7fea9f93c6b2e45873981547babca4ede))
* Run menu bar event listeners asynchronously ([#2254](https://github.com/RocketChat/Rocket.Chat.Electron/issues/2254)) ([d99352a](https://github.com/RocketChat/Rocket.Chat.Electron/commit/d99352afde37494910a9509e026c9fdf86aef18d))



# [3.7.0](https://github.com/RocketChat/Rocket.Chat.Electron/compare/3.6.0...3.7.0) (2021-11-30)


### Bug Fixes

* Empty screen from a fresh start + servers.json ([#2243](https://github.com/RocketChat/Rocket.Chat.Electron/issues/2243)) ([407c562](https://github.com/RocketChat/Rocket.Chat.Electron/commit/407c562531b5af841b40006f25aa657db56979f4))



# [3.6.0](https://github.com/RocketChat/Rocket.Chat.Electron/compare/3.5.7...3.6.0) (2021-11-16)


### Bug Fixes

* Add back desktop version to userAgent string ([#2217](https://github.com/RocketChat/Rocket.Chat.Electron/issues/2217)) ([07c6079](https://github.com/RocketChat/Rocket.Chat.Electron/commit/07c6079060a40d2549bc1502b55fc5d53219e018))
* Missing entitlements on mac app ([#2191](https://github.com/RocketChat/Rocket.Chat.Electron/issues/2191)) ([ce52cbc](https://github.com/RocketChat/Rocket.Chat.Electron/commit/ce52cbcf749a3e2147723ffa8f2d42a3b20f8047))


### Features

* Add clear cache and clear storage data options to server ([#2229](https://github.com/RocketChat/Rocket.Chat.Electron/issues/2229)) ([d65e73a](https://github.com/RocketChat/Rocket.Chat.Electron/commit/d65e73a6e87d10785d861ccf67a434d301698223))
* Setting to open video chat on application window or external browser ([#2227](https://github.com/RocketChat/Rocket.Chat.Electron/issues/2227)) ([d3364fd](https://github.com/RocketChat/Rocket.Chat.Electron/commit/d3364fdcf73b440d758af6a3ad59f63d972986e8))



## [3.5.7](https://github.com/RocketChat/Rocket.Chat.Electron/compare/3.5.6...3.5.7) (2021-10-06)


### Bug Fixes

* Prevent error if can reach the icon ([#2197](https://github.com/RocketChat/Rocket.Chat.Electron/issues/2197)) ([8c5217f](https://github.com/RocketChat/Rocket.Chat.Electron/commit/8c5217f96160fea0f24fa29e8b9f162ff9c906b6))
* Prevent invalid range for unit format ([#2195](https://github.com/RocketChat/Rocket.Chat.Electron/issues/2195)) ([cc4037b](https://github.com/RocketChat/Rocket.Chat.Electron/commit/cc4037b1fc0acd50f3cf8434434ccdc534568228))
* Prevent store send messages before the screen is ready ([#2198](https://github.com/RocketChat/Rocket.Chat.Electron/issues/2198)) ([34d185d](https://github.com/RocketChat/Rocket.Chat.Electron/commit/34d185d6b8781e60f446d298c487e5f418b44fe5))
* Redact info ([#2196](https://github.com/RocketChat/Rocket.Chat.Electron/issues/2196)) ([7a62f33](https://github.com/RocketChat/Rocket.Chat.Electron/commit/7a62f33f0a24bcbf6ceb928b87147490d03cc1f2))


### Features

* Electron dl for improve download experience ([#2200](https://github.com/RocketChat/Rocket.Chat.Electron/issues/2200)) ([a132009](https://github.com/RocketChat/Rocket.Chat.Electron/commit/a1320093880fe98f59be4f7cac0f3093e9195d33))



## [3.5.6](https://github.com/RocketChat/Rocket.Chat.Electron/compare/3.5.5...3.5.6) (2021-09-23)


### Bug Fixes

* Jitisi opening on browser ([#2180](https://github.com/RocketChat/Rocket.Chat.Electron/issues/2180)) ([1d34690](https://github.com/RocketChat/Rocket.Chat.Electron/commit/1d3469025e0f1b7988e542d02a8890308f136f6f))


### Features

* apple silicon universal support ([#2170](https://github.com/RocketChat/Rocket.Chat.Electron/issues/2170)) ([6f180c6](https://github.com/RocketChat/Rocket.Chat.Electron/commit/6f180c693fb9a4d22b981a1e891499bc547a1b61))



## [3.5.5](https://github.com/RocketChat/Rocket.Chat.Electron/compare/3.5.4...3.5.5) (2021-09-21)


### Bug Fixes

* Prevent errors on startup : Fix icon and window positioning errors ([#2173](https://github.com/RocketChat/Rocket.Chat.Electron/issues/2173)) ([d42ce30](https://github.com/RocketChat/Rocket.Chat.Electron/commit/d42ce30794d62ef494dbafd739e6eb0a5ce65b21))



## [3.5.4](https://github.com/RocketChat/Rocket.Chat.Electron/compare/3.5.3...3.5.4) (2021-09-16)


### Bug Fixes

* After zoom/reset navigating displays "white screen" ([#1947](https://github.com/RocketChat/Rocket.Chat.Electron/issues/1947)) ([a1323df](https://github.com/RocketChat/Rocket.Chat.Electron/commit/a1323df9ddb4dff8af6811e994d8e9b12f6fb24d))
* Fix memory leak after navigation ([#2168](https://github.com/RocketChat/Rocket.Chat.Electron/issues/2168)) ([8ef2d67](https://github.com/RocketChat/Rocket.Chat.Electron/commit/8ef2d67b361ce72d40b8b1d54d858730b2c9021f))



## [3.5.3](https://github.com/RocketChat/Rocket.Chat.Electron/compare/3.5.2...3.5.3) (2021-09-09)


### Bug Fixes

* Fix OAuth ([#2158](https://github.com/RocketChat/Rocket.Chat.Electron/pull/2158))([76bbba4](https://github.com/RocketChat/Rocket.Chat.Electron/commit/76bbba4d57bed9834c4fee9193b0d310ebccb907))
* Remove preventDefault from download ([#2159](https://github.com/RocketChat/Rocket.Chat.Electron/issues/2159)) ([4030e34](https://github.com/RocketChat/Rocket.Chat.Electron/commit/4030e34561c6c88d4825106869cea649cfe42c44))
* Removes rid param/conditional to fix deeplink ([#2160](https://github.com/RocketChat/Rocket.Chat.Electron/issues/2160)) ([2a72853](https://github.com/RocketChat/Rocket.Chat.Electron/commit/2a7285356c26af884496ad0763aa8591f43211c2))



## [3.5.2](https://github.com/RocketChat/Rocket.Chat.Electron/compare/3.5.1...3.5.2) (2021-09-09)


### Bug Fixes

* Bugsnag ([#2153](https://github.com/RocketChat/Rocket.Chat.Electron/issues/2153)) ([e3b1be7](https://github.com/RocketChat/Rocket.Chat.Electron/commit/e3b1be72db0facaa9890a07c5d8b38b7bf685fe9))
* Click Notification ([#2154](https://github.com/RocketChat/Rocket.Chat.Electron/issues/2154)) ([fb56545](https://github.com/RocketChat/Rocket.Chat.Electron/commit/fb565450ff0314e2cbc35140c287d6b7651f84bf))
* oauth ([#2152](https://github.com/RocketChat/Rocket.Chat.Electron/issues/2152)) ([898f3b4](https://github.com/RocketChat/Rocket.Chat.Electron/commit/898f3b49d2c58fe0c677025db4e2b5e89fe0aa59))
* remove typo text ([#2150](https://github.com/RocketChat/Rocket.Chat.Electron/issues/2150)) ([143fd48](https://github.com/RocketChat/Rocket.Chat.Electron/commit/143fd4810fc25538324db3db65e158b79601880d))



## [3.5.1](https://github.com/RocketChat/Rocket.Chat.Electron/compare/3.5.0...3.5.1) (2021-09-08)


### Bug Fixes

* Prevent Webcontent to navigate (outside) ([abd7a08](https://github.com/RocketChat/Rocket.Chat.Electron/commit/abd7a080c3cbdd99d9b398a2f724313b7a038648))
* Restore window on focus request ([ca0b8c6](https://github.com/RocketChat/Rocket.Chat.Electron/commit/ca0b8c6b8d9e7f0099655f2dc9bad7b5b08f71b1))
* Settings and Download view ([fecdd5a](https://github.com/RocketChat/Rocket.Chat.Electron/commit/fecdd5ad90edfe578474e9df6cf0fb20b36ab925))



# [3.5.0](https://github.com/RocketChat/Rocket.Chat.Electron/compare/3.4.0...3.5.0) (2021-09-06)


### Bug Fixes

* Set default server servers.json ([#2064](https://github.com/RocketChat/Rocket.Chat.Electron/issues/2064)) ([3965307](https://github.com/RocketChat/Rocket.Chat.Electron/commit/3965307ed4605af7880b95ebb1d195e247734ea1))
* Set default server servers.json and Open server on click notification ([#2144](https://github.com/RocketChat/Rocket.Chat.Electron/issues/2144)) ([b748b10](https://github.com/RocketChat/Rocket.Chat.Electron/commit/b748b10017c9937388c995278aa5ee1f82dcd469))


### Features

* Settings allow enable/disable flashframe ([#2142](https://github.com/RocketChat/Rocket.Chat.Electron/issues/2142)) ([1a48b69](https://github.com/RocketChat/Rocket.Chat.Electron/commit/1a48b6940a0aac2fbb2254817926cb5f6c4aee3e))
* Settings page and report opt-out ([#2138](https://github.com/RocketChat/Rocket.Chat.Electron/issues/2138)) ([12ca958](https://github.com/RocketChat/Rocket.Chat.Electron/commit/12ca9589f45298fa430bd9fd30e7053637ecc84f))



# [3.4.0](https://github.com/RocketChat/Rocket.Chat.Electron/compare/3.2.3...3.4.0) (2021-08-25)


### Bug Fixes

* Prevents Notifications on Linux to show the message "Rocket.Chat is ready" ([#2122](https://github.com/RocketChat/Rocket.Chat.Electron/issues/2122)) ([5ac093e](https://github.com/RocketChat/Rocket.Chat.Electron/commit/5ac093ec33c6b5dccc603b1fa4e91d0eaeb1a7d2))
* solve prettier errors ([bf16f55](https://github.com/RocketChat/Rocket.Chat.Electron/commit/bf16f550260e137883446229fd42cc126ab8e36c))



# [3.3.0](https://github.com/RocketChat/Rocket.Chat.Electron/compare/3.2.2...3.3.0) (2021-06-17)


### Bug Fixes

* **i18n:** Language update from LingoHub 🤖 ([#2042](https://github.com/RocketChat/Rocket.Chat.Electron/issues/2042)) ([cb07526](https://github.com/RocketChat/Rocket.Chat.Electron/commit/cb07526ed5f4831fd05458208561be8e81f5d218))
* **i18n:** Language update from LingoHub 🤖 ([#2047](https://github.com/RocketChat/Rocket.Chat.Electron/issues/2047)) ([891b7b7](https://github.com/RocketChat/Rocket.Chat.Electron/commit/891b7b70d9fb6382ca2070c1644669b3f38b17ef))



## [3.2.4](https://github.com/RocketChat/Rocket.Chat.Electron/compare/3.2.3...3.2.4) (2021-08-16)


### Bug Fixes

* Prevents Notifications on Linux to show the message "Rocket.Chat is ready" ([#2122](https://github.com/RocketChat/Rocket.Chat.Electron/issues/2122)) ([5ac093e](https://github.com/RocketChat/Rocket.Chat.Electron/commit/5ac093ec33c6b5dccc603b1fa4e91d0eaeb1a7d2))



# [3.3.0](https://github.com/RocketChat/Rocket.Chat.Electron/compare/3.2.2...3.3.0) (2021-06-17)


### Bug Fixes

* **i18n:** Language update from LingoHub 🤖 ([#2042](https://github.com/RocketChat/Rocket.Chat.Electron/issues/2042)) ([cb07526](https://github.com/RocketChat/Rocket.Chat.Electron/commit/cb07526ed5f4831fd05458208561be8e81f5d218))
* **i18n:** Language update from LingoHub 🤖 ([#2047](https://github.com/RocketChat/Rocket.Chat.Electron/issues/2047)) ([891b7b7](https://github.com/RocketChat/Rocket.Chat.Electron/commit/891b7b70d9fb6382ca2070c1644669b3f38b17ef))



## [3.2.3](https://github.com/RocketChat/Rocket.Chat.Electron/compare/3.2.2...3.2.3) (2021-07-01)


### Bug Fixes

* Desktop notifications not working ([2d4607d](https://github.com/RocketChat/Rocket.Chat.Electron/commit/2d4607dd3bb49dfb27c2df24f6a5b95d0b675ee4))



## [3.2.2](https://github.com/RocketChat/Rocket.Chat.Electron/compare/3.2.1...3.2.2) (2021-05-14)


### Bug Fixes

* **i18n:** Language update from LingoHub 🤖 ([#2032](https://github.com/RocketChat/Rocket.Chat.Electron/issues/2032)) ([39719ef](https://github.com/RocketChat/Rocket.Chat.Electron/commit/39719ef60284381abf5c6b0356f8377858878f0c))
* **jitsi:** JitsiMeetElectron unavailable on preload script ([#2031](https://github.com/RocketChat/Rocket.Chat.Electron/issues/2031)) ([1322938](https://github.com/RocketChat/Rocket.Chat.Electron/commit/1322938290e5aca5b9e6c2f335d1ee0f1132b2bc))



## [3.2.1](https://github.com/RocketChat/Rocket.Chat.Electron/compare/3.2.0...3.2.1) (2021-05-13)


### Bug Fixes

* **about-dialog:** About dialog not displaying version ([#2030](https://github.com/RocketChat/Rocket.Chat.Electron/issues/2030)) ([f82823c](https://github.com/RocketChat/Rocket.Chat.Electron/commit/f82823c36a47eef448ed8a11045c8c0b162f4320))



# [3.2.0](https://github.com/RocketChat/Rocket.Chat.Electron/compare/3.1.1...3.2.0) (2021-05-12)


### Bug Fixes

* **deps:** Update electron-builder ([b704680](https://github.com/RocketChat/Rocket.Chat.Electron/commit/b7046803e3394c288fa7ecf280c5221ac8e3d718))
* User presence not updating ([#2023](https://github.com/RocketChat/Rocket.Chat.Electron/issues/2023)) ([f10f24f](https://github.com/RocketChat/Rocket.Chat.Electron/commit/f10f24fbdbde4f21b2025f36b881066da846bd10))
* **deps:** Patch dependencies ([1e976cc](https://github.com/RocketChat/Rocket.Chat.Electron/commit/1e976cc09d526ec639fc4ba35a4d1e30cbf31b3a))
* **deps:** Upgrade build dependencies ([61aee42](https://github.com/RocketChat/Rocket.Chat.Electron/commit/61aee42123b7fbb7a02bc7963318100f2eb7c9f6))
* Download button size ([#1960](https://github.com/RocketChat/Rocket.Chat.Electron/issues/1960)) ([3424e6d](https://github.com/RocketChat/Rocket.Chat.Electron/commit/3424e6d297b48719c97362c7bb9fdad3cb068183))
* macOS dock icon size ([#1941](https://github.com/RocketChat/Rocket.Chat.Electron/issues/1941)) ([0eeb8b2](https://github.com/RocketChat/Rocket.Chat.Electron/commit/0eeb8b27c4f2b5b58ce12892aba5254801bb30bc))
* Missing French translations ([#2014](https://github.com/RocketChat/Rocket.Chat.Electron/issues/2014)) ([929e556](https://github.com/RocketChat/Rocket.Chat.Electron/commit/929e556352fb8043299958097180091f8360f2ec))
* Stop grabbing focus when dom-ready is emitted; and restore window position correctly when x or y is 0 ([#1954](https://github.com/RocketChat/Rocket.Chat.Electron/issues/1954)) ([c3ca0ef](https://github.com/RocketChat/Rocket.Chat.Electron/commit/c3ca0ef75ac29eb19934cfc8ddf0ad9d15681b3e)), closes [#1934](https://github.com/RocketChat/Rocket.Chat.Electron/issues/1934) [#1934](https://github.com/RocketChat/Rocket.Chat.Electron/issues/1934)
* Tray icon toggle action ([#2006](https://github.com/RocketChat/Rocket.Chat.Electron/issues/2006)) ([4d50b80](https://github.com/RocketChat/Rocket.Chat.Electron/commit/4d50b8085813398c55c51faa238c6f92819c2e7c)), closes [#1700](https://github.com/RocketChat/Rocket.Chat.Electron/issues/1700) [#1935](https://github.com/RocketChat/Rocket.Chat.Electron/issues/1935)
* Update hu.i18n.json ([#1944](https://github.com/RocketChat/Rocket.Chat.Electron/issues/1944)) ([e801f0f](https://github.com/RocketChat/Rocket.Chat.Electron/commit/e801f0f9d291fa7daefeefb085d240b13e0c425e))


### Features

* CLI argument '--start-hidden' to put the app in background on start ([#1407](https://github.com/RocketChat/Rocket.Chat.Electron/issues/1407)) ([223a698](https://github.com/RocketChat/Rocket.Chat.Electron/commit/223a698a73bb0c0157d649189e5f2a68ea369e2e))
* Flash root window on all platforms ([#1949](https://github.com/RocketChat/Rocket.Chat.Electron/issues/1949)) ([5934c56](https://github.com/RocketChat/Rocket.Chat.Electron/commit/5934c56f7a4551e3b527ba7ffb788648d501b80c))


### Performance Improvements

* TypeScript's strict mode ([#2015](https://github.com/RocketChat/Rocket.Chat.Electron/issues/2015)) ([1d5e612](https://github.com/RocketChat/Rocket.Chat.Electron/commit/1d5e61216ba91f77a8fc5fa676134cbbe9919af9))



## [3.1.1](https://github.com/RocketChat/Rocket.Chat.Electron/compare/3.1.0...3.1.1) (2020-12-25)


### Bug Fixes

* Apply sidebar padding change on macOS ([#1926](https://github.com/RocketChat/Rocket.Chat.Electron/issues/1926)) ([428ccf9](https://github.com/RocketChat/Rocket.Chat.Electron/commit/428ccf984f0154f89c44c1ba596313a74d9c825e))
* Preload script in sandboxed iframes ([#1925](https://github.com/RocketChat/Rocket.Chat.Electron/issues/1925)) ([15e39f3](https://github.com/RocketChat/Rocket.Chat.Electron/commit/15e39f3153e7cf97d5d36632484c7b241547dc27))



# [3.1.0](https://github.com/RocketChat/Rocket.Chat.Electron/compare/3.0.7...3.1.0) (2020-12-21)


### Bug Fixes

* Broken Jitsi's browser check ([#1902](https://github.com/RocketChat/Rocket.Chat.Electron/issues/1902)) ([01fafff](https://github.com/RocketChat/Rocket.Chat.Electron/commit/01fafff822be397f33ebb8250c7b667be66df396))
* Update hu.i18n.json ([#1886](https://github.com/RocketChat/Rocket.Chat.Electron/issues/1886)) ([d36897e](https://github.com/RocketChat/Rocket.Chat.Electron/commit/d36897ee5deb4fe509cd4f36b6b39d4bb6bd47ce))


### Features

* Download Manager ([#1700](https://github.com/RocketChat/Rocket.Chat.Electron/issues/1700)) ([ac30ab3](https://github.com/RocketChat/Rocket.Chat.Electron/commit/ac30ab396ec66f2437bbe2c3ce8ae5042a2c2b77))
* Isolated server view sessions ([#1883](https://github.com/RocketChat/Rocket.Chat.Electron/issues/1883)) ([4884d3f](https://github.com/RocketChat/Rocket.Chat.Electron/commit/4884d3f066d40f2d97d8649d0a1f8bf5b048f911))
* Rebranding ([#1884](https://github.com/RocketChat/Rocket.Chat.Electron/issues/1884)) ([12b4ca6](https://github.com/RocketChat/Rocket.Chat.Electron/commit/12b4ca6378689aa967d5b33d5a768561d408c67e))



## [3.0.7](https://github.com/RocketChat/Rocket.Chat.Electron/compare/3.0.6...3.0.7) (2020-11-09)


### Bug Fixes

* **build:** Force 32 and 64-bit builds for Windows ([e808e7a](https://github.com/RocketChat/Rocket.Chat.Electron/commit/e808e7a991490e5079bc3b2be6b9012b1af0988f))



## [3.0.6](https://github.com/RocketChat/Rocket.Chat.Electron/compare/3.0.5...3.0.6) (2020-11-03)


### Bug Fixes

* update.json files ignored ([#1861](https://github.com/RocketChat/Rocket.Chat.Electron/issues/1861)) ([d4c3368](https://github.com/RocketChat/Rocket.Chat.Electron/commit/d4c336870c51f518fbadb2f062ba523effba44bf))



## [3.0.5](https://github.com/RocketChat/Rocket.Chat.Electron/compare/3.0.4...3.0.5) (2020-10-28)


### Bug Fixes

* Apply TouchBar formatting button in focused message box ([#1851](https://github.com/RocketChat/Rocket.Chat.Electron/issues/1851)) ([52ca145](https://github.com/RocketChat/Rocket.Chat.Electron/commit/52ca1451ac5333578520c900e86b86968c69f76c))
* Bugsnag error reporting ([#1843](https://github.com/RocketChat/Rocket.Chat.Electron/issues/1843)) ([de0fe7f](https://github.com/RocketChat/Rocket.Chat.Electron/commit/de0fe7fc7c95f66d8ed07abae68b8e7fcdf2311d))
* Displaying warning every time the window is minimized to tray ([#1852](https://github.com/RocketChat/Rocket.Chat.Electron/issues/1852)) ([769a210](https://github.com/RocketChat/Rocket.Chat.Electron/commit/769a210433dccd5c833cdaf74c7c5b276515e890))
* Dragging and dropping outside content in servers list ([#1853](https://github.com/RocketChat/Rocket.Chat.Electron/issues/1853)) ([1e68f50](https://github.com/RocketChat/Rocket.Chat.Electron/commit/1e68f507dc325d4384aedf6a949edd3dc272d5c6))
* Select first server on startup ([#1850](https://github.com/RocketChat/Rocket.Chat.Electron/issues/1850)) ([c883d45](https://github.com/RocketChat/Rocket.Chat.Electron/commit/c883d454b6df207b3b4b077c5e880967e9e5e798))
* System idle threshold ([#1844](https://github.com/RocketChat/Rocket.Chat.Electron/issues/1844)) ([6c6e2a9](https://github.com/RocketChat/Rocket.Chat.Electron/commit/6c6e2a98ca68a796fa685b75b41fd4287ee8ccbb))



## [3.0.4](https://github.com/RocketChat/Rocket.Chat.Electron/compare/3.0.3...3.0.4) (2020-10-17)


### Bug Fixes

* Recover minimized/maximized state on show window when unread count changes ([#1810](https://github.com/RocketChat/Rocket.Chat.Electron/issues/1810)) ([15585f2](https://github.com/RocketChat/Rocket.Chat.Electron/commit/15585f21ff5405b6489edec833fd0fdadd589821))
* Server in subdirectory ([#1820](https://github.com/RocketChat/Rocket.Chat.Electron/issues/1820)) ([ff8b8a2](https://github.com/RocketChat/Rocket.Chat.Electron/commit/ff8b8a2e0aecc04edbd5279d80023bc99af46523))
* Unavailable languages in electron.session() ([#1813](https://github.com/RocketChat/Rocket.Chat.Electron/issues/1813)) ([ef32900](https://github.com/RocketChat/Rocket.Chat.Electron/commit/ef329006d323c4ac0089f6e445c33841f735a0d5))



## [3.0.3](https://github.com/RocketChat/Rocket.Chat.Electron/compare/3.0.2...3.0.3) (2020-10-13)


### Bug Fixes

* Cannot connect to server on subdirectory ([#1776](https://github.com/RocketChat/Rocket.Chat.Electron/issues/1776)) ([50c8585](https://github.com/RocketChat/Rocket.Chat.Electron/commit/50c8585eddd68b3b62c769b3a501848a92859d0d))
* Handle certificate errors and handshakes ([#1795](https://github.com/RocketChat/Rocket.Chat.Electron/issues/1795)) ([220f8b1](https://github.com/RocketChat/Rocket.Chat.Electron/commit/220f8b10b897a40453850d4730b348ba4f6066ea))
* Remove Electron and Chrome versions from User-Agent header ([#1809](https://github.com/RocketChat/Rocket.Chat.Electron/issues/1809)) ([88cbb23](https://github.com/RocketChat/Rocket.Chat.Electron/commit/88cbb23c100a475498c6286c15d4b10e363a1079))
* Set connection status ([#1800](https://github.com/RocketChat/Rocket.Chat.Electron/issues/1800)) ([738f65c](https://github.com/RocketChat/Rocket.Chat.Electron/commit/738f65cd1348850a2c05e916449fe39428ef1243))



## [3.0.2](https://github.com/RocketChat/Rocket.Chat.Electron/compare/3.0.1...3.0.2) (2020-10-03)


### Bug Fixes

* Add extension filters to save download dialog ([#1772](https://github.com/RocketChat/Rocket.Chat.Electron/issues/1772)) ([6c4fdcc](https://github.com/RocketChat/Rocket.Chat.Electron/commit/6c4fdcc894bac52fab875cca7b9146ee3cec40e1))
* Asynchronous window state changes ([#1773](https://github.com/RocketChat/Rocket.Chat.Electron/issues/1773)) ([0adc73c](https://github.com/RocketChat/Rocket.Chat.Electron/commit/0adc73c2ecfe7010adbb06583b22c55ff172a169))
* Increase server version range ([#1770](https://github.com/RocketChat/Rocket.Chat.Electron/issues/1770)) ([4ea6fea](https://github.com/RocketChat/Rocket.Chat.Electron/commit/4ea6fea99ed4dc4a11fe64119dc4d284d3a65a5f))
* Update pt-BR.i18n.json ([#1774](https://github.com/RocketChat/Rocket.Chat.Electron/issues/1774)) ([75f9c97](https://github.com/RocketChat/Rocket.Chat.Electron/commit/75f9c977b6a2ce895899f336dc06b2b9ccb86110))
* Update tr-TR.i18n.json ([#1763](https://github.com/RocketChat/Rocket.Chat.Electron/issues/1763)) ([61dac3e](https://github.com/RocketChat/Rocket.Chat.Electron/commit/61dac3e1f66eb3908cb0155867cafdf4e6de0fea))



## [3.0.1](https://github.com/RocketChat/Rocket.Chat.Electron/compare/3.0.0...3.0.1) (2020-10-02)


### Bug Fixes

* Server validation ([#1756](https://github.com/RocketChat/Rocket.Chat.Electron/issues/1756)) ([91f7c5a](https://github.com/RocketChat/Rocket.Chat.Electron/commit/91f7c5a2e4ad983c3d81a2383a96ef3b54850f51))
* Window state loading ([#1758](https://github.com/RocketChat/Rocket.Chat.Electron/issues/1758)) ([12ef49e](https://github.com/RocketChat/Rocket.Chat.Electron/commit/12ef49e4f608324ffb5982ff4435623b43ece6f2))



# [3.0.0](https://github.com/RocketChat/Rocket.Chat.Electron/compare/2.17.11...3.0.0) (2020-09-30)


### Bug Fixes

* Add snap connection for camera ([#1484](https://github.com/RocketChat/Rocket.Chat.Electron/issues/1484)) ([a6fe71d](https://github.com/RocketChat/Rocket.Chat.Electron/commit/a6fe71d054c08f2215017b5864067c41deb356ad))
* Bugs related to focused webContents ([#1525](https://github.com/RocketChat/Rocket.Chat.Electron/issues/1525)) ([402fec0](https://github.com/RocketChat/Rocket.Chat.Electron/commit/402fec00b3761fad55d5c570a2f93a1f968b20b0))
* Command line args handling on packaged apps ([#1522](https://github.com/RocketChat/Rocket.Chat.Electron/issues/1522)) ([cc99b78](https://github.com/RocketChat/Rocket.Chat.Electron/commit/cc99b7830f6636d9714969f879bf2d4bca8a91fc))
* Context isolation in preload script and `openExternal` handling ([#1710](https://github.com/RocketChat/Rocket.Chat.Electron/issues/1710)) ([c43a8a3](https://github.com/RocketChat/Rocket.Chat.Electron/commit/c43a8a31289290e61eacd0e30dba5f14619ee911))
* Display tray icon balloon when main window is hidden ([#1518](https://github.com/RocketChat/Rocket.Chat.Electron/issues/1518)) ([9291b1e](https://github.com/RocketChat/Rocket.Chat.Electron/commit/9291b1edc7c865c3830adcf964e851db9136114a))
* Error reporting on Bugsnag ([#1655](https://github.com/RocketChat/Rocket.Chat.Electron/issues/1655)) ([a6746f9](https://github.com/RocketChat/Rocket.Chat.Electron/commit/a6746f9c23fb96d694c8ecdfe5e004d038ba3668))
* Gracefully exit the app ([#1736](https://github.com/RocketChat/Rocket.Chat.Electron/issues/1736)) ([4d0c28d](https://github.com/RocketChat/Rocket.Chat.Electron/commit/4d0c28d61813eb3855ccba3281249bddf5dbc808))
* Media permissions ([#1740](https://github.com/RocketChat/Rocket.Chat.Electron/issues/1740)) ([1a23d4b](https://github.com/RocketChat/Rocket.Chat.Electron/commit/1a23d4b5fc5758b5ab1a14828ad18ceef7241e65))
* Menu bar crashing ([#1722](https://github.com/RocketChat/Rocket.Chat.Electron/issues/1722)) ([20bfcbf](https://github.com/RocketChat/Rocket.Chat.Electron/commit/20bfcbfa577887b3067de3d368f9ae083635ed69))
* Minimum width in split view on OS X is 600px ([#1549](https://github.com/RocketChat/Rocket.Chat.Electron/issues/1549)) ([8630847](https://github.com/RocketChat/Rocket.Chat.Electron/commit/86308478a8131396b35bbbbcdc066fd3c7f2d4e0))
* Missing tslib at runtime ([#1721](https://github.com/RocketChat/Rocket.Chat.Electron/issues/1721)) ([101957f](https://github.com/RocketChat/Rocket.Chat.Electron/commit/101957f7d20ee2bfc3f8f468a4a80984bb8af433))
* Opening links with external protocol ([#1709](https://github.com/RocketChat/Rocket.Chat.Electron/issues/1709)) ([a497abc](https://github.com/RocketChat/Rocket.Chat.Electron/commit/a497abc676a0750a73cef0a47a1d4d9f9a4022a2))
* Remove wrong entitlements on MAS builds ([#1654](https://github.com/RocketChat/Rocket.Chat.Electron/issues/1654)) ([394b19c](https://github.com/RocketChat/Rocket.Chat.Electron/commit/394b19cbede1fce0c3bcde24e9d2bae90a5205ce))
* Some structural issues ([#1515](https://github.com/RocketChat/Rocket.Chat.Electron/issues/1515)) ([5604281](https://github.com/RocketChat/Rocket.Chat.Electron/commit/56042818d484bb7a68e4787e07c84b113492e936)), closes [#1514](https://github.com/RocketChat/Rocket.Chat.Electron/issues/1514)
* Verify url protocol in window.open ([#1723](https://github.com/RocketChat/Rocket.Chat.Electron/issues/1723)) ([f21cca3](https://github.com/RocketChat/Rocket.Chat.Electron/commit/f21cca3d4302a103dcb1b9fcc32c08b82a78f8a9))


### Features

* Add Hungarian translation ([#1554](https://github.com/RocketChat/Rocket.Chat.Electron/issues/1554)) ([f2345aa](https://github.com/RocketChat/Rocket.Chat.Electron/commit/f2345aadd896c979b8821404e049273941b53c02))
* Add new locale for Ukrainian ([#1559](https://github.com/RocketChat/Rocket.Chat.Electron/issues/1559)) ([26e6c48](https://github.com/RocketChat/Rocket.Chat.Electron/commit/26e6c48044af9979c3f8f7bb18f707682af26b2c))
* Add Polish translation ([#1586](https://github.com/RocketChat/Rocket.Chat.Electron/issues/1586)) ([a2f4885](https://github.com/RocketChat/Rocket.Chat.Electron/commit/a2f4885ba5c0ff995f3098e5280bc3e1f8d8d2dc))
* Added option to disable GPU acceleration ([#1541](https://github.com/RocketChat/Rocket.Chat.Electron/issues/1541)) ([18c850c](https://github.com/RocketChat/Rocket.Chat.Electron/commit/18c850cc4ca175af17b9a04b413f4fc73fc4c76a))
* Deep links ([#1726](https://github.com/RocketChat/Rocket.Chat.Electron/issues/1726)) ([fda4bad](https://github.com/RocketChat/Rocket.Chat.Electron/commit/fda4badc06938e67a68cbc4a5857dcbd4e6e79b9))
* Embedded spell checking dictionaries ([#1523](https://github.com/RocketChat/Rocket.Chat.Electron/issues/1523)) ([c897582](https://github.com/RocketChat/Rocket.Chat.Electron/commit/c897582a6df338eba1d0bc0a675687f66eb3cd5d))
* Menu bar as components ([#1512](https://github.com/RocketChat/Rocket.Chat.Electron/issues/1512)) ([67172f0](https://github.com/RocketChat/Rocket.Chat.Electron/commit/67172f0930ad25cf055d8c301e9039c99e6af73a))
* MSI installer ([#1734](https://github.com/RocketChat/Rocket.Chat.Electron/issues/1734)) ([64ab2f3](https://github.com/RocketChat/Rocket.Chat.Electron/commit/64ab2f3d9d602fba282853a045d1e11148838d8c))
* New "Add Server" layout ([#1738](https://github.com/RocketChat/Rocket.Chat.Electron/issues/1738)) ([e0183d3](https://github.com/RocketChat/Rocket.Chat.Electron/commit/e0183d3db0f0509450b927cc1650a6719d77b4bd))
* Select client certificate dialog ([#1511](https://github.com/RocketChat/Rocket.Chat.Electron/issues/1511)) ([68e79d8](https://github.com/RocketChat/Rocket.Chat.Electron/commit/68e79d8bfbcfa231b2ed2cf64ede24dcf3d5f079))
* Use current server's favicon as window/taskbar icon ([#1720](https://github.com/RocketChat/Rocket.Chat.Electron/issues/1720)) ([c3d53c6](https://github.com/RocketChat/Rocket.Chat.Electron/commit/c3d53c6813185c1652d39a25a0a56336858e0a3a))


### Performance Improvements

* Improve away detection ([#1542](https://github.com/RocketChat/Rocket.Chat.Electron/issues/1542)) ([6449554](https://github.com/RocketChat/Rocket.Chat.Electron/commit/6449554dec8c75338e83606835d4875d5e3f128b))
* Notifications on main process ([#1675](https://github.com/RocketChat/Rocket.Chat.Electron/issues/1675)) ([062b4f9](https://github.com/RocketChat/Rocket.Chat.Electron/commit/062b4f958c942f2dc4eee9066ec8c28aa93db705))

## [2.17.11](https://github.com/RocketChat/Rocket.Chat.Electron/compare/2.17.10...2.17.11) (2020-07-21)


### Bug Fixes

* No notification when the avatar icon comes from a relative URL ([#1662](https://github.com/RocketChat/Rocket.Chat.Electron/issues/1662)) ([bad1562](https://github.com/RocketChat/Rocket.Chat.Electron/commit/bad156246bab4b9a0c478693dc397b9548177a6c))
* Remove wrong entitlements on MAS builds ([#1654](https://github.com/RocketChat/Rocket.Chat.Electron/issues/1654)) ([76c19ee](https://github.com/RocketChat/Rocket.Chat.Electron/commit/76c19eedac827f9833b5090eda4965fa438b9e25))



## [2.17.10](https://github.com/RocketChat/Rocket.Chat.Electron/compare/2.17.9...2.17.10) (2020-07-14)


### Bug Fixes

* Patch Electron ([d53ec40](https://github.com/RocketChat/Rocket.Chat.Electron/commit/d53ec4096c8fd9004821b13a755c2c5e818aa9c6))



## [2.17.9](https://github.com/RocketChat/Rocket.Chat.Electron/compare/2.17.8...2.17.9) (2020-03-12)


### Bug Fixes

* Update provision profile ([617c964](https://github.com/RocketChat/Rocket.Chat.Electron/commit/617c964dacde3738d86d28779f01fa0c9208b6b3))



## [2.17.8](https://github.com/RocketChat/Rocket.Chat.Electron/compare/2.17.7...2.17.8) (2020-03-01)


### Bug Fixes

* Allow MacOS users to browse for spell checking dictionaries ([3c75bfe](https://github.com/RocketChat/Rocket.Chat.Electron/commit/3c75bfe2270e5c2e434f85a27a717c875a63f9b0))
* Patch Electron for MAS builds ([e9cd8ad](https://github.com/RocketChat/Rocket.Chat.Electron/commit/e9cd8ad4b9cf0aeb5011189f6cedb24b71548579))



## [2.17.7](https://github.com/RocketChat/Rocket.Chat.Electron/compare/2.17.6...2.17.7) (2020-02-11)


### Bug Fixes

* Spell checking dictionaries files encoded as UTF-8 ([18b9524](https://github.com/RocketChat/Rocket.Chat.Electron/commit/18b95241a9df47751c5d67a55c5e2cf73e2763ca))



## [2.17.6](https://github.com/RocketChat/Rocket.Chat.Electron/compare/2.17.5...2.17.6) (2020-02-11)


### Bug Fixes

* Rollback to plain-text Hunspell dictionaries ([#1514](https://github.com/RocketChat/Rocket.Chat.Electron/issues/1514)) ([0f16d32](https://github.com/RocketChat/Rocket.Chat.Electron/commit/0f16d32845faf5b9a9b475db3c34420d982cb6bc))



## [2.17.5](https://github.com/RocketChat/Rocket.Chat.Electron/compare/2.17.4...2.17.5) (2020-02-04)


### Bug Fixes

* Handle unset enabled dictionaries ([2e3f203](https://github.com/RocketChat/Rocket.Chat.Electron/commit/2e3f20397f8b39d70e7e9261c20145b9e6987e91))
* Ignore Hunspell dictionaries on MacOS ([cccca77](https://github.com/RocketChat/Rocket.Chat.Electron/commit/cccca775e40c101798a870ee3f2ced79fdee20a3))



## [2.17.4](https://github.com/RocketChat/Rocket.Chat.Electron/compare/2.17.3...2.17.4) (2020-02-04)


### Bug Fixes

* Broken spell checking dictionary selection ([c11600c](https://github.com/RocketChat/Rocket.Chat.Electron/commit/c11600ca509c8c1806c734b189a33981b5ba002e))



## [2.17.3](https://github.com/RocketChat/Rocket.Chat.Electron/compare/2.17.2...2.17.3) (2020-01-30)


### Bug Fixes

* Screen sharing in Jitsi ([#1486](https://github.com/RocketChat/Rocket.Chat.Electron/issues/1486)) ([d7d463a](https://github.com/RocketChat/Rocket.Chat.Electron/commit/d7d463ae3cef91410525eb42d1333e3e18996d34))



<a name="2.17.2"></a>
## 2.17.2 (2019-12-19)


### Bug Fixes

- [#1450](https://github.com/RocketChat/Rocket.Chat.Electron/pull/1450) Windows select boxes
- [#1447](https://github.com/RocketChat/Rocket.Chat.Electron/pull/1447) TouchBar buttons



<a name="2.17.1"></a>
## 2.17.1 (2019-12-10)


### Bug Fixes

- [#1436](https://github.com/RocketChat/Rocket.Chat.Electron/pull/1436) Disable hardenedRuntime



<a name="2.17.0"></a>
# 2.17.0 (2019-12-02)


### Bug Fixes

- [#1402](https://github.com/RocketChat/Rocket.Chat.Electron/pull/1402) Embed dialogs
- [#1410](https://github.com/RocketChat/Rocket.Chat.Electron/pull/1410) Enable websecurity
- [#1415](https://github.com/RocketChat/Rocket.Chat.Electron/pull/1415) Fetch avatar images for notifications without CORS
- [#1412](https://github.com/RocketChat/Rocket.Chat.Electron/pull/1412) Loading error view updates
- [#1417](https://github.com/RocketChat/Rocket.Chat.Electron/pull/1417) Main window state handling
- [#1409](https://github.com/RocketChat/Rocket.Chat.Electron/pull/1409) Non context-aware native modules
- [#1419](https://github.com/RocketChat/Rocket.Chat.Electron/pull/1419) Preload script issues
- [#1381](https://github.com/RocketChat/Rocket.Chat.Electron/pull/1381) Update dialog events


### Improvements

- [#1418](https://github.com/RocketChat/Rocket.Chat.Electron/pull/1418) Focus main window on second app instance event
- [#1416](https://github.com/RocketChat/Rocket.Chat.Electron/pull/1416) Infer content type for notification icon
- [#1414](https://github.com/RocketChat/Rocket.Chat.Electron/pull/1414) Lean main process
- [#1380](https://github.com/RocketChat/Rocket.Chat.Electron/pull/1380) Notifications on Gnome
- [#1392](https://github.com/RocketChat/Rocket.Chat.Electron/pull/1392) Update to Electron 7


<details>
<summary>Others</summary>

- [#1401](https://github.com/RocketChat/Rocket.Chat.Electron/pull/1401) Update TouchBar API usage
</details>



<a name="2.16.2"></a>
## 2.16.2 (2019-11-07)


### Bug Fixes

- [#1381](https://github.com/RocketChat/Rocket.Chat.Electron/pull/1381) Update dialog events


### Improvements

- [#1380](https://github.com/RocketChat/Rocket.Chat.Electron/pull/1380) Notifications on Gnome



<a name="2.16.1"></a>
## 2.16.1 (2019-11-04)


### Bug Fixes

- [#1365](https://github.com/RocketChat/Rocket.Chat.Electron/pull/1365) powerMonitor API usage
- [#1366](https://github.com/RocketChat/Rocket.Chat.Electron/pull/1366) Spellchecker setup



<a name="2.16.0"></a>
# 2.16.0 (2019-10-11)


### Bug Fixes

- [#1275](https://github.com/RocketChat/Rocket.Chat.Electron/pull/1275) Ignore spurious did-fail load, fixes [#1273](https://github.com/RocketChat/Rocket.Chat.Electron/issues/1273).


### Improvements

- [#1325](https://github.com/RocketChat/Rocket.Chat.Electron/pull/1325) Add console warning to self-XSS
- [#1312](https://github.com/RocketChat/Rocket.Chat.Electron/pull/1312) Fixes and updates French translations


<details>
<summary>Others</summary>

- [#1347](https://github.com/RocketChat/Rocket.Chat.Electron/pull/1347) MacOS build
- [#1343](https://github.com/RocketChat/Rocket.Chat.Electron/pull/1343) Reenable webviews
- [#1346](https://github.com/RocketChat/Rocket.Chat.Electron/pull/1346) Revert Linux artifacts names
- [#1342](https://github.com/RocketChat/Rocket.Chat.Electron/pull/1342) Update dependencies
- [#1344](https://github.com/RocketChat/Rocket.Chat.Electron/pull/1344) Update tasks and metadata
- [#1306](https://github.com/RocketChat/Rocket.Chat.Electron/pull/1306) Bump eslint-utils from 1.3.1 to 1.4.2
- [#1305](https://github.com/RocketChat/Rocket.Chat.Electron/pull/1305) Bump js-yaml from 3.12.2 to 3.13.0
- [#1304](https://github.com/RocketChat/Rocket.Chat.Electron/pull/1304) Bump lodash from 4.17.11 to 4.17.15
- [#1307](https://github.com/RocketChat/Rocket.Chat.Electron/pull/1307) Bump lodash.merge from 4.6.1 to 4.6.2
- [#1308](https://github.com/RocketChat/Rocket.Chat.Electron/pull/1308) Bump mixin-deep from 1.3.1 to 1.3.2
</details>



<a name="2.15.5"></a>
## 2.15.5 (2019-08-09)


### Hot fix

- Bugsnag dependency error


<a name="2.15.4"></a>
## 2.15.4 (2019-08-08)


<details>
<summary>Others</summary>

- [#1198](https://github.com/RocketChat/Rocket.Chat.Electron/pull/1198) Add a module to handle deep links following the documentation
- [#1244](https://github.com/RocketChat/Rocket.Chat.Electron/pull/1244) Add Simplified Chinese translation file
- [#1287](https://github.com/RocketChat/Rocket.Chat.Electron/pull/1287) Reenable Bugsnag error tracking
- [#1196](https://github.com/RocketChat/Rocket.Chat.Electron/pull/1196) Safely compute initials for server name on sidebar
</details>


### Bug Fixes

- [#1286](https://github.com/RocketChat/Rocket.Chat.Electron/pull/1286) "Show window on unread changed" not working
- [#1285](https://github.com/RocketChat/Rocket.Chat.Electron/pull/1285) Remove missing variable reference
- [#1264](https://github.com/RocketChat/Rocket.Chat.Electron/pull/1264) Resolves issue with timing out when Rocket.Chat is in the background …



<a name="2.15.3"></a>
## 2.15.3 (2019-04-30)


### Bug Fixes

- [#1198](https://github.com/RocketChat/Rocket.Chat.Electron/pull/1198) Add a module to handle deep links following the documentation
- [#1196](https://github.com/RocketChat/Rocket.Chat.Electron/pull/1196) Safely compute initials for server name on sidebars



<a name="2.15.2"></a>
## 2.15.2 (2019-04-16)


### Bug Fixes

- [#1188](https://github.com/RocketChat/Rocket.Chat.Electron/pull/1188) Apply workaround for undo and redo actions
- [#1189](https://github.com/RocketChat/Rocket.Chat.Electron/pull/1189) Multiple language selection on spellchecking
- [#1164](https://github.com/RocketChat/Rocket.Chat.Electron/pull/1164) Only set user presence as online when auto away detection is disabled
- [#1125](https://github.com/RocketChat/Rocket.Chat.Electron/pull/1125) Sidebar and badges
- [#1187](https://github.com/RocketChat/Rocket.Chat.Electron/pull/1187) Update crashes when host is unreachable


### New Features

- [#1157](https://github.com/RocketChat/Rocket.Chat.Electron/pull/1157) Add Traditional Chinese translation



<a name="2.15.1"></a>
## 2.15.1 (2019-03-13)


### Improvements

- [#1117](https://github.com/RocketChat/Rocket.Chat.Electron/pull/1117) Updated Japanese translation


### Bug Fixes

- [#1132](https://github.com/RocketChat/Rocket.Chat.Electron/pull/1132) Apply memoization to spell checking
- [#1124](https://github.com/RocketChat/Rocket.Chat.Electron/pull/1124) Away detection
- [#1129](https://github.com/RocketChat/Rocket.Chat.Electron/pull/1129) Mac App Store startup issue
- [#1140](https://github.com/RocketChat/Rocket.Chat.Electron/pull/1140) Preload scripts compatibility
- [#1133](https://github.com/RocketChat/Rocket.Chat.Electron/pull/1133) Re-enable download links
- [#1130](https://github.com/RocketChat/Rocket.Chat.Electron/pull/1130) Reply notifications in MacOS
- [#1123](https://github.com/RocketChat/Rocket.Chat.Electron/pull/1123) Update button
- [#1115](https://github.com/RocketChat/Rocket.Chat.Electron/pull/1115) Auto reload server



<a name="2.15.0"></a>
# 2.15.0 (2019-02-24)


### Bug Fixes

- [#1028](https://github.com/RocketChat/Rocket.Chat.Electron/pull/1028) The behavior of clicking links when running RocketChat with subdir.
- [#1099](https://github.com/RocketChat/Rocket.Chat.Electron/pull/1099) Updates preloads scripts to be compatible with Rocket.Chat >0.74.0
- [#1101](https://github.com/RocketChat/Rocket.Chat.Electron/pull/1101) Use Electron notifications


### Improvements

- [#1096](https://github.com/RocketChat/Rocket.Chat.Electron/pull/1096) i18next
- [#1093](https://github.com/RocketChat/Rocket.Chat.Electron/pull/1093) New tray icons
- [#1045](https://github.com/RocketChat/Rocket.Chat.Electron/pull/1045) Pages and preload script changes
- [#1076](https://github.com/RocketChat/Rocket.Chat.Electron/pull/1076) Remove update-remind-later-dialog


<details>
<summary>Others</summary>

- [#1081](https://github.com/RocketChat/Rocket.Chat.Electron/pull/1081) Disable artifact collection by AppVeyor
- [#1074](https://github.com/RocketChat/Rocket.Chat.Electron/pull/1074) Fix for basic-auth servers connect
- [#1080](https://github.com/RocketChat/Rocket.Chat.Electron/pull/1080) Fix remember window state on load
</details>


### New Features

- [#919](https://github.com/RocketChat/Rocket.Chat.Electron/pull/919) Add "save image" to context menu
- [#1030](https://github.com/RocketChat/Rocket.Chat.Electron/pull/1030) Add Japanese translation.
- [#995](https://github.com/RocketChat/Rocket.Chat.Electron/pull/995) Automatic reload on error page
- [#1044](https://github.com/RocketChat/Rocket.Chat.Electron/pull/1044) Support for MacBooks Touch Bar


### BREAKING CHANGES

- [#1036](https://github.com/RocketChat/Rocket.Chat.Electron/pull/1036) Update dependencies



<a name="2.14.7"></a>
## 2.14.7 (2019-01-09)


### Bug Fixes

- Main window destroyed when closing on MacOS



<a name="2.14.6"></a>
## 2.14.6 (2018-12-06)


### Bug Fixes

- Add strings specifying why some permissions are needed in MacOS
- Fix servers.json path resolution



<a name="2.14.5"></a>
## 2.14.5 (2018-12-04)


### Improvements

- [#1010](https://github.com/RocketChat/Rocket.Chat.Electron/pull/1010) Remove unused modules


### Bug Fixes

- [#1026](https://github.com/RocketChat/Rocket.Chat.Electron/pull/1026) Add additional condition for option "Show on unread"
- [#1005](https://github.com/RocketChat/Rocket.Chat.Electron/pull/1005) Disable FreeDesktopNotification actions for Unity desktop
- [#1025](https://github.com/RocketChat/Rocket.Chat.Electron/pull/1025) Remove dependencies related to the npm's event-stream incident
- [#1019](https://github.com/RocketChat/Rocket.Chat.Electron/pull/1019) Rollback notifications for Windows



<a name="2.14.4"></a>
## 2.14.4 (2018-11-21)


### Bug Fixes

- [#1001](https://github.com/RocketChat/Rocket.Chat.Electron/pull/1001) Check for updates response when an error occurs
- [#978](https://github.com/RocketChat/Rocket.Chat.Electron/pull/978) Fallback notifications for Windows 7
- [#1000](https://github.com/RocketChat/Rocket.Chat.Electron/pull/1000) Notification errors
- [#990](https://github.com/RocketChat/Rocket.Chat.Electron/pull/990) Speed up servers.json loading


<details>
<summary>Others</summary>

- [#987](https://github.com/RocketChat/Rocket.Chat.Electron/pull/987) Update Russian translation
</details>



<a name="2.14.3"></a>
## 2.14.3 (2018-11-14)


### Bug Fixes

- [#978](https://github.com/RocketChat/Rocket.Chat.Electron/pull/978) Fallback notifications for Windows 7



<a name="2.14.2"></a>
## 2.14.2 (2018-11-13)


### Bug Fixes

- [#960](https://github.com/RocketChat/Rocket.Chat.Electron/pull/960) Dictionaries path detection in spell checker
- [#967](https://github.com/RocketChat/Rocket.Chat.Electron/pull/967) Main window closing behavior for Linux
- [#969](https://github.com/RocketChat/Rocket.Chat.Electron/pull/969) Notifications redesigned
- [#949](https://github.com/RocketChat/Rocket.Chat.Electron/pull/949) Reset app data under Windows
- [#959](https://github.com/RocketChat/Rocket.Chat.Electron/pull/959) System tray, dock, task bar and main window issues


### Improvements

- [#968](https://github.com/RocketChat/Rocket.Chat.Electron/pull/968) Node 11 support



<a name="2.14.1"></a>
## 2.14.1 (2018-10-25)


### New Features

- [#914](https://github.com/RocketChat/Rocket.Chat.Electron/pull/914) Tray tooltip


### Improvements

- [#933](https://github.com/RocketChat/Rocket.Chat.Electron/pull/933) App (main) page
- [#932](https://github.com/RocketChat/Rocket.Chat.Electron/pull/932) Report issue menu item links to desktop app repository


### Bug Fixes

- [#936](https://github.com/RocketChat/Rocket.Chat.Electron/pull/936) Autoupdate in MacOS
- [#927](https://github.com/RocketChat/Rocket.Chat.Electron/pull/927) Disable autoupdates
- [#938](https://github.com/RocketChat/Rocket.Chat.Electron/pull/938) Move about menu item for MacOS
- [#926](https://github.com/RocketChat/Rocket.Chat.Electron/pull/926) Preload issues
- [#922](https://github.com/RocketChat/Rocket.Chat.Electron/pull/922) Server icon not displayed on sidebar if server url ending with a trailing slash
- [#941](https://github.com/RocketChat/Rocket.Chat.Electron/pull/941) Window closing behavior for Linux environments without a system tray



<a name="2.14.0"></a>
# 2.14.0 (2018-10-11)


### New Features

- [#899](https://github.com/RocketChat/Rocket.Chat.Electron/pull/899) Optional status on tray for MacOS
- [#905](https://github.com/RocketChat/Rocket.Chat.Electron/pull/905) Add copy link in the context menu
- [#907](https://github.com/RocketChat/Rocket.Chat.Electron/pull/907) Disable autoupdate on windows installer
- [#911](https://github.com/RocketChat/Rocket.Chat.Electron/pull/911) Documentation to disable Autoupdates

### Improvements

- [#887](https://github.com/RocketChat/Rocket.Chat.Electron/pull/887) Update ESLint rules following Rocket.Chat guidelines


### Bug Fixes

- [#889](https://github.com/RocketChat/Rocket.Chat.Electron/pull/889) About dialog
- [#895](https://github.com/RocketChat/Rocket.Chat.Electron/pull/895) Menus
- [#884](https://github.com/RocketChat/Rocket.Chat.Electron/pull/884) Show tray icon status again
- [#900](https://github.com/RocketChat/Rocket.Chat.Electron/pull/900) Tray icon module
- [#902](https://github.com/RocketChat/Rocket.Chat.Electron/pull/902) Tray icon sizes for Linux
- [#912](https://github.com/RocketChat/Rocket.Chat.Electron/pull/912) Condition to quit on window close
- [#913](https://github.com/RocketChat/Rocket.Chat.Electron/pull/913) Show window on second instance running


<details>
<summary>Others</summary>

- [#916](https://github.com/RocketChat/Rocket.Chat.Electron/pull/916) Change back and forward shortcuts
</details>



<a name="2.13.3"></a>
## 2.13.3 (2018-09-18)


### Improvements

- [#881](https://github.com/RocketChat/Rocket.Chat.Electron/pull/881) End-to-end tests
- [#882](https://github.com/RocketChat/Rocket.Chat.Electron/pull/882) Set new DMG background


### Bug Fixes

- [#884](https://github.com/RocketChat/Rocket.Chat.Electron/pull/884) Show tray icon status again
- [#875](https://github.com/RocketChat/Rocket.Chat.Electron/pull/875) Toggled tray icon notifications
- [#880](https://github.com/RocketChat/Rocket.Chat.Electron/pull/880) Tray icon toggle crashes in MacOS
- [#869](https://github.com/RocketChat/Rocket.Chat.Electron/pull/869) Window state errors on save when antivirus software is present



<a name="2.13.2"></a>
## 2.13.2 (2018-09-10)


### Bug Fixes
- Dependencies updated
- Window state persistency triggering redefined
- AppId for Windows setups recovered
- Linux package names fixed
- Fixed multiple issues in provisioning profiles and entitlements for MacOS builds

<a name="2.13.1"></a>
## 2.13.1 (2018-08-30)


Fixes for MacOS and Windows builds.



<a name="2.13.0"></a>
# 2.13.0 (2018-08-27)


### New Features

- [#838](https://github.com/RocketChat/Rocket.Chat.Electron/pull/838) Russian translation
- [#837](https://github.com/RocketChat/Rocket.Chat.Electron/pull/837) Auto update fixes and settings enforcement


### Improvements

- [#821](https://github.com/RocketChat/Rocket.Chat.Electron/pull/821) Always force download of uploaded files
- [#824](https://github.com/RocketChat/Rocket.Chat.Electron/pull/824) Background process rearranged


### Bug Fixes

- [#817](https://github.com/RocketChat/Rocket.Chat.Electron/pull/817) Disabled update in builds for Mac App Store
- [#836](https://github.com/RocketChat/Rocket.Chat.Electron/pull/836) Window state persistency
- [#825](https://github.com/RocketChat/Rocket.Chat.Electron/pull/825) macOS menubar icon extra space removed
- [#835](https://github.com/RocketChat/Rocket.Chat.Electron/pull/835) Support On-Premise Jitsi screen sharing
- [#818](https://github.com/RocketChat/Rocket.Chat.Electron/pull/818) Fixed dock icon badge counter showing zero



<a name="2.12.1"></a>
## 2.12.1 (2018-08-14)

### Bug Fixes

- macOS dock badge fixed



<a name="2.12.0"></a>
# 2.12.0 (2018-08-04)


### New Features

- [#790](https://github.com/RocketChat/Rocket.Chat.Electron/pull/790) add pluralize
- [#777](https://github.com/RocketChat/Rocket.Chat.Electron/pull/777) New image for error page
- [#760](https://github.com/RocketChat/Rocket.Chat.Electron/pull/760) Notification on app icon
- [#776](https://github.com/RocketChat/Rocket.Chat.Electron/pull/776) Updated with new logo


### Bug Fixes

- [#778](https://github.com/RocketChat/Rocket.Chat.Electron/pull/778) Add snap build back
- [#791](https://github.com/RocketChat/Rocket.Chat.Electron/pull/791) Mac osx menubar color


<details>
<summary>Others</summary>

- [#785](https://github.com/RocketChat/Rocket.Chat.Electron/pull/785) Replace last couple of icons
</details>



<a name="2.11.0"></a>
# 2.11.0 (2018-06-10)


### New Features

- [#562](https://github.com/RocketChat/Rocket.Chat.Electron/pull/562) Add option to install language dictionaries
- [#691](https://github.com/RocketChat/Rocket.Chat.Electron/pull/691) Add german translation


### Bug Fixes

- [#670](https://github.com/RocketChat/Rocket.Chat.Electron/pull/670) Add & to menu items to avoid alt-shift menu popup
- [#685](https://github.com/RocketChat/Rocket.Chat.Electron/pull/685) CSS option in main.less
- [#742](https://github.com/RocketChat/Rocket.Chat.Electron/pull/742) cve 2018 1000136
- [#710](https://github.com/RocketChat/Rocket.Chat.Electron/pull/710) recompress PNG files lossless



<a name="2.10.5"></a>
## 2.10.5 (2018-02-07)

### Bug Fixes
- Dependencies updated



<a name="2.10.4"></a>
## 2.10.4 (2018-02-05)

### Bug Fixes
- macOS bundle version fixed



<a name="2.10.3"></a>
## 2.10.3 (2018-02-02)

### Bug Fixes
- Dependencies updated



<a name="2.10.2"></a>
## 2.10.2 (2018-01-26)


<details>
<summary>Others</summary>

- [#521](https://github.com/RocketChat/Rocket.Chat.Electron/pull/521) Mas entitlements
- [#520](https://github.com/RocketChat/Rocket.Chat.Electron/pull/520) npm deps update
</details>



<a name="2.10.1"></a>
# 2.10.1 (2017-11-09)

### Bug Fixes
- [#597](https://github.com/RocketChat/Rocket.Chat.Electron/pull/597) Fix MacOS dmg build


<a name="2.10.0"></a>
# 2.10.0 (2017-10-27)

### New Features
- [#552](https://github.com/RocketChat/Rocket.Chat.Electron/pull/552) Add context menu option for links
- [#556](https://github.com/RocketChat/Rocket.Chat.Electron/pull/556) Sidebar redesign and dynamic background color
- [#539](https://github.com/RocketChat/Rocket.Chat.Electron/pull/539) Adds drag and drop for servers in the sidebar
- [#533](https://github.com/RocketChat/Rocket.Chat.Electron/pull/533) New shortcut for moving back/forward between rooms

### Bug Fixes
- [#521](https://github.com/RocketChat/Rocket.Chat.Electron/pull/521) Fixes OSX build for AppStore
- [#546](https://github.com/RocketChat/Rocket.Chat.Electron/pull/546) Fixed wrong window size on loading screen
- [#532](https://github.com/RocketChat/Rocket.Chat.Electron/pull/532) Restores the help menu on Windows and Linux
- [#526](https://github.com/RocketChat/Rocket.Chat.Electron/pull/526) Fix notifications not opening the correct room


<a name="2.9.0"></a>
# 2.9.0 (2017-08-23)


### New Features

- [#320](https://github.com/RocketChat/Rocket.Chat.Electron/pull/320) Allow reply notifications on Mac OS
- [#490](https://github.com/RocketChat/Rocket.Chat.Electron/pull/490) Default servers improvements
- [#509](https://github.com/RocketChat/Rocket.Chat.Electron/pull/509) Add missing Services menu in application menu on macOS


### Bug Fixes

- [#494](https://github.com/RocketChat/Rocket.Chat.Electron/pull/494) Adding ESLint and fixing lint errors
- [#465](https://github.com/RocketChat/Rocket.Chat.Electron/pull/465) Fix bug in spellcheck
- [#512](https://github.com/RocketChat/Rocket.Chat.Electron/pull/512) Fix minimized start on Windows
- [#464](https://github.com/RocketChat/Rocket.Chat.Electron/pull/464) Remove duplicate notification on windows 7
- [#453](https://github.com/RocketChat/Rocket.Chat.Electron/pull/453) Read update settings from install location


<a name="2.8.0"></a>
# 2.8.0 (2017-05-17)


### New Features

- [#416](https://github.com/RocketChat/Rocket.Chat.Electron/pull/416) Snap build

### Bug Fixes

- [#440](https://github.com/RocketChat/Rocket.Chat.Electron/pull/440) Fix bug on some OS versions on about window, closes [#427](https://github.com/RocketChat/Rocket.Chat.Electron/issues/427)
- [#445](https://github.com/RocketChat/Rocket.Chat.Electron/pull/445) Fix bug when closing app in fullscreen




<a name="2.7.0"></a>
# 2.7.0 (2017-04-26)


### New Features

- [#411](https://github.com/RocketChat/Rocket.Chat.Electron/pull/411) Auto update when new version is released
- [#423](https://github.com/RocketChat/Rocket.Chat.Electron/pull/423) Open host from add new server page if it exists


### Bug Fixes

- [#417](https://github.com/RocketChat/Rocket.Chat.Electron/pull/417) Don't open dev tools on about, and show message when no updates
- [#425](https://github.com/RocketChat/Rocket.Chat.Electron/pull/425) Make sure app quits on mac on update
- [#426](https://github.com/RocketChat/Rocket.Chat.Electron/pull/426) Reduce drag region to fix manual scroll
- [#415](https://github.com/RocketChat/Rocket.Chat.Electron/pull/415) Updated README with servers.json instructions


<a name="2.6.1"></a>
## 2.6.1 (2017-04-04)

### Bug Fixes
- [#412](https://github.com/RocketChat/Rocket.Chat.Electron/pull/412) Fix bug with highlighting text & drag region on macOS


<a name="2.6.0"></a>
# 2.6.0 (2017-03-29)


### Bug Fixes

- [#384](https://github.com/RocketChat/Rocket.Chat.Electron/pull/384) Fix download file issue
- [#390](https://github.com/RocketChat/Rocket.Chat.Electron/pull/390) Fix speed issues with spellcheck on windows
- [#391](https://github.com/RocketChat/Rocket.Chat.Electron/pull/391) Only show reload screen if main webview error


<details>
<summary>Others</summary>

- [#336](https://github.com/RocketChat/Rocket.Chat.Electron/pull/336) Make it sexier in macOS
</details>

## 2.5.0 - 2017-Mar-05

- Add Fedora Dev Dependencies
- Allow opening of file urls
- Changed the function name and the switch is replaced with `icon-tray${title}.png`);
- Fix speed issues with spell check on Windows
- Fixed to put tray object in mainWindow
- Handle urls using click listener
- Load server config from file and tidy menu
- Show reload screen when server fails to load

## 2.4.0 - 2017-Fev-06

- Add .nvmrc
- Add download section to readme
- Add option to hide tray icon
- Add option to remove user data on uninstall
- Add option to toggle menu on windows and linux
- Allow multiple dictionaries if not using hunspell
- Capitalize menu items
- Fix blank notification issue
- Fix dictionaries path
- Fix issue with notification taking focus, and resize
- Fix issue with some notifications being blank
- Fix issues with desktop entry on linux
- Fix multiple certificate notifications and replacing webview with image
- Fix notification height with mulitple monitors
- Fix speed issues with spell check
- Improve design of screen selection
- Initial changes to enable screen share
- Keep user online if they are still active on their system
- Make windows notification unselectable
- Open link in app if internal url
- Prevent error from tray when window reloads
- Save disabled dictionary preference
- Set notification as inactive so it doesnt take focus from window
- Stop redirect when dragging image/url into window
- Update .editorconfig to match eslint
- Update jQuery to 3.1.1
- Update spectron 3.4. to 3.5.0

## 2.3.0 - 2017-Jan-24

- Add loading screen
- Add options of all users or current user for Windows install
- Add run at startup option on Windows
- Fix issues with Windows 7 notifications

## 2.2.3 - 2017-Jan-20

- Dependencies update

## 2.2.2 - 2017-Jan-20

- Fix client zoom keys the opposite way to be expected.
- Debounce window saveState call to avoid Error: EPERM: operation not permitted

## 2.2.1 - 2017-Jan-19

- Added left button click to taskbar-icon to show main window
- Fix various quirks with the windows installer

## 2.2.0 - 2017-Jan-11

### Upgrade electron-builder to 11.2.4

- Fix context menu

## 2.1.0 - 2017-Jan-10

- Better file organization
- Use [electron-builder](https://github.com/electron-userland/electron-builder) to generate our packages and installers
- Fix Spell Checker for all platforms
- Add builds for windows x32 and x64
- Add build automation with Travis and AppVeyor
- Fixed notifications on Windows 7
- Fixed post installation error messages on Windows 7

## 2.0.0 - 2016-Dec-26

### Upgrade electron to 1.4.13

## 1.3.1 - 2016-Apr-06

- Add underline keyboard shortcuts for Windows and Linux (#50)
- Add window min size 400px x 600px
- Prevent save window size for hidden windows
- Save state on window resize and move

## 1.3.0 - 2016-Apr-05

- Ask users to allow or deny when connecting to a server with invalid SSL
- HTTP Basic Authentication support (#144)
- Improve error handling for connecting to server (#143)
- OS X client - every word typed is highlighted as being misspelled (#162)
- Possibility to install without creating shortcut (#96)
- Restoring maximized window from tray restores to not maximized window size (#151)
- Save hidden state at Windows logout (#156)

## 1.2.0 - 2016-Mar-21

### Update electron-prebuilt to 0.36.10

- Add the "about" panel for windows and linux (#138)
- Add zoom options (#137)
- Application close (#123)
- Application crash when hiding or closing the app (#109)
- Do not add a big red dot on side bar for servers with unread messages (#132)
- Enable multilanguage spell checker; Allow user to set languages. (#124)
- Fix "Close Window" on OS X minimizes (#72)
- Improve spellchecker (#122)
- Improvements/huspell dicts (#128)
- Mac desktop client: Reload minimizes instead (#129)
- Open DevTools for active server (#136)
- Open DevTools for selected server instead of Electron (#133)
- Option to start the client hidden (#118)
- Prevent cache of server icon
- Reload current server instead of all application (#135)
- Right click reload server (#134)
- Spellchecker language not autodetecting on OS X (#119)
- Spellchecker not showing correct suggestions (#121)

## 1.1.0 - 2016-Feb-29

- Add server screen font not present on Windows (#100)
- Change Server Should be Add Server (#90)
- Close Now Closes the Application (#89)
- Have hotkeys to switch between Rocket chat instances. (#81)
- Make the taskbar blink when mentioned (#68)
- Open the app after installing on windows (#37)
- Option to change the install folder (#41)
- Right click -> copy / paste (#32)
- RIght click on URLs doesn't work cleanly in a cross-platform way. (#95)
- Start client with windows logon (#57)
- Tray icon on Windows requires triple click (#77)

> Special thanks to @floriangoeldi

## 1.0.0 - 2016-Feb-19

### Update electron to v0.36.4

- Add files to make branding easily
- Add spellchecker
- Create class to manage servers
- Create class to manage sidebar (servers list)
- Create class to manage webviews
- If you inform a server address with HTTPS we will fallback to HTTP if necessary
- Improve file upload getting file from inside the web view instead of from the main view and transmit to the webview via IPC
- Improve offline message
- Load all servers on aplication startup to enable notifications for all servers
- Load the last server and last room on application load or refresh
- Move all images to /app/images
- Now you can inform the server address without protocol, we will try HTTPS and then HTTP
- Open correct server from desktop notification
- Reactive tray icon
- Remove coffee-script dependency
- Remove font Roboto
- Remove unused CSS/LESS
- Show total of unreads in the application icon (OS X)
- Sidebar design improvement
- Sidebar now have a new button to add new servers
- Sidebar shows server's alert badge
- Sidebar shows server's icon or initials
- Sidebar shows server's title on mouse over
- Sidebar shows server's unread count
- Use webviews to allow multiple servers online at the same time

## 0.10.0 - 2015-Nov-11

### Update Electron to 0.34.0

## 0.9.0 - 2015-Oct-23

- Option to hide server's list

## 0.8.0 - 2015-Sep-14

### Update Electron to 0.32.2

## 0.7.0 - 2015-Aug-26

- Now you can add multiple servers

## 0.6.0 - 2015-Aug-07

### Updated Electron to 0.31.0

-  New demo URL

## 0.5.0 - 2015-Jul-27

### Upgrade electron to 0.30.2

- Better error message
- Disabled _tray.setTitle(title); until it can be optional
- Fix crash when closing app from try in OS X
- Fixed oAuth logins
- Increase start window size
- Listen for double-clicked event on tray to minimize/restore window
- Move window to front when click to show in tray
- Open http links as external
- Remove unnecessary files from OSX and Windows release
- Rename application executable and helpers
- Update Icons

## 0.4.0 - 2015-Jul-16

- Upgrade electron to 0.30.0 (Images from non HTTPS urls are displayed now)
- Improve icons for Windows
- Start using Coffee-Script

## 0.3.0 - 2015-Jul-15

- Tray icon
- Improve app icons

## 0.2.0 - 2015-Jul-10

- New app icon for OS X
- New background for dmg file
- Add application and context menus
