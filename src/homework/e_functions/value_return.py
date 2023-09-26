#
#takes an epoch_seconds parameter
def get_hour(epoch_seconds):
    hours = epoch_seconds // 3600
    return hours
#takes an epoch_seconds parameter
def get_minutes(epoch_seconds):
    minutes = (epoch_seconds // 60) % 60
    return minutes
#takes an epoch_seconds parameter
def get_seconds(epoch_seconds):
    seconds = epoch_seconds % 60
    return seconds

def display_time(epoch_seconds):
    hours = get_hour(epoch_seconds)
    minutes = get_minutes(epoch_seconds)
    seconds = get_seconds(epoch_seconds)
    print(f"Time: {hours:02}:{minutes:02}:{seconds:02}")