function log() {
    var msg = ["INSTALLER: "].concat([].slice.call(arguments));
    console.log(msg.join(" "));
}

function Controller() {
}

Controller.prototype.WelcomePageCallback = function() {
    log("WelcomePageCallback");
    gui.clickButton(buttons.NextButton);
}

Controller.prototype.IntroductionPageCallback = function() {
    log("IntroductionPageCallback");
    gui.clickButton(buttons.NextButton);
}

Controller.prototype.DynamicTargetWidgetCallback = function() {
    log("DynamicTargetWidgetCallback");
    var widget = gui.pageWidgetByObjectName("DynamicTargetWidget");

    if (widget != null) {
        widget.targetDirectory.setText("OUTPUT_DIRECTORY");
    }
    gui.clickButton(buttons.NextButton);
}

Controller.prototype.DynamicLicenseWidgetCallback = function() {
    log("DynamicLicenseWidgetCallback");
    var widget = gui.pageWidgetByObjectName("DynamicLicenseWidget");

    if (widget != null) {
        widget.acceptLicense.checked = true;
    }

    gui.clickButton(buttons.NextButton);

}

Controller.prototype.FinishedPageCallback = function() {
    log("FinishedPageCallback");
    gui.clickButton(buttons.FinishButton);
}

