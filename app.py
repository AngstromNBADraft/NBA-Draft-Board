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
        max-width: 900px !important; /* Reduced from 950px for better fit */
        width: 900px !important;
        margin-left: auto !important;
        margin-right: auto !important;
        box-sizing: border-box !important;
        overflow: visible !important;
    }

    /* Fix title and filter alignment */
    .big-board-title {
        font-size: 28px;
        font-weight: 800;
        color: #0E1726;
        letter-spacing: 1px;
        margin-bottom: 0px !important;
        text-transform: uppercase;
        border-bottom: 3px solid #FF6B00;
        padding-bottom: 8px;
        width: 75% !important; /* Take only 75% of the row width */
        display: inline-block !important;
        vertical-align: middle !important;
    }
    
    /* Fix filter positioning */
    .stSelectbox {
        margin-top: 0 !important;
        width: 150px !important;
        float: right !important;
        margin-right: 20px !important;
    }
    
    /* Clear float after the title/filter row */
    .filter-row:after {
        content: "";
        display: table;
        clear: both;
    }
    
    /* Make sure the About Us expander has proper width */
    [data-testid="stExpander"] {
        width: 900px !important;
        max-width: 900px !important;
        margin-left: auto !important;
        margin-right: auto !important;
        box-sizing: border-box !important;
        padding-right: 20px !important; /* Add padding to prevent right cut-off */
    }
    
    /* Fix app container width */
    [data-testid="stAppViewContainer"] > div:first-child {
        max-width: 900px !important;
        margin-left: auto !important;
        margin-right: auto !important;
    }
    
    /* Fix block container width */
    .block-container {
        max-width: 900px !important;
        padding-left: 0 !important;
        padding-right: 0 !important;
        margin-left: auto !important;
        margin-right: auto !important;
    }
    
    /* Fix dropdown container */
    div[data-baseweb="select"] {
        max-width: 220px !important;
        border: 1px solid #646E78  ;
        border-radius: 8px !important;
    }
    
    /* Ensure dropdown menu doesn't get cut off */
    div[data-baseweb="popover"] {
        z-index: 1000 !important;
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
.stApp {
    background: #E5E8ED    !important; /* Same blue background as the first app */
}

/* Update the app container to match the styling */
[data-testid="stAppViewContainer"] {
    max-width: 950px !important;
    background: white !important; /* Light gray background for content area */
    padding: .5rem !important;
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1) !important;
border-left: 1px solid #FF6B00;
border-right: 1px solid #FF6B00;
    margin: 0 auto !important;
    margin-top: 60px !important; /* Adjusted for the existing header */
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
        padding-bottom: 0px;
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
        margin-top: -10px !important;
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
        font-size: 13px;
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
        width: 210px !important;
        min-width: 210px !important;
        max-width: 210px !important;
        font-weight: 700;
        letter-spacing: 0.5px;
        box-sizing: border-box !important;
    }
    
    .pos-cell {
    width: 50px !important;
    min-width: 50px !important;
    max-width: 50px !important;
    text-align: left;
    color: #555;
    box-sizing: border-box !important;
    margin-right: 20px !important;
}

.height-cell {
    width: 50px !important;
    min-width: 50px !important;
    max-width: 50px !important;
    text-align: center;
    color: #555;
    box-sizing: border-box !important;
}
    
    .school-cell {
        width: 135px !important;
        min-width: 135px !important;
        max-width: 135px !important;
        text-align: center;
        box-sizing: border-box !important;
border-right: 2px solid #eaeaea;
    }
    
    .age-cell {
        width: 50px !important;
        min-width: 50px !important;
        max-width: 50px !important;
        text-align: center;
        box-sizing: border-box !important;

    }
    
    .stat-cell {
        width: 50px !important;
        min-width: 50px !important;
        max-width: 50px !important;
        text-align: center;
        font-size: 13px;
        box-sizing: border-box !important;
border-right: 2px solid #eaeaea;
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
    right: 0px !important;
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
    border-radius: 12px !important;
    background-color: #f8f9fa !important;
    max-width: 900px !important; /* Match the width of other components */
    width: 900px !important;
    margin-left: auto !important;
    margin-right: auto !important;
    margin-top: -160px !important;
    margin-bottom: -10px !important;
    box-sizing: border-box !important;
    padding-right: 0px !important; /* Remove extra padding */
}

/* Style for the expander header */
[data-testid="stExpander"] > div:first-child {
    border-radius: 12px !important;
    background-color: #f8f9fa !important;
    width: 100% !important;
    box-sizing: border-box !important;
}
    
    /* Style for the expander header */
    [data-testid="stExpander"] > div:first-child {
        border-radius: 6px !important;
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
        max-width: 950px !important;
        width: 950px !important;
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
        border-bottom: 5px solid #FF6B00;
        width: 900px !important;
    }
    
    /* Just minimal adjustments to position the filter */
    .stSelectbox {
        margin-top: 0px !important;
        width: 220px !important;
        margin-right: -2px !important;

    }
</style>
""", unsafe_allow_html=True)

# Create the title and filter row
# Create the title and filter row
title_container = st.container()
with title_container:
    st.markdown('<div class="filter-row">', unsafe_allow_html=True)
    col1, col2 = st.columns([0.85, 0.15])
    
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
    st.markdown('</div>', unsafe_allow_html=True)

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
    <div class="player-cell age-cell">AGE</div>
    <div class="player-cell school-cell">SCHOOL</div>
    <div class="player-cell stat-cell">OPTS</div>
    <div class="player-cell stat-cell">OREB</div>
    <div class="player-cell stat-cell">OTO</div>
    <div class="player-cell stat-cell">DPTS</div>
    <div class="player-cell stat-cell">DREB</div>
    <div class="player-cell stat-cell">DTO</div>
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

def create_player_row(player, expanded):
    row_class = "player-row expanded" if expanded else "player-row"
    
    # Write player row HTML - fixed width
    html = f"""
    <div class="{row_class}">
        <div class="player-cell rank-cell">{player['Rank']}</div>
        <div class="player-cell name-cell">{player['Name']}</div>
        <div class="player-cell pos-cell">{player['Position']}</div>
        <div class="player-cell height-cell">{player['Height']}</div>
        <div class="player-cell age-cell">{player['Age']}</div>
        <div class="player-cell school-cell">{player['School']}</div>
        <div class="player-cell stat-cell">{player['OPTS']}</div>
        <div class="player-cell stat-cell">{player['OREB']}</div>
        <div class="player-cell stat-cell">{player['OTO']}</div>
        <div class="player-cell stat-cell">{player['DPTS']}</div>
        <div class="player-cell stat-cell">{player['DREB']}</div>
        <div class="player-cell stat-cell">{player['DTO']}</div>
        <div class="player-cell stat-cell"></div>
    </div>
    """
    
    # If expanded, also return the expanded content with new professional design
    if expanded:
        # Generate a minimal HTML container for the expanded content
        expanded_html = f'''
        <div style="padding: 10px; background-color: #f8f9fa; border-radius: 8px; margin-bottom: 16px; border-left: 4px solid #FF6B00;">
            <!-- Placeholder for Streamlit components -->
        </div>
        '''
        
        # Return the basic HTML for the row and the expanded content
        return html, expanded_html
    
    return html, ""

# Add this new function to handle the expanded details with Streamlit's native components
import streamlit as st
# Fix for the SyntaxError

def display_expanded_player_details(player):
    # Apply custom CSS to make things more professional
    st.markdown("""
    <style>
    .section-title {
        color: #0E1726;
        font-size: 18px;
        font-weight: 700;
        margin-bottom: 15px;
        border-bottom: 2px solid #FF6B00;
        padding-bottom: 8px;
    }
    
    .comparison-item {
        padding: 10px 0;
        border-bottom: 1px solid #eaeaea;
        font-size: 15px;
    }
    
    .comparison-item:last-child {
        border-bottom: none;
    }
    
    .highlighted-rank {
        color: #FF6B00;
        font-weight: 700;
    }
    
    .rating-container {
        margin-bottom: 16px;
    }
    
    .rating-label {
        display: flex;
        justify-content: space-between;
        font-weight: 600;
        margin-bottom: 4px;
    }
    
    .rating-value {
        color: #FF6B00;
    }
    
    /* Style the Streamlit progress bar - override default styles */
    div.stProgress > div > div {
        background-color: #FF6B00;
    }
    
    .player-header {
        margin-bottom: 25px;
    }
    
    .player-name {
        font-size: 32px;
        font-weight: 800;
        margin: 0;
        color: #0E1726;
    }
    
    .player-subheader {
        font-size: 16px;
        color: #555;
    }
    
    .rank-badge {
        color: #FF6B00;
        font-weight: 700;
        font-size: 18px;
    }
    </style>
    """, unsafe_allow_html=True)
    
    
    # Create a row with 4 columns
    col_img, col_bio, col_comp, col_rank, col_rating = st.columns([1, 1.2, 1, 1, 1])
    
    with col_img:
        # Player image
        st.image("https://a.espncdn.com/combiner/i?img=/i/headshots/mens-college-basketball/players/full/5041939.png&w=350&h=254", 
                use_container_width=True)
        
        # Player name under image
        st.markdown(f"<div style='text-align: center; font-weight: bold; font-size: 18px; margin-top: 10px;'>{player['Name']}</div>", 
                   unsafe_allow_html=True)

    
    with col_bio:
        # Biometrics section with horizontal bars - more compact
        st.markdown('<h4 style="color: #0E1726; font-weight: 700; margin-bottom: 10px; border-bottom: 2px solid #FF6B00; padding-bottom: 5px;">Biometrics</h4>', unsafe_allow_html=True)
        biometrics = {
            "Height": {"value": player['Height'], "percentile": 89, "display": player['Height']},
            "Weight": {"value": f"{180 + player['Rank'] % 40} lbs", "percentile": 72, "display": f"{180 + player['Rank'] % 40} lbs"},
            "Wingspan": {"value": f"{6 + (player['Rank'] % 3)}'{ 8 + (player['Rank'] % 4)}\"", "percentile": 94, "display": f"{6 + (player['Rank'] % 3)}'{ 8 + (player['Rank'] % 4)}\""},
            "Standing Reach": {"value": f"{8 + (player['Rank'] % 2)}'{ 2 + (player['Rank'] % 6)}\"", "percentile": 87, "display": f"{8 + (player['Rank'] % 2)}'{ 2 + (player['Rank'] % 6)}\""},
            "Vertical": {"value": f"{30 + (player['Rank'] % 15)} inches", "percentile": 81, "display": f"{30 + (player['Rank'] % 15)} in"}
        }
        
        for key, data in biometrics.items():
            # Get the percentile
            percentile = data["percentile"]
            
            # Calculate color based on percentile
            # Blue for all (matching the image provided)
            color = f"rgb(107, 124, 180)"  # Blue
            
            # Create the metric visualization - more compact
            st.markdown(f"""
            <div style="margin-bottom: 8px;">
                <div style="display: flex; justify-content: space-between; margin-bottom: 2px;">
                    <span style="font-weight: 600; color: #555; font-size: 14px;">{key}</span>
                    <span style="font-weight: 700; color: #333; font-size: 14px;">{data['display']}</span>
                </div>
                <div style="height: 18px; background-color: #e0e0e0; border-radius: 4px; position: relative;">
                    <div style="position: absolute; left: 5px; top: 1px; font-size: 11px; font-weight: 600; color: white; z-index: 2;">{percentile}</div>
                    <div style="width: {percentile}%; height: 100%; background-color: {color}; border-radius: 4px;"></div>
                </div>
            </div>
            """, unsafe_allow_html=True)
    
    with col_comp:
        # Player Comparisons - more compact
        st.markdown('<h4 style="color: #0E1726; font-weight: 700; margin-bottom: 10px; border-bottom: 2px solid #FF6B00; padding-bottom: 5px;">Comparisons</h4>', unsafe_allow_html=True)
        player_comparisons = [
            "Paolo Banchero",
            "Zion Williamson",
            "Jabari Smith Jr.",
            "Chet Holmgren",
            "Victor Wembanyama"
        ]
        
        for comp in player_comparisons:
            st.markdown(f'<div style="padding: 4px 0; border-bottom: 1px solid #eaeaea; font-size: 14px;">{comp}</div>', unsafe_allow_html=True)
    
    with col_rank:
        # 3 Year Draft Rank - more compact with 7 players and rank in orange box
        st.markdown(f'<h4 style="color: #0E1726; font-weight: 700; margin-bottom: 10px; border-bottom: 2px solid #FF6B00; padding-bottom: 5px;">3-Year Mock <span style="display: inline-block; background-color: #FF6B00; color: white; padding: 2px 8px; border-radius: 4px; font-size: 12px; margin-left: 8px;">#{player["Rank"]}</span></h4>', unsafe_allow_html=True)
        
        # Generate a list of 7 players with current player in the middle
        current_rank = player['Rank']
        player_names = {
            current_rank-3: "Donovan Clingan",
            current_rank-2: "Matas Buzelis",
            current_rank-1: "Stephon Castle",
            current_rank: player['Name'],      # Current player
            current_rank+1: "Ron Holland",
            current_rank+2: "Nikola Topic",
            current_rank+3: "Zaccharie Risacher"
        }
        
        # Create draft ranks list
        draft_ranks = []
        for i in range(current_rank-3, current_rank+4):
            # Use the player name from the dictionary, or a generic name if not found
            name = player_names.get(i, f"Player {i}")
            draft_ranks.append({"rank": i, "name": name})
        
        for draft_player in draft_ranks:
            if draft_player["name"] == player['Name']:
                st.markdown(f"""
                <div style="padding: 4px 0; border-bottom: 1px solid #eaeaea; font-size: 14px; color: #FF6B00; font-weight: 700;">
                    #{draft_player['rank']} {draft_player['name']}
                </div>
                """, unsafe_allow_html=True)
            else:
                st.markdown(f"""
                <div style="padding: 4px 0; border-bottom: 1px solid #eaeaea; font-size: 14px;">
                    #{draft_player['rank']} {draft_player['name']}
                </div>
                """, unsafe_allow_html=True)
    
    with col_rating:
        # Player Ratings - more compact
        st.markdown('<h4 style="color: #0E1726; font-weight: 700; margin-bottom: 10px; border-bottom: 2px solid #FF6B00; padding-bottom: 5px;">Qualitative</h4>', unsafe_allow_html=True)
        ratings = {
            "Athleticism": {"percentile": 76, "display": "76.0"},
            "Competitiveness": {"percentile": 71, "display": "71.5"},
            "Maturity": {"percentile": 66, "display": "66.0"},
            "Potential": {"percentile": 81, "display": "81.0"},
            "Basketball IQ": {"percentile": 73, "display": "73.0"},
        }
        
        for category, data in ratings.items():
            percentile = data["percentile"]
            
            # Calculate color based on percentile - matching the image
            if percentile < 40:
                # Red for low percentiles
                color = f"rgb(203, 68, 74)"
            elif percentile < 60:
                # Gray for middle percentiles
                color = f"rgb(130, 130, 130)"
            else:
                # Blue for high percentiles
                color = f"rgb(107, 124, 180)"
                
            # Create the metric visualization - more compact
            st.markdown(f"""
            <div style="margin-bottom: 8px;">
                <div style="display: flex; justify-content: space-between; margin-bottom: 2px;">
                    <span style="font-weight: 600; color: #555; font-size: 14px;">{category}</span>
                    <span style="font-weight: 700; color: #333; font-size: 14px;">{data['display']}</span>
                </div>
                <div style="height: 18px; background-color: #e0e0e0; border-radius: 4px; position: relative;">
                    <div style="position: absolute; left: 5px; top: 1px; font-size: 11px; font-weight: 600; color: white; z-index: 2;">{percentile}</div>
                    <div style="width: {percentile}%; height: 100%; background-color: {color}; border-radius: 4px;"></div>
                </div>
            </div>
            """, unsafe_allow_html=True)

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
            display_expanded_player_details(player)

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