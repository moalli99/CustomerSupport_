from functools import lru_cache
from supabase import create_client,Client
from src.core.config import get_settings

@lru_cache
def get_supabase_client()->Client:
    setttings=get_settings()

    if not setttings.supabase_url:
        raise ValueError("Supabase_url is not configured")
    if not setttings.supabase_key:
        raise ValueError("supabase_key is not configured")

    return create_client(
        setttings.supabase_url,
        setttings.supabase_key.get_secret_value()
    )