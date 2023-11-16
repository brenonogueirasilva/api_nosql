class IntegrateApi:
    """
    A class for integrating with an API.
    """
    def params_to_dict(self, params) -> dict:
        """
        Converts parameters from a Pydantic model to a dictionary.
        Args:
            params: Pydantic model containing parameters.
        Returns:
            dict: A dictionary containing non-None values from the Pydantic model.
        """
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

    def list_params_to_dict(self, ls_params: list) -> list:
        """
        Converts a list of Pydantic models to a list of dictionaries.
        Args:
            ls_params (list): List of Pydantic models.
        Returns:
            list: List of dictionaries containing non-None values from each Pydantic model.
        """
        ls_treated_params = []
        for element in ls_params:
            ls_treated_params.append(self.params_to_dict(element))
        return ls_treated_params

    def update_params_to_dict(self, update_params: dict) -> dict:
        """
        Converts update parameters from Pydantic models to a dictionary.
        Args:
            update_params: Pydantic model containing update parameters.
        Returns:
            dict: A dictionary containing 'new_document' and 'query' keys with corresponding values.
        """
        update_dict = {}
        update_dict["new_document"] = self.params_to_dict( update_params.new_document )
        update_dict["query"] = self.params_to_dict( update_params.query)
        return update_dict