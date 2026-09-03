from __future__ import annotations

from dataclasses import asdict, dataclass, field, replace
from datetime import datetime, timezone
from enum import Enum
import json
from pathlib import Path
from typing import Iterable
from uuid import uuid4


class Priority(str, Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"


class Status(str, Enum):
    CAPTURED = "captured"
    RESEARCHING = "researching"
    PLANNED = "planned"
    BUILDING = "building"
    TESTING = "testing"
    BLOCKED = "blocked"
    COMPLETE = "complete"
    ARCHIVED = "archived"


class QualityState(str, Enum):
    DRAFT = "draft"
    REVIEW = "review"
    APPROVED = "approved"


def utc_now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()


def _clean_text(value: str, field_name: str) -> str:
    cleaned = value.strip()
    if not cleaned:
        raise ValueError(f"{field_name} must not be empty")
    return cleaned


@dataclass(frozen=True)
class Idea:
    idea_id: str
    title: str
    description: str
    category: str
    priority: Priority = Priority.MEDIUM
    status: Status = Status.CAPTURED
    created_at: str = field(default_factory=utc_now_iso)
    updated_at: str = field(default_factory=utc_now_iso)
    tags: tuple[str, ...] = ()
    notes: tuple[str, ...] = ()
    source_refs: tuple[str, ...] = ()
    project_refs: tuple[str, ...] = ()
    learning_objectives: tuple[str, ...] = ()
    product_refs: tuple[str, ...] = ()
    quality_state: QualityState = QualityState.DRAFT

    def __post_init__(self) -> None:
        object.__setattr__(self, "title", _clean_text(self.title, "title"))
        object.__setattr__(self, "description", _clean_text(self.description, "description"))
        object.__setattr__(self, "category", _clean_text(self.category, "category"))

    def to_dict(self) -> dict:
        data = asdict(self)
        data["priority"] = self.priority.value
        data["status"] = self.status.value
        data["quality_state"] = self.quality_state.value
        for key in (
            "tags",
            "notes",
            "source_refs",
            "project_refs",
            "learning_objectives",
            "product_refs",
        ):
            data[key] = list(data[key])
        return data

    @classmethod
    def from_dict(cls, data: dict) -> "Idea":
        required = ("idea_id", "title", "description", "category", "created_at", "updated_at")
        missing = [key for key in required if key not in data]
        if missing:
            raise ValueError(f"missing required fields: {', '.join(missing)}")
        return cls(
            idea_id=str(data["idea_id"]),
            title=str(data["title"]),
            description=str(data["description"]),
            category=str(data["category"]),
            priority=Priority(data.get("priority", Priority.MEDIUM.value)),
            status=Status(data.get("status", Status.CAPTURED.value)),
            created_at=str(data["created_at"]),
            updated_at=str(data["updated_at"]),
            tags=tuple(str(x) for x in data.get("tags", [])),
            notes=tuple(str(x) for x in data.get("notes", [])),
            source_refs=tuple(str(x) for x in data.get("source_refs", [])),
            project_refs=tuple(str(x) for x in data.get("project_refs", [])),
            learning_objectives=tuple(str(x) for x in data.get("learning_objectives", [])),
            product_refs=tuple(str(x) for x in data.get("product_refs", [])),
            quality_state=QualityState(data.get("quality_state", QualityState.DRAFT.value)),
        )


class IdeaLedger:
    """Deterministic in-memory ledger with optional JSON persistence.

    This reference implementation intentionally has no AI dependency. It is the
    baseline against which later AI-assisted and hybrid implementations are measured.
    """

    def __init__(self, ideas: Iterable[Idea] | None = None) -> None:
        self._ideas: dict[str, Idea] = {}
        for idea in ideas or ():
            if idea.idea_id in self._ideas:
                raise ValueError(f"duplicate idea_id: {idea.idea_id}")
            self._ideas[idea.idea_id] = idea

    def create(
        self,
        *,
        title: str,
        description: str,
        category: str,
        priority: Priority = Priority.MEDIUM,
        tags: Iterable[str] = (),
    ) -> Idea:
        now = utc_now_iso()
        idea = Idea(
            idea_id=str(uuid4()),
            title=title,
            description=description,
            category=category,
            priority=priority,
            created_at=now,
            updated_at=now,
            tags=tuple(dict.fromkeys(tag.strip() for tag in tags if tag.strip())),
        )
        self._ideas[idea.idea_id] = idea
        return idea

    def get(self, idea_id: str) -> Idea:
        try:
            return self._ideas[idea_id]
        except KeyError as exc:
            raise KeyError(f"unknown idea_id: {idea_id}") from exc

    def list(
        self,
        *,
        status: Status | None = None,
        category: str | None = None,
        priority: Priority | None = None,
        include_archived: bool = False,
    ) -> list[Idea]:
        category_key = category.strip().casefold() if category is not None else None
        result = []
        for idea in self._ideas.values():
            if not include_archived and idea.status is Status.ARCHIVED:
                continue
            if status is not None and idea.status is not status:
                continue
            if priority is not None and idea.priority is not priority:
                continue
            if category_key is not None and idea.category.casefold() != category_key:
                continue
            result.append(idea)
        return sorted(result, key=lambda item: (item.updated_at, item.idea_id), reverse=True)

    def update(
        self,
        idea_id: str,
        *,
        title: str | None = None,
        description: str | None = None,
        category: str | None = None,
        priority: Priority | None = None,
        status: Status | None = None,
        quality_state: QualityState | None = None,
    ) -> Idea:
        current = self.get(idea_id)
        if current.status is Status.ARCHIVED and status not in (None, Status.ARCHIVED):
            raise ValueError("archived ideas cannot be reactivated by update; use an explicit recovery workflow")
        updated = replace(
            current,
            title=current.title if title is None else title,
            description=current.description if description is None else description,
            category=current.category if category is None else category,
            priority=current.priority if priority is None else priority,
            status=current.status if status is None else status,
            quality_state=current.quality_state if quality_state is None else quality_state,
            updated_at=utc_now_iso(),
        )
        self._ideas[idea_id] = updated
        return updated

    def add_note(self, idea_id: str, note: str) -> Idea:
        current = self.get(idea_id)
        cleaned = _clean_text(note, "note")
        updated = replace(current, notes=current.notes + (cleaned,), updated_at=utc_now_iso())
        self._ideas[idea_id] = updated
        return updated

    def archive(self, idea_id: str) -> Idea:
        return self.update(idea_id, status=Status.ARCHIVED)

    def export_json(self, path: str | Path) -> Path:
        target = Path(path)
        target.parent.mkdir(parents=True, exist_ok=True)
        payload = {
            "schema_version": 1,
            "exported_at": utc_now_iso(),
            "ideas": [idea.to_dict() for idea in self.list(include_archived=True)],
        }
        target.write_text(json.dumps(payload, indent=2, sort_keys=True), encoding="utf-8")
        return target

    @classmethod
    def import_json(cls, path: str | Path) -> "IdeaLedger":
        source = Path(path)
        if not source.exists():
            raise FileNotFoundError(source)
        payload = json.loads(source.read_text(encoding="utf-8"))
        if payload.get("schema_version") != 1:
            raise ValueError("unsupported schema_version")
        ideas = [Idea.from_dict(item) for item in payload.get("ideas", [])]
        return cls(ideas)

    def health_check(self) -> dict:
        errors: list[str] = []
        seen: set[str] = set()
        for idea in self._ideas.values():
            if idea.idea_id in seen:
                errors.append(f"duplicate idea_id: {idea.idea_id}")
            seen.add(idea.idea_id)
            try:
                Idea.from_dict(idea.to_dict())
            except (TypeError, ValueError) as exc:
                errors.append(f"invalid idea {idea.idea_id}: {exc}")
        return {
            "status": "GREEN" if not errors else "RED",
            "idea_count": len(self._ideas),
            "errors": errors,
        }
