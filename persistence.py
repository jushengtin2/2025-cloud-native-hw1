class Database:
    def __init__(self):
        self.users = {}  # {username: User}
        self.listings = {}  # {listing_id: Listing}
        self.categories = {}  # {category: [listing_id]}

    def save_user(self, user):
        self.users[user.username] = user

    def get_user(self, username):
        return self.users.get(username.lower(), None)

    def save_listing(self, listing):
        self.listings[listing.id] = listing
        if listing.category not in self.categories:
            self.categories[listing.category] = []
        self.categories[listing.category].append(listing.id)

    def get_listing(self, listing_id):
        return self.listings.get(listing_id, None)

    def delete_listing(self, username, listing_id):
        if listing_id not in self.listings:
            return "Error - listing does not exist"

        listing = self.listings[listing_id]
        if listing.username != username:
            return "Error - listing owner mismatch"

        del self.listings[listing_id]
        self.categories[listing.category].remove(listing_id)
        return "Success"

    def get_category(self, category):
        if category not in self.categories or not self.categories[category]:
            return "Error - category not found"
        return "\n".join(self.listings[l].to_string() for l in sorted(self.categories[category], reverse=True)) 

    def get_top_category(self):
        return max(self.categories, key=lambda cat: (len(self.categories[cat]), cat), default="Error - no categories available") #降冪 比如s比e大