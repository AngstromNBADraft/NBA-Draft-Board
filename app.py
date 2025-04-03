import streamlit as st
import pandas as pd

# Function to add banner with text logo and white NBA DRAFT text
def add_banner():
    st.markdown("""
    <style>
    * {
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif;
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
        margin-top: -50px;
        padding-top: 0 !important;
    }
    
    section[data-testid="stSidebar"] {
        margin-top: 60px;
    }
    
    /* Who We Are section styling - updated to orange */
    .who-we-are {
        background-color: #f8f9fa;
        border-left: 6px solid #FF6B00;
        padding: 12px 16px;
        margin: 0 0 20px 0;
        border-radius: 8px;
        line-height: normal;
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
        margin-bottom: 5px !important;
        text-transform: uppercase;
        border-bottom: 3px solid #FF6B00;
        padding-bottom: 8px;
    }
    
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
        padding: 8px 0;
        border-bottom: 1px solid #eaeaea;
        transition: all 0.2s ease;
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
    }
    
    .rank-cell {
        width: 60px;
        text-align: center;
        font-weight: 700;
        color: #FF6B00;
    }
    
    .name-cell {
        width: 200px;  /* Wider name column */
        font-weight: 700;
        letter-spacing: 0.5px;
    }
    
    .pos-cell, .height-cell {
        width: 60px;
        text-align: center;
        color: #555;
    }
    
    .school-cell {
        width: 100px;
        text-align: center;
    }
    
    .age-cell, .stat-cell {
        width: 50px;
        text-align: center;
    }
    
    .arrow-cell {
        width: 60px;
        text-align: center;
    }
    
    .stat-cell {
        font-size: 13px;
    }
    
    .arrow-btn {
        background: #FF6B00 !important;
        color: white !important;
        border: none !important;
        border-radius: 4px !important;
        width: 25px !important;
        height: 25px !important;
        padding: 0 !important;
        display: flex !important;
        align-items: center !important;
        justify-content: center !important;
        font-weight: bold !important;
        transition: all 0.2s ease !important;
        margin: 0 auto !important;
    }
    
    .arrow-btn:hover {
        background: #E05E00 !important;
        transform: scale(1.1) !important;
    }
    
    /* More compact spacing for the expanded details */
    .player-details {
        padding: 16px;
        background-color: #FFF9F5; /* Very light orange background */
        border-radius: 0 0 4px 4px;
        margin-bottom: 10px;
        border-left: 4px solid #FF6B00;
    }
    
    .player-details h3 {
        color: #0E1726;
        margin-top: 0 !important;
        border-bottom: 2px solid #FFE5D3; /* Light orange border */
        padding-bottom: 8px;
    }
    
    /* Adjust metric bars */
    .metric-container {
        margin-bottom: 8px;
    }
    
    .metric-container div {
        height: 8px !important;
    }

    </style>
    
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
    }
    
    /* Style for the expander header */
    [data-testid="stExpander"] > div:first-child {
        border-radius: 8px !important;
        background-color: #f8f9fa !important;
    }
    
    /* Style for the expander content */
    [data-testid="stExpander"] > div:nth-child(2) {
        background-color: #f8f9fa !important;
        border-radius: 0 0 8px 8px !important;
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
        """)# Set up the page configuration
st.set_page_config(
    page_title="NBA Draft Big Board",
    page_icon="🏀",
    layout="wide"
)

# Add the banner
add_banner()

# Main content wrapper with margin adjustment
st.markdown('<div class="main-content">', unsafe_allow_html=True)

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

# Function to get player details
def get_player_details(player_name):
    return {
        "strengths": ["TO COME LATER"],
        "weaknesses": ["TO COME LATER"],
        "stats": {"TO COME LATER": "TO COME LATER"},
        "metrics": {"TO COME LATER": 0},
        "scouting": "TO COME LATER"
    }

# Get the data
df = get_draft_data()

# Store expanded player state in session state
if 'expanded_player' not in st.session_state:
    st.session_state.expanded_player = None

# Function to toggle player expansion
def toggle_player(player_name):
    if st.session_state.expanded_player == player_name:
        st.session_state.expanded_player = None
    else:
        st.session_state.expanded_player = player_name

# Main content
st.markdown('<div class="big-board-title">2025 NBA DRAFT BIG BOARD</div>', unsafe_allow_html=True)

# Table header with adjusted column widths
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
    <div class="player-cell arrow-cell"></div>
</div>
""", unsafe_allow_html=True)

# Display player rows
for idx, player in df.iterrows():
    is_expanded = st.session_state.expanded_player == player['Name']
    row_class = "player-row"
    if is_expanded:
        row_class += " expanded"
    
    st.markdown(f"""
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
        <div class="player-cell arrow-cell">
            <button class="arrow-btn" onclick="togglePlayer('{player['Name']}')">
                {'▲' if is_expanded else '▼'}
            </button>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # JavaScript for the toggle functionality
    st.markdown("""
    <script>
    function togglePlayer(playerName) {
        const currentPlayer = window.parent.document.getElementById('player-state').value;
        if (currentPlayer === playerName) {
            window.parent.document.getElementById('player-state').value = '';
        } else {
            window.parent.document.getElementById('player-state').value = playerName;
        }
        window.parent.document.querySelector('.stApp').dispatchEvent(new Event('click'));
    }
    </script>
    <input type="hidden" id="player-state" value="">
    """, unsafe_allow_html=True)
    
    # Show expanded details if this player is selected
    if is_expanded:
        details = get_player_details(player['Name'])
        with st.container():
            st.markdown(f"""
            <div class="player-details">
                <h3>{player['Name']} - #{player['Rank']} PROSPECT</h3>
                <p>{details['scouting']}</p>
                
                <div style="display: flex; flex-wrap: wrap; gap: 20px;">
                    <div style="flex: 1; min-width: 300px;">
                        <h4>STRENGTHS</h4>
                        <ul style="margin-top: 8px; padding-left: 20px;">
                            {"".join([f"<li style='margin-bottom: 6px;'>{s}</li>" for s in details['strengths']])}
                        </ul>
                        
                        <h4>WEAKNESSES</h4>
                        <ul style="margin-top: 8px; padding-left: 20px;">
                            {"".join([f"<li style='margin-bottom: 6px;'>{s}</li>" for s in details['weaknesses']])}
                        </ul>
                    </div>
                    
                    <div style="flex: 1; min-width: 300px;">
                        <h4>STATS</h4>
                        <table style="width: 100%; margin-top: 8px;">
                            {"".join([f"<tr><td style='padding: 4px 0; border-bottom: 1px solid #eee;'><b>{k}:</b></td><td style='padding: 4px 0; border-bottom: 1px solid #eee; text-align: right;'>{v}</td></tr>" for k, v in details['stats'].items()])}
                        </table>
                        
                        <h4 style='margin-top: 16px;'>PLAYER METRICS</h4>
                        {"".join([f'''
                        <div class="metric-container">
                            <div style="display: flex; justify-content: space-between; font-size: 13px; margin-bottom: 4px;">
                                <span><b>{k}</b></span>
                                <span>{v}/100</span>
                            </div>
                            <div style="height: 8px; width: 100%; background-color: #e1e4e8; border-radius: 4px;">
                                <div style="height: 8px; width: {v}%; background-color: #FF6B00; border-radius: 4px;"></div>
                            </div>
                        </div>
                        ''' for k, v in details['metrics'].items()])}
                    </div>
                </div>
            </div>
            """, unsafe_allow_html=True)

# Add footer
st.markdown("---")
st.write("DATA LAST UPDATED: APRIL 2025")

# Close the main content div
st.markdown('</div>', unsafe_allow_html=True)