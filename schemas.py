from app import ma

class FruitSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ("id", "name", "datetime", "_links")

    # Smart hyperlinking
    _links = ma.Hyperlinks(
        {
            "self": ma.URLFor("getById", values=dict(id="<id>")),
            "collection": ma.URLFor("getAll"),
        }
    )