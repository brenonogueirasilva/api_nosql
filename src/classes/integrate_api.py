class IntegrateApi:
    def params_to_dict(self, params):
        dict_params = { 
                'name' : params.name,               
                'year' : params.year,              
                'runtime' : params.runtime,         
                'genre' : params.genre,             
                'ratingValue' : params.ratingValue,
                'ratingCount' : params.ratingCount,
                'director.name' : params.director, 
                'cast.name' : params.cast           
            }
        dict_params = {key: value for key, value in dict_params.items() if value is not None}
        dict_params = dict(dict_params)
        return dict_params

    def list_params_to_dict(self, ls_params):
        ls_treated_params = []
        for element in ls_params:
            ls_treated_params.append(self.params_to_dict(element))
        return ls_treated_params

    def update_params_to_dict(self, update_params):
        update_dict = {}
        update_dict["new_document"] = self.params_to_dict( update_params.new_document )
        update_dict["query"] = self.params_to_dict( update_params.query)
        return update_dict