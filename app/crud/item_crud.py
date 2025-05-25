from sqlalchemy.orm import Session

from app.const import TodoItemStatusCode
from app.models.item_model import ItemModel
from app.models.list_model import ListModel
from app.schemas.item_schema import NewTodoItem, UpdateTodoItem


def get_todo_items(db: Session, todo_list_id: int, page: int = 1, per_page: int = 10):
    """指定されたTodoリストに紐づくすべてのTodo項目を取得する（ページネーション対応）"""
    skip = (page - 1) * per_page
    return db.query(ItemModel).filter(ItemModel.todo_list_id == todo_list_id).offset(skip).limit(per_page).all()


def get_todo_item(db: Session, todo_list_id: int, todo_item_id: int):
    """指定されたTodoリストに紐づく指定されたTodo項目を取得する"""
    return db.query(ItemModel).filter(
        ItemModel.todo_list_id == todo_list_id, 
        ItemModel.id == todo_item_id
    ).first()


def create_todo_item(db: Session, todo_list_id: int, new_todo_item: NewTodoItem):
    """指定されたTodoリストに新しいTodo項目を作成する"""
    # Todoリストが存在するか確認
    db_list = db.query(ListModel).filter(ListModel.id == todo_list_id).first()
    if db_list is None:
        return None
    
    # 新しいTodo項目を作成
    db_item = ItemModel(
        todo_list_id=todo_list_id,
        title=new_todo_item.title,
        description=new_todo_item.description,
        due_at=new_todo_item.due_at,
        status_code=TodoItemStatusCode.NOT_COMPLETED.value
    )
    
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item


def update_todo_item(db: Session, todo_list_id: int, todo_item_id: int, update_todo_item: UpdateTodoItem):
    """指定されたTodoリストに紐づく指定されたTodo項目を更新する"""
    db_item = get_todo_item(db, todo_list_id, todo_item_id)
    if db_item is None:
        return None
    
    if update_todo_item.title is not None:
        db_item.title = update_todo_item.title
    if update_todo_item.description is not None:
        db_item.description = update_todo_item.description
    if update_todo_item.due_at is not None:
        db_item.due_at = update_todo_item.due_at
    if update_todo_item.complete is not None:
        db_item.status_code = TodoItemStatusCode.COMPLETED.value if update_todo_item.complete else TodoItemStatusCode.NOT_COMPLETED.value
    
    db.commit()
    db.refresh(db_item)
    return db_item


def delete_todo_item(db: Session, todo_list_id: int, todo_item_id: int) -> bool:
    """指定されたTodoリストに紐づく指定されたTodo項目を削除する"""
    db_item = get_todo_item(db, todo_list_id, todo_item_id)
    if db_item is None:
        return False
    
    db.delete(db_item)
    db.commit()
    return True 