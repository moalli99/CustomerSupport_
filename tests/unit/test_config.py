from src.core.config import get_settings

def test_default_settings():
    settings=get_settings()

    assert settings.app_name=="Customer Support AI"
    assert settings.environment=="development"
    assert settings.debug is True