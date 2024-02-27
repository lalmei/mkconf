from pathlib import Path

from mkconf.plugin import ConfPlugin
from mkconf.config import ConfConfig
from mkdocs.config import load_config



def test_default_init(tmp_path:Path ) -> None:

    options = {"agenda": []}
    plugin = ConfPlugin()
    test_config_path = tmp_path / Path('mkdocs_test.yaml')
    test_config_path.touch()
    assert test_config_path.exists()
    errors, warnings = plugin.load_config(options,str(test_config_path))
    
    assert type(plugin.config) is ConfConfig
    assert plugin.config.speakers_file == "speakers.yml"
    assert plugin.config.organizers_file == "organizers.yml"
    assert plugin.config.agenda_file == "agenda.yml"

 
def test_dict_init(tmp_path:Path ) -> None:

    options = {"speakers_file": ".speakers_opt.yaml", 
               "organizers_file": ".organizers_opt.yaml", 
               "agenda_file": ".agenda_opt.yaml"}
    plugin = ConfPlugin()
    test_config_path = tmp_path / Path('mkdocs_test.yaml')
    test_config_path.touch()
    assert test_config_path.exists()
    errors, warnings = plugin.load_config(options,str(test_config_path))
    

    assert plugin.config.speakers_file == ".speakers_opt.yaml"
    assert plugin.config.organizers_file == ".organizers_opt.yaml"
    assert plugin.config.agenda_file == ".agenda_opt.yaml"

