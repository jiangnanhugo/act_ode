"""Utility functions."""


import commentjson as json


##### load configure files

def load_config(config=None):
    # Load user config
    print("user config file:", config)
    if isinstance(config, str):
        with open(config, encoding='utf-8') as f:
            user_config = json.load(f)
    elif isinstance(config, dict):
        user_config = config
    else:
        assert config is None, "Config must be None, str, or dict."
        user_config = {}
    return user_config
