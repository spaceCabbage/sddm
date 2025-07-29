.PHONY: preview install clean

# Preview the SDDM theme
preview:
	sddm-greeter-qt6 --test-mode --theme ./src

# Install the theme with hardcoded wallpaper
install:
	python install.py

# Clean any generated files
clean:
	@echo "Cleaning up..."
	@find . -name "*.pyc" -delete
	@find . -name "__pycache__" -type d -delete