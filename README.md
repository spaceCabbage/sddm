# NSA SDDM Theme

A sleek, modern SDDM (Simple Desktop Display Manager) theme with a NSA-inspired aesthetics.

![Preview](preview.png)

## Requirements

- SDDM (Simple Desktop Display Manager)
- Qt5/Qt6 with Quick Controls 2
- Python 3.x (for installation script)

### Arch Linux Dependencies
```bash
sudo pacman -S sddm qt5-quickcontrols2 qt6-quickcontrols2
```

## Installation

### Quick Install

1. Clone the repository:
```bash
git clone https://github.com/spaceCabbage/sddm.git
cd sddm

# Install the theme:
python install.py
```

3. Configure SDDM to use the theme by editing `/etc/sddm.conf`:
```conf
[Theme]
Current=nsa
```

## Preview

You can preview the theme to see how it looks:

```bash
make preview
```

## Troubleshooting

### Theme not showing up
- Ensure SDDM is installed and running
- Check that `/etc/sddm.conf` has the correct theme name
- Verify Qt5/Qt6 Quick Controls are installed

### Preview command fails
- Try using `sddm-greeter` instead of `sddm-greeter-qt6`
- Ensure you have proper display permissions

This project is open source and available under the [MIT License](LICENSE).

## Credits

- Based on the [Mono Code SDDM theme](https://github.com/Mono-Code-Scheme/sddm)
- NSA-inspired aesthetics and color scheme
- Icons from the original Mono Code theme