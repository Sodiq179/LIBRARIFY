from datetime import datetime
import uuid
from datetime import datetime
import models

class LibrarifyBase:
    """Base class for Librarify project
    Methods:
        __init__(self, *args, **kwargs)
        __str__(self)
        __save(self)
        __repr__(self)
        to_dict(self)
    """
    def __init__(self, *args, **kwargs):
        """
        Initialize attributes: random uuid,
                            dates created/updated
        """
        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at":
                    self.created_at = datetime.strptime(kwargs["created_at"],
                                                        "%Y-%m-%dT%H:%M:%S.%f")
                elif key == "updated_at":
                    self.updated_at = datetime.strptime(kwargs["updated_at"],
                                                        "%Y-%m-%dT%H:%M:%S.%f")
                elif key == "__class__":
                    pass
                else:
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)


    def __str__(self):
        """
        Return string representation of the model
        """
        return ("[{}] ({}) {}".
                format(self.__class__.__name__, self.id, self.__dict__))

    def save(self):
        """
        Update instance with updated time &
        save to serialized file
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        Return dic with string formats of times;
        add class info to dic
        """
        dictFormat = {}
        dictFormat["__class__"] = self.__class__.__name__
        for key, value in self.__dict__.items():
            if isinstance(value, (datetime, )):
                dictFormat[key] = value.isoformat()
            else:
                dictFormat[key] = value
        return  dictFormat



me = LibrarifyBase()
print(me)