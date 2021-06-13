# ------------------------------------------------------ Imports ----------------------------------------------------- #

# Local
from .xpath_attribute_value import XpathAttributeValue
from .enums import XPathConditionType

# -------------------------------------------------------------------------------------------------------------------- #



# ----------------------------------------- class: XpathAttributeValueEquals ----------------------------------------- #

class XpathAttributeValueEquals(XpathAttributeValue):

    # --------------------------------------------------- Init --------------------------------------------------- #

    def __init__(
        self,
        value: any
    ):
        super().__init__(
            value,
            XPathConditionType.EQUALS
        )


# -------------------------------------------------------------------------------------------------------------------- #