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
        if not self.categories:
            return ["Error - no categories available"]
        
        # Step 1: 找出最大 listing 數量
        max_count = max(len(lst) for lst in self.categories.values())
        
        # Step 2: 收集所有擁有最多 listings 的 category
        top_categories = [cat for cat, lst in self.categories.items() if len(lst) == max_count]
        
        # Step 3: 按照 lexicographical order 排序
        top_categories.sort()
        
        return " ".join(top_categories)