import threading
from server.app import app  # Adjust according to your actual import path
from gui.main import run_gui     # Import your Tkinter main function

def run_flask():
    app.run(port=5000, debug=True, use_reloader=False)  # Avoid double-starting

if __name__ == "__main__":
    flask_thread = threading.Thread(target=run_flask)
    flask_thread.start()  # Start Flask in a separate thread
    run_gui()             # Start the Tkinter GUI