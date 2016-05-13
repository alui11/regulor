#Main driver for parsing regular expressions

def eval(pattern, string):
    '''Evaluate a string against a regular expression pattern'''
    pat = cleanPattern(pattern)
    pos = 0
    i = 0
    for j in range(len(string)):
        if i != len(pat)-1:
            # possibly a positive and a while
            if match(pat[i], string[j]) and match(pat[i+1], string[j]):
                pass
            elif match(pat[i],string[j]) and not match(pat[i+1], string[j]):
                i = i - 1
            elif not match(pat[i],string[j]) and not match(pat[i+1], string[j]):
                return False
        else:
            if not match(pat[i], string[j]):
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


def match(symbol, character):
    if  '.' in symbol:
        return True
