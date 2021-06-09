from api.schema.root_schema import ma


class FruitSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ("id", "name", "datetime", "_links")

    # Smart hyperlinking
    _links = ma.Hyperlinks(
        {
            "self": ma.URLFor("api.get_by_id", values=dict(id="<id>")),
            "collection": ma.URLFor("api.get_all"),
        }
    )
