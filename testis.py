from pathlib import Path

# 1. Automatically get the current user's home directory (e.g., C:\Users\poazw)
HOME_DIR = Path.home()

# 2. Point to the folder on the Desktop (change "assets" to match your exact folder name)
ASSETS_DIR = HOME_DIR / "Desktop" /"ASSETS"

# 3. Safely get the files
if ASSETS_DIR.exists() and ASSETS_DIR.is_dir():
    asset_files = [file for file in ASSETS_DIR.iterdir() if file.is_file()]
    print(f"Success! Found {len(asset_files)} files.")
    for file in asset_files:
        print("-", file.name)
else:
    print(f"Error: Could not find the folder at: {ASSETS_DIR}")
