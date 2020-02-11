from cluster_maintenance import __version__
from cluster_maintenance.runner import cm


def test_that_help_menu_shows_with_cli_name(runner):
    result = runner.invoke(cm)
    assert result.exit_code == 0
    assert "Common commands for maintaining a cluster." in result.output


def test_that_version_outputs_correctly(runner):
    result = runner.invoke(cm, ["--version"])
    assert result.exit_code == 0
    assert result.output == f"cluster maintenance, version {__version__}\n"
