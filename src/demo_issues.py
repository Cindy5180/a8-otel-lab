"""Fixed version of the linting demo (all findings resolved)."""
import ast
import hashlib
import os
import subprocess  # noqa: S404 (used safely, no shell)

PASSWORD = os.environ.get("DEMO_PASSWORD", "")  # read from environment, never hard-code


def run(cmd):
    # argument list, no shell: prevents command injection (CWE-78)
    subprocess.run(cmd, shell=False, check=False)  # noqa: S603


def digest(data):
    return hashlib.sha256(data).hexdigest()  # SHA-256 instead of MD5


def parse(x):
    try:
        return ast.literal_eval(x)  # literal_eval instead of eval
    except (ValueError, SyntaxError):
        return None
