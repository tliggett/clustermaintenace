import click

from cluster_maintenance import __version__
from cluster_maintenance.ip import ip


@click.group()
@click.version_option(version=__version__, prog_name="cluster maintenance")
def cm():
    """Common commands for maintaining a cluster."""


cm.add_command(ip)
