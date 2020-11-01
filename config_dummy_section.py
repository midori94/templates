from configparser import ConfigParser

CONFIG_FILE = 'my_config.conf'
with open(CONFIG_FILE, 'r') as f:
  config_string = '[dummy_section]\n' + f.read()
config = ConfigParser().read_string(config_string)
