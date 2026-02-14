# test_question1_e2e.py
# Functional End-to-End Test using Pytest

def login(username, password):
    if username == "admin" and password == "admin123":
        return "token123"
    return None

def view_dashboard(token):
    if token == "token123":
        return "Dashboard Loaded"
    return "Access Denied"

def test_end_to_end_user_flow():
    # Step 1: User logs in
    token = login("admin", "admin123")
    assert token is not None

    # Step 2: User accesses dashboard
    result = view_dashboard(token)
    assert result == "Dashboard Loaded"
