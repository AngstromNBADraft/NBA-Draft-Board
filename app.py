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
        max-width: 120px !important;
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
/* Style for highlighting 2025 draft rows */
.highlighted-2025 {
    background-color: #EEEEEE   !important;
}

.highlighted-2025:hover {
    background-color: #c8cad2 !important; /* Same hover style as normal rows */
}

/* If row is both expanded and highlighted */
.player-row.expanded.highlighted-2025 {
    background-color: #FFA566 !important; /* Darker orange for expanded state */
    border-left: 4px solid #FF6B00 !important;
    border-bottom: none !important; /* Remove bottom border for expanded rows */
}

/* Add a Draft 2025 indicator badge */
.highlighted-2025 .name-cell:after {
    content: "2025";
    display: inline-block;
    background-color: #FF6B00;
    color: white;
    font-size: 10px;
    font-weight: bold;
    padding: 2px 2px;
    border-radius: 4px;
    margin-left: 6px;
    vertical-align: middle;
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
.spacer-cell {
    width: 15px !important;
    min-width: 15px !important;
    max-width: 15px !important;
    background-color: transparent !important;
    border: none !important;
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
        border-radius: 6px 6px 0 0;
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
        border: 1px solid #c0c0c0 ;

        transition: all 0.2s ease;
        height: 45px !important; /* Reduced height for more compact rows */
        margin: 0; /* Remove any margin */
        width: 950px !important; /* Fixed width matching header */

    }
    
    .player-row:hover {
        background-color: #EEEEEE;
    }
    
    .player-row.expanded {
        background-color: #FFF5EE; /* Light orange background for expanded row */
    }
    
    .player-cell {
        padding: 0 8px;
        font-size: 13px;
        text-transform: uppercase;
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
        font-weight: 700 !important;
        letter-spacing: 0.5px;
        box-sizing: border-box !important;
    }
    
    .pos-cell {
    width: 50px !important;
    min-width: 50px !important;
    max-width: 50px !important;
    text-align: left;
    font-weight: 500 !important;
    color: #555;
    box-sizing: border-box !important;
    margin-right: 0px !important;
}

.height-cell {
    width: 50px !important;
    min-width: 50px !important;
    max-width: 50px !important;
    text-align: center;
    color: #555;
font-weight: 500 !important;
    box-sizing: border-box !important;
}
    
    .school-cell {
        width: 135px !important;
        min-width: 135px !important;
        max-width: 135px !important;
        text-align: center;
font-weight: 500 !important;
        box-sizing: border-box !important;

    }
    
    .class-cell {
        width: 50px !important;
        min-width: 50px !important;
        max-width: 50px !important;
        text-align: center;
font-weight: 500 !important;
        box-sizing: border-box !important;
    }
    
    .stat-cell {
        width: 65px !important;
        min-width: 65px !important;
        max-width: 65px !important;
        text-align: center;
        font-size: 13px;




    }
.stat-cell-ranked {
    width: 65px !important;
    min-width: 65px !important;
    max-width: 65px !important;
    text-align: center;
    padding: 0px 3px !important;
    font-size: 13px;
    font-weight: 600 !important;
    box-sizing: border-box !important;
    color: black !important;
    border: 1px solid rgba(0, 0, 0, 0.08) !important;
    box-shadow: 0 1px 2px rgba(0, 0, 0, 0.05) !important;
    transition: all 0.2s ease !important;
}

/* Optional hover effect for better interactivity */
.stat-cell-ranked:hover {
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1) !important;
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
    margin: 7px 0 2px 0 !important;
    font-size: 12px !important;      /* Even smaller font */
    position: absolute !important;
    right: 20px !important;
    line-height: 1.65 !important;      /* Added to reduce height */
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

# Function to get draft data from CSV
def get_draft_data():
    try:
        # Load data from CSV
        df = pd.read_csv('AllProspects.csv')
        
        # Ensure all required columns exist
        required_columns = ['Draft', 'Rank', 'PlayerName', 'PositionDetail', 'Height', 
                            'PlayerClass', 'PlayerTeam', 'NBA', 'OScore', 'DScore', 'Score']
        
        # Check if all required columns exist
        missing_columns = [col for col in required_columns if col not in df.columns]
        if missing_columns:
            st.error(f"Missing columns in CSV: {', '.join(missing_columns)}")
            # Create a sample dataframe for demonstration if columns are missing
            return create_sample_dataframe()
        
        # Ensure OffenseRank, DefenseRank, and OverallRank are integers
        if 'OffenseRank' in df.columns:
            df['OffenseRank'] = df['OffenseRank'].fillna(-1).astype(int)
            df.loc[df['OffenseRank'] == -1, 'OffenseRank'] = None
        
        if 'DefenseRank' in df.columns:
            df['DefenseRank'] = df['DefenseRank'].fillna(-1).astype(int)
            df.loc[df['DefenseRank'] == -1, 'DefenseRank'] = None
            
        if 'OverallRank' in df.columns:
            df['OverallRank'] = df['OverallRank'].fillna(-1).astype(int)
            df.loc[df['OverallRank'] == -1, 'OverallRank'] = None
        
        return df
    
    except Exception as e:
        st.error(f"Error loading data: {e}")
        return create_sample_dataframe()

# Create a sample dataframe if CSV loading fails
def create_sample_dataframe():
    data = {
        'Draft': 2025,
        'Rank': list(range(1, 34)),
        'PlayerName': [
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
        'PositionDetail': [
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
        'PlayerClass': [
            "FR", "FR", "FR", "FR", "FR", "FR", "FR", "FR",
            "FR", "FR", "FR", "FR", "FR", "SO", "FR", "FR",
            "SO", "JR", "FR", "SR", "SR", "SO", "FR", "SR",
            "SR", "JR", "FR", "SO", "FR", "SR", "SO", "SR",
            "FR"
        ],
        'PlayerTeam': [
            "DUKE", "RUTGERS", "RUTGERS", "BAYLOR", "ILLINOIS", "DUKE", "DUKE", "TEXAS",
            "MARYLAND", "OKLAHOMA", "MICHIGAN STATE", "GEORGIA", "BYU", "SOUTH CAROLINA",
            "UCONN", "GEORGETOWN", "SAINT JOSEPH'S", "MICHIGAN", "ILLINOIS", "UAB",
            "COLORADO STATE", "FLORIDA", "ALABAMA", "MARQUETTE", "AUBURN", "ARKANSAS",
            "ARKANSAS", "TEXAS TECH", "ARIZONA", "UCONN", "SAN DIEGO STATE", "CREIGHTON",
            "DUKE"
        ],
        'Offense': list(range(1, 34)),
        'Defense': list(range(1, 34)),
        'Overall': list(range(1, 34))
    }
    return pd.DataFrame(data)

# Function to get player details
def get_player_details(player_name):
    return {
        "strengths": ["Elite scoring ability", "Defensive versatility", "High basketball IQ"],
        "weaknesses": ["Needs to improve free throw shooting", "Can be turnover prone in transition"],
        "scouting": "Shows excellent potential as a two-way player with room to develop as a playmaker. Has shown steady improvement throughout the season."
    }

# Set up the page configuration
st.set_page_config(
    page_title="NBA Draft Big Board",
    page_icon= "https://sdmntprsouthcentralus.oaiusercontent.com/files/00000000-d2a4-61f7-8c44-cb4e5e5deecd/raw?se=2025-04-10T13%3A29%3A38Z&sp=r&sv=2024-08-04&sr=b&scid=f9701198-a805-540b-a3df-ea5d37151a8f&skoid=0abefe37-d2bd-4fcb-bc88-32bccbef6f7d&sktid=a48cca56-e6da-484e-a814-9c849652bcb3&skt=2025-04-10T10%3A34%3A17Z&ske=2025-04-11T10%3A34%3A17Z&sks=b&skv=2024-08-04&sig=LeqbJbRUsH66mBcMshsjJhmMsfOF/wAJWZ1ODfhXpDo%3D",
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

# Get the data
# Replace the current title and filter section with this updated version
# that properly defines selected_draft before using it

# Get the data first
df = get_draft_data()
df_original = df.copy()

# Sort the dataframe by Rank if it exists
if 'Rank' in df.columns:
    df = df.sort_values('Rank')

# Store expanded player state in session state
if 'expanded_player' not in st.session_state:
    st.session_state.expanded_player = None

# Initialize button keys in session state if not present
if 'button_keys' not in st.session_state:
    # Create button keys that include both index and player name to ensure uniqueness
    st.session_state.button_keys = {
        row['PlayerName']: f"btn_{idx}_{row['PlayerName'].replace(' ', '_')}" 
        for idx, row in df.iterrows()
    }

# Create title and filter section with default Streamlit styling
# Place this CSS in your existing style section, for example in the title styling block:

st.markdown("""
<style>
    /* Title styling */
    .big-board-title {
    /* Size and typography */
    font-size: 29px !important;
    font-weight: 800;
    color: #0E1726;
    letter-spacing: 1px;
    text-transform: uppercase;
    
    /* Spacing and borders */
    margin-bottom: 0 !important;
    margin-top: 5px !important;
    padding-bottom: 15px;
    border-bottom: 7px solid #FF6B00;
    
    /* Display and dimensions */
    max-width: 950px;
    width: 100%;
    margin-left: auto;
    margin-right: auto;
    display: inline-block !important;
    vertical-align: middle !important;
}
    
    /* Just minimal adjustments to position the filter */
    .stSelectbox {
        margin-top: -10px !important;
        max-width: 250px !important;
    }
    
    /* Make selectbox containers shorter */
    div[data-baseweb="select"] {
        max-width: 120px !important;
        border: 1px solid #646E78 !important;
        border-radius: 8px !important;
        height: 32px !important;  /* Reduced height */
    }
    
    /* Adjust the internal elements of the selectbox */
    div[data-baseweb="select"] > div {
        height: 30px !important;  /* Reduced height */
        min-height: 30px !important;
        display: flex !important;
        align-items: center !important;
    }
    
    /* Adjust the selectbox text */
    div[data-baseweb="select"] span {
        font-size: 13px !important;  /* Smaller font size */
        line-height: 1 !important;  /* Tighter line height */
    }
    
    /* Adjust the dropdown arrow */
    div[data-baseweb="select"] svg {
        height: 16px !important;
        width: 16px !important;
    }
    
    /* Reduce the label height and adjust position */
    .stSelectbox label {
        font-size: 13px !important;
        margin-bottom: 2px !important;
        padding-top: 0 !important;
        line-height: 1 !important;
    }
    
    /* Remove extra padding in the container */
    .stSelectbox > div {
        padding-bottom: 5px !important;
        padding-top: 0 !important;
    }
</style>
""", unsafe_allow_html=True)
# Create the title and filter row
title_container = st.container()
with title_container:
    st.markdown('<div class="filter-row">', unsafe_allow_html=True)
    col1, col2, col3, col4 = st.columns([0.4, 0.1, 0.1, 0.1])
    
    # First get the filter values
    with col2:
        # Fetch unique draft years and sort them
        all_drafts = sorted(df['Draft'].unique().tolist())
        selected_draft = st.selectbox(
            "Year",
            ["ALL"] + all_drafts,
            index=0,
            key="draft_filter",
        )
    
    with col3:
        # Position filter will be updated based on draft selection
        filtered_df = df if selected_draft == "ALL" else df[df['Draft'] == selected_draft]
        all_positions = sorted(filtered_df['PositionDetail'].unique().tolist())
        selected_position = st.selectbox(
            "Position",
            ["ALL"] + all_positions,
            index=0,
            key="position_filter",
        )
    
    with col4:
        # Get all unique player names for the autocomplete dropdown
        all_player_names = sorted(df_original['PlayerName'].unique().tolist())
        
        # Add an "ALL" option at the beginning
        player_options = ["ALL"] + all_player_names
        
        # Player search box with autocomplete
        selected_player = st.selectbox(
            "Search",
            options=player_options,
            index=0,
            key="player_search"
        )
    
    # Now display the title with the selected_draft
    # Create the title with the selected_draft year in orange
    with col1:
        if selected_draft == "ALL":
            st.markdown('<div class="big-board-title"><span style="color: #FF6B00;">5-YEAR</span> NBA DRAFT BIG BOARD</div>', unsafe_allow_html=True)
        else:
            # Using span with orange color for the year
            st.markdown(f'<div class="big-board-title"><span style="color: #FF6B00;">{selected_draft}</span> NBA DRAFT BIG BOARD</div>', unsafe_allow_html=True)
    
    st.markdown('</div>', unsafe_allow_html=True)

# Apply filters
if selected_draft != 'ALL':
    df = df[df['Draft'] == selected_draft]

if selected_position != 'ALL':
    df = df[df['PositionDetail'] == selected_position]

if selected_player != "ALL":
    # Filter for the exact player name
    df = df[df['PlayerName'] == selected_player]

# Reset the ranking if a specific draft year is selected
if selected_draft != 'ALL':
    # Create a temporary copy of the dataframe to preserve original ranks
    temp_df = df.copy()
    # Sort by original rank
    temp_df = temp_df.sort_values('Rank')
    # Add a new column with consecutive numbering starting from 1
    temp_df['DisplayRank'] = range(1, len(temp_df) + 1)
    # Replace the dataframe with our temporary one
    df = temp_df
else:
    # If showing all years, use the original Rank
    df['DisplayRank'] = df['Rank']
# Wrap the table in a fixed-width container
st.markdown('<div class="table-container">', unsafe_allow_html=True)

# Table header with fixed width and aligned cells
st.markdown("""
<div class="table-header">
    <div class="player-cell rank-cell">RANK</div>
    <div class="player-cell name-cell">NAME</div>
    <div class="player-cell pos-cell">POS</div>
    <div class="player-cell height-cell">HT</div>
    <div class="player-cell class-cell">CLASS</div>
    <div class="player-cell school-cell">SCHOOL</div>
    <div class="player-cell stat-cell">NBA</div>
    <div class="player-cell stat-cell">OScore</div>
    <div class="player-cell stat-cell">DScore</div>
    <div class="player-cell spacer-cell"></div> 
    <div class="player-cell stat-cell">Score</div>
    <div class="player-cell arrow-cell"></div>
</div>
""", unsafe_allow_html=True)

# Function to toggle player expansion
def toggle_player(player_name):
    if st.session_state.expanded_player == player_name:
        st.session_state.expanded_player = None
    else:
        st.session_state.expanded_player = player_name

# Function to toggle player expansion
def toggle_player(player_name):
    if st.session_state.expanded_player == player_name:
        st.session_state.expanded_player = None
    else:
        st.session_state.expanded_player = player_name

def create_player_row(player, expanded, selected_draft):
    # Only highlight 2025 players when "ALL" is selected
    is_2025_draft = player['Draft'] == 2025 and selected_draft == "ALL"
    
    # Add a special class for 2025 draft players
    if is_2025_draft:
        row_class = "player-row expanded highlighted-2025" if expanded else "player-row highlighted-2025"
    else:
        row_class = "player-row expanded" if expanded else "player-row"
   
    # Function to get color based on score (0-100 scale where 100 is best)
    def get_color_for_rank(score):
        # Check if score is None or NaN
        if pd.isna(score) or score is None:
            return "#e2e5e9"  # Light gray for missing values
            
        # Normalize score to 0-1 scale where 1 is best (100) and 0 is worst (0)
        normalized = min(1.0, max(0.0, float(score) / 100))
        
        if normalized > 0.95:      # Excellent (95-100)
           return "#7cb342"      # Muted green
        elif normalized > 0.90:    # Very good (90-95)
           return "#8bc34a"      # Lighter muted green
        elif normalized > 0.85:    # Very good (85-90)
           return "#9ccc65"      # Pale green
        elif normalized > 0.80:    # Good (80-85)
           return "#a4d368"      # Light green
        elif normalized > 0.75:    # Good (75-80)
           return "#aed581"      # Very pale green
        elif normalized > 0.70:    # Above average (70-75)
           return "#b7de8c"      # Very pale green
        elif normalized > 0.65:    # Above average (65-70)
           return "#c1e597"      # Nearly neutral green
        elif normalized > 0.60:    # Above average (60-65)
           return "#caea9f"      # Very light green
        elif normalized > 0.55:    # Slightly above average (55-60)
           return "#d3efac"      # Extremely pale green
        elif normalized > 0.50:    # Slightly above average (50-55)
           return "#dcf4b9"      # Almost white-green
        elif normalized > 0.45:    # Average (45-50)
           return "#e0e0e0"      # Neutral gray
        elif normalized > 0.40:    # Slightly below average (40-45)
           return "#ffccbc"      # Nearly neutral red
        elif normalized > 0.30:    # Below average (30-40)
           return "#ffab91"      # Very pale red
        elif normalized > 0.20:    # Poor (20-30)
           return "#ff8a65"      # Pale red
        elif normalized > 0.10:    # Very poor (10-20)
           return "#ff7043"      # Light red
        else:                      # Terrible (0-10)
           return "#ff5722"      # Muted red
            
    # Write player row HTML - fixed width with black bold text
    html = f"""
<div class="{row_class}">
    <div class="player-cell rank-cell">{player['DisplayRank']}</div>
    <div class="player-cell name-cell">{player['PlayerName']}</div>
    <div class="player-cell pos-cell">{player['PositionDetail']}</div>
    <div class="player-cell height-cell">{player['Height']}</div>
    <div class="player-cell class-cell">{player['PlayerClass']}</div>
    <div class="player-cell school-cell">{player['PlayerTeam']}</div>
    <div class="stat-cell-ranked" style="background-color: {get_color_for_rank(player['NBA'])}">{player['NBA']}</div>
    <div class="stat-cell-ranked" style="background-color: {get_color_for_rank(player['OScore'])};">{player['OScore']}</div>
    <div class="stat-cell-ranked" style="background-color: {get_color_for_rank(player['DScore'])}">{player['DScore']}</div>
    <div class="player-cell spacer-cell"></div> 
    <div class="stat-cell-ranked" style="background-color: {get_color_for_rank(player['Score'])}">{player['Score']}</div>
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
# Function to handle the expanded details with Streamlit's native components
def display_expanded_player_details(player):
    # Apply custom CSS to make things more professional
    st.markdown("""
    <style>
    .section-title {
        color: #0E1726;
        font-size: 18px;
        font-weight: 700;
        margin-bottom: 15px;
        border-bottom: 1px solid #FF6B00;
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
    col_img, col_bio = st.columns([.5,.5])
    
    with col_img:
        # Player image
        st.image("https://a.espncdn.com/combiner/i?img=/i/headshots/mens-college-basketball/players/full/5041939.png&w=350&h=254", 
                use_container_width=True)
        
        # Player name under image
        st.markdown(f"<div style='text-align: center; font-weight: bold; font-size: 18px; margin-top: 10px;'>{player['PlayerName']}</div>", 
                   unsafe_allow_html=True)
    with col_bio:
        pass
   
        
# Display player rows using a more optimized layout with no gaps
for idx, player in df.iterrows():
    is_expanded = st.session_state.expanded_player == player['PlayerName']
    
    # Create the player row and get any expanded content - now passing the selected_draft
    row_html, expanded_html = create_player_row(player, is_expanded, selected_draft)
    
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
            btn_key = st.session_state.button_keys[player['PlayerName']]
            
            # Using on_click for the callback
            st.button(btn_text, key=btn_key, on_click=toggle_player, args=(player['PlayerName'],))
        
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