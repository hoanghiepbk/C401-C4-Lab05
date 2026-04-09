import sys
import os
from pathlib import Path

# Add the root directory to sys.path to resolve 'apps' and 'packages'
BASE_DIR = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(BASE_DIR))

from apps.api.main import app

# Vercel needs the app object to be named 'app'
# Since we already named it 'app' in main.py, we just import it.
