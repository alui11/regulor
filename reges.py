#Main driver for parsing regular expressions

def eval(pattern, string):
    '''Evaluate a string against a regular expression pattern'''
    pat = cleanPattern(pattern)
    pos = 0
    for i in range(len(pat)):
        if i != len(pat)-1:
            # possibly a positive and a while
            if not match(pat[i], string[0]) or match(pat[i+1], string[0]):
                return False
        else:
            if not match(pat[i], string[0]):
                return False
    return True


#need * or +
def cleanPattern(pattern):
    '''Clean up a pattern by handling validity and escape codes'''
    cleanpat = []
    symbols = [x for x in pattern if x != ' ']
    for sym in symbols:
        pos = symbols.index(sym)+1
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
        cleanpat.append(sym)
    return cleanpat


def match(symbol, character):
    if  '.' in symbol:
        return True
