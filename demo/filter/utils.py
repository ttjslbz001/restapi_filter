def get_value(record, arg):
    if isinstance(arg, dict) and arg.get('type') == 'hierarchical_key':
        keys = arg['value'].split('.')
        value = record
        for key in keys:
            value = value.get(key, None)
            if value is None:
                return None
        return value

    return record.get(arg, None)
