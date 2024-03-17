def v(a=0.1, b='__0.0.0__ V'):
    if b == '__0.0.0__ V':
        return str(a) + ' BETA ' + 'V'
    else:
        return str(a) + ' BETA ' + b
