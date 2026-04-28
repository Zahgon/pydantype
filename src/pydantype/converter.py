from __future__ import annotations
from typing import get_args, get_origin, Any, Union, List, Dict, Optional, Type, ForwardRef
from typing_extensions import TypedDict
from pydantic import BaseModel
from .utils import is_pydantic_model, is_optional
def convertt_type(annotation: Any, processed_models: set = None) -> Any:
    pass
def convert(model: Type[BaseModel], processed_models: set = None) -> Type[TypedDict]:
    pass
