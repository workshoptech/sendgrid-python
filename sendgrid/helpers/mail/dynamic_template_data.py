class DynamicData(object):
    """Handlebars compatible dynamic data to be applied to the text and HTML
    contents of the body of your email, as well as in the Subject and Reply-To
    parameters.
    """

    def __init__(self, key=None, value=None):
        """Create DynamicData with the given key and value.

        :param key: Text to be replaced with "value" param
        :type key: string, optional
        :param value: Value to substitute into email
        :type value: string or array of objects, optional
        """
        self.key = key
        self.value = value

    @property
    def key(self):
        return self._key

    @key.setter
    def key(self, value):
        self._key = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = value

    def get(self):
        """
        Get a JSON-ready representation of this DynamicData.

        :returns: This DynamicData, ready for use in a request body.
        :rtype: dict
        """
        dynamic_data = {}
        if self.key is not None and self.value is not None:
            dynamic_data[self.key] = self.value
        return dynamic_data
