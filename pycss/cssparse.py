
def parse( f ):
    output = []
    vars = {}
    
    for line in f:
        if line.startswith( '$' ):
            splitline = line.split( ':' )
            
            if len( splitline ) == 2:
                vars.update( { splitline[0]: splitline[1].strip() } )
        else:
            if '$' in line:
                var = line[line.find( '$' ):line.find( ';' )]
                if var in vars:
                    line = line.replace( var, vars[var] )
            output.append( line )
        
    return "".join( output )