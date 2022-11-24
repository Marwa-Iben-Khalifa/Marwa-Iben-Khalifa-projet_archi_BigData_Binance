from controllers.virtualcounters import data_virtual_counter

# Creation of routes


def create_routes(app):

    # Arbo counters
    @app.route('/api/py/arbo/counters', methods=['GET'])
    def get_ct_arbo():
        fluid = request.args.get('fluid')
        building = request.args.get('building')
        return get_arbo_counters(building, fluid)
