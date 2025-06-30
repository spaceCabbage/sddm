import os
import argparse
from pathlib import Path
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

accent_color = None

if args.scheme == "panther":
    if args.accent == "red":
        accent_color = "#FF7272"
    if args.accent == "orange":
        accent_color = "#FFAD72"
    if args.accent == "yellow":
        accent_color = "#FFDE72"
    if args.accent == "green":
        accent_color = "#A8FF72"
    if args.accent == "neon-green":
        accent_color = "#72FF7B"
    if args.accent == "cyan":
        accent_color = "#72E0FF"
    if args.accent == "blue":
        accent_color = "#72BBFF"
    if args.accent == "purple":
        accent_color = "#C272FF"
    if args.accent == "pink":
        accent_color = "#FF72F6"

if args.scheme == "lynx":
    if args.accent == "red":
        accent_color = "#9A0000"
    if args.accent == "orange":
        accent_color = "#9A5200"
    if args.accent == "yellow":
        accent_color = "#9A7100"
    if args.accent == "green":
        accent_color = "#5F9A00"
    if args.accent == "neon-green":
        accent_color = "#299A00"
    if args.accent == "cyan":
        accent_color = "#008B9A"
    if args.accent == "blue":
        accent_color = "#00679A"
    if args.accent == "purple":
        accent_color = "#62009A"
    if args.accent == "pink":
        accent_color = "#9A0074"

src_dir = Path(script_dir) / "src"
conf_path = src_dir / f"{args.scheme}.conf"
user_conf_path = src_dir / "theme.conf.user"

with open(conf_path, 'r') as f:
    content = f.read()

content = content.replace('accentColor=', f'accentColor="{accent_color}"')

if args.wallpaper:
    content = content.replace("background=", f"background={args.wallpaper}")

with open(user_conf_path, 'w') as f:
    f.write(content)

subprocess.run("sudo rm -rf /usr/share/sddm/themes/monocode/", shell=True)
subprocess.run(f"sudo cp -r {src_dir} /usr/share/sddm/themes/monocode/", shell=True)

print("✅ Installed Successfully")
print("To use the theme add the following in /etc/sddm.conf\n")
print("[Theme]\nCurrent=monocode")

apply = str(input("\n\nWould you like to change it now? [y/N]: ")).lower()

if apply == "yes" or apply == "y":
    subprocess.run("sudo vim /etc/sddm.conf", shell=True)
