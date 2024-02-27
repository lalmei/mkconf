import yaml
from typing import Optional
from pathlib import Path

from mkdocs.config import Config as MkDocsConfig
from mkdocs.plugins import BasePlugin, get_plugin_logger
from mkdocs.config import   config_options as opt
from jinja2 import Template

from mkconf.config import ConfConfig

logger = get_plugin_logger(__name__)


class ConfPlugin(BasePlugin[ConfConfig]):
    
    def on_config(self, config: MkDocsConfig, **kwargs): 
        
        conf_config = config.plugins['mkconf'].config
        print(kwargs)
        opt ={}
        if Path(conf_config.speakers_file).exists():
            with open(conf_config.speakers_file, 'r') as f:
                speakers_config = yaml.safe_load(f)
            opt["speakers"] = speakers_config
        else: 
            logger.error("Could not find speakers yaml file")

        if Path(conf_config.organizers_file).exists():
            with open(conf_config.organizers_file, 'r') as f:
                organizers_config = yaml.safe_load(f)
            opt["organizers"] = organizers_config
        else: 
            logger.error("Could not find organizers yaml file")

        if Path(conf_config.agenda_file).exists():
            with open(conf_config.agenda_file, 'r') as f:
                agenda_config = yaml.safe_load(f)
            opt["agenda"] = agenda_config
        else: 
            logger.error("Could not find agenda yaml file")
        
        self.load_config(options=opt)

        config.plugins['mkconf'].config = conf_config
        return config