__all__ = (
    'seconds_to_str',
)

# some comment
def seconds_to_str(seconds: int) -> str:
    """
    Функция должна вернуть текстовое представление времени
    20 -> 20s
    60 -> 01m00s
    65 -> 01m05s
    3700 -> 01h01m40s
    93600 -> 01d02h00m00s
    """
    # for action
    
    time = ''

    days = seconds // (24 * 3600)
    hours = seconds % (24 * 3600) // 3600
    minutes = seconds % 3600 // 60

    if(seconds // (24 * 3600) != 0):
        time += '{:02d}d'.format(seconds // (24 * 3600))

    if(seconds // 3600 != 0):
        time += '{:02d}h'.format(seconds % (24 * 3600) // 3600)

    if(seconds // 60 != 0):
        time += '{:02d}m'.format(seconds % 3600 // 60)

    time += '{:02d}s'.format(seconds % 60)

    return time




