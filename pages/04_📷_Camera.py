import streamlit as st
import streamlit.components.v1 as components

components.html("""
    <script src="https://aframe.io/releases/1.0.4/aframe.min.js"></script>
    <script src="https://unpkg.com/aframe-look-at-component@0.8.0/dist/aframe-look-at-component.min.js"></script>
    <script src="https://raw.githack.com/AR-js-org/AR.js/master/aframe/build/aframe-ar-nft.js"></script>
    <div id="aaa"/>
    <a-scene
      vr-mode-ui="enabled: false"
      embedded
      arjs="sourceType: webcam; debugUIEnabled: false;"
    >
      <a-text
        id="ar-pc1"
        value="BRM999 PC1"
        look-at="[gps-camera]"
        scale="60 60 60"
        gps-entity-place="latitude: {my-lat}; longitude: {my-long};"
      ></a-text>
      <a-camera gps-camera rotation-reader> </a-camera>
    </a-scene>
    <script>
        function getLocation() {
            document.getElementById("aaa").innerHTML = "hoge";
            navigator.geolocation.getCurrentPosition(setLatLong);
        }
        function setLatLong(position) {
            let ar-tag = document.getElementById("ar-pc1");
            let p = "latitude: " + position.coords.latitude + "; longitude: + " + position.coords.longitude +";";
            ar-tag.setAttribute("gps-entity-place", p);
        }
        window.onload = getLocation;
    </script>
""", height=480)