from datasette import hookimpl


@hookimpl
async def extra_template_vars(datasette, request, view_name):
    vars = {}
    if view_name == "index":
        db = datasette.get_database("demo")

        # only needed for the template version
        sql = "SELECT created, delta_sec FROM reports ORDER BY created DESC LIMIT ?"
        chart_size = 100
        chart = await db.execute(sql, params=[chart_size])

        vars.update({"chart_data": chart, "v": request.args.get("v", "2")})

    return vars
