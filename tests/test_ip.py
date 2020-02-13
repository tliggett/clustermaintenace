import socket
import urllib.request

from cluster_maintenance.runner import cm


def test_public_ip(runner):
    result = runner.invoke(cm, ["ip", "public"])
    assert result.exit_code == 0
    assert (
        urllib.request.urlopen("https://api.ipify.org").read().decode("utf-8")
        in result.output
    )


def test_local_ip(runner):
    result = runner.invoke(cm, ["ip", "local"])
    assert result.exit_code == 0
    assert socket.gethostbyname(socket.gethostname()) in result.output
