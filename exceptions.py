
#  include an oid i-var which can be set via the constructor
class DuplicateOid(Exception):
    def __init__(self, oid):
        self.oid = oid

# include an e-mail i-var which can be set via the constructor
class DuplicateEmail(Exception):
    def __init__(self, email):
        self.email = email

