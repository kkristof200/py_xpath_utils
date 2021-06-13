# ------------------------------------------------------ Imports ----------------------------------------------------- #

# Local
from .xpath_attribute_value import XpathAttributeValue
from .enums import XPathConditionType

# -------------------------------------------------------------------------------------------------------------------- #



# ---------------------------------------- class: XpathAttributeValueContains ---------------------------------------- #

class XpathAttributeValueContains(XpathAttributeValue):

    # --------------------------------------------------- Init --------------------------------------------------- #

    def __init__(
        self,
        value: any
    ):
        super().__init__(
            value,
            XPathConditionType.CONTAINS
        )


# -------------------------------------------------------------------------------------------------------------------- #