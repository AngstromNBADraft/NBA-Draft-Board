import streamlit as st
import pandas as pd

# Function to add banner with text logo and white NBA DRAFT text
def add_banner():
    # First inject the CSS styles
    st.markdown("""
    <style>
    * {
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif;
    }
.main-container,
.who-we-are,
.big-board-title,
.table-container,
.table-header,
.player-row,
.player-details,
.footer,
[data-testid="stExpander"] {
    max-width: 950px !important;
    width: 950px !important;
    margin-left: -20px !important;  /* Negative value to pull content left */
    margin-right: auto !important;
}

/* Also adjust the app container */
[data-testid="stAppViewContainer"] > div:first-child {
    max-width: 950px !important;
    margin-left: -20px !important;  /* Negative value to pull content left */
    margin-right: auto !important;
}

/* Make sure the block container is also shifted left */
.block-container {
    max-width: 950px !important;
    padding-left: 0 !important;
    padding-right: 0 !important;
    margin-left: -20px !important;  /* Negative value to pull content left */

}

/* Adjust the main container */
.main-container {
    max-width: 950px !important;
    width: 950px !important;
    margin-left: -20px !important;  /* Negative value to pull content left */
    margin-right: auto !important;
    padding: 0 !important;
    box-sizing: border-box !important;
    position: relative !important;

}
/* Make sure all elements align properly */
.big-board-title {
    margin-top: 20px !important;
}
    
    .banner-container {
        position: fixed;
        top: 0;
        left: 0;
        right: 0;
        height: 60px;
        background: #0E1726;
        z-index: 9999;
        display: flex;
        align-items: center;
        justify-content: space-between;
        padding: 0 24px;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
    }
    
    .angstrom-logo {
        height: 40px;
        object-fit: contain;
    }
    
    .banner-text-main {
        font-weight: 700;
        font-size: 20px;
        letter-spacing: 1.5px;
        color: white;
        text-transform: uppercase;
    }
    
    .banner-subtitle {
        font-size: 14px;
        letter-spacing: normal;
        color: #B0B7C3;
        margin-left: 8px;
        text-transform: uppercase;
    }
    
    /* Adjust main content to not be hidden behind banner */
    [data-testid="stHeader"] {
        visibility: hidden;
    }
    
    [data-testid="stAppViewContainer"] {
        margin-top: 60px;
        padding-top: 0 !important;
    }
    
    section[data-testid="stSidebar"] {
        margin-top: 60px;
    }
    
    /* Main container for the entire app content */
    .main-container {
        max-width: 950px !important;
        width: 950px !important;
        margin: 0 auto !important;
        padding: 0 !important;
        box-sizing: border-box !important;
        position: relative !important;
    }
    
    /* Make sure Streamlit containers respect our width */
    [data-testid="stAppViewContainer"] > div:first-child {
        max-width: 950px !important;
        margin: 0 auto !important;
    }
    
    /* Override Streamlit's default layout */
    .block-container {
        max-width: 950px !important;
        padding-left: 0 !important;
        padding-right: 0 !important;
    }
    
    /* Fixed width container for the entire table */
    .table-container {
        width: 950px !important;
        margin: 0 auto !important;
        overflow-x: auto !important;
        position: relative !important;
    }
    
    /* Who We Are section styling - updated to orange */
    .who-we-are {
        background-color: #f8f9fa;
        border-left: 6px solid #FF6B00;
        padding: 12px 16px;
        margin: 0 0 20px 0;
        border-radius: 8px;
        line-height: normal;
        max-width: 950px;
        width: 100%;
        margin-left: auto;
        margin-right: auto;
    }
    
    .who-we-are h4 {
        margin: 0 0 8px 0 !important;
        padding: 0 !important;
        line-height: normal !important;
        color: #1a1f36;
        font-size: 16px;
        font-weight: 700;
    }
    
    .who-we-are p {
        margin: 0 !important;
        padding: 0 !important;
        color: #4a5568;
        font-size: 14px;
        line-height: 1.4;
    }
    
    /* Modern table styling - updated to orange */
    .big-board-title {
        font-size: 28px;
        font-weight: 800;
        color: #0E1726;
        letter-spacing: 1px;
        margin-bottom: 0px !important;
        text-transform: uppercase;
        border-bottom: 3px solid #FF6B00;
        padding-bottom: 8px;
        max-width: 950px;
        width: 100%;
        margin-left: auto;
        margin-right: auto;
    }
    
    /* Table header styling */
    .table-header {
        display: flex;
        align-items: center;
        background-color: #0E1726;
        color: white;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 0.5px;
        font-size: 13px;
        padding: 10px 0;
        border-radius: 4px 4px 0 0;
        margin-bottom: 0 !important; /* Remove margin */
        width: 950px !important; /* Fixed width */
        box-sizing: border-box !important;
    }
    
    /* Make sure header cells align with content cells */
    .table-header .player-cell {
        padding: 0 8px;
        box-sizing: border-box !important;
    }

    /* Make ONLY the rank header orange */
    .table-header .rank-cell {
        color: #FF6B00 !important;
    }

    /* All other headers white */
    .table-header .player-cell:not(.rank-cell) {
        color: white !important;
    }
    
    .player-row {
        display: flex;
        align-items: center;
        padding: 5px 0;
        border-bottom: 2px solid #eaeaea;
        transition: all 0.2s ease;
        height: 45px !important; /* Reduced height for more compact rows */
        margin: 0; /* Remove any margin */
        width: 950px !important; /* Fixed width matching header */

    }
    
    .player-row:hover {
        background-color: #c8cad2;
    }
    
    .player-row.expanded {
        background-color: #FFF5EE; /* Light orange background for expanded row */
    }
    
    .player-cell {
        padding: 0 8px;
        font-size: 14px;
        text-transform: uppercase;
        font-weight: 500;
        color: #333;
        box-sizing: border-box !important;
    }
    
    /* Fixed column widths for perfect alignment */
    .rank-cell {
        width: 50px !important;
        min-width: 50px !important;
        max-width: 50px !important;
        text-align: center;
        font-weight: 700;
        color: #FF6B00;
        box-sizing: border-box !important;
    }
    
    .name-cell {
        width: 200px !important;
        min-width: 200px !important;
        max-width: 200px !important;
        font-weight: 700;
        letter-spacing: 0.5px;
        box-sizing: border-box !important;
    }
    
    .pos-cell, .height-cell {
        width: 45px !important;
        min-width: 45px !important;
        max-width: 45px !important;
        text-align: center;
        color: #555;
        box-sizing: border-box !important;
    }
    
    .school-cell {
        width: 130px !important;
        min-width: 130px !important;
        max-width: 130px !important;
        text-align: center;
        box-sizing: border-box !important;
    }
    
    .age-cell {
        width: 45px !important;
        min-width: 45px !important;
        max-width: 45px !important;
        text-align: center;
        box-sizing: border-box !important;
    }
    
    .stat-cell {
        width: 45px !important;
        min-width: 45px !important;
        max-width: 45px !important;
        text-align: center;
        font-size: 13px;
        box-sizing: border-box !important;
    }
    
    .arrow-cell {
        width: 30px !important;
        min-width: 30px !important;
        max-width: 30px !important;
        text-align: center;
        box-sizing: border-box !important;
        border-right: 2px solid #eaeaea;
    }
    
    div[data-testid="stButton"] button {
    background: #FF6B00 !important;
    color: white !important;
    border: none !important;
    border-radius: 4px !important;
    min-width: 30px !important;     /* Using min-width instead of width */
    min-height: 12px !important;     /* Using min-height */
    padding: 1px !important;        /* Reduced padding */
    display: flex !important;
    align-items: center !important;
    justify-content: center !important;
    font-weight: bold !important;
    transition: all 0.2s ease !important;
    margin: 6px 0 2px 0 !important;
    font-size: 12px !important;      /* Even smaller font */
    position: absolute !important;
    right: -5px !important;
    line-height: 1.75 !important;      /* Added to reduce height */
    overflow: hidden !important;    /* Ensures content doesn't expand button */
}
    
    div[data-testid="stButton"] button:hover {
        background: #E05E00 !important;
        transform: scale(1.1) !important;
    }
    
    /* Adjust button vertical alignment */
    [data-testid="column"]:last-child {
        display: flex !important;
        align-items: center !important;
        justify-content: center !important;
    }
    
    /* Hide the button label */
    div[data-testid="stButton"] button p {
        margin: 0 !important;
        padding: 0 !important;
    }
    
    /* Fix column alignment and spacing */
    [data-testid="column"]:first-child {
        padding-right: 0 !important;
    }
    
    [data-testid="column"]:last-child {
        padding-left: 0 !important;
    }
    
    /* More compact spacing for the expanded details */
    .player-details {
        padding: 16px;
        background-color: #FFF9F5; /* Very light orange background */
        border-radius: 0 0 4px 4px;
        margin-bottom: 10px;
        border-left: 4px solid #FF6B00;
        animation: fadeIn 0.3s ease-in-out;
        width: 950px !important; /* Fixed width */
        margin-left: auto;
        margin-right: auto;
    }
    
    @keyframes fadeIn {
        from { opacity: 0; max-height: 0; }
        to { opacity: 1; max-height: 1000px; }
    }
    
    .player-details h3 {
        color: #0E1726;
        margin-top: 0 !important;
        border-bottom: 2px solid #FFE5D3; /* Light orange border */
        padding-bottom: 8px;
    }
    
    .player-details h4 {
        color: #2D3748;
        margin: 12px 0 8px 0 !important;
    }
    
    .player-details ul {
        margin-top: 4px;
    }
    
    .player-details li {
        margin-bottom: 4px;
    }
    
    /* Adjust metric bars */
    .metric-container {
        margin-bottom: 8px;
    }
    
    .metric-container div {
        height: 8px !important;
    }
    
    /* Hide Streamlit elements we don't want */
    .stButton>button {
        font-size: 12px !important;
    }
    
    /* Container for the button to make it align better */
    .button-container {
        display: flex;
        justify-content: center;
        align-items: center;
    }
    
    /* Footer styling */
    .footer {
        max-width: 950px;
        width: 100%;
        margin: 10px auto;
        text-align: right;
        font-size: 12px;
        color: #666;
    }
# Add this to your CSS section



    </style>
    """, unsafe_allow_html=True)
    
    # Then inject the banner HTML separately
    st.markdown("""
    <div class="banner-container">
        <img src="https://workable-application-form.s3.amazonaws.com/advanced/production/61680297d9510741dcbe0421/367aeef4-3d61-441e-b77f-6d99a5ac26f9" 
             alt="Angstrom Sports" 
             class="angstrom-logo">
        <div>
            <span class="banner-text-main">NBA DRAFT</span>
            <span class="banner-subtitle">BIG BOARD</span>
        </div>
    </div>
    """, unsafe_allow_html=True)


def add_who_we_are_pure_streamlit():
    # Style the container to look like the original
    st.markdown("""
    <style>
    /* Style for the container */
    [data-testid="stExpander"] {
        border-left: 6px solid #FF6B00 !important;
        border-radius: 8px !important;
        background-color: #f8f9fa !important;
        max-width: 950px !important;
        width: 950px !important;
        margin-left: -20px !important;
        margin-right: auto !important;
        margin-top: -160px !important;
        margin-bottom: -10px !important;
    }
    
    /* Style for the expander header */
    [data-testid="stExpander"] > div:first-child {
        border-radius: 8px !important;
        background-color: #f8f9fa !important;
        width: 100% !important;
    }
    
    /* Style for the expander content */
    [data-testid="stExpander"] > div:nth-child(2) {
        background-color: #f8f9fa !important;
        border-radius: 0 0 8px 8px !important;
        width: 100% !important;
    }
    
    /* Text styling */
    [data-testid="stExpander"] p {
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif !important;
        font-size: 13px !important;
        line-height: 1.4 !important;
        color: #4a5568 !important;
    }
    
    /* Label styling */
    [data-testid="stExpander"] label {
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif !important;
        font-size: 15px !important;
        font-weight: 700 !important;
        color: #1a1f36 !important;
    }

    </style>
    """, unsafe_allow_html=True)
    
    # Simply use the built-in expander component
    with st.expander("About Angstrom Sports Forecasting"):
        st.markdown("""
        Angstrom Sports is a cutting-edge sports analytics company specializing in advanced metrics and player evaluation tools. 
        Our team combines expertise in data science, sports scouting, and machine learning to deliver unparalleled insights into player potential and performance. 
        This NBA Draft Big Board represents our comprehensive analysis of the top prospects in this year's draft class from NCAA prospects only.
        """)

# Set up the page configuration
st.set_page_config(
    page_title="NBA Draft Big Board",
    page_icon="🏀",
    layout="centered"  # Use centered layout for better control
)

# Add the banner
add_banner()

# Force the container width for the entire app
st.markdown("""
<style>
    /* Force Streamlit to use our container width */
    .main-container {
        max-width: 900px !important;
        width: 900px !important;
        margin: 0 auto !important;
        padding: 0 !important;
        position: relative !important;
    }
    
    section[data-testid="stSidebar"] {
        display: none !important;
    }
    
    [data-testid="stHeader"] {
        display: none !important;
    }
    
    .block-container {
        max-width: 900px !important;
        padding-left: 0 !important;
        padding-right: 0 !important;
    }
    
    /* Button container positioning fix */
    [data-testid="column"]:last-child {
        position: relative !important;
    }
    
    /* Position the button container correctly */
    [data-testid="column"]:last-child > div {
        position: absolute !important;
        right: 0 !important;
        top: 0 !important;
    }
</style>
""", unsafe_allow_html=True)

# Main content wrapper with fixed width container
st.markdown('<div class="main-container">', unsafe_allow_html=True)

# Add Who We Are section
add_who_we_are_pure_streamlit()

# Function to get draft data
def get_draft_data():
    data = {
        'Rank': list(range(1, 34)),
        'Name': [
            "COOPER FLAGG", "DYLAN HARPER", "ACE BAILEY", "VJ EDGECOMBE",
            "KASPARAS JAKUCIONIS", "KHAMAN MALUACH", "KON KNUEPPEL", "TRE JOHNSON",
            "DERIK QUEEN", "JEREMIAH FEARS", "JASE RICHARDSON", "ASA NEWELL",
            "EGOR DEMIN", "COLLIN MURRAY-BOYLES", "LIAM MCNEELEY", "THOMAS SORBER",
            "RASHEER FLEMING", "DANNY WOLF", "WILL RILEY", "YAXEL LENDEBORG",
            "NIQUE CLIFFORD", "ALEX CONDON", "LABARON PHILON", "KAM JONES",
            "JOHNI BROOME", "ADOU THIERO", "BOOGIE FLAND", "JT TOPPIN",
            "CARTER BRYANT", "ALEX KARABAN", "MILES BYRD", "RYAN KALKBRENNER",
            "ISAIAH EVANS"
        ],
        'Position': [
            "WING", "GUARD", "WING", "GUARD", "GUARD", "CENTER", "WING", "GUARD",
            "CENTER", "GUARD", "GUARD", "WING", "GUARD", "WING", "WING", "CENTER",
            "WING", "CENTER", "WING", "WING", "GUARD", "CENTER", "GUARD", "GUARD",
            "CENTER", "WING", "GUARD", "WING", "WING", "WING", "GUARD", "CENTER",
            "WING"
        ],
        'Height': [
            "6'10\"", "6'5\"", "6'9\"", "6'5\"", "6'6\"", "7'2\"", "6'7\"", "6'6\"",
            "6'10\"", "6'4\"", "6'3\"", "6'10\"", "6'9\"", "6'7\"", "6'8\"", "6'10\"",
            "6'9\"", "7'0\"", "6'8\"", "6'9\"", "6'6\"", "6'11\"", "6'4\"", "6'5\"",
            "6'10\"", "6'8\"", "6'2\"", "6'9\"", "6'8\"", "6'8\"", "6'7\"", "7'2\"",
            "6'6\""
        ],
        'School': [
            "DUKE", "RUTGERS", "RUTGERS", "BAYLOR", "ILLINOIS", "DUKE", "DUKE", "TEXAS",
            "MARYLAND", "OKLAHOMA", "MICHIGAN STATE", "GEORGIA", "BYU", "SOUTH CAROLINA",
            "UCONN", "GEORGETOWN", "SAINT JOSEPH'S", "MICHIGAN", "ILLINOIS", "UAB",
            "COLORADO STATE", "FLORIDA", "ALABAMA", "MARQUETTE", "AUBURN", "ARKANSAS",
            "ARKANSAS", "TEXAS TECH", "ARIZONA", "UCONN", "SAN DIEGO STATE", "CREIGHTON",
            "DUKE"
        ],
        'Age': [
            18.3, 18.9, 18.5, 18.8, 19.1, 18.8, 19.9, 19.3, 20.5, 18.7, 18.7, 19.7,
            19.3, 20.0, 19.7, 19.5, 20.9, 21.1, 19.4, 22.7, 23.4, 20.9, 19.6, 23.3,
            22.9, 21.1, 18.9, 20.0, 19.6, 22.6, 20.8, 23.4, 19.5
        ],
        'OPTS': [
            25.3, 22.1, 20.8, 18.5, 17.2, 14.8, 16.7, 19.1, 15.3, 18.9, 16.4, 14.2,
            15.7, 13.9, 12.8, 11.5, 14.1, 12.3, 15.6, 13.4, 16.8, 11.7, 17.3, 19.5,
            18.2, 15.1, 16.4, 14.7, 13.9, 14.3, 15.2, 16.1, 17.0
        ],
        'OREB': [
            3.2, 2.8, 3.5, 2.1, 1.8, 4.2, 2.3, 2.0, 3.8, 1.5, 1.9, 3.1, 2.2, 2.7,
            2.1, 3.5, 2.9, 3.2, 2.0, 3.3, 2.1, 3.6, 1.4, 1.8, 4.1, 2.8, 1.3, 3.2,
            2.7, 2.3, 1.9, 3.8, 2.1
        ],
        'OTO': [
            2.1, 3.2, 2.8, 2.9, 2.5, 1.8, 2.3, 3.1, 2.4, 3.3, 2.0, 2.6, 2.9, 2.1,
            2.7, 2.3, 2.5, 1.9, 2.8, 2.2, 2.3, 2.0, 2.9, 2.4, 1.7, 2.5, 3.0, 2.1,
            2.4, 2.2, 2.3, 1.5, 2.6
        ],
        'OFOUL': [
            1.8, 2.2, 1.9, 2.4, 2.1, 2.8, 1.7, 2.3, 3.1, 2.5, 1.9, 2.4, 2.2, 2.0,
            1.8, 2.9, 2.3, 2.7, 2.1, 2.6, 1.9, 2.8, 2.3, 2.0, 3.2, 2.4, 2.7, 2.3,
            2.0, 2.1, 1.8, 2.9, 2.2
        ],
        'DPTS': [
            12.3, 14.1, 11.8, 15.5, 13.2, 9.8, 12.7, 14.3, 10.5, 13.9, 11.4, 10.2,
            12.7, 9.9, 11.8, 8.5, 10.1, 9.3, 12.6, 10.4, 13.8, 8.7, 14.3, 16.5,
            15.2, 12.1, 13.4, 11.7, 10.9, 11.3, 12.2, 13.1, 14.0
        ],
        'DREB': [
            8.2, 6.8, 7.5, 5.1, 4.8, 9.2, 5.3, 5.0, 8.8, 4.5, 4.9, 7.1, 5.2, 6.7,
            5.1, 8.5, 6.9, 7.2, 5.0, 7.3, 5.1, 8.6, 4.4, 4.8, 9.1, 6.8, 4.3, 7.2,
            6.7, 5.3, 4.9, 8.8, 5.1
        ],
        'DTO': [
            1.1, 1.2, 0.8, 1.9, 1.5, 0.8, 1.3, 1.1, 1.4, 1.3, 1.0, 1.6, 1.9, 1.1,
            1.7, 1.3, 1.5, 0.9, 1.8, 1.2, 1.3, 1.0, 1.9, 1.4, 0.7, 1.5, 2.0, 1.1,
            1.4, 1.2, 1.3, 0.5, 1.6
        ],
        'DFOUL': [
            2.8, 3.2, 2.9, 3.4, 3.1, 3.8, 2.7, 3.3, 4.1, 3.5, 2.9, 3.4, 3.2, 3.0,
            2.8, 3.9, 3.3, 3.7, 3.1, 3.6, 2.9, 3.8, 3.3, 3.0, 4.2, 3.4, 3.7, 3.3,
            3.0, 3.1, 2.8, 3.9, 3.2
        ]
    }
    return pd.DataFrame(data)

# Function to get player details - placeholder details for now
def get_player_details(player_name):
    return {
        "strengths": ["Elite scoring ability", "Defensive versatility", "High basketball IQ"],
        "weaknesses": ["Needs to improve free throw shooting", "Can be turnover prone in transition"],
        "scouting": "Shows excellent potential as a two-way player with room to develop as a playmaker. Has shown steady improvement throughout the season."
    }

# Get the data
df = get_draft_data()

# Store expanded player state in session state
if 'expanded_player' not in st.session_state:
    st.session_state.expanded_player = None

# Initialize button keys in session state if not present
if 'button_keys' not in st.session_state:
    st.session_state.button_keys = {name: f"btn_{i}" for i, name in enumerate(df['Name'])}

# Create title and filter section with default Streamlit styling
st.markdown("""
<style>
    /* Title styling */
    .big-board-title {
        font-size: 28px;
        font-weight: 800;
        color: #0E1726;
        letter-spacing: 1px;
        margin-bottom: 0 !important;
        text-transform: uppercase;
        padding-bottom: 8px;
        border-bottom: 3px solid #FF6B00;
        width: 950px !important;
    }
    
    /* Just minimal adjustments to position the filter */
    .stSelectbox {
        margin-top: 25px !important;
        width: 200px !important;
    }
</style>
""", unsafe_allow_html=True)

# Create the title and filter row
title_container = st.container()
with title_container:
    col1, col2 = st.columns([0.8, 0.2])
    
    with col1:
        st.markdown('<div class="big-board-title">2025 NBA DRAFT BIG BOARD</div>', unsafe_allow_html=True)
    
    with col2:
        all_positions = ['ALL'] + sorted(df['Position'].unique().tolist())
        selected_position = st.selectbox(
            "Filter by Position",
            all_positions,
            index=0,
            key="position_filter",
            label_visibility="collapsed"
        )

# Apply filter
if selected_position != 'ALL':
    df = df[df['Position'] == selected_position]

# Filter the dataframe if a specific position is selected
if selected_position != 'ALL':
    df = df[df['Position'] == selected_position]

# Wrap the table in a fixed-width container
st.markdown('<div class="table-container">', unsafe_allow_html=True)

# Table header with fixed width and aligned cells
st.markdown("""
<div class="table-header">
    <div class="player-cell rank-cell">RANK</div>
    <div class="player-cell name-cell">NAME</div>
    <div class="player-cell pos-cell">POS</div>
    <div class="player-cell height-cell">HT</div>
    <div class="player-cell school-cell">SCHOOL</div>
    <div class="player-cell age-cell">AGE</div>
    <div class="player-cell stat-cell">OPTS</div>
    <div class="player-cell stat-cell">OREB</div>
    <div class="player-cell stat-cell">OTO</div>
    <div class="player-cell stat-cell">OFL</div>
    <div class="player-cell stat-cell">DPTS</div>
    <div class="player-cell stat-cell">DREB</div>
    <div class="player-cell stat-cell">DTO</div>
    <div class="player-cell stat-cell">DFL</div>
    <div class="player-cell stat-cell"></div>
    <div class="player-cell arrow-cell"></div>
</div>
""", unsafe_allow_html=True)

# Function to toggle player expansion
def toggle_player(player_name):
    if st.session_state.expanded_player == player_name:
        st.session_state.expanded_player = None
    else:
        st.session_state.expanded_player = player_name

# Function to create the accordion-style toggle (more professional)
def create_player_row(player, expanded):
    row_class = "player-row expanded" if expanded else "player-row"
    
    # Write player row HTML - fixed width
    html = f"""
    <div class="{row_class}">
        <div class="player-cell rank-cell">{player['Rank']}</div>
        <div class="player-cell name-cell">{player['Name']}</div>
        <div class="player-cell pos-cell">{player['Position']}</div>
        <div class="player-cell height-cell">{player['Height']}</div>
        <div class="player-cell school-cell">{player['School']}</div>
        <div class="player-cell age-cell">{player['Age']}</div>
        <div class="player-cell stat-cell">{player['OPTS']}</div>
        <div class="player-cell stat-cell">{player['OREB']}</div>
        <div class="player-cell stat-cell">{player['OTO']}</div>
        <div class="player-cell stat-cell">{player['OFOUL']}</div>
        <div class="player-cell stat-cell">{player['DPTS']}</div>
        <div class="player-cell stat-cell">{player['DREB']}</div>
        <div class="player-cell stat-cell">{player['DTO']}</div>
        <div class="player-cell stat-cell">{player['DFOUL']}</div>
        <div class="player-cell stat-cell"></div>
    </div>
    """
    
    # If expanded, also return the expanded content with new professional design
    if expanded:
        # Generate mock data for the new sections
        biometrics = {
            "Height": player['Height'],
            "Weight": f"{180 + player['Rank'] % 40} lbs",
            "Wingspan": f"{6 + (player['Rank'] % 3)}'{ 8 + (player['Rank'] % 4)}\"",
            "Standing Reach": f"{8 + (player['Rank'] % 2)}'{ 2 + (player['Rank'] % 6)}\"",
            "Vertical": f"{30 + (player['Rank'] % 15)} inches"
        }
        
        comparisons = [
            f"NBA: {['Jayson Tatum', 'Luka Doncic', 'Anthony Edwards', 'Jalen Green', 'Cade Cunningham'][player['Rank'] % 5]}",
            f"Historical: {['Michael Jordan', 'Kobe Bryant', 'LeBron James', 'Kevin Durant', 'Stephen Curry'][player['Rank'] % 5]}",
            f"Ceiling: {['All-Star', 'All-NBA', 'MVP Candidate', 'Franchise Player', 'Role Player'][player['Rank'] % 5]}",
            f"Floor: {['Rotation Player', 'Bench Scorer', 'Defensive Specialist', 'Two-Way Player', 'Development Project'][player['Rank'] % 5]}"
        ]
        
        position_ranks = [
            f"2024: #{1 + (player['Rank'] % 5)} {player['Position']}",
            f"2023: #{1 + (player['Rank'] % 7)} {player['Position']}",
            f"2022: #{1 + (player['Rank'] % 6)} {player['Position']}",
            f"2021: #{1 + (player['Rank'] % 8)} {player['Position']}",
            f"2020: #{1 + (player['Rank'] % 4)} {player['Position']}"
        ]
        
        # Create the biometrics HTML
        biometrics_html = ""
        for key, value in biometrics.items():
            biometrics_html += f'<div class="biometric-item"><span class="biometric-label">{key}:</span> <span class="biometric-value">{value}</span></div>'
        
        # Create the comparisons HTML
        comparisons_html = ""
        for comp in comparisons:
            comparisons_html += f'<li>{comp}</li>'
        
        # Create the position ranks HTML
        ranks_html = ""
        for rank in position_ranks:
            ranks_html += f'<li>{rank}</li>'
        
        # Create the expanded content HTML
        expanded_html = f"""
        <style>
        .player-details {{
            padding: 24px;
            background-color: white;
            border-radius: 0 0 8px 8px;
            margin-bottom: 16px;
            border-left: 4px solid #FF6B00;
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.05);
            width: 950px !important;
            margin-left: auto;
            margin-right: auto;
        }}
        
        .player-profile-header {{
            display: flex;
            align-items: center;
            margin-bottom: 24px;
            border-bottom: 1px solid #eaeaea;
            padding-bottom: 20px;
        }}
        
        .player-image-container {{
            width: 120px;
            height: 120px;
            border-radius: 8px;
            overflow: hidden;
            margin-right: 24px;
            border: 2px solid #FF6B00;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        }}
        
        .player-image {{
            width: 100%;
            height: 100%;
            object-fit: cover;
        }}
        
        .player-header-info {{
            flex: 1;
            position: relative;
        }}
        
        .player-header-info h2 {{
            margin: 0 0 8px 0;
            font-size: 28px;
            font-weight: 800;
            color: #0E1726;
            letter-spacing: 0.5px;
        }}
        
        .player-subheader {{
            font-size: 16px;
            color: #555;
            margin-bottom: 12px;
        }}
        
        .player-rank-badge {{
            display: inline-block;
            background: #FF6B00;
            color: white;
            padding: 6px 12px;
            border-radius: 4px;
            font-weight: 700;
            font-size: 14px;
            letter-spacing: 1px;
        }}
        
        .player-details-grid {{
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 24px;
        }}
        
        .player-details-section {{
            background: #f8f9fa;
            border-radius: 8px;
            padding: 16px;
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.05);
        }}
        
        .player-details-section h3 {{
            margin: 0 0 16px 0;
            font-size: 18px;
            font-weight: 700;
            color: #0E1726;
            border-bottom: 2px solid #FF6B00;
            padding-bottom: 8px;
        }}
        
        .biometrics-grid {{
            display: grid;
            grid-template-columns: 1fr;
            gap: 8px;
        }}
        
        .biometric-item {{
            display: flex;
            justify-content: space-between;
            padding: 4px 0;
            border-bottom: 1px dashed #ddd;
        }}
        
        .biometric-label {{
            font-weight: 600;
            color: #555;
        }}
        
        .biometric-value {{
            font-weight: 700;
            color: #0E1726;
        }}
        
        .comparisons-list, .rank-history-list {{
            list-style-type: none;
            padding: 0;
            margin: 0;
        }}
        
        .comparisons-list li, .rank-history-list li {{
            padding: 8px 0;
            border-bottom: 1px solid #eaeaea;
            font-size: 15px;
        }}
        
        .comparisons-list li:last-child, .rank-history-list li:last-child {{
            border-bottom: none;
        }}
        
        @media (max-width: 768px) {{
            .player-details-grid {{
                grid-template-columns: 1fr;
            }}
            
            .player-profile-header {{
                flex-direction: column;
                text-align: center;
            }}
            
            .player-image-container {{
                margin-right: 0;
                margin-bottom: 16px;
            }}
        }}
        </style>
        
        <div class="player-details">
            <div class="player-profile-header">
                <div class="player-image-container">
                    <img src="https://a.espncdn.com/combiner/i?img=/i/headshots/mens-college-basketball/players/full/5041939.png&w=350&h=254" 
                         alt="{player['Name']}" 
                         class="player-image">
                </div>
                <div class="player-header-info">
                    <h2>{player['Name']}</h2>
                    <div class="player-subheader">
                        <span class="player-school">{player['School']}</span> | 
                        <span class="player-position">{player['Position']}</span> | 
                        <span class="player-age">Age: {player['Age']}</span>
                    </div>
                    <div class="player-rank-badge">RANK #{player['Rank']}</div>
                </div>
            </div>
         
             
        """
        return html, expanded_html
    
    return html, ""

# Display player rows using a more optimized layout with no gaps
# Display player rows using a more optimized layout with no gaps
for idx, player in df.iterrows():
    is_expanded = st.session_state.expanded_player == player['Name']
    
    # Create the player row and get any expanded content
    row_html, expanded_html = create_player_row(player, is_expanded)
    
    # Create a container with no padding/margin
    row_container = st.container()
    
    with row_container:
        # Create a two-column layout with adjusted ratio to make player row wider
        cols = st.columns([0.97, 0.03])  # Adjust ratio to give more space for the button
        
        # First column: Player row data
        with cols[0]:
            st.markdown(row_html, unsafe_allow_html=True)
        
        # Second column: Arrow button
        with cols[1]:
            btn_text = "▲" if is_expanded else "▼"
            btn_key = st.session_state.button_keys[player['Name']]
            
            # Using on_click for the callback
            st.button(btn_text, key=btn_key, on_click=toggle_player, args=(player['Name'],))
        
        # Display expanded content if needed
        if expanded_html:
            st.markdown(expanded_html, unsafe_allow_html=True)

# Close the table container
st.markdown('</div>', unsafe_allow_html=True)

# Add footer
st.markdown('<div class="footer">DATA LAST UPDATED: APRIL 2025</div>', unsafe_allow_html=True)

# Close the main content div
st.markdown('</div>', unsafe_allow_html=True)

# Add additional padding at the bottom
st.markdown("""
<style>
    body {
        padding-bottom: 50px !important;
    }
</style>
""", unsafe_allow_html=True)