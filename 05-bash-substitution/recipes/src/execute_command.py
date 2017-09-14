import subprocess


def execute_command(cmd):
    """
    Execute the passed command
    """
    subprocess.call(cmd.split())


if __name__ == "__main__":
    execute_command("ls -a /usr")
