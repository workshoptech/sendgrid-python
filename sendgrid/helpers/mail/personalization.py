import warnings


class Personalization(object):
    """A Personalization defines who should receive an individual message and
    how that message should be handled.
    """

    def __init__(self):
        """Create an empty Personalization."""
        self._tos = []
        self._ccs = []
        self._bccs = []
        self._subject = None
        self._headers = []
        self._dynamic_template_data = []
        self._substitutions = []
        self._custom_args = []
        self._send_at = None

    @property
    def tos(self):
        """A list of recipients for this Personalization.

        :rtype: list(dict)
        """
        return self._tos

    @tos.setter
    def tos(self, value):
        self._tos = value

    def add_to(self, email):
        """Add a single recipient to this Personalization.

        :type email: Email
        """
        self._tos.append(email.get())

    @property
    def ccs(self):
        """A list of recipients who will receive copies of this email.

        :rtype: list(dict)
        """
        return self._ccs

    @ccs.setter
    def ccs(self, value):
        self._ccs = value

    def add_cc(self, email):
        """Add a single recipient to receive a copy of this email.

        :param email: new recipient to be CCed
        :type email: Email
        """
        self._ccs.append(email.get())

    @property
    def bccs(self):
        """A list of recipients who will receive blind carbon copies of this email.

        :rtype: list(dict)
        """
        return self._bccs

    @bccs.setter
    def bccs(self, value):
        self._bccs = value

    def add_bcc(self, email):
        """Add a single recipient to receive a blind carbon copy of this email.

        :param email: new recipient to be BCCed
        :type email: Email
        """
        self._bccs.append(email.get())

    @property
    def subject(self):
        """The subject of your email (within this Personalization).

        Char length requirements, according to the RFC:
        https://stackoverflow.com/a/1592310
        :rtype: string
        """
        return self._subject

    @subject.setter
    def subject(self, value):
        self._subject = value

    @property
    def headers(self):
        """The headers for emails in this Personalization.

        :rtype: list(dict)
        """
        return self._headers

    @headers.setter
    def headers(self, value):
        self._headers = value

    def add_header(self, header):
        """Add a single Header to this Personalization.

        :type header: Header
        """
        self._headers.append(header.get())

    @property
    def dynamic_template_data(self):
        """Dynamic Template Data to be applied within this Personalization.
        :rtype: list(dict)
        """
        return self._dynamic_template_data

    @dynamic_template_data.setter
    def dynamic_template_data(self, value):
        if len(self.substitutions) > 0:
            warnings.warn(
                "Dynamic template data should not be used in conjunction with "
                "substitutions")
        self._dynamic_template_data = value

    def add_dynamic_template_data(self, dynamic_template_data):
        """Add a new Substitution to this Personalization.
        :type substitution: Substitution
        """
        if len(self.substitutions) > 0:
            warnings.warn(
                "Dynamic template data should not be used in conjunction with "
                "substitutions")
        self._dynamic_template_data.append(dynamic_template_data.get())

    @property
    def substitutions(self):
        """Substitutions to be applied within this Personalization.

        :rtype: list(dict)
        """
        return self._substitutions

    @substitutions.setter
    def substitutions(self, value):
        if len(self.dynamic_template_data) > 0:
            warnings.warn(
                "Substitutions should not be used in conjunction with "
                "dynamic template data")
        self._substitutions = value

    def add_substitution(self, substitution):
        """Add a new Substitution to this Personalization.

        :type substitution: Substitution
        """
        if len(self.dynamic_template_data) > 0:
            warnings.warn(
                "Substitutions should not be used in conjunction with "
                "dynamic template data")
        self._substitutions.append(substitution.get())

    @property
    def custom_args(self):
        """The CustomArgs that will be carried along with this Personalization.

        :rtype: list(dict)
        """
        return self._custom_args

    @custom_args.setter
    def custom_args(self, value):
        self._custom_args = value

    def add_custom_arg(self, custom_arg):
        """Add a CustomArg to this Personalization.

        :type custom_arg: CustomArg
        """
        self._custom_args.append(custom_arg.get())

    @property
    def send_at(self):
        """A unix timestamp allowing you to specify when you want emails from
        this Personalization to be delivered. Scheduling more than 72 hours in
        advance is forbidden.

        :rtype: int
        """
        return self._send_at

    @send_at.setter
    def send_at(self, value):
        self._send_at = value

    def get(self):
        """
        Get a JSON-ready representation of this Personalization.

        :returns: This Personalization, ready for use in a request body.
        :rtype: dict
        """
        personalization = {}
        if self.tos:
            personalization["to"] = self.tos

        if self.ccs:
            personalization["cc"] = self.ccs

        if self.bccs:
            personalization["bcc"] = self.bccs

        if self.subject is not None:
            personalization["subject"] = self.subject

        if self.headers:
            headers = {}
            for key in self.headers:
                headers.update(key)
            personalization["headers"] = headers

        if self.dynamic_template_data:
            dynamic_template_data = {}
            for key in self.dynamic_template_data:
                dynamic_template_data.update(key)
            personalization["dynamic_template_data"] = dynamic_template_data

        if self.substitutions:
            substitutions = {}
            for key in self.substitutions:
                substitutions.update(key)
            personalization["substitutions"] = substitutions

        if self.custom_args:
            custom_args = {}
            for key in self.custom_args:
                custom_args.update(key)
            personalization["custom_args"] = custom_args

        if self.send_at is not None:
            personalization["send_at"] = self.send_at
        return personalization
