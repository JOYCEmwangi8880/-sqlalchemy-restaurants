from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.orm import declarative_base

db_url = "sqlite:///restaurants.db"
engine = create_engine(db_url)

Base = declarative_base()

class Restaurant(Base):
    __tablename__ = 'restaurants'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    price = Column(Integer)
    reviews = relationship('Review', back_populates='restaurant', overlaps="customers")
    customers = relationship('Customer', secondary='reviews', back_populates='restaurants', overlaps="reviews")
    
    def all_reviews(self):
        return [f"Review for {self.name} by {review.customer.full_name()}: {review.rating} stars. - {review.comment}" for review in self.reviews]

    @classmethod
    def fanciest(cls, session):
        return session.query(cls).order_by(cls.price.desc()).first()

class Customer(Base):
    __tablename__ = 'customers'
    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    reviews = relationship('Review', back_populates='customer', overlaps="restaurants")
    restaurants = relationship('Restaurant', secondary='reviews', back_populates='customers', overlaps="reviews")
    
    def full_name(self):
        return f"{self.first_name} {self.last_name}"
    
    def favorite_restaurant(self):
        if self.reviews:
            return max(self.reviews, key=lambda review: review.rating).restaurant

    def add_review(self, restaurant, rating):
        new_review = Review(restaurant=restaurant, customer=self, rating=rating)
        session.add(new_review)
        session.commit()

    def delete_reviews(self, restaurant):
        reviews_to_delete = [review for review in self.reviews if review.restaurant == restaurant]
        for review in reviews_to_delete:
            session.delete(review)
        session.commit()

class Review(Base):
    __tablename__ = 'reviews'
    id = Column(Integer, primary_key=True)
    rating = Column(Integer)
    comment = Column(String)
    restaurant_id = Column(Integer, ForeignKey('restaurants.id'))
    customer_id = Column(Integer, ForeignKey('customers.id'))
    restaurant = relationship('Restaurant', back_populates='reviews', overlaps="customers,restaurants")
    customer = relationship('Customer', back_populates='reviews', overlaps="customers,restaurants")

    def full_review(self):
        return f"Review for {self.restaurant.name} by {self.customer.full_name()}: {self.rating} stars. - {self.comment}"


# Create the database schema
Base.metadata.create_all(engine)

# Create a session
Session = sessionmaker(bind=engine)
session = Session()

# Sample data
restaurant1 = Restaurant(name='Kfc', price=1200) 
restaurant2 = Restaurant(name='Java House', price=3500)
customer1 = Customer(first_name='Maggy', last_name='Smith')  
customer2 = Customer(first_name='Joyce', last_name='Mwangi')

# Add data to the session and commit
session.add_all([restaurant1, restaurant2, customer1, customer2])
session.commit()

#  instances of Review and associate them with Restaurant and Customer
review1 = Review(restaurant=restaurant1, customer=customer1, rating=5, comment='Tasty')
review2 = Review(restaurant=restaurant2, customer=customer1, rating=4, comment='Nice Taste')
review3 = Review(restaurant=restaurant1, customer=customer2, rating=3, comment='Delicious')
review4 = Review(restaurant=restaurant2, customer=customer2, rating=2, comment='Amazing')

# Add data to the session and commit
session.add_all([review1, review2, review3, review4])
session.commit()

# Print customer's favorite restaurant and reviews
for customer in [customer1, customer2]:
    print(f"\n{customer.full_name()}'s favorite restaurant: {customer.favorite_restaurant().name}")

# Print all reviews
for customer in [customer1, customer2]:
    print(f"\nReviews by {customer.full_name()}:")
    
    for review in customer.reviews:
        print(review.full_review())
    print()

# Print the fanciest restaurant
fanciest_restaurant = Restaurant.fanciest(session)
print(f"The fanciest restaurant is: \n{fanciest_restaurant.name} with a price of {fanciest_restaurant.price}")
