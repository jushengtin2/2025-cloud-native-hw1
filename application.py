import datetime
from persistence import Database

class User:
    def __init__(self, username):
        self.username = username.lower()  # 用戶名忽略大小寫

class Listing:
    listing_counter = 100001

    def __init__(self, title, description, price, category, username):
        self.id = Listing.listing_counter
        Listing.listing_counter += 1
        self.title = title
        self.description = description
        self.price = price
        self.category = category
        self.username = username
        self.created_at = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def to_string(self):
        return f"{self.title}|{self.description}|{self.price}|{self.created_at}|{self.category}|{self.username}"

class MarketplaceApp:
    def __init__(self):
        self.db = Database()

    def register_user(self, username):
        """註冊用戶"""
        if self.db.get_user(username):
            return "Error - user already existing"
        self.db.save_user(User(username))
        return "Success"

    def create_listing(self, username, title, description, price, category):
        """創建商品"""
        user = self.db.get_user(username)
        if not user:
            return "Error - unknown user"

        listing = Listing(title, description, price, category, username)
        self.db.save_listing(listing)
        return listing.id

    def get_listing(self, username, listing_id):
        """查詢商品"""
        if not self.db.get_user(username):
            return "Error - unknown user"
        listing = self.db.get_listing(listing_id)
        return listing.to_string() if listing else "Error - not found"

    def delete_listing(self, username, listing_id):
        """刪除商品"""
        if not self.db.get_user(username):
            return "Error - unknown user"
        return self.db.delete_listing(username, listing_id)

    def get_category(self, username, category):
        """查詢類別"""
        if not self.db.get_user(username):
            return "Error - unknown user"
        return self.db.get_category(category)

    def get_top_category(self, username):
        """獲取最多商品的類別"""
        if not self.db.get_user(username):
            return "Error - unknown user"
        return self.db.get_top_category()