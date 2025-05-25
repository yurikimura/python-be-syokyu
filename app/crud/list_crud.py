from sqlalchemy.orm import Session

from app.models.list_model import ListModel
from app.schemas.list_schema import NewTodoList, UpdateTodoList


def get_todo_lists(db: Session, page: int = 1, per_page: int = 10):
    """すべてのTodoリストを取得する（ページネーション対応）"""
    skip = (page - 1) * per_page
    return db.query(ListModel).offset(skip).limit(per_page).all()


def get_todo_list(db: Session, todo_list_id: int):
    """指定されたIDのTodoリストを取得する"""
    return db.query(ListModel).filter(ListModel.id == todo_list_id).first()


def create_todo_list(db: Session, new_todo_list: NewTodoList):
    """新しいTodoリストを作成する"""
    db_list = ListModel(title=new_todo_list.title, description=new_todo_list.description)
    db.add(db_list)
    db.commit()
    db.refresh(db_list)
    return db_list


def update_todo_list(db: Session, todo_list_id: int, update_todo_list: UpdateTodoList):
    """指定されたIDのTodoリストを更新する"""
    db_list = get_todo_list(db, todo_list_id)
    if db_list is None:
        return None
    
    if update_todo_list.title is not None:
        db_list.title = update_todo_list.title
    if update_todo_list.description is not None:
        db_list.description = update_todo_list.description
    
    db.commit()
    db.refresh(db_list)
    return db_list


def delete_todo_list(db: Session, todo_list_id: int) -> bool:
    """指定されたIDのTodoリストを削除する"""
    db_list = get_todo_list(db, todo_list_id)
    if db_list is None:
        return False
    
    db.delete(db_list)
    db.commit()
    return True 