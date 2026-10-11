import streamlit as st
from supabase import create_client


def get_supabase_client():

    if "supabase_client" not in st.session_state:

        st.session_state.supabase_client = create_client(
            st.secrets["SUPABASE_URL"],
            st.secrets["SUPABASE_KEY"]
        )

    return st.session_state.supabase_client


def sign_up(email, password):

    client = get_supabase_client()

    response = client.auth.sign_up({
        "email": email.strip(),
        "password": password
    })

    return response


def sign_in(email, password):

    client = get_supabase_client()

    response = client.auth.sign_in_with_password({
        "email": email.strip(),
        "password": password
    })

    if response.user and response.session:

        st.session_state.auth_user = {
            "id": response.user.id,
            "email": response.user.email
        }

        return True

    return False


def sign_out():

    client = get_supabase_client()

    try:
        client.auth.sign_out()
    except Exception:
        pass

    st.session_state.pop(
        "auth_user",
        None
    )


def get_current_user():

    try:

        client = get_supabase_client()

        response = client.auth.get_user()

        if response.user:

            return {
                "id": response.user.id,
                "email": response.user.email
            }

    except Exception:
        return None

    return None



