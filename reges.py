#Main driver for parsing regular expressions

def eval(pattern, string):
    '''Evaluate a string against a regular expression pattern'''
    pat = cleanPattern(pattern)
    pos = 0
    i = 0
    for j in range(len(string)):
        if i != len(pat)-1:
            # possibly a positive and a while
            if match(pat[i+1], j, string):
                pass
            elif match(pat[i], j, string) and not match(pat[i+1], j, string):
                i = i - 1
            elif not match(pat[i],j, string) and not match(pat[i+1], j, string):
                return False
        else:
            if not match(pat[i], j, string):
                return False
    return True


#need * or +
def cleanPattern(pattern):
    '''Clean up a pattern by handling validity and escape codes'''
    cleanpat = []
    symbols = [x for x in pattern ]
    for sym in symbols:
        pos = symbols.index(sym)+1
        if sym == '*' or sym == '+':
            cleanpat[-1] = cleanpat[-1]+sym
            continue
        if sym == '\\':
            sym += symbols.pop(pos)
        elif sym == '{':
            while symbols[pos] != '}':
                sym += symbols.pop(pos)
            sym += symbols.pop(pos)
        elif sym == '[':
            while symbols[pos] != ']':
                sym += symbols.pop(pos)
            sym += symbols.pop(pos)
        elif sym == '(':
            while symbols[pos] != ')':
                sym += symbols.pop(pos)
            sym += symbols.pop(pos)
        cleanpat.append(sym)
    return cleanpat


def match(symbol, identifier, string):
    if '*' in symbol:
        return True
    elif '+' in symbol:
        if match(symbol.strip('+'), identifier, string) or match(symbol.string('+'), identifier-1, string):
            return True
        else:
            return False
    
    if symbol == '^':
        if identifier == 0:
            return True
        else:
            return False
    elif symbol == '$'
            


















