from config import shelve_name
import shelve

def set_active_user(chat_id,active):
    with shelve.open(shelve_name) as storage:
        storage[str(chat_id)]= active

def get_active_for_user(chat_id):
    with shelve.open(shelve_name) as storage:
        try:
            active = storage[str(chat_id)]
            return active
        except KeyError:
            return None

def finish_active_comand(chat_id):
    with shelve.open(shelve_name) as storage:
        del storage[str(chat_id)]

