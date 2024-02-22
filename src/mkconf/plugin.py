import yaml
from typing import Optional

from mkdocs.config import Config as MkDocsConfig
from mkdocs.plugins import BasePlugin, get_plugin_logger
from mkdocs.config import   config_options as opt
from jinja2 import Template

from mkconf.config import ConfConfig

logger = get_plugin_logger(__name__)


class ConfPlugin(BasePlugin[ConfConfig]):
    
    