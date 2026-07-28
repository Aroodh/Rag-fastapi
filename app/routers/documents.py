from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.dependencies import get_current_user

from app.models.user import User
from app.models.document import Document

from app.schemas.document import (
    DocumentCreate,
    DocumentResponse
)

router = APIRouter(
    prefix="/documents",
    tags=["Documents"]
)


# Upload a new document
@router.post(
    "/",
    response_model=DocumentResponse,
    status_code=status.HTTP_201_CREATED
)
def upload_document(
    document: DocumentCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    new_document = Document(
        title=document.title,
        content=document.content,
        owner_id=current_user.id
    )

    db.add(new_document)
    db.commit()
    db.refresh(new_document)

    return new_document


# Get all documents of logged-in user
@router.get(
    "/",
    response_model=list[DocumentResponse]
)
def get_documents(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    documents = db.query(Document).filter(
        Document.owner_id == current_user.id
    ).all()

    return documents


# Get one document
@router.get(
    "/{document_id}",
    response_model=DocumentResponse
)
def get_document(
    document_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    document = db.query(Document).filter(
        Document.id == document_id,
        Document.owner_id == current_user.id
    ).first()

    if document is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Document not found"
        )

    return document


# Delete a document
@router.delete("/{document_id}")
def delete_document(
    document_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    document = db.query(Document).filter(
        Document.id == document_id,
        Document.owner_id == current_user.id
    ).first()

    if document is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Document not found"
        )

    db.delete(document)
    db.commit()

    return {
        "message": "Document deleted successfully"
    }