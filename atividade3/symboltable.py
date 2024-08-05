class Symbol(object):
    def __init__(self, n, t=None, v=None):
        self.name = n
        self.type = t
        self.value = v

class BuiltInTypeSymbol(Symbol):
    def __init__(self, n):
        super().__init__(n)
    
    def __str__(self):
        return '<{n}>'.format(n=self.name)
    
    __repr__ = __str__

class VarSymbol(Symbol):
    def __init__(self, n, t, v=None):
        super().__init__(n, t, v=v)
    
    def __str__(self):
        return '<{n} : {t} = {v}>'.format(n=self.name, t=self.type, v=self.value)
    
    __repr__ = __str__

class SymbolTable(object):
    def __init__(self):
        self.symbols = {}
        #inicializar os tipos primitivos
        for primitive in ['INT','BOOLEAN','STRING']:
            self.insert(primitive, BuiltInTypeSymbol(primitive))
    
    def insert(self, name, data):
        self.symbols[name] = data

    #Retorna um objeto Symbol, se houver algo associado a esta chave (name) ou None
    def lookup(self, name):
        return self.symbols.get(name)

    def update(self, name, data):
        if self.lookup(name) is None:
            raise Exception("Símbolo inexistente: '%s'" % name)
        else: 
            self.insert(name,data)

    def __str__(self):
        symtab_header = '      Symbol Table      '
        lines = ['\n', symtab_header, '_' * len(symtab_header)]
        lines.extend(
            ('%2s: %r' % (key, value))
            for key, value in self.symbols.items()
        )
        lines.append('\n')
        s = '\n'.join(lines)
        return s
    
    __repr__ = __str__

class ScopedSymbolTable(object):
    def __init__(self, scope_name, scope_level, enclosing_scope=None):
        self.symbols = {}
        self.scope_name = scope_name
        self.scope_level = scope_level
        self.enclosing_scope = enclosing_scope
        if enclosing_scope is None:
            for primitive in ['INT', 'BOOLEAN', 'STRING']:
                self.insert(primitive, BuiltInTypeSymbol(primitive))
    
    def update(self, name, data):
        if self.lookup(name) is None:
            raise Exception("Símbolo inexistente: '%s'" % name)
        else:
            self.symbols[name] = data    
    
    def insert(self, name, data):
        self.symbols[name] = data
    
    def lookup(self, name, current_scope_only=False):
        symbol = self.symbols.get(name)
        if symbol is not None: 
            return symbol
        
        if current_scope_only: 
            return None
        
        if self.enclosing_scope is not None:
            return self.enclosing_scope.lookup(name)
    
    def __str__(self):
        h1 = 'SCOPE (SCOPED SYMBOL TABLE)'
        lines = ['\n', h1, '=' * len(h1)]
        for header_name, header_value in (
            ('Scope name', self.scope_name),
            ('Scope level', self.scope_level),
            ('Enclosing scope',
             self.enclosing_scope.scope_name if self.enclosing_scope else None
            )
        ):
            lines.append('%-15s: %s' % (header_name, header_value))
        h2 = 'Scope (Scoped symbol table) contents'
        lines.extend([h2, '-' * len(h2)])
        lines.extend(
            ('%7s: %r' % (key, value))
            for key, value in self.symbols.items()
        )
        lines.append('\n')
        s = '\n'.join(lines)
        return s
    
    __repr__ = __str__