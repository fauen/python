import sys
import json
from pathlib import Path

from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QHBoxLayout
from PyQt6.QtWebEngineWidgets import QWebEngineView
from PyQt6.QtWebEngineCore import QWebEngineSettings
from PyQt6.QtCore import QUrl, Qt
from PyQt6.QtGui import QShortcut, QKeySequence

CONFIG_FILE = Path(__file__).parent / "config.json"


def load_config() -> dict:
    if not CONFIG_FILE.exists():
        default = {
            "left_url": "https://example.com",
            "right_url": "https://example.com",
        }
        CONFIG_FILE.write_text(json.dumps(default, indent=2))
        print(f"Created default config at {CONFIG_FILE} — edit it to set your URLs.")
        return default
    with open(CONFIG_FILE) as f:
        return json.load(f)


def make_view(url: str) -> QWebEngineView:
    view = QWebEngineView()
    settings = view.settings()
    settings.setAttribute(QWebEngineSettings.WebAttribute.JavascriptEnabled, True)
    settings.setAttribute(QWebEngineSettings.WebAttribute.LocalStorageEnabled, True)
    settings.setAttribute(QWebEngineSettings.WebAttribute.FullScreenSupportEnabled, True)
    view.setContextMenuPolicy(Qt.ContextMenuPolicy.NoContextMenu)
    view.load(QUrl(url))
    return view


class SplitScreenWindow(QMainWindow):
    def __init__(self, left_url: str, right_url: str):
        super().__init__()

        central = QWidget()
        self.setCentralWidget(central)

        layout = QHBoxLayout(central)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)

        layout.addWidget(make_view(left_url), stretch=1)
        layout.addWidget(make_view(right_url), stretch=1)

        QShortcut(QKeySequence("Escape"), self, self.close)

        self.showFullScreen()


def main():
    config = load_config()
    app = QApplication(sys.argv)
    app.setApplicationName("SplitScreen")
    _window = SplitScreenWindow(config["left_url"], config["right_url"])
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
