from flask import Flask
from flask_cors import CORS
import sys
import os

# Get the absolute path of the project root (one level above backend)
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if project_root not in sys.path:
    sys.path.append(project_root)

try:
    from backend.processing.medical_routes import medical_bp  # ✅ Importing medical routes
except ModuleNotFoundError as e:
    print(f"❌ Module import error: {e}")
    print("⚠️ Ensure all required files exist and are correctly placed.")
    sys.exit(1)  # Exit script if module import fails

app = Flask(__name__)
CORS(app)  # Enable Cross-Origin Resource Sharing

# Register Blueprints
app.register_blueprint(medical_bp, url_prefix="/medical")

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)  # ✅ Accessible in local network  
