# app/models.py

from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Text
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.storage import Base


class Document(Base):
    __tablename__ = "document"

    id = Column(Integer, primary_key=True, index=True)
    filename = Column(String, nullable=False)
    file_path = Column(String, nullable=False)
    doc_type = Column(String)
    source = Column(String, nullable=False)

    uploaded_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )

    document_chunks = relationship(
        "DocumentChunk",
        back_populates="document"
    )


class DocumentChunk(Base):
    __tablename__ = "document_chunk"

    id = Column(Integer, primary_key=True, index=True)

    document_id = Column(
        Integer,
        ForeignKey("document.id")
    )

    chunk_index = Column(
        Integer,
        index=True,
        nullable=False
    )

    raw_text = Column(Text)
    explanation = Column(Text)

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )

    document = relationship(
        "Document",
        back_populates="document_chunks"
    )


class PipelineLog(Base):
    __tablename__ = "pipeline_logs"

    id = Column(Integer, primary_key=True, index=True)

    document_id = Column(
        Integer,
        ForeignKey("document.id")
    )

    stage = Column(String)
    status = Column(String)

    logged_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )