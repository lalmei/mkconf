from pathlib import Path

from mkdocs.commands import build
from mkdocs import plugins 
from mkdocs.config import load_config

from mkconf.plugin import ConfPlugin

def test_plugin_init() -> None:
  
    test_config_path = Path('tests/test_data/mkdocs.yml')
    assert test_config_path.exists()
    config= load_config(config_file=str(test_config_path))
    assert config.plugins['mkconf'] is not None
    plugin = config.plugins['mkconf'] 
    assert plugin.config.speakers_file == '.speakers.yaml'
    assert plugin.config.organizers_file == '.organizers.yaml'
    assert plugin.config.agenda_file == '.agenda.yaml'

def test_event_plugin() -> None:

    plugin = ConfPlugin()
    plugin.load_config(options={}, config_file_path=None)
    collection = plugins.PluginCollection()
    collection['mkdocs'] =plugin

    assert plugin.on_config in collection.events["config"] 


def test_plugin_run(tmp_path:Path) -> None:

    test_config_path = Path('tests/test_data/mkdocs.yml')
    config= load_config(config_file=str(test_config_path))
    config.site_dir = tmp_path  
    build.build(config)
    assert (tmp_path / "index.html").exists()
    with open( (tmp_path / "index.html"), 'r') as file:
        html = file.read()
    assert 'name1' in html
    assert 'name2' in html
    assert 'title1' in html
    assert 'title2' in html