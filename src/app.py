"""Ordinary application source file - not part of the legacy-config retirement runbook."""


def load_settings(path: str) -> dict:
    """Load current (non-legacy) application settings."""
    return {"source": path, "format": "yaml"}


def main() -> None:
    settings = load_settings("config/current-settings.yaml")
    print(f"Application booted with settings: {settings}")


if __name__ == "__main__":
    main()
