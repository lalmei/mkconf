from mkdocs.config import Config as MkDocsConfig
from mkdocs.plugins import get_plugin_logger
from mkdocs.config import config_options as opt

logger = get_plugin_logger(__name__)


class TimeDisplayConfig(MkDocsConfig):
    h = opt.Type(int, default=0)
    m = opt.Type(int, default=0)
    a = opt.Type(type_=opt.Choice(["am", "pm"]), default="am")


class AgendaConfig(MkDocsConfig):
    """
    Configuration for an agenda item.

    Args:
        range_t (list[str]): The time range for the agenda item.
        desc (str): The description of the agenda item.
        display (ListofItems[TimeDisplayConfig]): The time display configuration for the agenda item.
        location (str): The location of the agenda item.
    """

    range_t = opt.Type(list[str], default=[])
    desc = opt.Type(str, default="")
    display = opt.SubConfig(TimeDisplayConfig)
    location = opt.Type(str, default="")


class OrganizersConfig(MkDocsConfig):
    """
    Configuration for an organizer.

    Args:
        name (str): The name of the organizer.
        title (str): The title of the organizer.
        company (str): The company that the organizer works for.
        social_link (str): The social media link for the organizer.
        image (str): The image of the organizer.

    """

    name = opt.Type(str, default="")
    title = opt.Type(str, default="")
    company = opt.Type(str, default="")
    social_link = opt.Type(str, default="")
    image = opt.Type(str, default="")


class SpeakersConfig(MkDocsConfig):
    """
    Configuration for a speaker.

    Args:
        name (str): The name of the speaker.
        title (str): The title of the speaker.
        company (str): The company that the speaker works for.
        social_link (str): The social media link for the speaker.
        image (str): The image of the speaker.
    """

    name = opt.Type(str, default="")
    title = opt.Type(str, default="")
    company = opt.Type(str, default="")
    social_link = opt.Type(str, default="")
    image = opt.Type(str, default="")


class ConfConfig(MkDocsConfig):

    conference_title = opt.Type(str, default="")
    conference_subtitle = opt.Type(str, default="")
    conference_location = opt.Type(str, default="")

    speakers_file = opt.Type(str, default="speakers.yml")
    organizers_file = opt.Type(str, default="organizers.yml")
    agenda_file = opt.Type(str, default="agenda.yml")

    speakers = opt.ListOfItems(opt.SubConfig(SpeakersConfig), default=[])
    organizers = opt.ListOfItems(opt.SubConfig(OrganizersConfig), default=[])
    agenda = opt.ListOfItems(opt.SubConfig(AgendaConfig), default=[])
