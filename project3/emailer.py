# do not test directly
# similar to singleton example in class, USE (CLS)
class Emailer:

    _sender_address = ""
    _sole_instance = None # the only instance of this class

    # sets the class variable as specified
    @classmethod
    def configure(cls, sender_address):
        return cls._sender_address

    # return the only instance of this class
    @classmethod
    def instance(cls):
        if cls._sole_instance is None:
            cls._sole_instance = cls()
            return cls._sole_instance

    # Note: this is an instance method.  recipients must be
    # a collection of email addresses (not TeamMembers!).
    # subject and message are strings.  Just have this method
    # print f"Sending mail to: {recipient}" for each recipient in
    # the recipients list.  We'll cover sending e-mail from Python later.
    def send_plain_email(self, recipients, subject, message):
        return f"Sending mail to: {recipients}"
