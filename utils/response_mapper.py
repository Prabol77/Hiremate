"""
Generic response mapper.

Maps parsed AI JSON responses into dataclass models.
"""

from dataclasses import fields


def map_response(
    data: dict,
    model,
):
    """
    Populate a dataclass model using a dictionary.

    Args:
        data:
            Parsed JSON dictionary.

        model:
            Dataclass instance.

    Returns:
        Populated model.
    """

    for field in fields(model):

        setattr(

            model,

            field.name,

            data.get(

                field.name,

                getattr(
                    model,
                    field.name,
                ),

            ),

        )

    return model