import yaml
from pathlib import Path

from mkdocs.config import Config as MkDocsConfig
from mkdocs.plugins import BasePlugin, get_plugin_logger


from mkconf.config import ConfConfig

logger = get_plugin_logger(__name__)


class ConfPlugin(BasePlugin[ConfConfig]):
    def on_config(self, config: MkDocsConfig, **kwargs) -> MkDocsConfig:
        # file paths should be relateive to mkdocs config.
        configuration_files = [
            self.config.speakers_file,
            self.config.organizers_file,
            self.config.agenda_file,
        ]

        opt: dict = {}

        for config_file in configuration_files:
            config_file = Path(config.config_file_path).parent / config_file

            if not Path(config_file).exists():
                logger.error(f"Could not find {config_file}")
            try:
                with open(config_file, "r") as f:
                    config_content = yaml.safe_load(f)
                    for key, value in config_content.items():
                        opt[key] = value
            except Exception as e:
                logger.error(f"Could not load configureation from {config_file}: {e}")

        if len(opt) == 0:
            logger.error("configuration is empty")

        self.config.load_dict(patch= opt)
        return config
