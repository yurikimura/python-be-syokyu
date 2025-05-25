from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.crud import item_crud
from app.dependencies import get_db
from app.schemas.item_schema import NewTodoItem, ResponseTodoItem, UpdateTodoItem

router = APIRouter(
    prefix="/lists/{todo_list_id}/items",
    tags=["Todo項目"],
)


@router.get("/", response_model=List[ResponseTodoItem])
def get_todo_items(todo_list_id: int, page: int = 1, per_page: int = 10, db: Session = Depends(get_db)):
    """指定されたTodoリストに紐づくすべてのTodo項目を取得する（ページネーション対応）"""
    items = item_crud.get_todo_items(db, todo_list_id, page, per_page)
    return items


@router.get("/{todo_item_id}", response_model=ResponseTodoItem)
def get_todo_item(todo_list_id: int, todo_item_id: int, db: Session = Depends(get_db)):
    """指定されたTodoリストに紐づく指定されたTodo項目を取得する"""
    db_item = item_crud.get_todo_item(db, todo_list_id, todo_item_id)
    if db_item is None:
        raise HTTPException(status_code=404, detail="Todo item not found")
    return db_item


@router.post("/", response_model=ResponseTodoItem)
def post_todo_item(todo_list_id: int, todo_item: NewTodoItem, db: Session = Depends(get_db)):
    """指定されたTodoリストに新しいTodo項目を作成する"""
    db_item = item_crud.create_todo_item(db, todo_list_id, todo_item)
    if db_item is None:
        raise HTTPException(status_code=404, detail="Todo list not found")
    return db_item


@router.put("/{todo_item_id}", response_model=ResponseTodoItem)
def put_todo_item(todo_list_id: int, todo_item_id: int, todo_item: UpdateTodoItem, db: Session = Depends(get_db)):
    """指定されたTodoリストに紐づく指定されたTodo項目を更新する"""
    db_item = item_crud.update_todo_item(db, todo_list_id, todo_item_id, todo_item)
    if db_item is None:
        raise HTTPException(status_code=404, detail="Todo item not found")
    return db_item


@router.delete("/{todo_item_id}")
def delete_todo_item(todo_list_id: int, todo_item_id: int, db: Session = Depends(get_db)):
    """指定されたTodoリストに紐づく指定されたTodo項目を削除する"""
    result = item_crud.delete_todo_item(db, todo_list_id, todo_item_id)
    if not result:
        raise HTTPException(status_code=404, detail="Todo item not found")
    return {} 