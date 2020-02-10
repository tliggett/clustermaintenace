import subprocess


def get_public_ip() -> str:
    """Retrieves the public ip address of the current system."""
    return subprocess.check_output(
        ['curl', 'https://ipinfo.io/ip'],
        encoding='utf-8',
        stderr=subprocess.DEVNULL
    ).strip()


if __name__ == '__main__':
    print(get_public_ip())

