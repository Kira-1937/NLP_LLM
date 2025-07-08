class Session:
    def __init__(self, session_id, user_id, start_time):
        self.session_id = session_id
        self.user_id = user_id
        self.start_time = start_time
        self.history = []
