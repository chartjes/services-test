import os
import platform
import ConfigParser


def get_os():
    """
    Get the current Operating System.
    """
    return platform.system().lower().split('_').pop(0)


def load_firefox_paths(in_file, out_file):
    """
    Load Firefox configs from an input .INI file and add them as exportable
    environment variables in a new file.
    """
    env_vars = []
    system = get_os()

    if os.path.isfile(out_file):
        os.remove(out_file)

    if not os.path.isfile(in_file):
        print 'Config file not found: %s' % (in_file)
        exit(1)

    Config = ConfigParser.ConfigParser()
    Config.read(in_file)

    try:
        for key in Config.options(system):
            value = Config.get(system, key)
            env_vars.append('export %s=%s' % (key.upper(), value))
    except:
        print 'Unable to find config for "%s" in %s' % (system, in_file)
        print 'Valid environments are: %s' % (', '.join(Config.sections()))
        exit(1)

    with open(out_file, 'w') as f:
        f.write('\n'.join(env_vars))


load_firefox_paths('path_firefox.ini', '.env')
