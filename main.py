import streamlit as st
import requests
from db_utils import get_db_connection, get_cached_result, cache_result
from datetime import datetime



API_KEY=${{ API_KEY}}

st.set_page_config(page_title="Space Explorer", page_icon=":rocket:", layout="wide")

st.title("Space Explorer :rocket:")
st.markdown("Explore the latest space missions and their details.")
#st.markdown("Data sourced from [Launch Library 2 API](https://thespacedevs.com/llapi).")
st.markdown("Data sourced from [NASA APOD API](https://api.nasa.gov/).")
st.markdown("Developed by [Ravin Bhakta](https://ravinbhaktaresume.netlify.app/).")

selected_date = st.date_input("Select a date to view space missions:", datetime.now()).strftime("%Y-%m-%d")
st.markdown(f"### Space Missions on {selected_date}")

import json

def fetch_space_missions(date):
    conn = get_db_connection()
    cached = get_cached_result(conn, date)
    if cached:
        st.info(f"Loaded cached result for {date}")
        return json.loads(cached)
    url = f"https://api.nasa.gov/planetary/apod?date={date}&api_key={API_KEY}"
    response = requests.get(url, headers={"Authorization": f"Bearer {API_KEY}"}, verify=False)
    response.raise_for_status()
    data = response.json()
    cache_result(conn, date, json.dumps(data))
    st.info(f"Fetched and cached result for {date}")
    return data

data = fetch_space_missions(selected_date)
missions = data.get("results", [])


st.subheader(f"Total Missions: {len(missions)}")
st.subheader(data.get("title", "No Title Found"))
st.write(data.get("description", "No Description Found"))
for mission in missions:
    st.markdown(f"#### {mission['name']}")
    st.write(f"**Launch Time:** {mission['net']}")
    st.write(f"**Status:** {mission['status']['name']}")
    st.write(f"**Rocket:** {mission['rocket']['configuration']['name']}")
    st.write(f"**Mission Description:** {mission['mission']['description'] if mission.get('mission') else 'No Description Available'}")
    st.write(f"**Launch Pad:** {mission['pad']['name']}, {mission['pad']['location']['name']}")
    st.markdown("---")

st.markdown("### About")
st.markdown("""
This application allows users to explore space missions scheduled for a selected date.
It fetches data from the Launch Library 2 API and displays mission details including launch time, status, rocket configuration, mission description, and launch pad information.
""")
st.markdown("### Contact")
st.markdown("For any inquiries or feedback, please reach out to [Ravin Bhakta](https://ravinbhaktaresume.netlify.app/).")
st.markdown("### License")
st.markdown("This project is licensed under the MIT License.")
st.markdown("### Acknowledgements")
st.markdown("Data provided by [The Space Devs](https://thespacedevs.com/).")
st.markdown("Developed using [Streamlit](https://streamlit.io/).")
st.markdown("### Version")
st.markdown("Version 1.0.0")
st.markdown("### Updates")
st.markdown("Stay tuned for future updates and features!")
st.markdown("### Feedback")
st.markdown("Your feedback is valuable! Please share your thoughts and suggestions.")
st.markdown("### Support")
st.markdown("If you find this app useful, consider supporting its development.")
st.markdown("### Follow Me")
st.markdown("Follow me on [LinkedIn](https://www.linkedin.com/in/ravin-rohitbhai-bhakta/) and [GitHub](https://github.com/bhaktaravin).")
st.markdown("### Disclaimer")
st.markdown("This app is for educational purposes only. Data accuracy is not guaranteed.")
st.markdown("### Privacy Policy")
st.markdown("This app does not collect any personal data.")
st.markdown("### Terms of Service")
st.markdown("By using this app, you agree to the terms of service.")
