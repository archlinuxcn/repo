const { existsSync, renameSync } = require("fs");
const { join } = require("path");

module.exports = afterPack = async context => {
    const { packager } = context;
    const { platformSpecificBuildOptions, config } = packager;

    const sources = [platformSpecificBuildOptions.icon, (config.mac && config.mac.icon) || config.icon].filter(
        str => !!str
    );

    // If no explicit sources are defined, fallback to buildResources directory, then default framework icon
    let fallbackSources = [packager.getDefaultFrameworkIcon()];
    const buildResources = config.directories && config.directories.buildResources;
    if (buildResources && existsSync(join(buildResources, "icons"))) {
        fallbackSources = [buildResources].concat(fallbackSources);
    }

    await packager.resolveIcon(sources, fallbackSources, "set");

    const filesToRename = [
        {
            old: "icon_16x16.png",
            new: "icon_16.png"
        },
        {
            old: "icon_48x48.png",
            new: "icon_48.png"
        }
    ];

    filesToRename.forEach(file => {
        const oldPath = join(config.directories.output, ".icon-set", file.old);
        const newPath = join(config.directories.output, ".icon-set", file.new);
        if (existsSync(oldPath)) {
            renameSync(oldPath, newPath);
        }
    });
};
