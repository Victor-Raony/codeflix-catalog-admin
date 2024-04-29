import unittest
from uuid import UUID
import uuid

from category import Category

class TestCategory(unittest.TestCase):
  def test_name_is_required(self):
    with self.assertRaisesRegex(TypeError, 'missing 1 required positional argument: \'name\''):
      Category()
      
  def test_name_must_have_less_than_256_characters(self):
    with self.assertRaisesRegex(ValueError, 'name must be less than 256 characters'):
      Category('a' * 256)
        
  def test_category_must_be_created_with_id_or_uuid_by_default(self):
    category = Category(name="Filme")
    self.assertEquals(type(category.id), UUID)
      
  def test_created_category_with_default_values(self):
    category = Category(name="Filme")
    self.assertEquals(category.name, "Filme")
    self.assertEquals(category.description, "")
    self.assertEquals(category.is_active, True)
  
  def test_category_is_created_as_active_by_default(self):
    category = Category(name="Filme")
    self.assertEquals(category.is_active, True)
    
  def test_category_is_created_with_provided_values(self):
    cat_id = uuid.uuid4()
    category = Category(
      name="Filme", 
      id=cat_id, 
      description="descrição", 
      is_active=False,
    )
    self.assertEquals(category.id, cat_id)
    self.assertEquals(category.name, "Filme")
    self.assertEquals(category.description, "descrição")
    self.assertEquals(category.is_active, False)
  
  
if __name__ == '__main__':
  unittest.main()