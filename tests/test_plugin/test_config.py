from pathlib import Path

from mkconf.plugin import ConfPlugin
from mkdocs.config import load_config

# -----------------------------------------------------------------------------
# Classes
# -----------------------------------------------------------------------------


def test_default_init(tmp_path:Path ) -> None:
    options = {"agenda": []}
    plugin = ConfPlugin()
    test_config_path = tmp_path / Path('mkdocs_test.yaml')
    test_config_path.touch()
    assert test_config_path.exists()
    errors, warnings = plugin.load_config(options,str(test_config_path))
    
    print(plugin.config)
    assert plugin.config.speakers_file == "speakers.yaml"
    assert plugin.config.organizers_file == "organizers.yaml"
    assert plugin.config.agenda_file == "agenda.yaml"
    
def test_file_init() -> None:
    options = {"speakers_file": ".speakers.yaml", 
               "organizers_file": ".organizers.yaml", 
               "agenda_file": ".agenda.yaml"}
    plugin = ConfPlugin()
    test_config_path = Path('tests/test_data/mkdocs.yml')
    assert test_config_path.exists()
    errors, warnings = plugin.load_config(options,str(test_config_path))
    
    print(plugin.config)
    assert plugin.config.speakers_file == ".speakers.yaml"
    assert plugin.config.organizers_file == ".organizers.yaml"
    assert plugin.config.agenda_file == ".agenda.yaml"

def test_plugin_init() -> None:
    options = {}

    test_config_path = Path('tests/test_data/mkdocs.yml')
    assert test_config_path.exists()
    config= load_config(config_file=str(test_config_path))
    print(config)
    assert False