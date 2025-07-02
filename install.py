import os
import argparse
from pathlib import Path
from enum import Enum
import subprocess

script_dir = os.path.dirname(os.path.abspath(__file__))

parser = argparse.ArgumentParser(description="Monocode SDDM Installer")

def valid_file(path):
    if not os.path.isfile(path):
        raise argparse.ArgumentTypeError(f"{path} is not a valid file")
    return os.path.abspath(path)

parser.add_argument('--scheme', choices=['panther', 'lynx'], default='panther', help="Base theme (default: panther)")
parser.add_argument('--accent', choices=['red', 'orange', 'yellow', 'green', 'neon-green', 'cyan', 'blue', 'purple', 'pink'], default="yellow", help="Accent color (default: yellow)")
parser.add_argument('--wallpaper', type=valid_file, help="Path to wallpaper image", default=None)

args = parser.parse_args()

class PantherAccentColor(Enum):
    RED = "#FF7272"
    ORANGE = "#FFAD72"
    YELLOW = "#FFDE72"
    GREEN = "#A8FF72"
    NEON_GREEN = "#72FF7B"
    CYAN = "#72E0FF"
    BLUE = "#72BBFF"
    PURPLE = "#C272FF"
    PINK = "#FF72F6"


class LynxAccentColor(Enum):
    RED = "#9A0000"
    ORANGE = "#9A5200"
    YELLOW = "#9A7100"
    GREEN = "#5F9A00"
    NEON_GREEN = "#299A00"
    CYAN = "#008B9A"
    BLUE = "#00679A"
    PURPLE = "#62009A"
    PINK = "#9A0074"

def get_accent_color(scheme: str, accent: str) -> str:
    try:
        if scheme == "panther":
            print(PantherAccentColor[accent.upper().replace("-", "_")].value)
            return PantherAccentColor[accent.upper().replace("-", "_")].value
        elif scheme == "lynx":
            return LynxAccentColor[accent.upper().replace("-", "_")].value
        else:
            raise ValueError(f"Unknown scheme: {scheme}")
    except KeyError:
        raise ValueError(f"Unknown accent: {accent}")

src_dir = Path(script_dir) / "src"
conf_path = src_dir / f"{args.scheme}.conf"
user_conf_path = src_dir / "theme.conf.user"

with open(conf_path, 'r') as f:
    content = f.read()

content = content.replace('accentColor=', f'accentColor="{get_accent_color(args.scheme, args.accent)}"')

subprocess.run("sudo rm -rf /usr/share/sddm/themes/monocode/", shell=True)
subprocess.run("sudo mkdir /usr/share/sddm/themes/monocode/", shell=True)

if args.wallpaper:
    extension = Path(args.wallpaper).suffix
    content = content.replace("background=", f"background=/usr/share/sddm/themes/monocode/wallpaper{extension}")
    result = subprocess.run(f"sudo cp '{args.wallpaper}' /usr/share/sddm/themes/monocode/wallpaper{extension}", shell=True, check=True)
    print(result.stdout)
    print(result.stderr)

with open(user_conf_path, 'w') as f:
    f.write(content)

subprocess.run(f"sudo cp -r {src_dir}/* /usr/share/sddm/themes/monocode/", shell=True)

print("✅ Installed Successfully")
print("To use the theme add the following in /etc/sddm.conf\n")
print("[Theme]\nCurrent=monocode")

apply = str(input("\n\nWould you like to change it now? [y/N]: ")).lower()

if apply == "yes" or apply == "y":
    subprocess.run("sudo vim /etc/sddm.conf", shell=True)
