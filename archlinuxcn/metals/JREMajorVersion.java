import java.util.regex.Pattern;
import java.util.regex.Matcher;

public final class JREMajorVersion {

  private static final Pattern sanitizePattern =
    Pattern.compile("^\\s*([0-9]+(\\.[0-9]+)*)");

  private static final String bugLink =
    "Please report this as a bug to https://aur.archlinux.org/packages/metals/";

  private static String sanitizeVersion(final String value) {
    final Matcher m = JREMajorVersion.sanitizePattern.matcher(value);
    if (m.find()) {
      return m.group(1);
    } else {
      throw new AssertionError("Unable to parse valid version number from input: " +
                               value +
                               ". This may be a bug in the Arch Linux package of metals, or something very odd in the JRE you are using. " +
                               JREMajorVersion.bugLink);
    }
  }

  private static String getMajorVersion() {
    final String javaVersion = sanitizeVersion(System.getProperty("java.version"));
    if (javaVersion == null) {
      throw new AssertionError("System property \"java.version\" is null. " + JREMajorVersion.bugLink);
    } else {
      final String[] javaVersionComponents = javaVersion.split("\\.");
      if (javaVersionComponents.length < 1) {
        // In this case there is no '.' in the version number, e.g. it
        // is "15"
        return javaVersion;
      } else if (javaVersionComponents[0].equals("1")) {
        // Probably using the older version number scheme,
        // e.g. "1.8.0"
        return javaVersionComponents[1];
      } else {
        return javaVersionComponents[0];
      }
    }
  }

  public static void main(final String[] args) {
    System.out.println(JREMajorVersion.getMajorVersion());
  }
}
