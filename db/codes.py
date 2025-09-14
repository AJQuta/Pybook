from enum import Enum

# * List of Exit and Error Codes for database executions

class EXIT_CODE(Enum):
    SUCCESS = 0
    FAIL = 1

    IO_ERROR = 2
    OUT_OF_MEM = 3
    INVALID_CMD = 4

    class INVALID_PERM(Enum):
        OWNERSHIP = 5
        READ = 6
        WRITE = 7