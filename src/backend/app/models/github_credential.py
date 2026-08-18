"""GitHub credential model (encrypted PAT storage)."""

from datetime import datetime

from sqlalchemy import DateTime, ForeignKey, String, Text, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.backend.app.extensions import db


class GitHubCredential(db.Model):
    """Encrypted GitHub PAT + target organization for a user."""

    __tablename__ = "github_credentials"

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    # Encrypted PAT (Fernet ciphertext); never store plaintext
    encrypted_pat: Mapped[str] = mapped_column(Text, nullable=False)
    target_org: Mapped[str | None] = mapped_column(String(255), nullable=True)
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now(), nullable=False
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now(),
        nullable=False,
    )

    user: Mapped["User"] = relationship(back_populates="github_credentials")

    def __repr__(self) -> str:
        return f"<GitHubCredential id={self.id} user_id={self.user_id}>"
