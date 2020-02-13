import socket
import subprocess

import click


@click.group()
def ip():
    """Retrieves the ip address of the current system"""


@ip.command(short_help="Retrieve the public ip address.")
def public():
    """Retrieves the ip address of the current system"""
    click.secho(
        subprocess.check_output(
            ["curl", "https://ipinfo.io/ip"],
            encoding="utf-8",
            stderr=subprocess.DEVNULL,
        ).strip(),
        fg="green",
    )


@ip.command(short_help="Retrieve the local ip address.")
def local():
    click.secho(socket.gethostbyname(socket.gethostname()), fg="green")
