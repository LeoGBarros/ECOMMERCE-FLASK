from sqlalchemy import func
import uuid
from app import db
from app.utils.date import formatDateISO

class Product(db.Model):
  id = db.Column(db.String, primary_key=True, default=lambda: str(uuid.uuid4()))
  name = db.Column(db.String(80), nullable=False)
  description = db.Column(db.Text, nullable=True)
  price = db.Column(db.Float, nullable=False)
  image_url = db.Column(db.String(200), nullable=True)
  stock_quantity = db.Column(db.Integer, nullable=False)
  category_id = db.Column(db.String, db.ForeignKey('category.id'))
  created_at = db.Column(db.DateTime(timezone=True), server_default=func.now())
  updated_at = db.Column(db.DateTime(timezone=True), server_default=func.now(), onupdate=func.now())

  def to_dict(self):
    return {
      'id': self.id,
      'name': self.name,
      'description': self.description,
      'price': self.price,
      'imageUrl': self.image_url,
      'stockQuantity': self.stock_quantity,
      'category': self.category_id,
      'createdAt': formatDateISO(self.created_at),
      'updatedAt': formatDateISO(self.updated_at),
    }
  
class Category(db.Model):
  id = db.Column(db.String, primary_key=True, default=lambda: str(uuid.uuid4()))
  name = db.Column(db.String(80), nullable=False)
  slug = db.Column(db.String(80), nullable=False, unique=True)
  products = db.relationship('Product', backref='category')
  created_at = db.Column(db.DateTime(timezone=True), server_default=func.now())
  updated_at = db.Column(db.DateTime(timezone=True), server_default=func.now(), onupdate=func.now())
 
  def to_dict(self):
    return {
      'id': self.id,
      'name': self.name,
      'slug': self.slug,
      'createdAt': formatDateISO(self.created_at),
      'updatedAt': formatDateISO(self.updated_at),
    }
  
class Cart(db.Model):
  id = db.Column(db.String, primary_key=True, default=lambda: str(uuid.uuid4()))
  created_at = db.Column(db.DateTime(timezone=True), server_default=func.now())
  updated_at = db.Column(db.DateTime(timezone=True), server_default=func.now(), onupdate=func.now())

  def to_dict(self):
    return {
      'id': self.id,
      'createdAt': formatDateISO(self.created_at),
      'updatedAt': formatDateISO(self.updated_at),
    }