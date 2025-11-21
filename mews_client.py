"""
Mews API Client for Kitchen Meal Planning
Handles all API communication with Mews Connector API
"""

import requests
from datetime import datetime, timedelta
from typing import Dict, List, Optional
import json


class MewsAPIClient:
    """Client for interacting with Mews Connector API"""

    def __init__(self, client_token: str, access_token: str, base_url: str = "https://api.mews.com"):
        """
        Initialize Mews API Client

        Args:
            client_token: Your Mews Client Token
            access_token: Property Access Token
            base_url: API base URL (use demo URL for testing)
        """
        self.client_token = client_token
        self.access_token = access_token
        self.base_url = base_url
        self.headers = {
            "Content-Type": "application/json"
        }

    def _make_request(self, endpoint: str, payload: Dict) -> Dict:
        """
        Make API request to Mews

        Args:
            endpoint: API endpoint path
            payload: Request payload

        Returns:
            Response data as dictionary
        """
        url = f"{self.base_url}{endpoint}"

        # Add authentication to payload
        payload["ClientToken"] = self.client_token
        payload["AccessToken"] = self.access_token
        payload["Client"] = "KitchenMealPlanner 1.0"

        try:
            response = requests.post(url, headers=self.headers, json=payload, timeout=30)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"API Request Error: {e}")
            if hasattr(e.response, 'text'):
                print(f"Response: {e.response.text}")
            raise

    def get_services(self, service_ids: Optional[List[str]] = None) -> List[Dict]:
        """
        Get all services from Mews

        Args:
            service_ids: Optional list of specific service IDs to retrieve

        Returns:
            List of service objects
        """
        endpoint = "/api/connector/v1/services/getAll"
        payload = {}

        if service_ids:
            payload["ServiceIds"] = service_ids

        response = self._make_request(endpoint, payload)
        return response.get("Services", [])

    def get_products(self, service_ids: Optional[List[str]] = None) -> List[Dict]:
        """
        Get all products (meals) from Mews

        Args:
            service_ids: Optional filter by service IDs

        Returns:
            List of product objects
        """
        endpoint = "/api/connector/v1/products/getAll"
        payload = {}

        if service_ids:
            payload["ServiceIds"] = service_ids

        response = self._make_request(endpoint, payload)
        return response.get("Products", [])

    def get_reservations(self, start_date: datetime, end_date: datetime,
                        states: Optional[List[str]] = None) -> Dict:
        """
        Get all reservations for a date range

        Args:
            start_date: Start date for reservation query
            end_date: End date for reservation query
            states: Optional reservation states filter (Confirmed, Started, etc.)

        Returns:
            Dictionary with Reservations, ReservationGroups, etc.
        """
        endpoint = "/api/connector/v1/reservations/getAll"

        # Default to confirmed and started reservations
        if states is None:
            states = ["Confirmed", "Started"]

        payload = {
            "TimeFilter": {
                "CollidingUtc": {
                    "StartUtc": start_date.strftime("%Y-%m-%dT%H:%M:%SZ"),
                    "EndUtc": end_date.strftime("%Y-%m-%dT%H:%M:%SZ")
                }
            },
            "States": states,
            "Extent": {
                "Reservations": True,
                "ReservationGroups": True,
                "Customers": True
            }
        }

        response = self._make_request(endpoint, payload)
        return response

    def get_order_items(self, start_date: datetime, end_date: datetime,
                       service_ids: Optional[List[str]] = None) -> List[Dict]:
        """
        Get all order items (meal orders) for a date range

        Args:
            start_date: Start date for query
            end_date: End date for query
            service_ids: Optional filter by service IDs

        Returns:
            List of order item objects
        """
        endpoint = "/api/connector/v1/orderItems/getAll"

        payload = {
            "ConsumedUtc": {
                "StartUtc": start_date.strftime("%Y-%m-%dT%H:%M:%SZ"),
                "EndUtc": end_date.strftime("%Y-%m-%dT%H:%M:%SZ")
            },
            "Types": ["ProductOrder"]
        }

        if service_ids:
            payload["ServiceIds"] = service_ids

        response = self._make_request(endpoint, payload)
        return response.get("OrderItems", [])

    def get_age_categories(self) -> List[Dict]:
        """
        Get age categories (Adult, Child, etc.)

        Returns:
            List of age category objects
        """
        endpoint = "/api/connector/v1/ageCategories/getAll"
        payload = {}

        response = self._make_request(endpoint, payload)
        return response.get("AgeCategories", [])
