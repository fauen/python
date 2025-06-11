import Pushover

thing = Pushover.Pushover("api_key", "user_key")
message = "A nice message."
thing.send_message(message)
