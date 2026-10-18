import os

import pandas as pd
import requests
from dotenv import load_dotenv

load_dotenv()


class Genius:
    """Small wrapper around the Genius API."""

    def __init__(self, access_token):
        self.access_token = access_token
        self.headers = {"Authorization": f"Bearer {access_token}"}

    def _get(self, path, **params):
        """GET from the Genius API and return the 'response' part."""
        url = f"https://api.genius.com{path}"
        response = requests.get(url, headers=self.headers, params=params)
        data = response.json()
        if "response" not in data:
            raise RuntimeError(f"Genius API error {response.status_code}: "
                               f"{data.get('meta', data)}")
        return data["response"]

    def get_artist(self, search_term):
        """Return the info dict for the top artist matching `search_term`."""
        hits = self._get("/search", q=search_term)["hits"]
        artist_id = hits[0]["result"]["primary_artist"]["id"]
        return self._get(f"/artists/{artist_id}")["artist"]

    def get_artists(self, search_terms):
        """Return a DataFrame with one row per search term."""
        rows = []
        for term in search_terms:
            artist = self.get_artist(term)
            rows.append({
                "search_term": term,
                "artist_name": artist["name"],
                "artist_id": artist["id"],
                "followers_count": artist.get("followers_count"),
            })
        return pd.DataFrame(rows)
