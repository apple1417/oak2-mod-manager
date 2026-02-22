from ._uobject_children import UScriptStruct
from ._wrapped_struct import WrappedStruct

class GbxDefPtr:
    """
    EXPERIMENTAL TYPE.

    It may currently leak memory and/or cause crashes, and it's semantics are all
    liable to change, it might even get removed.
    """

    _experimental_name: str
    _experimental_ref: UScriptStruct
    @property
    def _experimental_instance(self) -> WrappedStruct | None: ...
    def __init__(self) -> None:
        """Creates a default (empty) GbxDefPtr."""
    def __repr__(self) -> str:
        """
        Gets a string representation of this GbxDefPtr.

        Returns:
            The string representation.
        """
