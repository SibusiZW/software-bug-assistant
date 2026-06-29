import subprocess

def run_command(cmd: str) -> str:
    try:
        cmd_output = subprocess.run(cmd, capture_output=True, text=True, shell=True)
        return cmd_output.stdout
    except Exception as e:
        return str(e)