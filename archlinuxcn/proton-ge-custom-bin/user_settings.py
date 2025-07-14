#Settings here will take effect for all games run with this Proton version.

user_settings = {
    ###### Proton GE flags ######

    #Disables DX12.
#    "PROTON_NO_D3D12": "1",

    #Disable AMD FidelityFX Super Resolution (FSR), as it is enabled by default. FSR only works in vulkan games (dxvk and vkd3d-proton included).
#    "WINE_FULLSCREEN_FSR": "0",

    #By default, the "balanced" resolution option for FSR is added to the resolution list if a mode is not specified.
    #possible modes : ultra, quality, balanced, performance.
#    "WINE_FULLSCREEN_FSR_MODE": "performance",

    #Add "widthxheight" to the in-game resolution list. Example resolution: 1234x4321
#    "WINE_FULLSCREEN_FSR_CUSTOM_MODE": "1234x4321"

    #The default sharpening of 5 is enough without needing modification, but can be changed with 0-5 if wanted.
    #0 is the maximum sharpness, higher values mean less sharpening.
    #2 is the AMD recommended default and is set by proton-ge.
#    "WINE_FULLSCREEN_FSR_STRENGTH": "2",

    ###### Proton flags ######

    #Enable use of the ntsync kernel driver to improve performance and compatibility of Windows NT synchronization primitives.
#   "PROTON_USE_NTSYNC": "1",

    #Enable automatic upgrading of AMD FidelityFX Super Resolution (FSR) to FSR4.
#   "PROTON_FSR4_UPGRADE": "1",

    #Enable Wayland display output. Games running with native Vulkan and OpenGL may have problems. Required for HDR support
#   "PROTON_ENABLE_WAYLAND": "1",

    #Enable HDR support. Requires Wayland to be enabled and for HDR to be enabled in system settings.
#   "PROTON_ENABLE_HDR":    "1",

    #Convenience method for dumping a useful debug log to $PROTON_LOG_DIR/steam-$APPID.log
#    "PROTON_LOG": "1",

    #Log directory can be overridden with $PROTON_LOG_DIR.
#    "PROTON_LOG_DIR": "~/",

    #When running a game, Proton will write some useful debug scripts for that game into $PROTON_DEBUG_DIR/proton_$USER/.
#    "PROTON_DUMP_DEBUG_COMMANDS": "1",

    #Root directory for the Proton debug scripts, /tmp by default.
#    "PROTON_DEBUG_DIR": "1",

    #Use OpenGL-based wined3d for d3d11, d3d10, and d3d9 instead of Vulkan-based DXVK
#    "PROTON_USE_WINED3D": "1",

    #Disable d3d11.dll, for d3d11 games which can fall back to and run better with d3d9.
#    "PROTON_NO_D3D11": "1",

    #DDisable d3d10.dll and dxgi.dll, for d3d10 games which can fall back to and run better with d3d9.
#    "PROTON_NO_D3D10": "1",

    #Disable eventfd-based in-process synchronization primitives
#    "PROTON_NO_ESYNC": "1",

    #Disable futex-based in-process synchronization primitives
#    "PROTON_NO_FSYNC": "1",

    #Enable NVIDIA's NVAPI GPU support library.
#    "PROTON_ENABLE_NVAPI": "1",

    #Force Wine to enable the LARGE_ADDRESS_AWARE flag for all executables. Enabled by default.
#    "PROTON_FORCE_LARGE_ADDRESS_AWARE": "0",

    #Delay freeing some memory, to work around application use-after-free bugs.
#    "PROTON_HEAP_DELAY_FREE": "1",

    #Create an S: drive which points to the Steam Library which contains the game.
#    "PROTON_SET_GAME_DRIVE": "1",

    #Create an S: drive which points to the Steam Library which contains the game.
#    "PROTON_OLD_GL_STRING": "1",

    #Force Nvidia GPUs to always be reported as AMD GPUs.
    #Some games require this if they depend on Windows-only Nvidia driver functionality.
    #See also DXVK's nvapiHack config, which only affects reporting from Direct3D.
#    "PROTON_HIDE_NVIDIA_GPU": "1",

    #Disable support for memory write watches in ntdll.
    #This is a very dangerous hack and should only be applied if you have verified that the game can operate without write watches.
    #This improves performance for some very specific games (e.g. CoreRT-based games).
#    "PROTON_NO_WRITE_WATCH": "1",

    #When this envvar is set steam input and hidraw are disabled so that SDL takes priority over controller support.
#    "PROTON_PREFER_SDL": "1",

    ###### DXVK flags ######

    #DXVK debug logging; none|error|warn|info|debug
#    "DXVK_LOG_LEVEL": "info",

    #DXVK debug log; Set to none to disable log file creation entirely, without disabling logging.
#    "DXVK_LOG_PATH": "~/",

    #Enables use of the VK_EXT_debug_utils extension for translating performance event markers.
#    "DXVK_PERF_EVENTS": "1",

    #Enables use of the VK_EXT_debug_utils extension for translating performance event markers.
#    "DXVK_CONFIG_FILE": "~/.config/dxvk.conf",

    #Enable DXVK's HUD; devinfo|fps|frametimes|submissions|drawcalls|pipelines|memory|gpuload|version|api|compiler|samplers|scale=x
#    "DXVK_HUD": "devinfo,fps",

    #Limit the frame rate. A value of 0 uncaps the frame rate, while any positive value will limit rendering to the given number of frames per second.
#    "DXVK_FRAME_RATE": "60",

    #DXVK pipeline cache; "0" disable|"/some/directory" Defaults to the current working directory of the application.
#    "DXVK_STATE_CACHE": "0",

    #Selects devices with a matching Vulkan device name, which can be retrieved with tools such as vulkaninfo.
#    "DXVK_FILTER_DEVICE_NAME": "Device Name",

    #Vulkan debug layers. Requires the Vulkan SDK to be installed.
#    "VK_INSTANCE_LAYERS": "VK_LAYER_KHRONOS_validation",

    ###### Wine flags ######

    #Enable integer scaling mode, to give sharp pixels when upscaling.
#    "WINE_FULLSCREEN_INTEGER_SCALING": "1",

    #Wine debug logging
#    "WINEDEBUG": "+timestamp,+pid,+seh,+unwind,+debugstr,+loaddll,+mscoree",

    #vkd3d debug logging
#    "VKD3D_DEBUG": "warn",

    #wine-mono debug logging (Wine's .NET replacement)
#    "WINE_MONO_TRACE": "E:System.NotImplementedException",
#    "MONO_LOG_LEVEL": "info",

    #general purpose media logging
#    "GST_DEBUG": "4",
    #or, verbose converter logging (may impact playback performance):
#    "GST_DEBUG": "4,WINE:7,protonaudioconverter:7,protonaudioconverterbin:7,protonvideoconverter:7",
#    "GST_DEBUG_NO_COLOR": "1",
}
