from datetime import datetime

class User:
    def __init__(self, email, password_hash, first_name, last_name, address, country, is_admin=False):
        self.id = None
        self.email = email
        self.password_hash = password_hash
        self.first_name = first_name
        self.last_name = last_name
        self.address = address
        self.country = country
        self.is_admin = is_admin
        self.total_bids = 0
        self.total_auctions_participated = 0
        self.total_wins = 0
        self.created_at = datetime.utcnow()


class Auction:
    def __init__(self, title, description, image_url, start_price, ticket_price, max_bids_per_ticket,
                 start_datetime, end_datetime, bid_timeout_seconds, total_tickets_available):
        self.id = None
        self.title = title
        self.description = description
        self.image_url = image_url
        self.start_price = start_price
        self.ticket_price = ticket_price
        self.max_bids_per_ticket = max_bids_per_ticket
        self.start_datetime = start_datetime
        self.end_datetime = end_datetime
        self.bid_timeout_seconds = bid_timeout_seconds
        self.total_tickets_available = total_tickets_available
        self.total_tickets_sold = 0
        self.status = "scheduled"
        self.winner_user_id = None
        self.winner_price = None
        self.winner_message_text = ""


class Ticket:
    def __init__(self, user_id, auction_id, bids_left):
        self.id = None
        self.user_id = user_id
        self.auction_id = auction_id
        self.bids_left = bids_left
        self.created_at = datetime.utcnow()


class Bid:
    def __init__(self, user_id, auction_id, amount):
        self.id = None
        self.user_id = user_id
        self.auction_id = auction_id
        self.amount = amount
        self.created_at = datetime.utcnow()
        self.is_last_active = False