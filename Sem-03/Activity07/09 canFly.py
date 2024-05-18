def can_fly(obj):
    if hasattr(obj, 'fly') and callable(obj.fly):
        return True
    return False
