import os

from .client import Client
from .objects import Artist
from .objects import Event
from .objects import Venue


class Bandsintown(Client):
    """
    Provides the Bandsintown API v2 REST calls but returns
    Python objects instead of JSON
    """

    def get(self, *args, **kwargs):
        """
        Searches for a single artist via this endpoint:

            https://www.bandsintown.com/api/requests#artists-get

        Requires one of the following artist identifiers:

            - A single string argument of an artist's name
            - A `fbid` kwarg with the artist's Facebook ID
            - A `mbid` kwarg with the artist's MusicBrainz ID

        Returns a dict or None if not found

        Usage:

            client = Client(app_id=1234)
            client.get('Bad Religion')
            client.get(fbid=168803467003)
            client.get(mbid='149e6720-4e4a-41a4-afca-6d29083fc091')
        """
        data = super(Bandsintown, self).get(*args, **kwargs)
        return Artist(data)


    def events(self, *args, **kwargs):
        """
        Get events for a single artist, calling this endpoint:

            https://www.bandsintown.com/api/requests#artists-events

        Requires an artist identifier, similar to the `get` method,
        and accepts the following keyword arguments:

            date (string) (optional)
                Can be one of the following:
                    - "upcoming"
                    - "all"
                    - A date string in the format: yyyy-mm-dd
                    - A date range string in the format: yyyy-mm-dd,yyyy-mm-dd

        Returns a list or None if not found

        Usage:

            client = Client(app_id=1234)
            client.events('Bad Religion')
            client.events('Bad Religion', location='Portland,OR')
        """
        data = super(Bandsintown, self).events(*args, **kwargs)
        return self._json_to_events(data)


    def search(self, *args, **kwargs):
        """
        Gets events for a single artist with search criteria using
        this endpoint:

            https://www.bandsintown.com/api/requests#artists-event-search

        Requires an artist identifier, similar to the `get` method,
        and accepts the following keyword arguments:

            location (string)
                A location string in one of the following formats:
                    - city,state (US or CA)
                    - city,country
                    - lat,lon
                    - IP address

            radius (string/integer) (optional)
                Number of miles radius around location to search within.
                Defaults to 25, max is 150

            date (string) (optional)
                Can be one of the following:
                    - "upcoming"
                    - "all"
                    - A date string in the format: yyyy-mm-dd
                    - A date range string in the format: yyyy-mm-dd,yyyy-mm-dd
        """
        data = super(Bandsintown, self).search(*args, **kwargs)
        return self._json_to_events(data)

    
    def recommended(self, *args, **kwargs):
        """
        Gets recommended events based on single artist and location and other
        optional search criteria using this endpoint:

            https://www.bandsintown.com/api/requests#artists-recommended-events

        Requires an artist identifier, similar to the `get` method,
        and accepts the following keyword arguments:

            location (string)
                A location string in one of the following formats:
                    - city,state (US or CA)
                    - city,country
                    - lat,lon
                    - IP address

            radius (string/integer) (optional)
                Number of miles radius around location to search within.
                Defaults to 25, max is 150

            date (string) (optional)
                Can be one of the following:
                    - "upcoming"
                    - "all"
                    - A date string in the format: yyyy-mm-dd
                    - A date range string in the format: yyyy-mm-dd,yyyy-mm-dd

            only_recs (boolean) (optional)
                If True, only recommended events are returned, if False the
                artist's events are included along with the recommended ones
        """
        data = super(Bandsintown, self).recommended(*args, **kwargs)
        return self._json_to_events(data)


    def _json_to_events(self, data):
        return [Event(e) for e in data]

