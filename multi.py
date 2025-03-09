import streamlit as st

st.markdown("""
<!-- Meta Pixel Code -->
<script>
!function(f,b,e,v,n,t,s)
{if(f.fbq)return;n=f.fbq=function(){n.callMethod?
n.callMethod.apply(n,arguments):n.queue.push(arguments)};
if(!f._fbq)f._fbq=n;n.push=n;n.loaded=!0;n.version='2.0';
n.queue=[];t=b.createElement(e);t.async=!0;
t.src=v;s=b.getElementsByTagName(e)[0];
s.parentNode.insertBefore(t,s)}(window, document,'script',
'https://connect.facebook.net/en_US/fbevents.js');
fbq('init', '486407351189911');
fbq('track', 'PageView');
fbq('track', 'Contact');
</script>
<noscript><img height="1" width="1" style="display:none"
src="https://www.facebook.com/tr?id=486407351189911&ev=PageView&noscript=1"
/></noscript>
<!-- End Meta Pixel Code -->
""", unsafe_allow_html=True)

# --- SHARED ON ALL PAGES ---
st.logo("a.png")

# --- PAGE SETUP ---
beranda = st.Page(
    page="produk/Gaxee.py",
    title="Beranda",
    icon=":material/home:",
    default=True,
)
rakp = st.Page(
    page="produk/rakp.py",
    title="Rak Piring Stainless",
    icon=":material/shelves:",
)
rakm = st.Page(
    page="produk/rakm.py",
    title="Rak Organizer Susun",
    icon=":material/shelves:",
)
toples = st.Page(
    page="produk/toples.py",
    title="Toples Penyimpanan",
    icon=":material/takeout_dining:",
)
sikat = st.Page(
    page="produk/sikat.py",
    title="Sikat Electric",
    icon=":material/cleaning:",
)
senter = st.Page(
    page="produk/snter.py",
    title="Super Senter LED",
    icon=":material/highlight:",
)
toothp = st.Page(
    page="produk/toothp.py",
    title="Toothpick Otomatis",
    icon=":material/tools_flat_head:",
)
pelp = st.Page(
    page="produk/pelperas.py",
    title="X-Shape Magic Mop",
    icon=":material/mop:",
)
pels = st.Page(
    page="produk/pel2.py",
    title="Automatic Water Spray Mop",
    icon=":material/mop:",
)
vacuum = st.Page(
    page="produk/vacuum1.py",
    title="Vacuum Cleaner 3 in 1 Portable",
    icon=":material/vacuum:",
)
catatan = st.Page(
    page="produk/oalah.py",
    title="CATATAN",
    icon=":material/description:",
)
# --- NAVIGATION SETUP [WITHOUT SECTIONS] ---
# pg = st.navigation(pages=[about_page, project_1_page, project_2_page])

# --- NAVIGATION SETUP [WITH SECTIONS]---
pg = st.navigation(
    {
        "Home": [beranda],
        "Detail Produk": [rakp,rakm,toples,sikat,senter,toothp,pelp,pels,vacuum],
        "Info": [catatan]
    }
)

# --- RUN NAVIGATION ---
pg.run()
