from flask import Flask
from flask_cors import CORS
import sys
import os

# Ensure backend directory is in Python path
backend_path = os.path.abspath(os.path.dirname(__file__))
if backend_path not in sys.path:
    sys.path.append(backend_path)

try:
    from processing.medical_routes import medical_bp  # ✅ Importing medical routes
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
