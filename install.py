import argparse
import os
import subprocess
from enum import Enum
from pathlib import Path

script_dir = os.path.dirname(os.path.abspath(__file__))


def valid_file(path):
    if not os.path.isfile(path):
        raise argparse.ArgumentTypeError(f"{path} is not a valid file")
    return os.path.abspath(path)


scheme = "nsa"
wallpaper = os.path.join(script_dir, "src", "nsa-wallpaper.png")


src_dir = Path(script_dir) / "src"
conf_path = src_dir / f"{scheme}.conf"
user_conf_path = src_dir / "theme.conf.user"

with open(conf_path, "r") as f:
    content = f.read()

subprocess.run("sudo rm -rf /usr/share/sddm/themes/monocode/", shell=True)
subprocess.run("sudo mkdir /usr/share/sddm/themes/monocode/", shell=True)

extension = Path(wallpaper).suffix
content = content.replace(
    "background=",
    f"background=/usr/share/sddm/themes/monocode/wallpaper{extension}",
)
result = subprocess.run(
    f"sudo cp '{wallpaper}' /usr/share/sddm/themes/monocode/wallpaper{extension}",
    shell=True,
    check=True,
)
print(result.stdout)
print(result.stderr)

with open(user_conf_path, "w") as f:
    f.write(content)

subprocess.run(f"sudo cp -r {src_dir}/* /usr/share/sddm/themes/monocode/", shell=True)

print("✅ Installed Successfully")
print("To use the theme add the following in /etc/sddm.conf\n")
print("[Theme]\nCurrent=monocode")

apply = str(input("\n\nWould you like to change it now? [y/N]: ")).lower()

if apply == "yes" or apply == "y":
    subprocess.run("sudo nano /etc/sddm.conf", shell=True)
