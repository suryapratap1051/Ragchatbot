import requests

class ComplaintChatSession:
    def __init__(self):
        self.reset()

    def reset(self):
        self.data = {"name": None, "phone_number": None, "email": None, "complaint_details": None}
        self.stage = 0

    def get_next_prompt(self):
        if not self.data["name"]:
            return "Please provide your name."
        if not self.data["phone_number"]:
            return "What is your phone number?"
        if not self.data["email"]:
            return "Can you share your email address?"
        if not self.data["complaint_details"]:
            return "Please describe your complaint."
        return None

    def update_data(self, user_input):
        if not self.data["name"]:
            self.data["name"] = user_input
        elif not self.data["phone_number"]:
            self.data["phone_number"] = user_input
        elif not self.data["email"]:
            self.data["email"] = user_input
        elif not self.data["complaint_details"]:
            self.data["complaint_details"] = user_input

    def is_complete(self):
        return all(self.data.values())

    def submit_complaint(self):
        res = requests.post("http://127.0.0.1:8000/complaints", json=self.data)
        return res.json()
