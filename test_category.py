import pytest 
from uuid import UUID
import uuid

from category import Category

class TestCategory:
  def test_name_is_required(self):
    with pytest.raises(TypeError, match='missing 1 required positional argument: \'name\''):
      Category()
      
  def test_name_must_have_less_than_256_characters(self):
    with pytest.raises(ValueError, match='name cannot be longer than 255 characters'):
      Category('a' * 256)
        
  def test_category_must_be_created_with_id_or_uuid_by_default(self):
    category = Category(name="Filme")
    assert isinstance(category.id, UUID)
      
  def test_created_category_with_default_values(self):
    category = Category(name="Filme")
    assert category.name == "Filme"
    assert category.description == ""
    assert category.is_active is True
  
  def test_category_is_created_as_active_by_default(self):
    category = Category(name="Filme")
    assert category.is_active is True
    
  def test_category_is_created_with_provided_values(self):
    cat_id = uuid.uuid4()
    category = Category(
      id=cat_id, 
      name="Filme", 
      description="Filme em geral", 
      is_active=False,
    )
    assert category.id == cat_id
    assert category.name == "Filme"
    assert category.description == "Filme em geral"
    assert category.is_active is False  
    
  def test_cannot_create_category_with_empty_name(self):
    with pytest.raises(ValueError,  match="name cannot be empty"):  
      Category(name="") 
  
  
class TestUpdateCategory:
  def test_update_category_with_name_and_description(self):
    category = Category(name="Filme", description="Filme de geral")
    
    category.update_category(name="Serie", description="Series em geral")
    
    assert category.name == "Serie"
    assert category.description == "Series em geral"
    assert category.is_active is True
    
  def test_update_category_with_invalid_name_raises_exception(self):
    category = Category(name="Filme", description="Filme de geral")
    
    with pytest.raises(ValueError, match="name cannot be longer than 255 characters"):
      category.update_category(name="Serie" * 256, description="Series em geral")
      
  def test_cannot_update_category_with_empty_name(self):
    with pytest.raises(ValueError, match="name cannot be empty"):
      Category(name="")
      
class TestActivate:
  def test_activate_inactive_category(self):
    category = Category(
      name="Filme", 
      description="Filme de geral",
      is_active=False
      )
    category.activate()
    assert category.is_active is True
  
  def test_activate_active_category(self):
    category = Category(
      name="Filme", 
      description="Filme de geral",
      is_active=True
      )
    category.activate()
    assert category.is_active is True
    
  def test_desactivate_active_category(self):
    category = Category(
      name="Filme", 
      description="Filme de geral",
      is_active=True
      )
    category.deactivate()
    assert category.is_active is False
    
  def test_desactivate_inactive_category(self):
    category = Category(
      name="Filme", 
      description="Filme de geral",
      is_active=False
      )
    category.deactivate()
    assert category.is_active is False
    
class TestEquality:
  def test_when_categories_have_same_id_they_are_equals(self):
    cat_id = uuid.uuid4()
    category_1 = Category(id=cat_id, name="Filme")
    category_2 = Category(id=cat_id, name="Filme")
    
    assert category_1 == category_2
    
  def test_equality_different_class(self):
    class Dummy:
      pass
    
    cammon_id = uuid.uuid4()
    category = Category(name="Filme", id=cammon_id)
    dummy = Dummy()
    dummy.id = cammon_id
    
    assert category != dummy