import dateutil.parser

try:
    from urllib.parse import urlencode
except ImportError:
    from urllib import urlencode

class Artist:
    def __init__(self, data):
        self.name = data.get('name')
        self.image_url = data.get('image_url')
        self.thumb_url = data.get('thumb_url')
        self.facebook_tour_dates_url = data.get('facebook_tour_dates_url')
        self.mbid = data.get('mbid')
        self.upcoming_events_count = data.get('upcoming_events_count')
        self.tracker_count = data.get('tracker_count')

    def __str__(self):
        return self.name


class Venue:
    def __init__(self, data):
        self.name = data.get('name')
        self.place = data.get('place')
        self.city = data.get('city')
        self.region = data.get('region')
        self.latitude = data.get('latitude')
        self.longitude = data.get('longitude')

    def __str__(self):
        return self.name
    
    @property
    def google_maps_url(self):
        query = "{},{},{}".format(self.name, self.city, self.region)
        return "http://maps.google.com/?q={}&ll={},{}".format(urlencode(query), self.longitude, self.latitude)


class Event:
    def __init__(self, data):
        self.id = data.get('id')
        self.title = data.get('title')
        self.datetime = data.get('datetime')
        self.formatted_datetime = data.get('formatted_datetime')
        self.formatted_location = data.get('location')
        self.ticket_url = data.get('ticket_url')
        self.ticket_type = data.get('ticket_type')
        self.ticket_status = data.get('ticket_status')
        self.on_sale_datetime = data.get('on_sale_datetime')
        self.facebook_rsvp_url = data.get('facebook_rsvp_url')
        self.description = data.get('description')
        self.artists = [Artist(a) for a in data.get('artists')]
        self.venue = Venue(data.get('venue'))

    @property
    def artist_names(self):
        return ', '.join(a.name for a in self.artists)

    @property
    def strftime(self, format='%b %d'):
       date = dateutil.parser.parse(self.datetime) 
       return date.strftime(format)

    def __str__(self):
        return self.title

