# import streamlit as st


# from supabase import create_client, Client

# supabase: Client = create_client(
#     SUPABASE_URL = "https://your-project-id.supabase.co"
#     SUPABASE_KEY = "your-anon-key"

# )

from supabase import create_client

SUPABASE_URL = "https://ultqgjwinmwowkcwxmpo.supabase.co"
SUPABASE_KEY = "sb_publishable_koh7aLEpmgwXKSL_MclJyA_oR2quZrA"

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)