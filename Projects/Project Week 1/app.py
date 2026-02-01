import streamlit as st
import pandas as pd
from manager import CipherVault, Secret


st.set_page_config(page_title="CipherVault", page_icon="🔐")
st.title("🔐 CipherVault: Secure Password Manager")
st.markdown("Store your passwords securely with **Base64 Encryption**.")


vault = CipherVault()


with st.sidebar:
    st.header("➕ Add New Secret")
    with st.form("add_secret_form"):
        service = st.text_input("Service Name (e.g., Netflix, Gmail)")
        username = st.text_input("Username / Email")
        password = st.text_input("Password", type="password")
        
        submitted = st.form_submit_button("Save to Vault")
        
        if submitted:
            if service and username and password:
                new_secret = Secret(service, username, password)
                success, msg = vault.add_secret(new_secret)
                if success:
                    st.success(msg)
                else:
                    st.error(msg)
            else:
                st.warning("Please fill in all fields.")


st.subheader("📂 Your Secured Vault")

data = vault.get_all_secrets()

if data:
    # Convert to DataFrame
    df = pd.DataFrame(data)
    
    
    show_passwords = st.checkbox("Show Decrypted Passwords")
    
    if not show_passwords:
    
        df["Password"] = "••••••••"
    
    # Display the table
    st.dataframe(df, use_container_width=True)
    
    st.info(f"Total Secrets Stored: {len(data)}")
else:
    st.info("Vault is empty. Add your first secret from the sidebar!")


st.markdown("---")
st.caption("🔒 CipherVault stores passwords in `secrets.csv` using standard Base64 encoding.")