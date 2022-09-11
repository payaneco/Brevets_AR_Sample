import streamlit as st
from bokeh.models.widgets import Button
from bokeh.models import CustomJS
from streamlit_bokeh_events import streamlit_bokeh_events
import streamlit.components.v1 as components

html_format = """
    <script src="https://aframe.io/releases/1.0.4/aframe.min.js"></script>
    <script src="https://unpkg.com/aframe-look-at-component@0.8.0/dist/aframe-look-at-component.min.js"></script>
    <script src="https://raw.githack.com/AR-js-org/AR.js/master/aframe/build/aframe-ar-nft.js"></script>
    <a-scene vr-mode-ui="enabled: false" embedded arjs="sourceType: webcam; debugUIEnabled: false;">
      <a-text value="PC1" look-at="[gps-camera]" scale="{0} {0} {0}" gps-entity-place="latitude: {1}; longitude: {2};" color="white"></a-text>
      <a-text value="PC2" look-at="[gps-camera]" scale="{0} {0} {0}" gps-entity-place="latitude: {3}; longitude: {4};" color="red"></a-text>
      <a-text value="PC3" look-at="[gps-camera]" scale="{0} {0} {0}" gps-entity-place="latitude: {5}; longitude: {6};" color="navy"></a-text>
      <a-text value="PC4" look-at="[gps-camera]" scale="{0} {0} {0}" gps-entity-place="latitude: {7}; longitude: {8};" color="green"></a-text>
      <a-camera gps-camera rotation-reader> </a-camera>
    </a-scene>
"""

st.write("現在地を取得すると周辺にARマークを生成します")

loc_button = Button(label="現在地を取得")
loc_button.js_on_event("button_click", CustomJS(code="""
    navigator.geolocation.getCurrentPosition(
        (loc) => {
            document.dispatchEvent(new CustomEvent("GET_LOCATION", {detail: {lat: loc.coords.latitude, lng: loc.coords.longitude}}))
        }
    )
    """))
result = streamlit_bokeh_events(
    loc_button,
    events="GET_LOCATION",
    key="get_location",
    refresh_on_update=False,
    override_height=75,
    debounce_time=0)

if result:
    lat = result["GET_LOCATION"]["lat"]
    lng = result["GET_LOCATION"]["lng"]
    lat1 = lat + 0.0001
    lat2 = lat - 0.0001
    lng1 = lng + 0.0001
    lng2 = lng - 0.0001
    html = html_format.format(60, lat1, lng1, lat2, lng1, lat2, lng2, lat1, lng2)
    components.html(html, height=480)