class BrewtrackerError(RuntimeError):
    def __init__(self, *args, **kwargs):
        super(RuntimeError, self).__init__(*args, **kwargs)
