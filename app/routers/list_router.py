from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.crud import list_crud
from app.dependencies import get_db
from app.schemas.list_schema import NewTodoList, ResponseTodoList, UpdateTodoList

router = APIRouter(
    prefix="/lists",
    tags=["Todoリスト"],
)


@router.get("/", response_model=List[ResponseTodoList])
def get_todo_lists(page: int = 1, per_page: int = 10, db: Session = Depends(get_db)):
    """すべてのTodoリストを取得する（ページネーション対応）"""
    return list_crud.get_todo_lists(db, page, per_page)


@router.post("/", response_model=ResponseTodoList)
def post_todo_list(todo_list: NewTodoList, db: Session = Depends(get_db)):
    """新しいTodoリストを作成する"""
    return list_crud.create_todo_list(db, todo_list)


@router.get("/{todo_list_id}", response_model=ResponseTodoList)
def get_todo_list(todo_list_id: int, db: Session = Depends(get_db)):
    """指定されたIDのTodoリストを取得する"""
    db_list = list_crud.get_todo_list(db, todo_list_id)
    if db_list is None:
        raise HTTPException(status_code=404, detail="Todo list not found")
    return db_list


@router.put("/{todo_list_id}", response_model=ResponseTodoList)
def put_todo_list(todo_list_id: int, todo_list: UpdateTodoList, db: Session = Depends(get_db)):
    """指定されたIDのTodoリストを更新する"""
    db_list = list_crud.update_todo_list(db, todo_list_id, todo_list)
    if db_list is None:
        raise HTTPException(status_code=404, detail="Todo list not found")
    return db_list


@router.delete("/{todo_list_id}")
def delete_todo_list(todo_list_id: int, db: Session = Depends(get_db)):
    """指定されたIDのTodoリストを削除する"""
    result = list_crud.delete_todo_list(db, todo_list_id)
    if not result:
        raise HTTPException(status_code=404, detail="Todo list not found")
    return {} 