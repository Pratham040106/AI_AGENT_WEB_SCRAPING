import streamlit as st
import requests, html2text
from datetime import datetime

# Setup
st.set_page_config(page_title="Web Content Extractor", page_icon="📄")
st.title("📄 Web Content Extractor")

def scrape_to_markdown(url):
    try:
        response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'}, timeout=10)
        if response.ok:
            h = html2text.HTML2Text()
            h.body_width = 0
            h.ignore_images = False  # Keep images
            return h.handle(response.text)
    except Exception as e:
        st.error(f"Error: {e}")
    return None

def save_content(content, url):
    if not content: return
    filename = f"web_content_{datetime.now().strftime('%Y%m%d_%H%M%S')}.md"
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(f"# Extracted Content from {url}\n\n")
        f.write(f"## Summary\n\n{content[:500]}...\n\n")
        f.write(f"## Full Content\n\n{content}\n\n")
        f.write(f"## Conclusion\n\nKey points extracted from the page.")
    return filename

# Main App
url = st.text_input("Enter URL to extract content:")
if st.button("Extract & Save") and url:
    with st.spinner("Processing..."):
        if content := scrape_to_markdown(url):
            filename = save_content(content, url)
            st.success(f"Content saved as {filename}")
            st.download_button("Download", content, file_name=filename)
            with st.expander("Preview Content"):
                st.markdown(content[:2000] + ("..." if len(content) > 2000 else ""))
        else:
            st.error("Failed to extract content")