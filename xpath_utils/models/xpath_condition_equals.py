# ------------------------------------------------------ Imports ----------------------------------------------------- #

# System
from typing import Optional

# Local
from .xpath_condition import XPathCondition
from .enums import XPathConditionType

# -------------------------------------------------------------------------------------------------------------------- #



# -------------------------------------------- class: XPathConditionEquals ------------------------------------------- #

class XPathConditionEquals(XPathCondition):

    # --------------------------------------------------- Init --------------------------------------------------- #

    def __init__(
        self,
        name: str = None,
        value = None,
        **kwargs
    ):
        super().__init__(
            name=name,
            value=value,
            condition_type=XPathConditionType.EQUALS,
            **kwargs
        )


# -------------------------------------------------------------------------------------------------------------------- #